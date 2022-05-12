from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import re

url = "https://www.skku.edu/skku/campus/skk_comm/news.do"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.find_all("div", class_='news_listCont')

titles = []
for x in title:
    titles.append(re.sub(r"[\n\t\s]*", "", x.find("a").get_text()))
titles

for i in range(0, len(titles)):
    print(str(i + 1) +"번 뉴스:", titles[i])