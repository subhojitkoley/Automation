import getpass
import sys
import telnetlib
#line 1 to 15 is fix code///then line 17 to 21 is router/switch configration command
HOST = "192.168.88.166"     #r/sw telnet-access ip
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
tn.write("conf t\n")
tn.write("int s 0/0\n")
tn.write("ip add 1.0.0.1 255.0.0.0\n")
tn.write("no shut\n")
tn.write("int s 0/2\n")
tn.write("ip add 2.0.0.1 255.0.0.0\n")
tn.write("no shut\n")
tn.write("int s 0/0\n")
tn.write("ip add 1.0.0.1 255.0.0.0\n")
tn.write("router rip\n")      #rip/ospf/eigrp
tn.write("net 1.0.0.0\n")
tn.write("net 2.0.0.0\n")
tn.write("end\n")
tn.write("exit\n")


print tn.read_all()