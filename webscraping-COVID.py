# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req =Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

print(soup.title.text)

table_rows = soup.findAll("tr")

#print(table_rows[:2])
state_death_ratio=""
state_best_testing = ""
state_worst_testing = ""
highest_death_ratio = 0.0
best_test_ratio = 0.0
worst_test_ratio = 1000.0



for row in table_rows[2:53]:
    td = row.findAll("td")
    #print(td)
    state = td[1].text.strip('\n')
    total_cases = int(td[2].text.replace(',',''))
    total_deaths = int(td[4].text.replace(',',''))
    total_tested = int(td[10].text.replace(',',''))
    population = int(td[12].text.replace(',',''))
    
    
    death_ratio = total_deaths/total_cases
    test_ratio = total_tested/population

    if death_ratio > highest_death_ratio:
        highest_death_ratio=death_ratio
        state_death_ratio=state
    
    if test_ratio > best_test_ratio:
        best_test_ratio=test_ratio
        state_best_testing=state

    if test_ratio< worst_test_ratio:
        worst_test_ratio = test_ratio
        state_worst_testing = state

    #print(death_ratio)
    #print(test_ratio)
    

print("State with the highest death ratio is:",state_death_ratio)
print(f'Death Ratio: {highest_death_ratio:.2%}')
print()
print()
print('State with the the best testing ration is:',state_best_testing)
print(f'Test ratio: {best_test_ratio:.2%}')
print()
print()
print('State with the worst testing ratio is',state_worst_testing)
print(f'Test Ratio: {worst_test_ratio:.2%}')






#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

