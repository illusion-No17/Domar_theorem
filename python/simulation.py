# -*- coding: utf-8 -*-

#################################################################################
# simulation.py
#
# 名目成長率 > 利子率（名目成長率はプラスの値）かつ、プライマリーバランス赤字の
# 対ＧＤＰ比が一定ならば、政府債務残高の対ＧＤＰ比は無限大に発散しない。  
#
# ※上記の条件では、プライマリーバランスは黒字にしなくてもよい。
#################################################################################

import numpy as np
import matplotlib.pyplot as plt

# 初期値
Y_init = 550  # 名目GDP初期値(兆円)
D_init = 1100 # 政府債務残高初期値(兆円)
PB0    = - 80 # プライマリーバランス初期値(兆円)

# パラメータ
r0     = 0.01 # 政府債務の利子率
n0     = 0.04 # 名目成長率
time_length = 500

# 時系列
time = np.array([i for i in range(time_length)])

D     = np.zeros(time_length) # 政府債務残高(兆円)
Y     = np.zeros(time_length) # 名目GDP(兆円)
d     = np.zeros(time_length) # 政府債務残高対GFP比
PB    = np.zeros(time_length) # プライマリーバランス
Y[0]  = Y_init
D[0]  = D_init
d[0]  = D[0]/Y[0]
PB[0] = PB0

# 漸化式
for t in time[0:time_length-1]:
    D[t+1]  = (1 + r0)*D[t] - PB[t]
    Y[t+1]  = (1 + n0)*Y[t]
    PB[t+1] = (1 + n0)*PB[t]
    d[t+1]  = D[t+1]/Y[t+1]


# グラフを出力
plt.plot(time, d)
plt.xlabel("year")
plt.ylabel("Government debt against GDP")
plt.grid(True)
plt.show()