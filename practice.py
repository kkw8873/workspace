import time
print(time.strftime('%d-%b-%Y')) # 현재 날짜 일-월-연도

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))