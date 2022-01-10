import getpass
import sys
import telnetlib

HOST = "192.168.88.141"  #router telnet access ip
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")     #router user name
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")  #router user password
    tn.write(password + "\n")

tn.write("enable\n")             # \n mins>next line
tn.write("1234\n")               #router enable password



print tn.read_all()

