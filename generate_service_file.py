#!/bin/python
from subprocess import call

def file_create(server, port, user):
    """ Create the service file
    with user input.
    """
    file = open("secure-tunnel.service", "w")

    print("Creating service file..."),

    # Service file contents
    file.write("""[Unit]
    Description=secureTunnel - secure tunnel daemon
    After=network.target
    Documentation=https://github.com/ArctiqTeam/secureTunnel

    [Service]
    ExecStart=/usr/bin/ssh -NT -L 8001:{}:{} {}@{}
    RestartSec=5
    Restart=always

    [Install]
    WantedBy=multi-user.target""".format(server, port, user, server))

    file.close()
    print("[OK]")
 
def main():
    """ Start the program, call the
    file_create function, move the service
    file and then start it.
    """
    print ("Welcome to the secureTunnel generator.")

    # Ask the user for some details
    server = raw_input("Target host: ")
    port = raw_input("Target port: ")
    user = raw_input("User to login as: ")
    
    file_create(server, port, user)

    # Move service file to proper location
    print("Moving service file to '/etc/systemd/system/'..."),
    call(["mv", "secure-tunnel.service", "/etc/systemd/system/"])
    print("[OK]")

    # Start the service
    print("Starting the service..."),
    call(["systemctl", "start", "secure-tunnel.service"])
    print("[OK]")

if __name__ == "__main__":
   main()
