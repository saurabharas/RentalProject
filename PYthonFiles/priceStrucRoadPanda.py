import time
from datetime import datetime, timedelta
import calendar
import numpy as np
import re
from collections import OrderedDict


'''
Input:
bikeName,
Lkm=5
Rkm=10
Pkm=15
LBase=84(upto 6hr)
RBase=120
PBase150
LweekdayRate=14(per hr increase after 6 hr)
RweekdayRate=20
PweekdayRate=25
LweekendRate=18(per hr increase after 6 hr)
pweekendRate=26
RweekendRate=32

Return:
Lcost,Rcost,Pcost
LkmLimit,RkmLimt,PkmLimit

'''

def priceStrucRoadPanda(location,subLocation,bikeName,LweekdayRate,RweekdayRate,PweekdayRate,LweekendRate,RweekendRate,PweekendRate,weekdayCountHr,weekendCountHr,pickUpTotal,dropTotal):
    Lcost,Rcost,Pcost,LkmLimit,RkmLimit,PkmLimit=0,0,0,0,0,0
    totalHr=weekdayCountHr+weekendCountHr
    print("Total Hr=",totalHr)


    if(totalHr<=6):
        LkmLimit=6*5
        RkmLimit=6*10
        PkmLimit=6*15

        if(pickUpTotal.weekday()<=3):           
            Lcost=6*LweekdayRate
            Rcost=6*RweekdayRate
            Pcost=6*PweekdayRate
        if(pickUpTotal.weekday()>3):
            Lcost=6*LweekendRate
            Rcost=6*RweekendRate
            Pcost=6*PweekendRate
            
    if(totalHr>6):
        LkmLimit=totalHr*5
        RkmLimit=totalHr*10
        PkmLimit=totalHr*15
        
        Lcost=weekdayCountHr*LweekdayRate+weekendCountHr*LweekendRate
        Rcost=weekdayCountHr*RweekdayRate+weekendCountHr*RweekendRate
        Pcost=weekdayCountHr*PweekdayRate+weekendCountHr*PweekendRate
            
    print(Lcost,Rcost,Pcost,LkmLimit,RkmLimit,PkmLimit)
    dictRoadPandaFinal={}
    dictRoadPandaFinal={location:{subLocation:{bikeName:{'pickUpDate':pickUpTotal,'dropDate':dropTotal,'Lcost':Lcost,'Rcost':Rcost,'Pcost':Pcost,'LkmLimit':LkmLimit,'RkmLimit':RkmLimit,'PkmLimit':PkmLimit}}
                                  }
                        }
    #dictRoadPandaFinal[location][subLocation][bikeName]={'pickUpDate':pickUpTotal,'dropDate':dropTotal}
    return dictRoadPandaFinal      
    #return Lcost,Rcost,Pcost,LkmLimit,RkmLimit,PkmLimit       
        

    


def dateDefault(pickUpTotal,dropTotal):
    dateDiff=dropTotal-pickUpTotal
    totalHr=dateDiff.total_seconds()/3600
    pickVar=pickUpTotal
    dropVar=dropTotal
    qut=0
    rem=0
    i=0
    weekdayCount=0
    weekendCount=0
    remDropHr=0
    weekdayCountHr=0
    weekendCountHr=0
    cost=0
    weekdayCountHr1=0
    weekendCountHr1=0
#   print(totalHr)
    if(totalHr>24):
        #See pick up is a weekday or weekend,weekday then wd=24-pickup else wn is 24-pickup
        if(pickUpTotal.weekday()<=3):
            weekdayCountHr=24-int(pickUpTotal.strftime('%H'))
            totalHr=totalHr-weekdayCountHr
                
        else:
            weekendCountHr=24-int(pickUpTotal.strftime('%H'))
            totalHr=totalHr-weekendCountHr
        #qut=remianing hr from 12,no of full days count

        qut=int(totalHr/24)
    
        pickVar=pickUpTotal+timedelta(days=1)
        print(totalHr)
        print(qut)
        while(i<qut):
            if(pickVar.weekday()<=3):
                weekdayCount=weekdayCount+1
            else:
                weekendCount=weekendCount+1
            print(pickVar)
            pickVar=pickVar+timedelta(days=1)
#            print(weekdayCount,weekendCount,rem)
            i=i+1
        #remaining are the drop hr
        #total=24-pickup+fulldays*24+drophr
        if(dropVar.weekday()<=3):
            weekdayCountHr=weekdayCountHr+int(dropTotal.strftime('%H'))
        else:
            weekendCountHr=weekendCountHr+int(dropTotal.strftime('%H'))
    #less than 24 hr count
    else:
        if(pickUpTotal.weekday()<=3 and dropTotal.weekday()<=3):
            weekdayCountHr=totalHr
        if(pickUpTotal.weekday()>3 and dropTotal.weekday()>3):
            weekendCountHr=totalHr
        if(pickUpTotal.weekday()<=3 and dropTotal.weekday()>3):
            weekdayCountHr=24-int(pickUpTotal.strftime('%H'))
            weekendCountHr=int(dropTotal.strftime('%H'))
        if(pickUpTotal.weekday()>3 and dropTotal.weekday()<=3):
            weekendCountHr=24-int(pickUpTotal.strftime('%H'))
            weekendCountHr=int(dropTotal.strftime('%H'))


        
    weekdayCountHr=weekdayCountHr+weekdayCount*24
    weekendCountHr=weekendCountHr+weekendCount*24    
#    print(weekdayCountHr,weekendCountHr)
    dictRoadPanda=internalDB()
    #location,subLocation,bikeName,LweekdayRate,RweekdayRate,PweekdayRate,LweekendRate,pweekendRate,RweekendRate,weekdayCountHr,weekendCountHr
    l=[]
    for k1,v1 in dictRoadPanda.iteritems():
        #print(k1)
        for k2,v2 in dictRoadPanda[k1].iteritems():
            #print(k1,k2)
            for k3,v3 in dictRoadPanda[k1][k2].iteritems():
                #print(k1,k2,k3,dictRoadPanda[k1][k2][k3][0])
                #print(k1,k2,k3,dictRoadPanda[k1][k2][k3][0],dictRoadPanda[k1][k2][k3][1],dictRoadPanda[k1][k2][k3][2],dictRoadPanda[k1][k2][k3][3],dictRoadPanda[k1][k2][k3][4],dictRoadPanda[k1][k2][k3][5],weekdayCountHr,weekendCountHr)            
                a=priceStrucRoadPanda(k1,k2,k3,dictRoadPanda[k1][k2][k3][0],dictRoadPanda[k1][k2][k3][1],dictRoadPanda[k1][k2][k3][2],dictRoadPanda[k1][k2][k3][3],dictRoadPanda[k1][k2][k3][4],dictRoadPanda[k1][k2][k3][5],weekdayCountHr,weekendCountHr,pickUpTotal,dropTotal)
                l.append(a)
    print(l)

    
    #bikeName,Lkm,Rkm,Pkm,LweekdayRate,RweekdayRate,PweekdayRate,LweekendRate,PweekendRate,RweekendRate='honda',5,10,15,84,120,150,108,156,192,30,60,90,14,20,25,18,26,32




    
def internalDB():
    #dictRoadPanda=OrderedDict()
    #Order:'LweekdayRate':14,'RweekdayRate':20,'PweekdayRate':25,'LweekendRate':18,'RweekendRate':26,'PweekendRate':32
    dictRoadPanda={'mumbai':
                       {'IITPowaiMainGate':{'Honda Activa':[14,20,25,18,26,32]
                                            }
                        },
                   'bangalore':
                       {'HSR Layout Sector 5':{
                                            'Honda Dio':[14,20,25,18,26,32]
                                            ,'AVENGER STREET 220':[22,30,38,28 ,39,50]
                                            ,'YAMAHA FZS V2':[22,30,38,28,39,50]
                                            ,'THUNDER BIRD 500':[29,40,51,37,53,67]
                                            ,'DESERT STORM':[29,40,51,37,53,67]
                                            ,'AVENGER CRUISE 220':[22,30,38,28,39,50]
                                            ,'RE CLASSIC 350':[29,40,51,37,53,67]
                                            ,'HONDA HORNET':[22,30,38,28,39,50]
                                            ,'HONDA NAVI':[13,18,23,17,24,36]
                                            ,'HONDA ACTIVA 110':[14,20,25,18,26,32]
                                            }
                        },
                   'hydrabad':
                        {'Ayyappa soceiy Madhapur':{
                                                    'HONDA HORNET':[22,30,38,28,39,50]
                                                    ,'HONDA ACTIVA 110':[14,20,25,18,26,32]
                                                    }
                                                 
                        }
                   }
    
    #print(dictRoadPanda)
    #eg:k1=bangalore,k2=HSRLAYOut,k3=Hoda Dio
                
                #print(k3,":",dictRoadPanda[k1][k2][k3])
                
    return dictRoadPanda

pickUpTotal=datetime.strptime('24-02-2017 22', "%d-%m-%Y %H")                                                                            
dropTotal=datetime.strptime('27-02-2017 11', "%d-%m-%Y %H")
dateDefault(pickUpTotal,dropTotal)
#dateDefault(pickUpTotal,dropTotal)
