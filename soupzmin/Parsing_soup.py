import requests
from bs4 import BeautifulSoup
# from PIL import Image
# from io import BytesIO


search=input('Search for: ')
params={
    'q': search
}
r=requests.get('https://www.bing.com/search', params=params)


soup=BeautifulSoup(r.text, 'html.parser')
results=soup.find('ol', {'id': 'b_results'})
links=results.findAll('li', {'class':'b_algo'})

for item in links:
    item_text=item.find('a').text
    item_href=item.find('a').attrs['href']

    if item_text and item_href:
        print(item_text)
        print(item_href)