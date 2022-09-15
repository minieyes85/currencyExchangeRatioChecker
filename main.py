from datetime import datetime
from woori_exchange_inb import get_latest_cur_exch_table
from date_setting import get_year, get_month, get_day
from telegram_bot import tel_private_txt, tel_group_txt
from invest_exch import find_ex_cur

# 현재시간 구하기
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# ex_jpy = find_ex_cur("jpy")
investExCurUSD = find_ex_cur("usd")

# 한국투자 매매기준 달러팔때 우대율 95%
korInvestExCurUSD = float(investExCurUSD) * 0.9995
korInvestExCurUSD = "{:.1f}".format(korInvestExCurUSD)

# print(investExCurUSD)
# print(ex_usd)
# tel_group_txt(ex_usd)
# tel_private_txt(ex_usd)

# 우리은행 환율 구하기
woori_table_html = get_latest_cur_exch_table(get_year(), get_month(), get_day())
wooriExCurUSD = woori_table_html.get('USD')[0]
# print(woori_table_html)
# print(woori_table_html.get('USD'))

msgTEXT0 = "현재시간 : " + current_time
msgTEXT1 = "\n우리은행 달러 살때 : " + wooriExCurUSD + " 원/달러"
msgTEXT2 = "\n한국투자 달러 팔때 : " + korInvestExCurUSD + " 원/달러"

gapExUSD = float(korInvestExCurUSD) - float(wooriExCurUSD)

if gapExUSD > 1.0:
    msgTEXT3 = "\n결과 : " + str(gapExUSD) + " 원/달러 이득"
elif gapExUSD == 0.0:
    msgTEXT3 = "\n결과 : 매수/매도 동일"
else:
    msgTEXT3 = "\n결과 : " + str(-gapExUSD) + " 원/달러 손해"

# print(gapExUSD)

# print(msgTEXT0)
# print(msgTEXT1)
# print(msgTEXT2)

msg_str = []
msg_str.append(msgTEXT0)
msg_str.append(msgTEXT1)
msg_str.append(msgTEXT2)
msg_str.append(msgTEXT3)
msg_str = ''.join(msg_str)

print(msg_str)

tel_private_txt(msg_str)
# tel_group_txt(msg_str)

