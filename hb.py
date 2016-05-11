#!/usr/bin/env python3
from slackclient import SlackClient
import socket
import urllib.request


token = open("creds", "rt").read().strip()
sc = SlackClient(token)
print(sc.api_call("api.test"))


# get hostname, local ip, public ip, and the reverse dns of the public ip.
host = socket.gethostname()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("8.8.8.8",80))
    local_ip = s.getsockname()[0]

public_ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode('ascii')
public_rdns = socket.gethostbyaddr(public_ip)[0]
message = "This is '{0}' with local IP of {1}, and public IP of {2} ({3})".format(host, local_ip, public_ip, public_rdns)
print("Sending " + message)
#sys.exit()

print(sc.api_call(
    "chat.postMessage", channel="#heartbeat",
    text=message,
    username=host + " bot", icon_emoji=':robot_face:'))

