import getpass
import sys
import telnetlib

HOST = "192.168.88.151"  #switch telnet access ip
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")     #switch user name
tn.write(user + "\n")           #tn is a vareable/u can use any in (tn)
if password:
    tn.read_until("Password: ")  #switch user password
    tn.write(password + "\n")

tn.write("enable\n")             # \n mins>next line
tn.write("1234\n")               #switch enable password
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name voice\n")
tn.write("vlan 3\n")
tn.write("name message\n")
tn.write("exit\n")
print tn.read_all()

