import pandas as pd
from math import sqrt
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error

merged = pd.read_csv('weather.com.cn.csv', index_col=0)
rmse = mean_squared_error(merged['o3'], merged['t7'], squared=False)
mae = mean_absolute_error(merged['o3'], merged['t7'])
label = 'RMSE: %.3f\nMAE: %.3f' % (rmse, mae)
print(label)