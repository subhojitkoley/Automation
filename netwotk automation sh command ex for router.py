import getpass
import sys
import telnetlib

HOST = "192.168.88.141"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("1234\n")
tn.write("sh ip int br\n")
tn.write("sh ip route\n")
tn.write("exit\n")


print tn.read_all()

