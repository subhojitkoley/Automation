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

tn.write("conf t\n")

for n in range (2 , 10):
    tn.write("vlan " +str(n) + "\n")
    tn.write("name data_vlan_" +str(n) + "\n")

tn.write("end\n")              
tn.write("exit\n")
print tn.read_all()