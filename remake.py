from bs4 import BeautifulSoup
import requests
import pandas as pd

#add header and url

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
url = 'https://en.wikipedia.org/wiki/List_of_film_remakes_(A%E2%80%93M)'
r = requests.get(url)

#initilaise beautiful soup

soup = BeautifulSoup(r.content ,'html.parser')
table = soup.findAll('table')
#print('Table is ' , table)
rows = soup.findAll('tr')
row_list = list()

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)
    #print("Row is ", row)

# Create Pandas Dataframe and print it
df_bs = pd.DataFrame(row_list,columns=['Original','Remake','Notes'])
df_bs.set_index('Original',inplace=True)
print(df_bs.head())

# Exporting the data into csv
df_bs.to_csv('Remake_Movie.csv')
