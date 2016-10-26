# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:35:00 2016

@author: Old Chen
"""

import numpy as np
import matplotlib.pyplot as plt

K1 =9000
K2 =9200
K3 =9500
Premium_Call_K3 = 33.5
Premium_Put_K2 = 118
Premium_Put_K1 = 64
Interval = 1000
ST = np.arange(9250-Interval, 9250+Interval+1)

Payoff_LongCall_K3 = np.maximum(ST-K3,0) - Premium_Call_K3
Payoff_LongPut_K2 = np.maximum(K2-ST,0) - Premium_Put_K2
Payoff_LongPut_K1 = np.maximum(K1-ST,0) - Premium_Put_K1

Payoff_ShortCall_K3 = -Payoff_LongCall_K3
Payoff_ShortPut_K2 = -Payoff_LongPut_K2

Payoff_Combination = Payoff_LongPut_K1+Payoff_ShortPut_K2+Payoff_ShortCall_K3

#plt.plot(ST,Payoff_ShortCall_K3)
#plt.plot(ST,Payoff_ShortPut_K2)
#plt.plot(ST,Payoff_LongPut_K1)
plt.plot(ST,Payoff_Combination)
