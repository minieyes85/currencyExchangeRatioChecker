import re
from datetime import datetime
from woori_exchange_inb import get_latest_cur_exch_table
from date_setting import get_year, get_month, get_day
from telegram_bot import tel_private_txt, tel_group_txt
from invest_exch import find_ex_cur

# 현재시간 구하기
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

#메세지 텍스트
currency_text = {"usd" : ["달러 환율" ,  "원/달러"],"jpy" : ["엔화 환욜" , "원/100엔"]}

# if cur == "jpy":
#     jpy_exch = cur_exch * 100
#     out_txt = current_time + "\n" + currency_text[cur][0] + " " + "{:.2f}".format(jpy_exch) + " " + currency_text[cur][1]
# else:
#     out_txt = current_time + "\n" + currency_text[cur][0] + " " + cur_exch_str + " " + currency_text[cur][1]

# ex_jpy = find_ex_cur("jpy")
ex_usd = find_ex_cur("usd")

# print(ex_usd)
# tel_group_txt(ex_usd)
# tel_private_txt(ex_usd)

# 우리은행 환율 구하기
woori_table_html = get_latest_cur_exch_table(get_year(), get_month(), get_day())
print(woori_table_html)

# print(get_year())
# print(get_month())
# print(get_day())


