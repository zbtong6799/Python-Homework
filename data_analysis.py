# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:57:53 2019
Mission：data analysis
@author: Botong Zhao
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#open file and get data
df=pd.read_excel(r'.\date.xlsx',sheet_name='Sheet1')
#print(df.head())

df.columns = ['date','num']
df['date'] = pd.to_datetime(df['date']) #将数据类型转换为日期类型
df = df.set_index('date') # 将date设置为index
#print(df.head(2))
#print(df.tail(2))
print(df.shape)
"""
Simple analysis of the results
"""
#the amount of all news
sum_news=np.size(df,0)
#every week's news
week=df.resample('w').sum()
"""
plt.plot(week)
"""
full_path = 'The total amount news of each week' + '.csv'  
week.to_csv(full_path,index=False,header=False)
#The average amount news of each day
day=df.resample('D').sum()
num_day=np.size(day,0)
avg_news_day=sum_news/num_day
avg_news_week=sum_news/np.size(week,0)
plt.rcParams['font.sans-serif'] = ['SimSun']#指定字体
week.boxplot(column = ['num'],sym = 'o', vert = True, whis = 1.5, patch_artist = True,meanline = False, showmeans = True,showbox = True,showfliers = True, notch = True, return_type='dict')
plt.show()
