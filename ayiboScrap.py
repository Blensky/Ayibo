import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

host = "https://ayibopost.com"
res = requests.get(f'{host}/category/podcast/')

soup = bs(res.text, 'html.parser')

content_list = soup.find_all('article', {'class': 'post--vertical'})
article_list = []

for div in content_list:
    titre = div.find('h3', {'class': 'post__title'}).get_text()
    date = div.find('time', {'class': 'time published'}).get_text()
    
    article_list.append({
        "Titre": titre,
        "Date": date,
    })

print("Create Dataframe ...")
data = pd.DataFrame(article_list)
data.to_csv('ayiboScrap.csv')
print("Saving Dataframe to CSV")

print("\nEND SCRIPT")
