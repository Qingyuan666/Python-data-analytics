#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:10:16 2022

@author: Qingyuan Zheng, Minyi Sun
"""

#question a
import re
import csv
daily_yield_curves1=[]
number_1=0
with open ('daily-treasury-rates.csv') as list_1:
    for list_2 in list_1.readlines():
        daily_yield_curves1.append(list_2)
                

def clean_strings(strings): 
    daily_yield_curves = []
    index = 0
    for value in strings:
        value = value.strip()
        value = re.sub('[,\n]', ' ', value) 
        value = value.title() 
        l=value.split(' ')
        daily_yield_curves.insert(1, l)
        daily_yield_curves[0]=['Date', '1 mo', '2 mo', '3 mo', '6 mo', '1 yr', '2 yr',
         '3 yr', '5 yr', '7 yr', '10 yr', '20 yr', '30 yr']
    return daily_yield_curves

print(clean_strings(daily_yield_curves1))
daily_yield_curves=clean_strings(daily_yield_curves1)

for r in range(1, len(daily_yield_curves)):
    for c in range(1, len(daily_yield_curves[r])):
        daily_yield_curves[r][c] = float(daily_yield_curves[r][c])

CL=open('daily_yield_curves_2020.txt', 'w')

for l in daily_yield_curves:
        content='{:11}{:11}{:11}{:11}{:11}{:11}{:11}{:11}{:11}{:11}{:11}{:11}{:11}\n'. format(l[0].strip(),l[1],l[2],
                                                                                           l[3],l[4],l[5],l[6],l[7],
                                                                                           l[8],l[9],l[10],l[11],l[12])
        CL.writelines(content)       


CL.close()

#Question b
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

# define values for x, y, and z axis
x_days = np.array([[x] for x in range(1, len(daily_yield_curves))])
y_months = np.array([[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]])
z_rates = np.array([daily_yield_curves[m][1:] for m in range(1, len(daily_yield_curves))])


fig = plt.figure(figsize=plt.figaspect(2))
# construct the first plot
ax = fig.add_subplot(2, 1, 1, projection='3d')
surf = ax.plot_surface(x_days, y_months, z_rates, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Customize the z axis (interest rate)
ax.set_zlim(0.0, 4.0)
# label the axes
ax.set_xlabel('trading days since 01/02/20')
ax.set_ylabel('months to maturity')
ax.set_zlabel('rate')


clb = fig.colorbar(surf, shrink=0.5, aspect=5)
clb.ax.tick_params(labelsize=8)

# construct the second plot
ax2 = fig.add_subplot(2, 1, 2, projection='3d')
wire = ax2.plot_wireframe(x_days, y_months, z_rates, cmap=cm.coolwarm,
                       linewidth=1, antialiased=False)
# Customize the z axis (interest rate)
ax2.set_zlim(0.0, 4.0)
# label the axes
ax2.set_xlabel('trading days since 01/02/20')
ax2.set_ylabel('months to maturity')
ax2.set_zlabel('rate')

plt.show()

#Question c
import pandas as pd
l0=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
l10=[]
l11=[]
l12=[]

for lis in daily_yield_curves[1:len(daily_yield_curves)]:
    l0.append(lis[0])
    l1.append(lis[1])
    l2.append(lis[2])
    l3.append(lis[3])
    l4.append(lis[4])
    l5.append(lis[5])
    l6.append(lis[6])
    l7.append(lis[7])
    l8.append(lis[8])
    l9.append(lis[9])
    l10.append(lis[10])
    l11.append(lis[11])
    l12.append(lis[12])

header=daily_yield_curves[0]
dic={header[1]:l1, header[2]:l2, header[3]:l3,header[4]:l4,header[5]:l5,
      header[6]:l6, header[7]:l7, header[8]:l8, header[9]:l9, header[10]:l10, 
      header[11]:l11, header[12]:l12}

yield_curve_df = pd.DataFrame(dic,index=l0)

print(yield_curve_df)

import matplotlib.pyplot as plt
yield_curve_df=yield_curve_df.astype(float)
yield_curve_df.plot(title='Interest Rate Time Series, 2020')

plt.show()

l0_=[]
l1_=[]



i=1
while i < 252:
    lis=daily_yield_curves[i]
    l0_.append(lis[0])
    data=lis[1:13]
    l1_.append(data)
    i=i+20

dic={l0_[0]:l1_[0], l0_[1]:l1_[1], l0_[2]:l1_[2],l0_[3]:l1_[3],l0_[4]:l1_[4],
l0_[5]:l1_[5], l0_[6]:l1_[6], l0_[7]:l1_[7], l0_[8]:l1_[8], l0_[9]:l1_[9], 
l0_[10]:l1_[10], l0_[11]:l1_[11], l0_[12]:l1_[12]}

header1=[1,2,3,6,12,24,36,60,84,120,240,360]


by_day_yield_curve_df = pd.DataFrame(dic, index=header1)
by_day_yield_curve_df=by_day_yield_curve_df.astype(float)
plot1=by_day_yield_curve_df.plot(title='2020 Yield Curves, 20 Day Intervals')

plot1.legend(loc=1)
plt.show()
print(by_day_yield_curve_df)



    



