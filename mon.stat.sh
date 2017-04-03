#!/bin/bash - 
#======================================================
#
#          FILE: mon.stat.sh
# 
USAGE="./mon.stat.sh"
# 
#   DESCRIPTION: get monthly data statistic, 
#                prepare for plot
# 
#       OPTIONS: --- file name (country, year)
#                --- number of mon
#  REQUIREMENTS: ---
#          BUGS: --- unknown
#         NOTES: ---
#        AUTHOR: |CHAO.TANG| , |chao.tang.1@gmail.com|
#  ORGANIZATION: 
#       CREATED: 04/02/17 14:51
#      REVISION: 1.0
#=====================================================
#set -o nounset           # Treat unset variables as an error

# GLOBAL DECLARATIONS: 

prefix=WRDC
Tline=1412                                      # total line number
MONTH=(JAN FEB MAR APR MAR JUN JUL AUG SEP OCT NOV DEC)    # from 0
list=link.country_station_year                  # list of file
DIR=/Users/ctang/climate/GLOBALDATA/OBSDATA/WRDC/Southern.Afria


#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  MonMeanFlag
#   DESCRIPTION:  get monthly mean flags
#    PARAMETERS:  file name
#       RETURNS:  flag 1,2,3,...12
#-------------------------------------------------------------------------------

function MonMeanFlag()
{
    file=$1
    for m in {0..11}
    do
        #echo =============$m
        mon=${MONTH[$m]}
        len=$(awk 'NR==20' $file | grep "$mon")

        if [ ${#len} -gt 0 ];then
            column=$(awk -v val=$mon -F '|' 'NR==20{for (i=1;i<=NF;i++)\
                if ($i ~ val) {print i}}' $file )
            awk -F "|" 'NR==86{printf "%s,", $('$column'+1)}' $file
        else
            echo -n -999,                   # not availible in WRDC
        fi
    done
    echo ""
}



#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  SpatialInfo
#   DESCRIPTION:  get spation info
#    PARAMETERS:  output file name 
#       RETURNS:  index,country,stition,lat,lon,elevation,year,12(monthly flag)
#-------------------------------------------------------------------------------
function SpatialInfo()
{
    output=$1
    rm -rf $output 2>&1

    cd $DIR
    for line in $(seq -s " " 1 $Tline)
    do
        file=$(ls $prefix.*.*.*.line_$line.csv)
        country=$(echo $file | awk -F "." '{print $2}')
        station=$(echo $file | awk -F "." '{print $3}')
        year=$(echo $file | awk -F "." '{print $4}')

        lat=$(awk 'NR==9'  $file | grep -o '[0-9]\+')
        lat=$(echo $lat | awk '{print (-1)*($1+$2/60)}')

        lon=$(awk 'NR==11' $file | grep -o '[0-9]\+')
        lon=$(echo $lon | awk '{print $1+$2/60}')

        elevation=$( awk 'NR==13{print $3}' $file)

        echo -n $line,$country,$station,$lat,$lon,$elevation,$year, >> $output

        MonMeanFlag $file >> $output

        # running log
        echo ----------- $line / $Tline

    done
}

SpatialInfo flag.MonMean
exit

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  monData
#   DESCRIPTION:  get monthly data
#    PARAMETERS:  file_name_(country,year) mumber_of_month.
#       RETURNS:  monthly data value
#-------------------------------------------------------------------------------
function monData()
{
    echo jj
}

monData 1983 1

