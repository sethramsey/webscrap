from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

'''''''''''''''
####### Part 1 #####

url = 'https://coinmarketcap.com/'

page = urlopen(url)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

crypto_data = soup.findAll("td")
		
print(crypto_data[61].text)

                                                                    #how to add symbol?
counter = 1
for x in range(5):
    number = crypto_data[counter].text
    name = crypto_data[counter+1].text
    current_price = float(crypto_data[counter +2].text.strip('$').replace(',',''))
    change = float(crypto_data[counter+3].text.strip('%'))
    corresponding_price = round(current_price / (1 +(change/100)),2)
    
    print(f'No.{number}')
    print(f'Name: {name}')
    print(f'Current Price: {current_price}')
    print(f'Change over the past 24 hours: {change}')
    print(f'Corresponding price: {corresponding_price}')


    counter += 11


'''''''''''''''



##### Part 2 #######
webpage = 'http://quotes.toscrape.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)


quotes = soup.findAll("div", class_="quote")

author_list = {}
text_dict = {}
tag_dict = {}
text_list = []

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small',class_='author').text
    tags = quote.find('div',class_='tags').text
    #print(text)
    #print(author)
    #print(tags)
    
    text_list = text_list.append(text)
    
    ###make this a author in author_dic
    if author_dict.get(author) is not None:
        author_dict[author] +=1
    else:
        author_dict[author] += 1

    if text_dict[text] ==1:
        text_dict[text] +=1
    else:
        text_dict[text] ==1

    if tag_dict[tags] ==1:
        tag_dict[tags] += 1
    else :
        tag_dict[tags] == 1

author_count = author_dict.count()

####use polty from scarps
