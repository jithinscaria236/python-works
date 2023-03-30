import paramiko
from paramiko import SSHClient
from scp import SCPClient
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('3.80.68.166', username='ec2-user', key_filename='test.pem')

stdin, stdout, stderr = ssh.exec_command('pwd')
print (stdout.readlines())
with SCPClient(ssh.get_transport()) as scp:
    scp.put('my_file.txt', 'my_file.txt')
ssh.close()
