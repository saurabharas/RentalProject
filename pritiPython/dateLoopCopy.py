'''
1.find currentTime
2.if currentTime > 12 & currentTime <9
2.1 
'''
import time
import SEL_Bykemania
from datetime import datetime, timedelta
def commonLoop():
    #dateVar=datetime.now()..............currentTime
    #print dateVar.hour
    #dateVar1=datetime.now()
    #dateVar=dateVar1.hour
    dateVar=14
    if(dateVar>=0 and dateVar<9):
        slots=0
        nightCount=0
        dateLoop=datetime.now()
        while(nightCount<1):
            while(slots<25):
                pickTime=9
                dropTime=pickTime+3
                n=0
                dateChange=dateLoop.strftime("%d,%m,%Y")
                while(n<5):
                    print(dateChange,pickTime,dropTime,n,slots)
                    pickTime=pickTime+3
                    dropTime=dropTime+3
                    n=n+1
                    slots=slots+1

                dateLoop=dateLoop+timedelta(days=1)
        nightCount=nightCount+1
    elif(dateVar>=9 and dateVar<24):
        slots=0
        nightCount=0
        dateLoop=datetime.now()
        if(dateVar>9 and dateVar<=12):
            n=1
            pickTime=12
            dropTime=pickTime+3
            
        elif(dateVar>=12 and dateVar<=15):
            n=2
            pickTime=15
            dropTime=pickTime+3

        elif(dateVar>=15 and dateVar<=18):
            n=3
            pickTime=18
            dropTime=pickTime+3
        
        elif(dateVar>=18 and dateVar<=21):
            n=4
            pickTime=21
            dropTime=pickTime+3
        '''
        elif(dateVar>=21 and dateVar<=24):
            n=4
            pickTime=21
            dropTime=pickTime+3
        '''
        
        while(slots<15):
            #n=0
            dateChange=dateLoop.strftime("%Y/%m/%d")
            while(n<5):
                #print(dateChange+' '+str(pickTime))
                #print(dateChange+' '+str(dropTime))
                SEL_Bykemania.main(dateChange,str(pickTime),str(dropTime))


        
                
                pickTime=pickTime+3
                dropTime=dropTime+3
                n=n+1
                slots=slots+1
                if(slots>15):
                    break
                
            n=0
            pickTime=9
            dropTime=pickTime+3
            dateLoop=dateLoop+timedelta(days=1)
        
        
        
                    
        

commonLoop()
