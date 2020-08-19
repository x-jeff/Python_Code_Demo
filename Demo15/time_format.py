from datetime import datetime
from datetime import timedelta
from time import mktime
import pandas as pd

# 输出现在的时间
current_time = datetime.now()
print("current time : ", current_time)
print(type(current_time))

# 将时间转换成字符串
print(current_time.strftime('%Y-%m-%d'))

# 将字符串转换成时间
print(datetime.strptime('2020-08-19', '%Y-%m-%d'))

# 时间往前回溯一天
print(current_time - timedelta(days=1))

# 时间往后推移十天
print(current_time - timedelta(days=-10))
print(current_time + timedelta(days=10))

# 将datetime转换为UNIX timestamp
print(mktime(current_time.timetuple()))
print(current_time.timetuple())

# 将UNIX timestamp转换为datetime
print(datetime.fromtimestamp(1597849076))

# 在pandas转换时间
df = pd.read_csv("../Demo14/house_price.csv")
print(df)
df["日期"] = pd.to_datetime(df["日期"], format="%Y年%m月%d日")
print(df)