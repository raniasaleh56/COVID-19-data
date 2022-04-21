# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
print(response)
a = []
def get_stat(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all(class_ = "maincounter-number")
    for item in data:
        item.find("span")
        #print(item.text)
        a.append(item.text)
    return a
    
result = """\nTotal COVID-19 cases in the world:{}
\nTotal COVID-19 deaths in the world:{}
\nTotal COVID-19 patients recovered in the world:{}
"""
# * used to unpack items of an iterable like a list

if __name__ == "__main__":
    print(result.format(*get_stat(url)))
#---------------------------------------