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


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


def verify_mac_change(options, current_mac):
    if not options.new_mac == current_mac:
        print("[-] MAC Address for " + options.interface + "was unable to be changed. \n[-] Retaining old MAC "
                                                           "address: " + current_mac)
    else:
        print("[-] MAC Address for " + options.interface + " successfully changed to: " + options.new_mac)


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
verify_mac_change(options, current_mac)
print("Current MAC = " + str(current_mac))
