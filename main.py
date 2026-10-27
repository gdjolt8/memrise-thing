import requests
import json
import os
from pathlib import Path

headers_1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Alt-Used": "community-courses.memrise.com",
    "Connection": "keep-alive",
    "Host": "community-courses.memrise.com",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:158.0) Gecko/20100101 Firefox/158.0",
}



print ("Auto-Memriser: ME © 2026")

s_id = ""
csrf = ""
username = ""
c_url = ""
try:
    file = open(f"{str(Path.home())}/am.txt", "r", encoding="utf-8")
    print("found defaults from save file")
    data = json.loads(file.read())
    s_id = data["s_id"]
    csrf = data["csrf"]
    username = data["username"]
    c_url = data["c_url"]
except:
    print("for these steps you will need to go into your browser and fetch these cookies for this software to work")
    s_id = input("what is your session id? ")
    csrf = input("what is your csrf token? ")
    print("then, you need memrise details")
    username = input("what is your username? ")
    c_url = input("what is the course url? ")

y_o_n = input("set as env so you don't have to do ts every time? your input doesn't matter but still")

with open(f"{str(Path.home())}/am.txt", "w", encoding="utf-8") as file:
    file.write(json.dumps({"s_id": s_id, "csrf": csrf, "username": username, "c_url": c_url}))
    print("saved")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:158.0) Gecko/20100101 Firefox/158.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://community-courses.memrise.com/aprender/speed?course_id=5577172",
    "Content-Type": "application/json",
    "X-CSRFToken": csrf,
    "x-correlation-id": "13022b80-d9b9-4065-ac52-79b7e905672e",
    "x-client-type": "web",
    "x-timezone": "America/New_York",
    "x-os": "windows",
    "x-os-version": "10",
    "x-device-type": "desktop",
    "x-browser": "Firefox",
    "x-browser-version": "158.0",
    "Origin": "https://community-courses.memrise.com",
    "Alt-Used": "community-courses.memrise.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
    "TE": "trailers",
}

cookies = {
    "g_state": '{"i_l":1,"i_ll":1791501485307,"i_b":"pGyqFlacVZCSN27CR81bcIDU8IJZU6q9I8sTnCj+sGY","i_e":{"enable_itp_optimization":24},"i_et":1791501485307}',
    "sessionid_2": s_id,
    "colorSchemePreference": "auto",
    "colorSchemeResolved": "dark",
    "i18next": "en",
    "csrftoken": c_url,
}
c_id = ""
for i in range(len(c_url.split("/"))):
    if c_url.split("/")[i] == 'course':
        c_id = c_url.split("/")[i+1]

url = "https://community-courses.memrise.com/v1.25/progress/register/"
max_search = 1000
url_1 = f"https://community-courses.memrise.com/ajax/leaderboard/course/{c_id}/?period=week&how_many={max_search}"
get_p = requests.get(
    url=url_1,
    headers=headers_1,
    cookies=cookies
)




l = json.loads(get_p.text)
v = None
for i in l["rows"]:
    if i["username"] == username:
        v = i

if v == None:
    print(f"{username} not found in course. check course id")
    exit(1)

print(f"you have {v["points"]} points and are in {v["position"]}th place on the weekly leaderboard")

points = int(v["points"])
print("you have a couple of options.\n(set) points to specific value (e.g set 10000) \n(add) points to number (e.g add 10000)")
ans = input("")
cmd = ans.split(" ")
new_p = 0
if cmd[0] == "set":
    if len(cmd) > 1:
        new_p = int(cmd[1]) - points
        print(f"set to ... {new_p + points}")
    else:
        print("expected number")
        exit(1)
elif cmd[1] == "add":
    if len(cmd) > 1:
        new_p = int(cmd[1])
        print(f"add {new_p} to... {points}")
    else:
        print("expected number")
        exit(1)
else:
    print(f"invalid command {cmd[0]} no points for you")
    exit(1)
payload = {"events":[{"box_template":"multiple_choice","bonus_points":0,"course_id":int(c_id),"time_spent":4156,"given_answer":"ernst","learning_element":"ernst","definition_element":"serious","test_id":"b8957ac3-047c-40c7-a456-f3f55a813d94","mem_id":None,"created_date":1773831748,"current_streak":11,"growth_level":11,"learnable_id":17205485699330,"next_date":1797201682,"last_date":1793054195,"not_difficult":False,"total_streak":11,"when":1793054195,"correct":11,"attempts":11,"interval":48,"points":new_p,"score":1,"starred":False,"ignored":False},{"box_template":"multiple_choice","bonus_points":0,"course_id":5577172,"time_spent":701,"given_answer":"das Rindfleisch","learning_element":"besorgt","definition_element":"worried","test_id":"e7687169-7ddb-4f5c-997d-afe7ff627183","mem_id":None,"created_date":1773791360,"current_streak":0,"growth_level":10,"learnable_id":17205484978434,"next_date":1793097617,"last_date":1793054196,"not_difficult":False,"total_streak":-1,"when":1793054196,"correct":10,"attempts":11,"interval":0.5,"points":0,"score":0,"starred":False,"ignored":False},{"box_template":"multiple_choice","bonus_points":0,"course_id":5577172,"time_spent":712,"given_answer":"fangen","learning_element":"faul","definition_element":"lazy","test_id":"31a65eeb-162f-4967-8ddd-18a5c4352271","mem_id":None,"created_date":1773831748,"current_streak":0,"growth_level":10,"learnable_id":17205485764866,"next_date":1793097531,"last_date":1793054197,"not_difficult":False,"total_streak":-1,"when":1793054197,"correct":10,"attempts":11,"interval":0.5,"points":0,"score":0,"starred":False,"ignored":False},{"box_template":"multiple_choice","bonus_points":0,"course_id":5577172,"time_spent":802,"given_answer":"fünf,five","learning_element":"fleißig","definition_element":"hard-working","test_id":"246e7076-a233-4b3b-a286-a7096d1994e6","mem_id":None,"created_date":1773831748,"current_streak":0,"growth_level":10,"learnable_id":17205485830402,"next_date":1793097923,"last_date":1793054198,"not_difficult":False,"total_streak":-1,"when":1793054198,"correct":10,"attempts":11,"interval":0.5,"points":0,"score":0,"starred":False,"ignored":False}],"sync_token":0,"limit":0}


response = requests.post(
    url,
    headers=headers,
    cookies=cookies,
    json=payload,
)

if response.status_code == 200:
    print(f"success w/ {url_1}")
