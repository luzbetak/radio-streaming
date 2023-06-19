#!/usr/bin/env python3
import os, time
import subprocess
from urllib.parse import parse_qs

def radio_action(url, name):
    subprocess.run(["mpc", "clear"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["mpc", "add", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["mpc", "play"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(1)
    print(f"<p>{name} Started!</p>")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

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
    elif action == "hitradio":
        radio_action("http://orf-live.ors-shoutcast.at/oe3-q2a", "Hitradio O3")
    elif action == "krone":
        radio_action("http://raj.krone.at/kronehit-ultra-hd.aac", "Krone Hit")
    elif action == "viva":
        radio_action("https://stream.sepia.sk:8000/viva320.mp3", "Viva Slovakia")
    elif action == "fun":
        radio_action("http://stream.funradio.sk:8000/fun128.mp3", "Fun Radio Slovakia")
    elif action == "psyradio":
        radio_action("http://komplex2.psyradio.org:8010/stream/1/", "PSY Radio")
    elif action == "psyndora":
        radio_action("https://cast.magicstreams.gr:9111/stream/1/", "Psyndora Psytrance")
    elif action == "bucharest":
        radio_action("http://62.210.105.16:7000/stream/1/", "Bucharest - Deep House")
    elif action == "nature":
        radio_action("http://mpc2.mediacp.eu:8376/stream/1/", "Ambient - Nature Radio Sleep")
    elif action == "chillout":
        radio_action("http://2.58.194.54:8840/stream/1/", "Ambient - Chillout Essentials")

menu = [
    {"link": "http://192.168.1.229", "name": "Living Room Radio"},
    {"link": "?action=start", "name": "Start Music Player"},
    {"link": "?action=stop", "name": "Stop Music Player"},
    {"link": "?action=hitradio", "name": "Austria - Hitradio O3"},
    {"link": "?action=krone", "name": "Austria - Krone Hit"},
    {"link": "?action=viva", "name": "Slovakia - Viva"},
    {"link": "?action=fun", "name": "Slovakia - Fun Radio"},
    {"link": "?action=psyradio", "name": "PSY Radio"},
    {"link": "?action=psyndora", "name": "Psyndora Psytrance"},
    {"link": "?action=bucharest", "name": "Bucharest - Deep House"},
    {"link": "?action=nature", "name": "Ambient - Nature Radio Sleep"},
    {"link": "?action=chillout", "name": "Ambient - Chillout Essentials"},
]

print("""
<html>
<head>
    <style>
    body {{
        font-family: Arial, sans-serif;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    td {{
        padding: 10px;
        border: 1px solid #ccc;
    }}
    a {{
        text-decoration: none;
        color: #333;
    }}
    tr:nth-child(even) {{
        background-color: #f2f2f2;
    }}
    </style>
</head>
<body>
    <table>
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

