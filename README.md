**Installation**
````
1) Spin docker container
2) Create admin user
3) Modyfy tokens
4) Run send event as backround service
5) Configure home-assistant with yaml config files
````
**Automation hints**
````
Host network is rather mandatory
Docker container can be run as a /etc/systemd/system/foo.service (root)
Send event service can be run as autostart script (normal user)
````