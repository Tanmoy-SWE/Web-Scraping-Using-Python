import requests
import os
import bs4

url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd',exist_ok = True)
while not url.endswith('#'):
    #Download the page
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')