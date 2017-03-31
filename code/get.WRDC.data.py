#!/usr/bin/env python
########################################
# to get WRDC data:
########################################

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import numpy as np
import pandas as pd
import bs4
import re

url='http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/t1.html'
url='http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/'

country_url=(\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/angola.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/kenya.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/madagascar/madagascar.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/mozambique.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/namibia/namibia.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/rsa.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/reunion/reunion.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/tanzania.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/zaire.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/zambia.html',\
'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zimbabwe/zimbabwe.html')


region_url=(\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/dundo/dundo.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/luanda/luanda.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/de_belas/de_belas.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/malange/malange.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/luena_luso/luena_luso.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/nova_lisboa_chianga/nova_lisboa_chianga.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/menongue_serpa_pinto/menongue_serpa_pinto.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/lubango_sa_da_bandeira/lubango_sa_da_bandeira.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/mocamedes/mocamedes.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/angola/pereira_de_eca/pereira_de_eca.html',\

    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/mount_kenya/mount_kenya.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/narok/narok.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/muguga/muguga.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/nairobi_dagoretti_corner/nairobi_dagoretti_corner.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/nairobi_kenyatta_arpt/nairobi_kenyatta_arpt.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/lamu/lamu.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/malindi/malindi.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/voi/voi.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/mombasa_moi_arpt/mombasa_moi_arpt.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/madagascar/antsiranana/antsiranana.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/madagascar/antananarivo/antananarivo.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/madagascar/toliara/toliara.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/pemba/pemba.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/lichinga/lichinga.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/lumbo/lumbo.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/nampula/nampula.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/gurue/gurue.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/tete/tete.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/mocuba/mocuba.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/quelimane/quelimane.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/chimoio/chimoio.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/beira/beira.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/chicualacuala/chicualacuala.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/inhambane/inhambane.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/chokwe/chokwe.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/maniquenique/maniquenique.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/xai-xai/xai-xai.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/bobole/bobole.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/maputo_mavalane/maputo_mavalane.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/maputo/maputo.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/mozambique/umbeluzi/umbeluzi.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/namibia/windhoek/windhoek.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/namibia/keetmanshoop/keetmanshoop.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/nelspruit/nelspruit.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/roodeplaat/roodeplaat.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/pretoria_forum/pretoria_forum.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/pretoria/pretoria.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/pretoria_irene/pretoria_irene.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/upington/upington.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/alexander_bay/alexander_bay.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/bloemfontein/bloemfontein.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/durban_louis_botha/durban_louis_botha.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/middelburgh/middelburgh.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/cape_town/cape_town.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/port_elizabeth/port_elizabeth.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/gough_is_/gough_is_.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/rsa/marion_is_/marion_is_.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/reunion/st-denis_gillot/st-denis_gillot.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/bukoba/bukoba.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/musoma/musoma.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/mwanza/mwanza.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/arusha/arusha.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/kilimanjaro_arpt/kilimanjaro_arpt.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/same/same.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/kigoma/kigoma.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/tabora_arpt/tabora_arpt.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/dodoma/dodoma.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/zanzibar_kisauni/zanzibar_kisauni.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/morogoro/morogoro.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/dar_es_salaamarpt/dar_es_salaamarpt.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/iringa/iringa.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/mtwara/mtwara.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/tanzania/songea/songea.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/boende/boende.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/goma/goma.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/inongo/inongo.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/bukavu/bukavu.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/kindu/kindu.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/kinshasa_binza/kinshasa_binza.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/kananga/kananga.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/kalemie/kalemie.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/mbuji-mayi/mbuji-mayi.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zaire/lubumbashi_karavia/lubumbashi_karavia.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/kasama/kasama.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/mansa/mansa.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/ndola/ndola.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/mfuwe/mfuwe.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/mongu/mongu.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/lusaka_city_arpt/lusaka_city_arpt.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zambia/livingstone/livingstone.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zimbabwe/harare_belvedere/harare_belvedere.html',\
    'http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zimbabwe/bulawayo_goetz_obs_/bulawayo_goetz_obs_.html')


url = open("link.country_station_year").read().split()
station = open("link.station").read().split()
years = open("link.year").read().split()
country = open("link.country").read().split()


#url = open("redo.temp").read().split()
#station = open("redo.temp.station").read().split()
#years = open("redo.temp.year").read().split()
#country = open("redo.temp.country").read().split()

print len(url),len(country),len(station),len(years)

#print len(Southern_Africa)
#for i in range(len(Southern_Africa)):
    #for link in Southern_Africa[i]:
        #print(url+Southern_Africa[i][0]+'/'+link+'.html')
        #http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zimbabwe/bulawayo_goetz_obs_/bulawayo_goetz_obs_.html

print "startttttttttttttttt"
#for url in region_url:
    #print "=========================="+str(url)
    #beautiful = urllib2.urlopen(url)
    #print beautiful.read()

#http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/nairobi_kenyatta_arpt/nairobi_kenyatta_arpt_23_t1.1.csv.html
#url='http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/zimbabwe/bulawayo_goetz_obs_/bulawayo_goetz_obs__1991_t1.html'
#for i in range(len(year_url)):
#for i in range(len(url)):
for i in range(1220,1500,1):
    output='WRDC.'+country[i]+'.'+station[i]+'.'+years[i]+'.line_'+str(i+1)+'.csv'
    print output,url[i]

    beautiful = urllib2.urlopen(url[i]).read()
    
    print beautiful
    with open(output, 'w') as f:
        f.write(beautiful)



#url='http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/nairobi_kenyatta_arpt/nairobi_kenyatta_arpt_1984_t1.1.csv.html'
#http://wrdc.mgo.rssi.ru/wrdccgi/protect.exe?data_list_full_protected/t1/kenya/lamu/lamu_1980_t1.1.csv.html

#use re.findall to get all the links


quit()
with open('output.txt', 'w') as f:
        f.write(beautiful.read())
#print beautiful.info


