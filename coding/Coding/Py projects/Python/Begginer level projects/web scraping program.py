import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user
r = req.get(url)
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)


