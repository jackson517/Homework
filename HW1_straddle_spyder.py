# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:35:00 2016

@author: Old Chen
"""

import numpy as np
import matplotlib.pyplot as plt
K =9500
Premium_Call = 33.5
Premium_Put = 285
Interval = 1000
ST = np.arange(K-Interval, K+Interval+1)
Payoff_LongCall = np.maximum(ST-K,0) - Premium_Call
Payoff_LongPut = np.maximum(K-ST,0) - Premium_Put
Payoff_ShortCall = -Payoff_LongCall
Payoff_straddle = Payoff_LongCall + Payoff_LongPut


plt.plot(ST,Payoff_LongCall)
plt.plot(ST,Payoff_LongPut)
plt.plot(ST,Payoff_straddle)

#plt.plot(ST,Payoff_LongCall)
#plt.plot(ST,Payoff_ShortCall)
#plt.plot(ST,Payoff_LongCall+Payoff_ShortCall)
