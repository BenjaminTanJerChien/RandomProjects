import requests
from bs4 import BeautifulSoup as bs

username = input("Input Github Username: ")

url = f"https://github.com/{username}/"
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {"alt" : "Avatar"})["src"]
print(profile_image)
