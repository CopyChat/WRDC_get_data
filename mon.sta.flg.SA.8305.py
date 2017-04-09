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

#=================================================== plot
STATION_all = 'flag.MonMean' # space was removed 
# index,country,station,lat,lon,elevation,year,mon1,mon2,3,4,5,6,7,8,9,10,11,12
# 27,angola,luanda,8.85,13.2333,74,1986,0,0,0,0,0,0,0,0,0,0,2,1,

station_all = np.array(pd.read_csv(DIR+STATION_all,header=None))

station_id = station_all[:,0]
country = station_all[:,1]      
station = station_all[:,2]        
year = station_all[:,6]        
lats = station_all[:,3]*-1       # should be removed 
lons = station_all[:,4]        

month12 = station_all[:,7:19]

for i in range(len(station_id)):
    for j in range(12):
        if month12[i,j] == '-':
            month12[i,j] = 2
        if month12[i,j] == ')':
            month12[i,j]= 1

# counting number of months
mon_count_year = np.zeros((len(station_id)))
for i in range(len(station_id)):
    k=0
    for j in range(12):

        if int(month12[i,j]) == 0:
            k = k + 1
    mon_count_year[i] = k
    print country[i],station[i],year[i],i,k,mon_count_year[i] 


# info of each station:
for i in range(len(station_id)):
    if i == 0:
        station_count = 0
        lon_uniq = [lons[i]]
        lat_uniq = [lats[i]]
        country_uniq = [country[i]]
        station_uniq = [station[i]]
    if i > 0:
        if country[i] == country[i-1] and station[i] == station[i-1]:
            station_count = station_count
        else:
            station_count = station_count+1
            country_uniq.append(country[i])
            station_uniq.append(station[i])
            lon_uniq.append(lons[i])
            lat_uniq.append(lats[i])

for i in range(len(station_uniq)):
    print country_uniq[i],station_uniq[i],i+1

# counting for each station between 1983 2005
mon_count = np.zeros((len(station_uniq)))
for k in range(len(station_uniq)):
    for i in range(len(station_id)):
        if year[i] >= 1983 and year[i] <= 2005:
            if country[i] == country_uniq[k] and station[i] == station_uniq[k]:
                mon_count[k] = mon_count[k] + mon_count_year[i]
    print k,country_uniq[k],station_uniq[k],lat_uniq[k],lon_uniq[k],mon_count[k]

#=================================================== plotting
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10,8),\
        facecolor='w', edgecolor='k') # figsize=(w,h)
#fig.subplots_adjust(left=0.04,bottom=0.15,right=0.98,\
        # hspace=0.15,top=0.8,wspace=0.43)

plt.sca(axes) # active shis subplot 
axx=axes

vmin = 1
vmax = 250

cmap = plt.cm.YlOrRd
cmaplist = [cmap(i) for i in range(cmap.N)]
bounds = np.linspace(vmin,vmax,13)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

map=Basemap(projection='cyl',llcrnrlat=-45,urcrnrlat=1,llcrnrlon=0,urcrnrlon=60,resolution='h')
ctang.setMap(map)

for sta in range(len(station_uniq)):
    if mon_count[sta] > 0:
        sc=plt.scatter(\
            lon_uniq[sta], lat_uniq[sta], c=mon_count[sta],edgecolor='black',\
            zorder=2,norm=norm,vmin=vmin,vmax=vmax,s=55, cmap=cmap)

cb=plt.colorbar(sc,orientation='horizontal',shrink=0.6)
cb.ax.tick_params(labelsize=9) 
cb.ax.set_title("number of monthly records")


# how many station has ZERO good record in 1983-2005 ?
print "NO-ZERO,sattion: ",np.count_nonzero(mon_count)

title='WRDC monthly RSDS obs in southern Africa 1983-2005 ('+\
        str(np.count_nonzero(mon_count))+' out of 110 WRDC stations)'
# fig.suptitle(title,fontsize=12)

# plot record num of each station
for sta in range(len(station_uniq)):
    print "plotting: ",sta
    if mon_count[sta] > 0 and mon_count[sta] < 12:
        plt.annotate( int(mon_count[sta]),xy=(lon_uniq[sta], lat_uniq[sta]), xytext=(-15, 15),\
            textcoords='offset points', ha='right', va='bottom',color='blue',\
            # bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),\
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

plt.savefig('mon.flg.sta.SA.8305.eps',format='eps')
#=================================================== 

print "done"
# plt.show()

quit()

