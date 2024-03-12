# ghostfs
This repository allows deploying a GhostFS Server and Auth Server, and a GhostFS Auth Backend.

## Install
1. Clone this repository and `cd` into the cloned folder.
2. Copy the template file:
   ```bash
   cp auth_backend/auth_backend.env.template auth_backend/auth_backend.env
   ```
   In the newly created file, update the domain name to where the GhostFS Auth Backend will run on.
3. To generate a self-signed SSL certificate and key for the GhostFS Server running on the same `domain_name` as above, execute the following command:
    ```bash
    ./gen_cert.sh <domain_name>
    ```
4. If needed, edit the `.env` to update the version of GhostFS Server and Auth Server.
5. To install a GhostFS server and a GhostFS Auth Backend running on PM2 with a Caddy reverse proxy, execute the following command:
    ```bash
    ./install_ghostfs.sh
    ```
    When requested, enter a username and password for the GhostFS Auth Backend `htpsswd`.
6. Verify that everything is running correctly using:
    ```bash
    sudo pm2 status
    ```
7. Verify that there are no errors in the logs of each process:
     ```bash
     sudo pm2 logs <id>
     ```
     
The GhostFS Auth Backend API is available at `https://domain_name:CADDY_PORT/fs/ok`

The GhostFS Server is available at `domain_name:3444`

The GhostFS Auth Server is available at `domain_name:3555`

The served data is stored in `/mnt/nextcloud-dp/nextcloud/data`

## Update

To update GhostFS Server and Auth Server to another version, edit `.env` with the new version number, then execute:
```bash
./get_ghostfs.sh
```

## Acknowledgements

The GhostFS Server, Client and Auth Server are developed by [Pouya Eghbali](https://github.com/pouya-eghbali) and [Nathalie Casati](https://github.com/idmple) as part of [Ako Grid](https://akogrid.com).

This research was supported by the EBRAINS research infrastructure, funded from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).
