# ghostfs

## Install
1. Clone this repository and cd into the cloned folder.

2. Edit `auth_backend/auth_backend.env.template` and update the domain name to where the GhostFS Auth Backend will run.

3. To generate a self-signed SSL certificate and key for the GhostFS server running on the same <domain_name> as above, execute the following command:

    ```bash
    ./gen_cert.sh <domain_name>
    ```

4. If needed, edit the `.env` to update the version of GhostFS.


5. To install a GhostFS server and a GhostFS Auth Backend running on PM2 with a Caddy reverse proxy, execute the following command:

    ```bash
    ./install_ghostfs.sh
    ```

6. Verify that everything is running correctly using:
    ```bash
    sudo pm2 status
    ```

7. Verify that there are no errors in the logs:
     ```bash
     sudo pm2 logs <id>
     ```

## Acknowledgement

This research was supported by the EBRAINS research infrastructure, funded from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).
