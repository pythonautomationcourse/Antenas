#!/usr/bin/env  python3

from netmiko import SSHDetect
from netmiko import BaseConnection
from netmiko import ConnectHandler
from netmiko import Netmiko
from time import sleep
import logging

logging.basicConfig(filename='logg.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


remote_device = {
    'device_type': 'autodetect',
    'host': '192.168.9.140',
    'username': 'ytgadmin',
    'password': 'admin'
}

guesser = Netmiko(**remote_device, verbose=True)

guesser.write_channel("restart\r\n")
# print(output)
sleep(0.5)
output = guesser.read_channel()
print(output)

guesser.write_channel("y\r\n")
# print(output)
sleep(0.5)
output = guesser.read_channel()
print(output)

# guesser.write_channel("\n")
# sleep(0.5)
# output = guesser.read_channel()
# print(output)
guesser.disconnect()