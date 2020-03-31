import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta

date_from = '20200125'
date_to = '20200328' # 20200315

# get real data from db
con = create_engine('mysql+pymysql://root:toor@localhost:3306/air?charset=utf8')
sql = "select datehour, o3 from air_quality where location = '成都' and datehour >= %s12 and datehour < %s12;" % (date_from, date_to)
df_db = pd.read_sql(sql, con, index_col='datehour')
df_db.index = pd.to_datetime(df_db.index, format='%Y%m%d%H')
# df_db['o3'] = df_db['o3'].map(int)

df = None
df_out = pd.DataFrame()
date_str = date_from
date, date_bar, date_next, date_next_nobar = None, None, None, None

def setAirData(obj):
    global df, df_out, date_str, date_next_nobar
    df = pd.DataFrame(obj['data'])
    df.rename(columns={'t1': 'aqi', 't3': 'pm2_5', 't4': 'pm10', 't5': 'co', 't6': 'no2', 't9': 'so2'}, inplace=True)
    df['time'] = df['time'].map(lambda time: ( date_str if int(time) >= 12 else date_next_nobar) + time)
    df['time'] = pd.to_datetime(df['time'], format='%Y%m%d%H')
    df.set_index(["time"], inplace=True)
    df['t7'] = df['t7'].map(lambda val: int(val) if val != '' and val != '0' else None)
    df_out = pd.concat([df_out, df['t7'].tail(24)], axis=0)

while date_str != date_to:
    # parse date
    date = datetime.strptime(date_str, '%Y%m%d')
    date_bar = datetime.strftime(date, '%Y-%m-%d')
    date_next = date + timedelta(days=1)
    date_next_nobar = datetime.strftime(date_next, '%Y%m%d')
    print(date_str)
    # open jsonp files
    with open('weather.com.cn/%s-12.json' % date_bar) as f:
        jsonp = f.read()
        eval(jsonp)
    date_str = date_next_nobar

print(df_out.shape, df_db.shape)
merged = pd.concat([df_out, df_db['o3']], axis=1).dropna(axis=0)
merged.to_csv('weather.com.cn.csv')