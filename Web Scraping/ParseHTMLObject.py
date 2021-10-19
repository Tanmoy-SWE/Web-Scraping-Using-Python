import bs4
import ImportObject

exampleFile = open('Example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'html.parser')
elems = exampleSoup.select('#author')
print(elems)
# -->  [<span id="author">Tanmoy Ahsan</span>]
print(elems[0])
# --> <span id="author">Tanmoy Ahsan</span>
#That means we have only one element using this id
print(elems[0].getText())
# --> 'Tanmoy Ahsan'
print(elems[0].attrs)
# --> {'id': 'author'}

pElems = exampleSoup.select('p')
print(str(pElems[0]))
# --> <p>Watch my <strong>Github Profile</strong>from here<a href="GitHub : https://github.com/Tanmoy-SWE">MY GitHub</a>.</p>
print(pElems[0].getText())
# --> Watch my Github Profilefrom here MY GitHub.
print(str(pElems[1]))
# --> <p class="slogan">GitHub : https://github.com/Tanmoy-SWE</p>
print(str(pElems[1].getText()))
# --> GitHub : https://github.com/Tanmoy-SWE
#Same goes for next p elements
print(str(pElems[2]))
print(str(pElems[2].getText()))
#.getText() method returns the text inside the element