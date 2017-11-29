# secureTunnel
secureTunnel - secure tunnel daemon

## Requirements
Below are the requirements needed to use the script:
* [SSH keys](#SSH-Keys) are added to the target host
* Script is run as root or user with sudo privileges

## Usuage
To use this application, run the script:
```
chmod u+x generate_service_file.py
./generate_service_file.py
```
Once the script has been run, verify the service has successfully started:
```
systemctl status sercure-tunnel.service
```
The tunnel can also be verified by trying to pull a file that the target host is serving on the web (ex. the target host in the example has `bootstrap.py` located at `/var/www/html/pub/`:
```
curl -O localhost:8001/pub/bootstrap.py
```

## SSH Keys
To add keys to the target host:
1. Generate RSA key pair and follow steps (if does not exist):
```
ssh-keygen -t rsa
```
2. Copy the public key to the target host:
```
ssh-copy-id <user>@<target_host>
```
