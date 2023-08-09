import requests
from bs4 import BeautifulSoup


#to prevent being flagged as a bot change the headers often if you use this often
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Language': 'en-US,en;q=0.9',
 'Accept-Encoding': 'gzip, deflate, br'}

print("Enter the website to scrape <h1> and <h2> tags from (enter the entirety of the url): ")
inputurl = input()

url = str(inputurl)

##url = 'https://www.donaldjtrump.com/agenda47' ##Example URL, try this out if your input isnt working
##very funny h-tags... ; )

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html,'html5lib')

hdoc1 = soup.find_all('h1')
hdoc2 = soup.find_all('h2')




print(hdoc1)
print(hdoc2)

with open('myhtags.txt', 'a') as f:
    f.write(str(hdoc1))
    f.write(str(hdoc2))

#whatever is your current working directory is where the file will be saved, please be aware
