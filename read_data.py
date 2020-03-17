import os
import timeit
import pandas as pd
from sqlalchemy import create_engine

con = create_engine('mysql+pymysql://root:toor@localhost:3306/air?charset=utf8')

def process_csv(path):
    dataset = pd.read_csv(path)
    # 将列名的 . 换为 _ 便于导入
    dataset['type'] = dataset['type'].map(lambda tag : tag.replace('.', '_').lower())
    # 将日期和小时合并为 datehour
    dataset['datehour'] = dataset['date'].map(str) + dataset['hour'].map("{:0>2d}".format)
    dataset = dataset.drop(labels=['date', 'hour'],axis=1)
    # 行列互换，列为各项检测值，行为时间地点
    dataset.columns.name = 'location'
    dataset = dataset.pivot(index='datehour', columns='type').stack(level=0)
    # 导入数据库
    pd.io.sql.to_sql(dataset, 'air_quality', con, schema='air', if_exists='append')

start_timer = timeit.default_timer()
dir_path = 'air_city'
files = os.listdir(dir_path)
for file in files:
    path = dir_path + '/' + file
    print(path)
    process_csv(path)
    print('elapsed: ', (timeit.default_timer() - start_timer))