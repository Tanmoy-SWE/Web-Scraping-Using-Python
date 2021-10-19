import webbrowser as wb
import requests
import bs4
#bs4 = beautifulSoup
website = 'https://nostarch.com'
res = " "
try:
 # wb.open(website)
  res = requests.get(website)
except:
  print("Invalid website url.")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))
# -->  <class 'bs4.BeautifulSoup'>
exampleFIle = open('Example.html')
exampleSoup = bs4.BeautifulSoup(exampleFIle, 'html.parser')
print(type(exampleSoup))
# -->  <class 'bs4.BeautifulSoup'>