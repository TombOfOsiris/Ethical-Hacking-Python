#!/user/bin/env python

import subprocess

subprocess.run("ifconfig eth0 down", shell=True)
subprocess.run("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.run("ifconfig eth0 up", shell=True)
subprocess.run("ifconfig", shell=True)
