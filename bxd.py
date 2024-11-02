from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
t=[]
t2=[]
ti=[]
t3=[]
"""本科生院"""
url='https://www.bkjx.sdu.edu.cn/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}
response = requests.get(url,headers=headers).text.encode("ISO-8859-1").decode("utf-8")
soup = BeautifulSoup(response, 'html.parser')
all_herf = soup.find_all(class_='leftNews1')
for herf in all_herf:
    title=herf.find_all('a')
    for tittles in title:
        t.append(tittles.string)
all_time=soup.find_all(class_='timeClass')
for times in all_time:
    ti.append(times.string)
"""研究生院"""
url1 = 'https://grad.sdu.edu.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}
response = requests.get(url1, headers=headers).text.encode("ISO-8859-1").decode("utf-8")
soup1 = BeautifulSoup(response, 'html.parser')
all_Tittle = soup1.find_all(class_="clearfix")
for Tittles in all_Tittle:
    Tittle = Tittles.find_all('a')
    for Tittl in Tittle:
        t2.append(Tittl.string)
all_time = soup1.find_all(class_="clearfix")
for times in all_time:
        ti = times.find_all(class_="fr")
        for tittles in ti:
            t3.append(tittles.string)

df=pd.DataFrame(columns=['title1','time1','url1'])
for i in range(len(t)):
  df.loc[len(df)] = t[i],ti[i],url
df.to_excel("shanda.xlsx")



