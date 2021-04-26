# -*- coding: utf-8 -*-       
from bs4 import BeautifulSoup
import requests, re, os

def get_bs_obj():
    url = "https://m.map.naver.com/directions/?ename=경기대학교%20수원캠퍼스제2공학관&ex=127.0400132&ey=37.3003339&edid=19213652&incomeUrl=https%3A%2F%2Fm.map.naver.com%2Fsearch2%2Fsearch.naver%3Fquery%3D%25EA%25B2%25BD%25EA%25B8%25B0%25EB%258C%2580%25ED%2595%2599%25EA%25B5%2590%2520%25EC%25A0%259C2%25EA%25B3%25B5%25ED%2595%2599%25EA%25B4%2580%26sm%3Dhty%26style%3Dv5#/publicTransit/list/%25EC%25A5%25AC%25EC%2594%25A8%2520%25EC%2588%2598%25EC%259B%2590%25EA%25B2%25BD%25EA%25B8%25B0%25EB%258C%2580%25EC%25A0%2590,127.0307218,37.3002402,127.0306410,37.3001930,false,37903682/%25EA%25B2%25BD%25EA%25B8%25B0%25EB%258C%2580%25ED%2595%2599%25EA%25B5%2590%2520%25EC%2588%2598%25EC%259B%2590%25EC%25BA%25A0%25ED%258D%25BC%25EC%258A%25A4%25EC%25A0%259C2%25EA%25B3%25B5%25ED%2595%2599%25EA%25B4%2580,127.0400132,37.3003339,,,false,19213652/0"
    result = requests.get(url)  #get html
    bs_obj = BeautifulSoup(result.content, "html.parser")
    #print(bs_obj)
    return bs_obj


bs_obj = get_bs_obj()
#bs_obj

for i in bs_obj.find("title"):
    Bus_all = bs_obj.find("meta")

print(Bus_all)

data = []