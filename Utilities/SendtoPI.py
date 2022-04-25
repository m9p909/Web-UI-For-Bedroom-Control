#!/usr/bin/env python3

#This utility sends the pyrest folder to a rasppi using scp
import paramiko
from scp import SCPClient
import os
import typer

app = typer.Typer()

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

@app.command()
def sendToPi(server: str = "192.168.7.75"):
    port = "22"
    user = "pi"
    remote_path = "/home/pi/projects/"
    os.chdir('..')
    password = typer.prompt("pi password: ", hide_input=True)
    ssh = createSSHClient(server, port, user, password)
    transport = ssh.get_transport()
    ssh.exec_command("rm -r "+remote_path)
    if transport:
        scp = SCPClient(transport)
        scp.put("./pyrest",remote_path=remote_path ,recursive = True)
    else:
        print("ssh was null, connection failed")

if __name__ =="__main__":
    app()
