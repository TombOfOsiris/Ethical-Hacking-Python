#!/user/bin/env python

import subprocess

interface = input("interface > ")
new_mac = input("new MAC > ")

print("[+] Changing MAC Address for " + interface + " to " + new_mac)

subprocess.run("ifconfig " + interface + " down", shell=True)
subprocess.run("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.run("ifconfig " + interface + " up", shell=True)
subprocess.run("ifconfig", shell=True)
