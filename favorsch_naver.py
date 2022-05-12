from bs4 import BeautifulSoup
import requests
from datetime import datetime

#headers 정의 후 url 뒤에 넣어주는게 필요
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('span', 'item_title')

search_rank_file = open("rankresult.txt","w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위"+result.get_text()+"\n")
    print(rank,"위 : ",result.get.text(),"\n")
    rank += 1