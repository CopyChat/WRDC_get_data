#!/bin/bash - 
#===============================================================================
#
#          FILE: get.WRDC.southern.africa.sh
# 
USAGE="./get.WRDC.southern.africa.sh  "
# 
#   DESCRIPTION:   get all this from WRDC web: http://wrdc.mgo.rssi.ru/
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#                   1. link.country_station, checked by eyes !!!
#                   2. get.WRDC.data.py 
#          BUGS: --- no process indicators (fixed)
#         NOTES: ---
#        AUTHOR: Tang (Tang), chao.tang.1@gmail.com
#  ORGANIZATION: le2p
#       CREATED: 03/27/17 18:42:11 RET
#      REVISION:  ---
#===============================================================================

#set -o nounset                             # Treat unset variables as an error
shopt -s extglob 							# "shopt -u extglob" to turn it off
source ~/Shell/functions.sh      			# TANG's shell functions.sh
#=================================================== 

link='link.country_station'

# get link on the level of year:
function get_link()
{
    rm *temp
    line=$(wc -l < $link)
    echo $line
    for i in $(seq -s " " 1 $line)
    do
        l1=$(awk 'NR=='$i'' $link)
        echo $i,$l1
        curl --silent $l1 | grep data_list_full_protected | awk -F "\"" '{print $2}' >> link.country_station_year
    done
}

function get_info()
{
    file='link.country_station_year'
    for a in $(cat $file); do b=${a##*t1/}; c=${b%%/*};  echo $c ; done > link.country
    for a in $(cat link.country_station_year); do b=${a##*/}; c=${b%_t1*}; d=${c%*_????}; echo $d; done > link.station
    for a in $(cat $file); do b=${a##*/}; c=${b%_*}; d=${c##*_}; echo $d; done > link.year
}

function getdata()
{
    link='link.country_station_year'
    line=$(wc -l < $link)


    for i in $(seq -s " " 1 $line)
    do
        l1=$(awk 'NR=='$i'' $link)

        country=$(awk 'NR=='$i'' link.country)
        station=$(awk 'NR=='$i'' link.station)
        year=$(awk 'NR=='$i'' link.year)

        # download:
        output=WRDC.$country.$station.$year.line_$i.csv
        links -dump $l1 > $output

        echo "============= $i/$line"
    done
}

#=================================================== 
# to check is all the data are well downloaded: 94 lines each file
function check()
{
    line=$(wc -l < link.country_station_year)

    # if not, output the failed iterms to :
    output=redo.temp

    for i in $(seq -s " " 1 $line)
    do
        wc=$(wc -l WRDC.*.*.*.line?$i.csv | awk '{print $1}')
        echo $i,$wc
        if ! [ $wc -eq 41 ];
        then
            echo $i,$wc
            awk 'NR=='$i'' link.station.southern.africa >> $output

            awk 'NR=='$i'' link.station >> $output.station
            awk 'NR=='$i'' link.country >> $output.country
            awk 'NR=='$i'' link.year >> $output.year
        fi
    done

}

#get_link 

#get_info

# download using get.WRDC.data.py
#python ./get.WRDC.data.py >> download.log ( off line, use current script only )

# start to download
getdata
# NOTE: output file name : line number is the line of link.country_station_year

# check if all are downloaded
#check
# change the value of 'link' variable & rerun getdata to download these "missing" data.
