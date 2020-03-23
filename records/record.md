## 0: 7 * 24h -> 24h, CPU
LSTM 40, LSTM 20, Dropout 0.3, Dense 1(sigmoid), epochs 50, batch_size 120

## 1: 7 * 24h -> 24h, TPU 13694.807s
LSTM 40, LSTM 20, Dropout 0.3, Dense 1(sigmoid), epochs 100, batch_size 128
13722 test cases, RMSE 24.125

## 2: 7 * 24h -> 24h, 13495.855s
shuffle data (both)
LSTM 50, LSTM 40, Dropout 0.3, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
13722 test cases, RMSE 18.212

## 3: 7 * 24h -> 24h, 7309.474s
shuffle train only (fit shuffle)
LSTM 60, Dropout 0.3, LSTM 40, Dropout 0.2, Dense 1(tanh), epochs 80, batch_size 128 * 8 * 16
12954 test cases, RMSE 31.106

## 4: 7 * 24h -> 24h, 7398.155s
shuffle train only (sample, fit shuffle)
LSTM 50, LSTM 40, Dropout 0.3, Dense 1(sigmoid), epochs 80, batch_size 128 * 8 * 4
12954 test cases, RMSE 31.566

## 5: 3 * 24h -> 24h, 9080.806s
no shuffle
LSTM 40, BidirectionalLSTM 40, Dropout 0.2, Dense 1(sigmoid), epochs 100, batch_size 128 * 8
18432 test cases, RMSE 18.462