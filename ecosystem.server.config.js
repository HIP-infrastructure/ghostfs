const data = "/mnt/nextcloud-dp/nextcloud/data";
const host = "0.0.0.0";
const suffix = "files";

module.exports = {
  apps: [
    {
      script: "su",
      cwd: __dirname,
      watch: false,
      args: `-s /bin/sh www-data -c "./GhostFS --server --root ${data} --bind ${host} --suffix ${suffix}"`,
    },
  ],
};
