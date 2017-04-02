
# The WRDC data quality flags

## In database In bulletins    Description
   0                           Good value
   1           )               Questionable value  as estimated at  National Meteorological Service
   2           -               Value is not available or is rejected at National Meteorological Service
   3           e               Value calculated or interpolated at  National Meteorological Service
   4           P.N.            Polar night
   5,7         q               Questionable value as estimated at WRDC
   6           m               Value considered outlier to own climate-defined upper limit as estimated at WRDC
   8           i               Diffuse radiation value exceeds associated global radiation value
   9           r               Value is rejected at WRDC
 
* http://wrdc.mgo.rssi.ru/wrdccgi/quality_flags_en.htm


## Procedure to Calculate Daily and Monthly Totals
 
 1. A daily total of radiation balance is determined in case the data for all hour intervals of the 24-hour period are available.
 If at least one hourly total value is missing, the daily total is not calculated and the sign of missing data "-" is entered in the table instead.

 2. Daily totals of global and diffuse radiation are determined in case the data for all hour intervals of the daytime are available, with the exception of sunrise and sunset hour intervals.
 To avoid unduly great losses of daily totals due to the gaps in the data for sunrise and sunset hours, the following procedure of data processing is accepted.  In case observational data are missing for the above-mentioned hour intervals on a number of days, we recommend to determine hs (sun's altitude) for those hours.  If hs > 5° , the lack of an hourly total is identified as the lack of observation, and the daily total is not determined for that day.  If hs £ 5° , the daily total is calculated in similar situation.

 3. If data for each day of the month are available:
    a) the monthly total is calculated by adding together daily/hourly totals for each day of the month;
    b) the monthly mean of daily/hourly totals is calculated by dividing the monthly total by the number of days in the calendar month.

 4. If there are days with missing data, first of all the monthly mean of daily/ hourly totals is calculated and  then monthly total is obtained: 
    a) the monthly mean of daily/hourly totals is calculated by dividing the sum of daily/hourly totals for the days with available data (including estimated and questionable values) by the number of days with observations;
    b) the monthly total is calculated by multiplying the monthly mean of daily/ hourly totals by the number of days in the calendar month.

 5. If there are 10 or more days with missing daily/hourly totals, the monthly total and the monthly mean of daily/ hourly totals are not calculated and "-" is entered in respective columns.

 6. If there are from 5 to 9 days with missing daily/hourly totals, the monthly total and the monthly mean of daily/hourly totals are enclosed in brackets.

 7. If there are 5 or more daily/hourly totals enclosed in brackets (estimated or questionable), the monthly totals and the monthly mean of daily/hourly totals are enclosed in brackets.

 8. If the number of days with missing daily/hourly totals and daily/hourly totals in brackets added together is from 5 to 9, the monthly total and the monthly mean of daily/hourly totals are enclosed in brackets, and if there are 10 or more such days the monthly total and the monthly mean of daily/ hourly totals are not calculated and "- " is entered in respective columns. All radiation parameters and sunshine duration are subject to this rule.

 9. The monthly means of daily totals of appropriate radiation parameters from Tables I-III are also given in Tables IV-VI along with monthly means of hourly totals, with the exception of the cases when these values are absent in Table I-III. In such situations the monthly means of daily totals are calculated by summing up the monthly means of hourly totals for all hour intervals of the 24-hour period for radiation balance and for all hour intervals of the daytime for global and diffuse radiation.

### summary: for the use of monthly mean: (ctang)


<!--(                                                                                                 

* missing : number of missing day/hour
* Q&E : number of questionable and estimated record

                            ----- monthly mean is GOOD ---- flag: 0                                  
                            |                                                                        
                            |                                                                        
                --------YES |                                                                       
                |           |                                                                        
                |           |                                                                     
                |           |                                                                     
Daily/Hourly    |           ----- monthly total is GOOD ---- flag: 0                                 
   are      ==> |                                                                                   
  GOOD          |                                                                                  
                |                                                                                 
                |                                                                                 
                |                                                                                 
                |           ----- 5 < missing < 9     ----- flag: '1'                             
                |           |                                                                     
                |           |                                                                     
                -------- NO |                                                                        
                            |                                                                        
                            --------- missing < 10    ----- flag: '2'                             
                            |                                                                        
                            |                                                                        
                            -------- 5 < Q&E < 9      ----- flag: '1'                             
                            |                                                                        
                            |                                                                        
                            ------------ Q&E > 10     ----- flag: '2'                             
                            |                                                                        
                            |                                                                        
                            |                                                                        
                            ---- (missing + Q&E) > 10 ----- flag: '2'                             
                            |                                                                        
                            |                                                                        
                            |                                                                        
                            - 5 < (missing + Q&E) < 9 ----- flag: '1'

)--> 








