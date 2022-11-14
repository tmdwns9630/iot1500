from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver


html = urlopen ("https://www.naver.com/")
bsObject = BeautifulSoup(html, "html.parser")

# print(bsObject.head.title)

# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))
    
# print("가져오기")  
# print(bsObject.head.find("meta",{"name":"description"}))

for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))