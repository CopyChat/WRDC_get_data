#!/usr/bin/env python
"""
========
ctang, a map of geba stations in southern africa
========
"""
import math
import datetime
import pandas as pd
import numpy as np
import matplotlib as mpl
from textwrap import wrap
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap , addcyclic
from matplotlib.dates import YearLocator,MonthLocator,DateFormatter,drange
import sys 
sys.path.append('/Users/ctang/Code/Python/')
import ctang



DIR='/Users/ctang/climate/GLOBALDATA/OBSDATA/WRDC/Southern.Africa/'

title='WRDC monthly RSDS obs in southern Africa 1970-2005'

#=================================================== plot
STATION_all = 'flag.MonMean' # space was removed 
# index,country,station,lat,lon,elevation,year,mon1,mon2,3,4,5,6,7,8,9,10,11,12
# 27,angola,luanda,8.85,13.2333,74,1986,0,0,0,0,0,0,0,0,0,0,2,1,

station_all = np.array(pd.read_csv(DIR+STATION_all,header=None))

station_id = station_all[:,0]
country = station_all[:,1]      
station = station_all[:,2]        
year = station_all[:,6]        

month12 = station_all[:,7:19]

for i in range(1412):
    for j in range(12):
        if month12[i,j] == '-':
            month12[i,j] = 2
        if month12[i,j] == ')':
            month12[i,j]= 1

print month12
#=================================================== plotting

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(120,30),\
        facecolor='w', edgecolor='k') # figsize=(w,h)
fig.subplots_adjust(left=0.2)

ax.xaxis.set_major_locator(MonthLocator(1)) # interval = 5
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m'))
ax.fmt_xdata = DateFormatter('%Y-%m')

ax.set_title(title,fontsize=14)
ax.set_ylabel('Station',fontsize=14)
ax.set_xlabel('TIME',fontsize=14)

ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

height=0
station_name=[str(country[0])+"_"+str(station[0])]
for i in range(len(station_id)):
# for i in range(2):

    if i > 0:
        if country[i] == country[i-1] and station[i] == station[i-1]:
            height = height
        else:
            height = height+1
            station_name.append(str(country[i])+"_"+str(station[i]))
            print station_name
            print "there're ",len(station_name),"stations"

    dates=pd.date_range((pd.datetime(year[i]-1,12,1)\
            +pd.DateOffset(months=1)), periods=12, freq='MS')

    for j in range(12):
        if int(month12[i,j]) == 0:
            color = 'green'
            sc=plt.scatter(dates[j],height,zorder=2,s=50,color=color)
            # print j,dates[j],month12[i,j],color
            print i,"1412",country[i],station[i],year[i],month12[i,j],height
        else:
            color = 'gray'
            sc=plt.scatter(dates[j],height,zorder=2,s=50,color=color)
            # print j,dates[j],month12[i,j],color
            print i,"1412",country[i],station[i],year[i],month12[i,j],height

plt.xlim(datetime.datetime(1982,12,01),datetime.datetime(2006,1,31))

plt.xticks(rotation=70)

ax.set_ylim((-1,height))
ax.set_yticks(range(0,height+10,1))
ax.set_yticklabels(station_name)

sc=plt.scatter(dates[1],-10,zorder=2,s=50,color='gray',label='bad data')
sc=plt.scatter(dates[1],-10,zorder=2,s=50,color='green',label='good data')
legend = ax.legend(loc='upper left', shadow=False ,prop={'size':10})

plt.savefig('mon.series.SA.8305.png')

#===================================================  end of subplot 3
print "done"
# plt.show()

quit()
