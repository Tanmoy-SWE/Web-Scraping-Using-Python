import requests
import os
import bs4


url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd',exist_ok = True)

while not url.endswith('#'):
    #Finding the URL of the comic image.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else :
        comicUrl = 'https:'+comicElem[0].get('src')
        # Download the page
        print("Downloading page %s..." % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        #soup = bs4.BeautifulSoup(res.text, 'html.parser')
        #save the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        #Getting the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com'+prevLink.get('href')

print('Done')