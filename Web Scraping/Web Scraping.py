import webbrowser as wb
import requests
website = 'https://automatetheboringstuff.com/files'
try:
  wb.open(website)
except:
  print("Invalid website url.")

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
# --> <class 'requests.models.Response'>
#By writing this we can get all the texts of the website
text = res.text
print(res.text)

#Opening a file to write on it
textFile = open('AutomatePython.txt','w')
try :
  textFile.write(text)
  print("The text is written successfully.")
except :
  print("The file doesn't exist.")
