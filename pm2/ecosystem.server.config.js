const path = require("path");
const dotenv = require("dotenv");
const { execSync } = require("child_process");

const which = cmd => execSync(`which ${cmd}`).toString().trimEnd();
const relative = (...dir) => path.resolve(__dirname, ...dir);

const env = dotenv.config({ path: relative("../auth_backend/auth_backend.env") }).parsed;

const gunicorn = which("gunicorn");
const caddy = which("caddy");

const data = "/mnt/nextcloud-dp/nextcloud/data";
const host = "0.0.0.0";
const suffix = "files";

module.exports = {
  apps: [
    {
      script: "su",
      cwd: relative('..'),
      name: 'ghostfs',
      watch: false,
      args: `-s /bin/sh www-data -c "./GhostFS --server --root ${data} --bind ${host} --suffix ${suffix}"`,
    },
    {
      script: gunicorn,
      args: '--workers 40 --timeout 120 --bind 127.0.0.1:3446 --pythonpath auth_backend auth_backend:app',
      cwd: relative('..'),
      watch: relative('../auth_backend'),
      interpreter: 'python3' 
    },
    {
      script: caddy,
      args: 'run',
      cwd: relative('../caddy'),
      watch: relative('../caddy'),
      env
    },
  ],
};
