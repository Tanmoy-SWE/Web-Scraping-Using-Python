#Step - 0 :- Install all requirements

import requests
from bs4 import BeautifulSoup
url = "https://github.com/Tanmoy-SWE"

#Step - 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#Step - 2 : Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
#Printing the html content
#print(soup)
#Printing the HTML content in a more organized way.
#print(soup.prettify())
#Show what is HTML tree
#Step - 3 : HTML tree traversal
#Commonly used type of objects
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment
# title = soup.title
# print(title) # 1. Tag
# print(title.string) # 2. NavigableString
# print(soup) # 3. BeautifulSoup

#Get the Title of Navigable String
title = soup.title
print(title)

#Get all the paragraphs from the page
paras = soup.find_all('p')
#paras is a list
print(paras)
#first paragraph
print(paras[0])
#Get all anchor tags from the page
anchors = soup.find_all('a')
print(anchors)
#Get all the links in the page
all_links = []
for link in anchors:
    all_links.append(link.get('href'))
#Get the first paragraph
firstParagraph = soup.find('p')
print(firstParagraph)
#Get classes of any element in the page
print(firstParagraph['class'])

#Find all the elements with class Lead
print(soup.find_all('p',class_='lead'))

#Get the text from the tags/soup
text = soup.find_all('p')[0].get_text()
print(text)
