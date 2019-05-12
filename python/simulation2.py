# -*- coding: utf-8 -*-

#################################################################################
# simulation2.py
# 
# 名目成長率 > 利子率（名目成長率はプラスの値を想定）かつ、プライマリーバランス赤字の
# 対ＧＤＰ比が一定ならば、政府債務残高の対ＧＤＰ比は無限大に発散しない。  
#
# ※上記の条件では、プライマリーバランスは黒字にしなくてもよい。
#
# 名目成長率 > 利子率の条件で、名目成長率と利子率も変化させるものとする。
#################################################################################

import numpy as np
import matplotlib.pyplot as plt
import random

# 初期値
Y_init = 550  # 名目GDP初期値(兆円)
D_init = 1100 # 政府債務残高初期値(兆円)
PB0    = - 80 # プライマリーバランス初期値(兆円)
r0     = 0.01 # 政府債務の利子率
n0     = 0.04 # 名目成長率
time_length = 500

# 時系列
time = np.array([i for i in range(time_length)])

D     = np.zeros(time_length) # 政府債務残高(兆円)
Y     = np.zeros(time_length) # 名目GDP(兆円)
d     = np.zeros(time_length) # 政府債務残高対GFP比
PB    = np.zeros(time_length) # プライマリーバランス
n    = np.zeros(time_length)  # 名目成長率
r    = np.zeros(time_length)  # 利子率

Y[0]  = Y_init
D[0]  = D_init
d[0]  = D[0]/Y[0]
PB[0] = PB0
n[0]  = n0
r[0]  = r0

# 漸化式
for t in time[0:time_length-1]:
    D[t+1]  = (1 + r[t] )*D[t] - PB[t]

    Y[t+1]  = (1 + n[t])*Y[t]

    d[t+1]  = D[t+1]/Y[t+1]

    PB[t+1] = (1 + n[t])*PB[t]

    # とりあえず乱数で名目成長率と利子率を変化させる（変化の仕方に妥当性はない）。
    r[t+1] = 0.01*random.random()+0.01
    n[t+1] = 0.01*random.random()+0.04

# グラフを出力
plt.plot(time, d)
plt.xlabel("year")
plt.ylabel("Government debt against GDP")
plt.grid(True)
plt.show()