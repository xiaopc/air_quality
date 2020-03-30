## 0: 7 * 24h -> 24h, CPU
LSTM 40, LSTM 20, Dropout 0.3, Dense 1(sigmoid), epochs 50, batch_size 120

## 1: 7 * 24h -> 24h, TPU 13694.807s
LSTM 40, LSTM 20, Dropout 0.3, Dense 1(sigmoid), epochs 100, batch_size 128
13722 test cases, RMSE 24.125

## 2: 7 * 24h -> 24h, TPU 13495.855s
shuffle data (both)
LSTM 50, LSTM 40, Dropout 0.3, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
13722 test cases, RMSE 18.212

## 3: 7 * 24h -> 24h, TPU 7309.474s
shuffle train only (fit shuffle)
LSTM 60, Dropout 0.3, LSTM 40, Dropout 0.2, Dense 1(tanh), epochs 80, batch_size 128 * 8 * 16
12954 test cases, RMSE 31.106

## 4: 7 * 24h -> 24h, TPU 7398.155s
shuffle train only (sample, fit shuffle)
LSTM 50, LSTM 40, Dropout 0.3, Dense 1(sigmoid), epochs 80, batch_size 128 * 8 * 4
12954 test cases, RMSE 31.566

> 以上为探索性测试，未控制变量

## 5: 3 * 24h -> 24h, TPU 9080.806s
no shuffle
LSTM 40, BidirectionalLSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE 18.462, MAE: 12.923

## 6: 3 * 24h -> 24h, TPU 2680.535s / 7309.293s
batch shuffle
LSTM 40, LSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE 17.848, MAE: 12.739

## 7: 3 * 24h -> 24h, TPU 8826.802s
batch shuffle
BidirectionalLSTM 40, LSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE 18.448, MAE: 13.142

## 8: 3 * 24h -> 24h, TPU 10435.726s
batch shuffle
BidirectionalLSTM 40, BidirectionalLSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE 18.474, MAE: 13.050

> 5 6 7 8 测试双向，无显著？

## 9: 3 * 24h -> 24h, TPU 5055.57s / 7389.401s
batch shuffle
GRU 40, GRU 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE 17.533, MAE 12.212

## 10: 3 * 24h -> 24h, TPU 8814.012s
batch shuffle
BidirectionalGRU 40, GRU 40, Dropout 0.2, Dense 1(sigmoid), epochs 500, batch_size 128 * 8
18432 test cases, RMSE 17.392, MAE 12.267

## 11: 3 * 24h -> 24h, TPU 8983.278s
batch shuffle
GRU 40, BidirectionalGRU 40, Dropout 0.2, Dense 1(sigmoid), epochs 500, batch_size 128 * 8
18432 test cases, RMSE 17.971, MAE 12.248

## 12: 3 * 24h -> 24h, TPU 10647.766s
batch shuffle
BidirectionalGRU 40, BidirectionalGRU 40, Dropout 0.2, Dense 1(sigmoid), epochs 500, batch_size 128 * 8
18432 test cases, RMSE 18.083, MAE 12.623

> 9 10 11 12 测试 GRU 双向，参数减少但速度未变？

## 13: 3 * 24h -> 24h, CPU 1085.879s
batch shuffle
LSTM 40, LSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE: 31.086, MAE: 20.930

> 同样的 batch_size、epochs 下，CPU 训练时间短，但几乎未拟合

## 14: 3 * 24h -> 24h, CPU 5495.925s
no shuffle
LSTM 40, LSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 500, batch_size 128 * 8
18432 test cases, RMSE: 20.373, MAE: 14.220

## 15: 3 * 24h -> 24h, CPU 4568.471s
no shuffle
GRU 40, GRU 40, Dropout 0.2, Dense 1(sigmoid), epochs 500, batch_size 128 * 8
18432 test cases, RMSE: 18.784, MAE: 13.139

## 16: 3 * 24h -> 24h, CPU 10429.39s
no shuffle
GRU 80, GRU 80, Dropout 0.2, Dense 1(sigmoid), epochs 500, batch_size 128 * 8
18432 test cases, RMSE: 24.380, MAE: 17.619

## 17: 3 * 24h -> 24h, CPU 6169.064s
no shuffle
GRU 80, GRU 80, Dropout 0.2, Dense 1(sigmoid), epochs 300, batch_size 128 * 8
18432 test cases, RMSE: 19.306, MAE: 13.686

## 18: 3 * 24h -> 24h, CPU 1268.457s
no shuffle
LSTM(0) 40, LSTM(1) 40, Attention(1), Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE: 17.741, MAE: 12.798

> 18# 起非序列的 H5 文件需要 2.2.4-tf 才能加载