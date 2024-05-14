import requests 
from bs4 import BeautifulSoup

url = 'https://10.70.57.4:7001/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('span'):
        link_text = link.text
        print(link_text)
else:
    print('Error')