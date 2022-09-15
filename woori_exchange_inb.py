import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

def get_latest_cur_exch_table(year, month, day):
    
    driver.get("https://spot.wooribank.com/pot/Dream?withyou=FXXRT0011")

    time.sleep(0.5)

    select_year = Select(driver.find_element(By.XPATH,'//*[@id="SELECT_DATEY"]'))
    select_month = Select(driver.find_element(By.XPATH,'//*[@id="SELECT_DATEM"]'))
    select_day = Select(driver.find_element(By.XPATH,'//*[@id="SELECT_DATED"]'))
    
    select_year.select_by_value(year)
    select_month.select_by_value(month)
    select_day.select_by_value(day)

    time.sleep(0.5)
    
    driver.find_element(By.XPATH,'//*[@id="frm"]/fieldset/div/span/input').click()

    time.sleep(0.5)

    # result = driver.find_element(By.XPATH,'//*[@id="resultArea"]')

    
    
    # result_html = BeautifulSoup(result_raw_html, 'html.parser')
    # result_body = result_html.find('table').find('tbody')

    # result_table = pd.read_html(result_body)
    
    # print(result_body)
    
    result = driver.find_element(By.XPATH,'//*[@id="fxprint"]')
    result_raw_html = result.get_attribute('innerHTML')
    
    # print(result_raw_html)
    
    # table_html = BeautifulSoup(result_raw_html, 'html.parser')
    
    driver.close()
    
    
    df_list = pd.read_html(result_raw_html,header=1)
    df = pd.DataFrame(df_list[0])
    # print(result_df_list)
    df.set_index('통화표시')
    
    # print(type(df))
    # print(df)
    # print(df.loc[df['통화표시'] == 'USD',['통화표시','매매기준율','기준환율']])
    # print(result)
    
    
    # print(table_html)
    
    # tr_raw = result_body.find_all('tr')
    # tr = []
    # for i in tr_raw:
    #     print(i)
    #     target = BeautifulSoup(i,'html.parser')
    #     td_raw = target.find_all('td')
    #     print(td_raw)
    #     # tr.append(target.find_all('td'))
    
    vals = df.values.tolist()

    # print(type(vals))

    o_dict = {}

    for i in vals:
        j = i[0]
        if j == "USD" or j == "JPY":
            # print(i[0] + " " + str(i[8]) + " " + str(i[9]))
            
            buyWithComm = float(i[4])
            stdCurr = float(i[8])
            
            comm = buyWithComm - stdCurr
            
            # 우대율 90%
            realComm = comm*(1-0.9)
            realCurr = "{:.1f}".format(stdCurr + realComm)
            
            o_dict[j] = [realCurr, stdCurr]
    
    return o_dict

    # //*[@id="fxprint"]/table/tbody/tr[1]
    
# test = get_latest_cur_exch_table("2022","09","02")

# print(test)


