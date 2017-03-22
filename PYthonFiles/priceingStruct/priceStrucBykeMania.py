import time
from datetime import datetime, timedelta
import calendar
import numpy as np
import re
from collections import OrderedDict



def pricingStrucBykeMania(location,subLocation,bikeName,deposit,WeekDayRateHr,WeekDayRateDay, WeekEndRateHr, WeekEndRateDay,pickUpTotal,dropTotal):
    dateDiff=dropTotal-pickUpTotal
    totalHr=dateDiff.total_seconds()/3600
    pickVar=pickUpTotal
    dropVar=dropTotal
    qut=int(totalHr/24)
    rem=totalHr%24
    i=0
    weekdayCount=0
    weekendCount=0
    remDropHr=0
    cost=0
    while(i<qut):
        if(pickVar.weekday()<=3):
            weekdayCount=weekdayCount+1
        else:
            weekendCount=weekendCount+1
#        print(pickVar)
        pickVar=pickVar+timedelta(days=1)
#        print(weekdayCount,weekendCount,rem)
        i=i+1
    print(totalHr)
    if(totalHr<21):
        if(pickUpTotal.weekday()<=3):
            hrCost=totalHr*WeekDayRateHr
        else:
            hrCost=totalHr*WeekEndRateHr
    elif(rem>=21 and rem<24):
        if(pickUpTotal.weekday()<=3):
            hrCost=WeekDayRateDay
        else:
            hrCost=WeekEndRateDay
    else:
        if(dropVar.weekday()<=3):
            hrCost=rem*WeekDayRateHr
        else:
            hrCost=rem*WeekEndRateHr
    cost=weekdayCount*WeekDayRateDay+weekendCount*WeekEndRateDay+hrCost
    dictBykeManiaFinal={}
    dictBykeManiaFinal={location:{subLocation:{bikeName:{'pickUpDate':pickUpTotal,'dropDate':dropTotal,'Deposit':deposit,'Cost':cost}}
                                  }
                        }
    
    #print(location,subLocation,bikeName,cost)
    return dictBykeManiaFinal






def dateDefault(pickUpTotal,dropTotal):
    l=[]
    dictBykeMania=internalDBBykeMania()
    for k1,v1 in dictBykeMania.iteritems():
        #print(k1)
        for k2,v2 in dictBykeMania[k1].iteritems():
            #print(k1,k2)
            for k3,v3 in dictBykeMania[k1][k2].iteritems():
                #print(k1,k2,k3,v3)
                #print(k1,k2,k3,dictRoadPanda[k1][k2][k3][0])
                #print(k1,k2,k3,dictBykeMania[k1][k2][k3][0],dictBykeMania[k1][k2][k3][1],dictBykeMania[k1][k2][k3][2],dictBykeMania[k1][k2][k3][3],dictBykeMania[k1][k2][k3][4],pickUpTotal,dropTotal)            
                a=pricingStrucBykeMania(k1,k2,k3,dictBykeMania[k1][k2][k3][0],dictBykeMania[k1][k2][k3][1],dictBykeMania[k1][k2][k3][2],dictBykeMania[k1][k2][k3][3],dictBykeMania[k1][k2][k3][4],pickUpTotal,dropTotal)
                l.append(a)
    print(l)
    
    
def internalDBBykeMania():
    #Order in List:deposit=500,weekdayRate/hr=35,weekdayRate/day=700,weekendRate/hr=45,weekendRate/day=800    
    dictBykeMania={'bangalore':
                       {'Koramangala (opp. Forum Mall)':{
                                           'Bajaj Avenger Cruise 220':[500,35,700,45,850]
                                           ,'Royal Enfield Classic 350':[500,45,900,60,1200]
                                           ,'Honda CBR 250r':[1500,62,1340,75,1620]
                                           ,'Royal Enfield Thunderbird 500':[1500,65,1400,80,1700]
                                           ,'Royal Enfield Classic 500':[1500,65,1400,80,1750]
                                           ,'Bajaj Avenger Street 220':[500,35,700,45,850]
                                           ,'Yamaha FZ':[500,30,650,40,800]
                                           ,'Royal Enfield Himalayan':[1500,90,1900,100,2100]
                                           ,'Honda Dio':[500,20,350,23,400]
                                           ,'Honda Activa':[500,20,350,23,400]
                                           ,'KTM Duke 200':[1500,60,1300,75,1650]
                                           ,'KTM Rc 390':[1500,95,2050,110,2370]

                                          }
                        ,'Kumarswamy layout(Bykemania)':{
                                            'Bajaj Avenger Cruise 220':[500,35,700,45,850]
                                           ,'Kawasaki Z800':[5000,418,8030,418,8580]
                                           ,'Bajaj Pulsar180':[500,30,650,40,800]
                                           ,'Royal Enfield Classic 350':[500,45,900,60,1200]
                                           ,'Bajaj Pulsar135':[500,23,500,30,600]
                                           ,'Bajaj Dominar 400':[2000,106,2080,106,2300]
                                           ,'Yamaha FZ-S FI':[500,30,650,40,800]
                                           ,'KTM RC 200':[2000,96,1640,96,2080]
                                           ,'Bajaj Avenger Street 220':[500,35,700,45,850]
                                           ,'Yamaha FZ':[500,30,650,40,800]
                                           ,'Royal Enfield Himalayan':[2000,101,1640,101,2190]
                                           ,'Mahindra Mojo':[2000,96,1640,96,2080]
                                           ,'Triumph Street':[5000,418,8030,418,8580]
                                           ,'Honda Dio':[500,20,350,23,400]
                                           ,'Honda Activa':[500,20,350,23,400]
                                           ,'KTM Duke 200':[1500,76,1530,76,1640]
                                           ,'KTM Duke 390':[2000,96,1640,96,2080]
                                           ,'KTM Rc 390':[2000,116,1860,116,2520]
                                           ,'Yamaha R3':[2000,116,1860,116,2520]

                                            }
                        ,'V.V. Puram(near lalbagh)':{
                                            'Royal Enfield Classic 350':[500,50,950,65,1300]
                                           ,'Hero Karizma R':[500,30,650,40,800]
                                           ,'Suzuki Access':[500,23,350,25,400]
                                           ,'Yamaha FZ-S FI':[500,30,700,45,850]
                                           ,'Bajaj Avenger Street 220':[500,37,850,50,950]
                                           ,'Yamaha FZ':[500,30,700,45,850]
                                           ,'Honda Activa':[500,23,350,25,400]

                                            }
                        ,'Mathikere (Near Ramaiah college)':{
                                           'Royal Enfield Classic 350':[500,45,900,60,1200]
                                           ,'Bajaj Avenger Street 220':[500,35,700,45,850]
                                           ,'Yamaha FZ':[500,30,650,40,800]
                                           ,'Honda Dio':[500,20,350,23,400]
                                            }
                        
                        
                        
                        }
                   
                   }
    #print(dictBykeMania)
    return dictBykeMania

    

    
pickUpTotal=datetime.strptime('24-02-2017 12', "%d-%m-%Y %H")                                                                            
dropTotal=datetime.strptime('26-02-2017 9', "%d-%m-%Y %H")

pickUpDate=pickUpTotal.strftime('%d')                                                                            
dropDate=dropTotal.strftime('%d')

pickUpTime=pickUpTotal.strftime('%H')                                                                            
dropTime=dropTotal.strftime('%H')

dateDefault(pickUpTotal,dropTotal)



#costCalc(pickUpTotal,dropTotal,35,700,45,850)


'''
algo:
q=days
r=hr
diff=4
while 

'''










