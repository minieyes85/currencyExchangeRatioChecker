import requests
import re
from bs4 import BeautifulSoup

# 현재환율 구하기
def find_ex_cur(cur):
    
    # 환율 구하기
    headers = {'User-Agent':'Mozilla/5.0'}
    URL = 'https://kr.investing.com/currencies/'+cur+'-krw'
    

    resp = requests.get(URL, headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    suup = soup.find('span',{'data-test':'instrument-price-last'})
    cur_exch_str = re.sub(",","",suup.text)
    cur_exch = float(cur_exch_str)
    
    if cur == "jpy":
        jpy_exch = cur_exch * 100
        return "{:.2f}".format(jpy_exch)
    else:
        return cur_exch_str