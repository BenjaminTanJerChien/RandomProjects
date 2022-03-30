import requests
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime
import json

username = input("Input Instagram Username: ")


link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'


now = datetime.now()
time = int(now.timestamp())
response = requests.get(link)
csrf = response.cookies['csrftoken']
password = "MYERadmin2002"

payload = {
    'username': "myermovement",
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}: {password}',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

login_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "x-csrftoken": csrf
}

login_response = requests.post(login_url, data=payload, headers=login_header)
json_data = json.loads(login_response.text)

if json_data["authenticated"]:

    print("login successful")
    cookies = login_response.cookies
    cookie_jar = cookies.get_dict()
    csrf_token = cookie_jar['csrftoken']
    print("csrf_token: ", csrf_token)
    session_id = cookie_jar['sessionid']
    print("session_id: ", session_id)
else:
    print("login failed ", login_response.text)


userurl = f"https://www.instagram.com/{username}/"
r = requests.get(userurl)
soup = bs(r.content, "html.parser")
print(soup) #login required
profile_image = soup.find("img", {"alt" : f"{username}'s profile picture"})
print(profile_image)
