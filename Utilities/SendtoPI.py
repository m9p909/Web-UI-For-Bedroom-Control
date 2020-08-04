#This utility sends the pyrest folder to a rasppi using scp
import paramiko
from scp import SCPClient
import os
server = "192.168.0.188"
port = "22"
user = "pi"
password = "***REMOVED***" #make sure this is blank before committing
os.chdir('..')
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())


scp.put("./pyrest",remote_path = "/home/pi/projects/",recursive = True)
