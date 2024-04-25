import requests
from bs4 import BeautifulSoup

target_url = input("Enter your target website: ")
found_links = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
       found_link = link.get('href')
       if found_link:
           if '#' in found_link:
               found_link = found_link.split('#')[0]
           if target_url in found_link and found_link not in found_links:
               found_links.append(found_link)
               print(found_link)
               crawl(found_link) #recursive

crawl(target_url)