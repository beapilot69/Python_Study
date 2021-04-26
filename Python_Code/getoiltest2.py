from bs4 import BeautifulSoup
import requests,re ,os

def get_bs_obj():
    url = "https://www.knoc.co.kr"
    result = requests.get(url)  #get html
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

bs_obj = get_bs_obj()
cost_all = bs_obj.find("table", {"class":"tbl_domestic"})

data = []

for tr in cost_all.find_all('tr'):
    tds = list(tr.find_all('td'))
    data.append(tds[0].text)

costOfGasoline = float(data[0])
costOfDiesel = float(data[1])

print(costOfGasoline)
print(costOfDiesel)

# CAN NOT USING KOREAN!!