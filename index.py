#!/usr/bin/env python3
import os, time
import subprocess
import socket
from urllib.parse import parse_qs


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    finally:
        s.close()
    return IP


def radio_action(url, name):
    subprocess.run(["mpc", "clear"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["mpc", "add", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["mpc", "play"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(1)
    print(f"<p>{name} Started!</p>")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

# Read the CSS from the file
with open("styles.css") as f:
    css = f.read()


# Parse the query string
query = parse_qs(os.environ.get("QUERY_STRING", ""))

if "action" in query:
    action = query["action"][0]

    if action == "start":
        subprocess.run(["mpc", "play"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("<p>Music Player Started!</p>")
    elif action == "stop":
        subprocess.run(["mpc", "stop"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("<p>Music Player Stopped!</p>")
    elif action == "hitradio": radio_action("http://orf-live.ors-shoutcast.at/oe3-q2a", "Hitradio O3")
    elif action == "krone": radio_action("http://raj.krone.at/kronehit-ultra-hd.aac", "Krone Hit")
    elif action == "viva": radio_action("https://stream.sepia.sk:8000/viva320.mp3", "Viva Slovakia")
    elif action == "fun": radio_action("http://stream.funradio.sk:8000/fun128.mp3", "Fun Radio Slovakia")
    elif action == "jemne": radio_action("https://stream.bauermedia.sk/melody-hi.mp3", "Slovakia Radio Jemne")
    elif action == "psyradio": radio_action("http://komplex2.psyradio.org:8010/stream/1/", "PSY Radio")
    elif action == "psyndora": radio_action("https://cast.magicstreams.gr:9111/stream/1/", "Psyndora Psytrance")
    elif action == "bucharest": radio_action("http://62.210.105.16:7000/stream/1/", "Bucharest - Deep House")
    elif action == "nature": radio_action("http://mpc2.mediacp.eu:8376/stream/1/", "Ambient Nature Sleep")
    elif action == "chillout": radio_action("http://2.58.194.54:8840/stream/1/", "Ambient Chillout Essentials")
    elif action == "mozart": radio_action("http://37.251.146.169:8300/stream/1/", "Classic Mozart")

menu = [
    {"link": "?action=start", "name": "Start Music Player"},
    {"link": "?action=stop", "name": "Stop Music Player"},
    {"link": "?action=hitradio", "name": "Austria Hitradio O3"},
    {"link": "?action=viva", "name": "Slovakia Viva"},
    {"link": "?action=krone", "name": "Austria Krone Hit"},
    {"link": "?action=fun", "name": "Slovakia Fun Radio"},
    {"link": "?action=psyradio", "name": "PSY Radio"},
    {"link": "?action=jemne", "name": "Slovakia Radio Jemne"},
    {"link": "?action=psyndora", "name": "Psyndora Psytrance"},
    {"link": "?action=bucharest", "name": "Bucharest Deep House"},
    {"link": "?action=nature", "name": "Ambient Nature Sleep"},
    {"link": "?action=chillout", "name": "Ambient Chillout Essen"},
    {"link": "?action=mozart", "name": "Classic Mozart"},
]

print(f"""
<html>
<head>
    <style>
    {css}
    </style>
</head>
<body>
    <table><tr><td align=center colspan=2><a href="http://{get_ip_address()}">{get_ip_address()}</a></td></tr>
""")


for i in range(0, len(menu), 2):
    print('<tr>')
    print(f'<td><a href="{menu[i]["link"]}">{menu[i]["name"]}</a></td>')
    if i+1 < len(menu):
        print(f'<td><a href="{menu[i+1]["link"]}">{menu[i+1]["name"]}</a></td>')
    print('</tr>')

print("""
    </table>
</body>
</html>
""")

