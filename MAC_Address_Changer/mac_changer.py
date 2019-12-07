#!/user/bin/env python

# The first byte of the mac address cannot be odd. Add input validation to verify.

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface or not options.new_mac:
        parser.error("[-] Please specify an interface and mac, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def verify_mac_change(interface, new_mac):
    ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        if not ifconfig_result == mac_address_search_result.group(0):
            print("[-] MAC Address for " + interface + " was unable to be changed. Retaining old MAC address: " +
                  mac_address_search_result.group(0))
        else:
            print("[-] MAC Address for " + interface + " successfully changed to: " + new_mac)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()
change_mac(options.interface, options.new_mac)
verify_mac_change(options.interface, options.new_mac)
