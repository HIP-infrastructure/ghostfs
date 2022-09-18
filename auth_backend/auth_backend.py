from flask import Flask
from flask import request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
import pathlib
from werkzeug.security import generate_password_hash, check_password_hash
import json
import subprocess
import os
from dotenv import load_dotenv

__author__ = "Nathalie Casati"
__email__ = "nathalie.casati@chuv.ch"

app = Flask(__name__)
auth = HTTPBasicAuth()

# get path for secret
ENV_PATH = pathlib.Path(__file__).parent

load_dotenv(ENV_PATH.joinpath("auth_backend.env"))

def get_domain():
  return str(os.getenv('AUTH_BACKEND_DOMAIN'))

def get_credentials():
  with open(ENV_PATH.joinpath("auth_backend.secret"), mode='r') as secret:
    username, password = secret.read().split('@')
  return {username: password}


users = get_credentials()


class InvalidUsage(Exception):
  status_code = 400

  def __init__(self, message, status_code=None, payload=None):
    Exception.__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
    self.payload = payload

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['message'] = self.message
    return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
  response = jsonify(error.to_dict())
  response.status_code = error.status_code
  return response

@auth.verify_password
def verify_password(username, password):
  if username in users:
    return check_password_hash(users.get(username), password)
  return False


@app.route('/')
@auth.login_required
def index():
  return "Hello, %s!" % auth.username()

@app.route('/ok')
def health_check():
  return "GhostFS Authentication Backend currently running on %s" % get_domain()

@app.route('/token', methods=['GET'])
@auth.login_required
def token():
  # here we want to get the value of hip_user and group_folders
  # (i.e. ?hipuser=value&gf=[{"id":3,"label":"CHUV","path":"__groupfolders/3"}])
  hip_user = request.args.get('hipuser')
  group_folders = json.loads(request.args.get('gf'))

  if hip_user is None:
    raise InvalidUsage('Invalid action', status_code=500)

  # authorize hipuser
  cmd = ["../GhostFS", "--authorize", "--user", hip_user, "--retries", "1"]
  output = subprocess.run(cmd, cwd=ENV_PATH, text=True, capture_output=True)

  # error
  if output.stderr.rstrip() is not None and output.stderr.rstrip():
    response = { "error": output.stderr.rstrip() }
    return jsonify(response)

  # we got a token
  if output.stdout.rstrip() is not None and output.stdout.rstrip():
    response = { "token": output.stdout.rstrip() }

    # mount group folders if any
    for group_folder in group_folders:
      cmd = ["../GhostFS", "--mount", "--user", hip_user, "--source", group_folder['path'], "--destination", group_folder['label']]
      output = subprocess.run(cmd, cwd=ENV_PATH, text=True, capture_output=True) 

      # error
      if output.stderr.rstrip() is not None and output.stderr.rstrip():
        response = { "error": output.stderr.rstrip() }
        return jsonify(response)

    return jsonify(response)

  raise InvalidUsage('Unknown error', status_code=500)


if __name__ == '__main__':
  app.run(port=3446)
