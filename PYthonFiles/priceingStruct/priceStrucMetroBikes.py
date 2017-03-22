import time
from collections import Counter
from datetime import datetime, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import defaultdict

'''        
pickUpTotal=datetime.strptime('19-02-2017 12', "%d-%m-%Y %H")                                                                            
dropTotal=datetime.strptime('22-02-2017 19', "%d-%m-%Y %H")

pickUpDate=pickUpTotal.strftime('%d')                                                                            
dropDate=dropTotal.strftime('%d')

pickUpTime=pickUpTotal.strftime('%H')                                                                            
dropTime=dropTotal.strftime('%H')


cost=wickedRideTmingStruc(int(pickUpDate),int(dropDate),int(pickUpTime),int(dropTime),164,41,55,787,1200,pickUpTotal,dropTotal)
print(cost)
'''


'''

#This will give 
#weekdayInitialBaseCost=1-4hr(weekday)
#weekdayBaseRate=5-19 rate eg 41
#weekdayFinalBase=above 24 base(weekday) cost eg 787
#weekendFinalBase=above 24 base(weekend) cost eg 1200
#weekendBaseRate=>24 rate eg55

def rateScraper(pickUpDate,pickUpHr,dropDate,dropHr,count1):
    #dateReq.strftime('%d-%m-%Y')
    browser1=webdriver.Chrome()
    browser1.get("http://www.wickedride.com/booking/choose-models?start_date="+pickUpDate.strftime("%d")+"+Feb+2017&start_time="+str(pickUpHr)+"%3A00&end_date="+dropDate.strftime("%d")+"+Feb+2017&end_time="+str(dropHr)+"%3A00&city_id=1&_token=b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw")
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeTitleUL=soup.find_all("ul",{"class":"book_bike_fleet happy_customers item"})
    weekdayInitialBaseCostList1=[]
    weekdayBaseRateList1=[]    
    weekdayFinalBaseList1=[]
    weekendFinalBaseList1=[]
    weekendBaseRateList1=[]
    #1255-1200
    weekendBaseRateList2=[]
    bikeDict={}
    listReturned=[]

    bikeTitleUL=soup.find_all("ul",{"class":"book_bike_fleet happy_customers item"})
    bikeTitleList=[]
    
        
        
    if(count1==1):
        weekdayInitialBaseCostList=soup.find_all("div",{"class":"price total-price"})
        weekdayBikeNameList1=soup.find_all("div",{"class":"price total-price"})
        for value in weekdayInitialBaseCostList:
            a=value.text.encode("UTF-8")
            a1=a.replace("RS ", "")
            weekdayInitialBaseCostList1.append(int(a1))        
        listReturned=weekdayInitialBaseCostList1    
    elif(count1==2):
        weekdayBaseRateList=soup.find_all("div",{"class":"price total-price"})
        myDivisionHr=(24-int(pickUpHr))+int(dropHr)
        for value in weekdayBaseRateList:
            a=value.text.encode("UTF-8")
            a1=a.replace("RS ", "")
            myReqCost=int(int(a1)/myDivisionHr)
            weekdayBaseRateList1.append(myReqCost)
        listReturned=weekdayBaseRateList1
    elif(count1==3):
        weekdayFinalBaseList=soup.find_all("div",{"class":"price total-price"})
        for value in weekdayFinalBaseList:
            a=value.text.encode("UTF-8")
            a1=a.replace("RS ", "")
            weekdayFinalBaseList1.append(int(a1))
        listReturned=weekdayFinalBaseList1
    elif(count1==4):
        weekendFinalBaseList=soup.find_all("div",{"class":"price total-price"})
        for value in weekendFinalBaseList:
            a=value.text.encode("UTF-8")
            a1=a.replace("RS ", "")
            weekendFinalBaseList1.append(int(a1))
        listReturned=weekendFinalBaseList1
    elif(count1==5):
        weekendBaseRateList=soup.find_all("div",{"class":"price total-price"})
        for value in weekendBaseRateList:
            a=value.text.encode("UTF-8")
            a1=a.replace("RS ", "")

            weekendBaseRateList1.append(int(a1))
        #for x in range(0,len(weekendBaseRateList1)-1):
            #weekendBaseRateList2[x]=int(weekendBaseRateList1[x].encode("UTF-8").replace("RS ", ""))-int(weekendFinalBaseList1[x].encode("UTF-8").replace("RS ", ""))
        listReturned=weekendBaseRateList1
    for value in bikeTitleUL:
        tempList=[]
        #print(value)
        for value2 in value.contents[0].contents:
            tempList.append(value2)
        #print(tempList[0].text,tempList[1].contents[0].get("src"))
        bikeTitleList.append(tempList[0].text.encode('utf8'))
    
    #print(len(weekendBaseRateList1))
    #print(len(weekendFinalBaseList1))

    #the syntax is: mydict[key] = "value"
    #released["iphone 5S"] = 2013
                             
    for x in range(0,len(listReturned)-1):
        bikeDict[bikeTitleList[x]]=listReturned[x]
    

                             
    return bikeDict
        

    


def weekDayFindOut(pickUpDate,pickUpHr,dropHr,count):
        count1=0
        weekdayInitialBaseCostList1={}
        weekdayBaseRateList1={}    
        weekdayFinalBaseList1={}
        d=()
        pickUpHr=int(pickUpDate.strftime("%H"))
        dropHr=pickUpHr+3
        dropDate=pickUpDate
        #print(pickUpDate.strftime("%d"),pickUpHr,dropDate.strftime("%d"),dropHr)

        weekdayInitialBaseCostList1=rateScraper(pickUpDate,pickUpHr,dropDate,dropHr,1)

        #print(weekdayInitialBaseCostList1)
        #print("\n \n")
        #print(weekdayBaseRateList1)
        pickUpHr1=pickUpHr+3
        dropHr1=(pickUpHr1+17)-24
        pickUpDate1=pickUpDate
        dropDate1=pickUpDate+timedelta(days=1)
        #print(pickUpHr1,dropHr1,pickUpDate1.strftime("%d"),dropDate1.strftime("%d"))

        weekdayBaseRateList1=rateScraper(pickUpDate1,pickUpHr1,dropDate1,dropHr1,2)

        #print(weekdayBaseRateList1)
        #print("\n \n")
        #print(weekdayBaseRateList1)
        #function
         
        pickUpHr2=pickUpHr
        dropHr2=(pickUpHr+21)-24
        pickUpDate2=pickUpDate
        dropDate2=pickUpDate+timedelta(days=1)
        #print(pickUpHr2,dropHr2,pickUpDate2.strftime("%d"),dropDate2.strftime("%d"))

        weekdayFinalBaseList1=rateScraper(pickUpDate2,pickUpHr2,dropDate2,dropHr2,3)
        #print(weekdayFinalBaseList1)
        #print("\n \n")
        #function
        currentDay=pickUpDate.weekday()
        dayToBeadded=5-currentDay
        nextDate=pickUpDate+timedelta(days=dayToBeadded)
        if(count==0):
            a,b=weekendFindOut(nextDate,pickUpHr,dropHr,1)
            d=(weekdayInitialBaseCostList1,weekdayBaseRateList1,weekdayFinalBaseList1,a,b)
        else:
            d=(weekdayInitialBaseCostList1,weekdayBaseRateList1,weekdayFinalBaseList1)
        return d
def weekendFindOut(pickUpDate,pickUpHr,dropHr,count):
        weekendFinalBaseList1={}
        weekendBaseRateList1={}
        #1255-1200
        weekendBaseRateList2={}       
        #function
        d=()
        if(pickUpDate.weekday()==5):

            pickUpHr1=int(pickUpDate.strftime("%H"))+5
            dropHr1=pickUpHr1+1
            pickUpDate1=pickUpDate
            dropDate1=pickUpDate
            #print(pickUpHr1,dropHr1,pickUpDate1.strftime("%d"),dropDate1.strftime("%d"))
            weekendFinalBaseList1=rateScraper(pickUpDate1,pickUpHr1,dropDate1,dropHr1,4)
            #print(weekendFinalBaseList1)
        

            pickUpHr2=int(pickUpDate.strftime("%H"))+5
            dropHr2=(pickUpHr2+25)-24
            pickUpDate2=pickUpDate
            dropDate2=pickUpDate+timedelta(days=1)
            #print(pickUpHr2,dropHr2,pickUpDate2.strftime("%d"),dropDate2.strftime("%d"))
            weekendBaseRateList1=rateScraper(pickUpDate2,pickUpHr2,dropDate2,dropHr2,5)
        elif(pickUpDate.weekday()==6):

            pickUpHr1=int(pickUpDate.strftime("%H"))+5
            dropHr1=pickUpHr1+1
            pickUpDate1=pickUpDate+timedelta(days=6)
            dropDate1=pickUpDate1
            #print(pickUpHr1,dropHr1,pickUpDate1.strftime("%d"),dropDate1.strftime("%d"))
            weekendFinalBaseList1=rateScraper(pickUpDate1,pickUpHr1,dropDate1,dropHr1,4)
            #print(weekendFinalBaseList1)
                    
            pickUpDate2=pickUpDate+timedelta(days=6)
            dropDate2=pickUpDate2+timedelta(days=1)
            pickUpHr2=int(pickUpDate2.strftime("%H"))+5
            dropHr2=(pickUpHr2+25)-24
            #print(pickUpDate2.strftime("%d %H"),dropDate2.strftime("%d %H"))
            #print(pickUpHr2,dropHr2,pickUpDate2.strftime("%d"),dropDate2.strftime("%d"))
            weekendBaseRateList1=rateScraper(pickUpDate2,pickUpHr2,dropDate2,dropHr2,5)
        #Counter({'a':1, 'b':2, 'c':3})            
        #cost2-cost1
        #function
        #weekendBaseRate=cost2-cost1
        

        #print(weekendBaseRateList1)
        #print("\n \n")
        #print(weekendFinalBaseList1)
        #print("\n \n")   
        #print(len(weekendBaseRateList1))
        #print(len(weekendFinalBaseList1))
        A=Counter(weekendBaseRateList1)
        B=Counter(weekendFinalBaseList1)
        C=A-B
        #print(C)
        #print("\n \n") 
        for x in range(0,len(weekendBaseRateList1)-1):
            pass
            
            a=weekendBaseRateList1[x].encode("UTF-8")
            a1=a.replace("RS ", "")
            b=weekendFinalBaseList1[x].encode("UTF-8")
            b1=b.replace("RS ", "")
            weekendBaseRateList2.append(int(a1)-int(b1))
           
         
        #print(weekendBaseRateList1)
        #print(weekendBaseRateList2)    
        #print(weekendBaseRateList1)

    
        dayToBeadded=7-pickUpDate.weekday()
        nextDate=pickUpDate+timedelta(days=dayToBeadded)
        if(count==0):
            a,b,c=weekDayFindOut(nextDate,pickUpHr,dropHr,1)
            d=(a,b,c,weekendFinalBaseList1,C)
        else:
            d=(weekendFinalBaseList1,C)
        return d
'''    

#from datetime import datetime

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
#datetime.now().strftime('%H')
def pricingStrucMetroBikes(location,subLocation,bikeName,weekdayBaseRate,weekdayFinalBase,weekendBaseRate,weekendFinalBase,weekdayInitialBaseCost,minimumBillingHr,pickUpTotal,dropTotal,pickUpDate,dropDate,pickUpTime,dropTime):
#weekdayBaseRate=5-19 rate eg 41
#weekendBaseRate=>24 rate eg55
#weekdayFinalBase=above 24 base(weekday) cost eg 787
#weekendFinalBase=above 24 base(weekend) cost eg 1200
#weekdayInitialBaseCost=1-4hr(weekday) eg 164

    totalDays=(dropDate-pickUpDate)+1
    totalHr=0
    cost=0
    diffDate=dropTotal-pickUpTotal
    totalHr=diffDate.total_seconds()/3600
#    print(totalHr)
    '''
    if(dropTime>pickUpTime):
        totalHr=(totalDays-2)*24+((dropTime)+(24-pickUpTime))
    else:
        totalHr=(totalDays-2)*24+((dropTime)+(24-pickUpTime))
    print(totalHr)
    '''
    #weekday-weekday
    if(pickUpTotal.weekday()<5 and dropTotal.weekday()<5):
#        print("1")
        if(totalHr<=4):
            cost=weekdayInitialBaseCost
#            print("1.1")
        if(totalHr>=5):
#                print("3.2.1")
                #noOfWeekday=dropDate.weekday()-pickUpDate.weekday()
                qot=int(totalHr/24)
#                print(qot)
                rem=totalHr%24
#                print(rem)
                if(rem<20):
#                    print("3.2.1.1")
                    cost=qot*weekdayFinalBase+rem*weekdayBaseRate
                else:
#                    print("3.2.1.2")  
                    cost=qot*weekendFinalBase+weekdayFinalBase

 
    #weekend-weekend
    if(pickUpTotal.weekday()>4 and dropTotal.weekday()>4):
#        print("2")
        if(totalHr<=24):
            cost=weekendFinalBase
#            print("2.1")
        if(totalHr>=25):
            cost=weekendFinalBase+(totalHr-24)*weekendBaseRate
#            print("2.2")
    #weekday-weekend
    noOfWeekday=0
    if(pickUpTotal.weekday()<5 and dropTotal.weekday()>4):
    
#        print("3")
        if(totalDays<=1):
#            print("3.1")
            if(totalHr<=24):
                cost=weekendFinalBase
#                print("3.1.1")
        if(totalDays>=2):
#            print("3.2")
            if(dropTotal.weekday()==5):
#                print("3.2.1")
                #noOfWeekday=dropDate.weekday()-pickUpDate.weekday()
                totalWeekdayHr=totalHr-24
                qot=int(totalWeekdayHr/24)
                rem=totalWeekdayHr%24
                if(rem<20):
#                    print("3.2.1.1")
                    cost=weekendFinalBase+qot*weekdayFinalBase+rem*weekdayBaseRate
                else:
#                    print("3.2.1.2")  
                    noOfWeekday=dropDate.weekday()-pickUpDate.weekday()
                    cost=weekendFinalBase+qot*weekdayFinalBase+weekdayFinalBase
            if(dropTotal.weekday()==6):
                noOfWeekday=dropTotal.weekday()-pickUpTotal.weekday()
#                print("3.2.2")
                #(noOfWeekday-2)*weekdayFinalBase)
                cost=((24-pickUpTime)*weekdayBaseRate)+(noOfWeekday-2)*weekdayFinalBase+weekendFinalBase+(dropTime*weekendBaseRate)
    #weekend-weekday         
    if(pickUpTotal.weekday()>4 and dropTotal.weekday()<5):
        noOfWeekday=0
#        print("4.1")
        noOfWeekday=dropTotal.weekday()-pickUpTotal.weekday()
        if(totalDays<=1):
#            print("4.1")
            if(totalHr<=24):
#                print("4.1.1")
                cost=weekendFinalBase
        if(totalDays>=2):
#            print("4.2")
            if(pickUpTotal.weekday()==6):
#                print("4.2.1")
                #noOfWeekday=dropDate.weekday()-pickUpDate.weekday()
                totalWeekdayHr=totalHr-24
                qot=int(totalWeekdayHr/24)
                rem=totalWeekdayHr%24
                if(rem<20):
#                    print("4.2.1.1")
                    cost=weekendFinalBase+qot*weekdayFinalBase+rem*weekdayBaseRate
                else:
#                    print("4.2.1.2")
                    noOfWeekday=dropTotal.weekday()-pickUpTotal.weekday()
                    cost=weekendFinalBase+qot*weekdayFinalBase+weekdayFinalBase
            if(pickUpTotal.weekday()==5):
                noOfWeekday=pickUpTotal.weekday()-dropTotal.weekday()
    #                print("4.2.2")
                cost=(24-pickUpTime)*weekendBaseRate+(noOfWeekday-1)*weekdayFinalBase+weekendFinalBase+dropTime*weekdayBaseRate
        


    print(location,subLocation,bikeName,cost)    


    #return cost







'''                        
def dateDefault(pickUpTotal,dropTotal):
    currentDate=datetime.now()+timedelta(hours=1)
    print(currentDate)
    currentTimeHr=currentDate.strftime('%H')
    pickUpHr=0
    dropHr=0
    count=0
    count1=0
    d=()
    
    if(int(currentTimeHr)>=13 and int(currentTimeHr)<=15):
        if(currentDate.weekday()<5):
            d=weekDayFindOut(currentDate,pickUpHr,dropHr,0)
        elif(currentDate.weekday()>4):
            d=weekendFindOut(currentDate,pickUpHr,dropHr,0)
    else:
        d=({'Iron 883': 2290, 'Ninja ER-6n': 2880, 'Himalayan': 272, 'Monster 821': 3950, 'TNT 300': 1030, 'Forty Eight': 2970, 'Thunderbird - 350': 164, 'Street 750': 1330, 'Thunderbird - 500': 204, 'Versys 650': 3100, 'Scrambler': 2370, 'Avenger': 132, 'Classic - 350': 164, 'RC 390': 316, 'Duke 390': 248, 'Dominar': 850, 'TNT 600 GT': 2160, 'Bullet 350':164, 'RC 200': 256, 'TNT 600i': 2880, 'Desert Storm - 500': 204, 'Hyperstrada': 3710, 'Ninja 650': 1710, 'Tiger 800 XR': 3430, 'Bullet Electra - 350': 164, 'Mojo': 204, 'Duke 200': 200}, {'Iron 883': 229, 'Ninja ER-6n': 288, 'Himalayan': 68, 'Monster 821': 395, 'TNT 300': 103, 'Forty Eight': 297, 'Thunderbird - 350': 41, 'Street 750': 133, 'Thunderbird - 500': 51, 'Versys 650': 310, 'Scrambler': 237, 'Avenger': 33, 'Classic - 350': 41, 'RC 390': 79, 'Duke 390': 62, 'Dominar': 85, 'TNT 600 GT': 216, 'Bullet 350': 41, 'RC 200': 64, 'TNT 600i': 288, 'Desert Storm - 500': 51, 'Hyperstrada': 371, 'Ninja 650': 171, 'Tiger 800 XR': 343, 'Bullet Electra - 350': 41, 'Mojo': 51, 'Duke 200': 50}, {'Iron 883': 4809, 'Ninja ER-6n': 6048, 'Himalayan': 1305, 'Monster 821': 8295, 'TNT 300': 1977, 'Forty Eight': 6237, 'Thunderbird - 350': 787, 'Street 750': 2553, 'Thunderbird - 500': 979, 'Versys 650': 6510, 'Scrambler': 4550, 'Avenger': 633, 'Classic - 350': 787, 'RC 390': 1516, 'Duke 390': 1190, 'Dominar': 1785, 'TNT 600 GT': 4147, 'Bullet 350': 787, 'RC 200': 1228, 'TNT 600i': 6048, 'Desert Storm - 500': 979, 'Hyperstrada': 7791, 'Ninja 650': 3283, 'Tiger 800 XR': 7203, 'Bullet Electra - 350': 787, 'Mojo': 979, 'Duke 200': 960}, {'Iron 883': 5496, 'Ninja ER-6n': 6912, 'Himalayan': 2000, 'Monster 821': 10824, 'Z 250': 2592, 'TNT 300': 3312, 'Forty Eight': 7128, 'Thunderbird - 350': 1320, 'Street 750': 4272, 'Thunderbird - 500': 1656, 'Versys 650': 7440, 'Scrambler': 7584, 'Avenger': 960, 'Classic - 350': 1200, 'RC 390': 2544, 'Duke 390': 1992, 'TNT 600 GT': 6912, 'Bullet 350': 1200, 'RC 200': 2064, 'TNT 600i': 6912, 'Desert Storm - 500': 1656, 'Hyperstrada': 11880, 'Ninja 650': 5496, 'Tiger 800 XR': 8232, 'Duke 200': 1608, 'Mojo': 1656, 'Bullet Electra - 350': 1200}, Counter({'Hyperstrada': 495, 'Monster 821': 451, 'Tiger 800 XR': 343, 'Scrambler': 316, 'Versys 650': 310, 'Forty Eight': 297, 'Ninja ER-6n': 288, 'TNT 600 GT': 288, 'TNT 600i': 288, 'Iron 883': 229, 'Ninja 650': 229, 'Street 750': 178, 'TNT 300': 138, 'Z 250': 108, 'RC 390': 106, 'Himalayan': 91, 'RC 200': 86, 'Duke 390': 83, 'Thunderbird - 500': 69, 'Desert Storm - 500': 69, 'Mojo': 69, 'Duke 200': 67, 'Thunderbird - 350': 55, 'Classic - 350': 55, 'Bullet 350': 55, 'Bullet Electra - 350': 55, 'Avenger': 44}))
    
    #print(len(d[4]))
    d1=d[0]
    d2=d[1]
    d3=d[2]
    d4=d[3]
    d5=d[4]
        

    dd = defaultdict(list)

    for d in (d1, d2,d3,d4,d5): # you can list as many input dicts as you want here
        for key, value in d.iteritems():
            dd[key].append(value)

    
    pickUpTotal=datetime.strptime('19-02-2017 12', "%d-%m-%Y %H")                                                                            
    dropTotal=datetime.strptime('22-02-2017 19', "%d-%m-%Y %H")

    pickUpDate=pickUpTotal.strftime('%d')                                                                            
    dropDate=dropTotal.strftime('%d')

    pickUpTime=pickUpTotal.strftime('%H')                                                                            
    dropTime=dropTotal.strftime('%H')


    cost=wickedRideTmingStruc(int(pickUpDate),int(dropDate),int(pickUpTime),int(dropTime),164,41,55,787,1200,pickUpTotal,dropTotal)
    print(cost)

    
    

    
    for key, value in dd.iteritems():
        #print(key)    
        print(key,value[0])

    #print(dd)
    
'''
def dateDefault(pickUpTotal,dropTotal):
    dictMetroBikes=internalDBMetroBikes()
    #location,subLocation,bikeName,LweekdayRate,RweekdayRate,PweekdayRate,LweekendRate,pweekendRate,RweekendRate,weekdayCountHr,weekendCountHr
   

    pickUpDate=pickUpTotal.strftime('%d')                                                                            
    dropDate=dropTotal.strftime('%d')

    pickUpTime=pickUpTotal.strftime('%H')                                                                            
    dropTime=dropTotal.strftime('%H')

    

    l=[]
    for k1,v1 in dictMetroBikes.iteritems():
        #print(k1)
        for k2,v2 in dictMetroBikes[k1].iteritems():
            #print(k1,k2)
            for k3,v3 in dictMetroBikes[k1][k2].iteritems():
                #print(k1,k2,k3,dictRoadPanda[k1][k2][k3][0])
                #print(k1,k2,k3,dictRoadPanda[k1][k2][k3][0],dictRoadPanda[k1][k2][k3][1],dictRoadPanda[k1][k2][k3][2],dictRoadPanda[k1][k2][k3][3],dictRoadPanda[k1][k2][k3][4],dictRoadPanda[k1][k2][k3][5],weekdayCountHr,weekendCountHr)            
                #weekdayBaseRate,weekendBaseRate,weekdayFinalBase,weekendFinalBase,weekdayInitialBaseCost,minimumBillingHr,pickUpTotal,dropTotal,pickUpDate,dropDate,pickUpTime,dropTime
                a=pricingStrucMetroBikes(k1,k2,k3,dictMetroBikes[k1][k2][k3][0],dictMetroBikes[k1][k2][k3][1],dictMetroBikes[k1][k2][k3][2],dictMetroBikes[k1][k2][k3][3],164,10,pickUpTotal,dropTotal,int(pickUpDate),int(dropDate),int(pickUpTime),int(dropTime))
                #print(a)
                #l.append(a)

    #print(l)




def internalDBMetroBikes():
    '''
    #Order in List:
    weekdayInitialBaseCost=1-4hr(weekday) eg 164
    weekdayBaseRate=5-19 rate eg 41
    weekendBaseRate=>24 rate eg55
    weekdayFinalBase=above 24 base(weekday) cost eg 787
    weekendFinalBase=above 24 base(weekend) cost eg 1200
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '''


    #Values to be put remains
    dictMetroBikes={'bangalore':
                       {'Jayanagar':     {
                                           'IRON 883':[500,229,5496,229,5496]
                                           ,'STREET 750':[500,133,4272,178,2553]
                                           ,'THUNDERBIRD - 500':[500,62,1340,75,1620]
                                           ,'CLASSIC - 350':[1500,65,1400,80,1700]
                                           ,'THUNDERBIRD - 350':[1500,65,1400,80,1750]
                                           ,'TIGER 800 XR':[500,35,700,45,850]
                                           ,'SCRAMBLER':[500,30,650,40,800]
                                           ,'ENFIELD BULLET ELECTRA - 350':[1500,90,1900,100,2100]
                                           ,'FORTY EIGHT':[500,20,350,23,400]
                                           ,'HIMALAYAN':[500,20,350,23,400]
                                           ,'AVENGER':[1500,60,1300,75,1650]
                                           ,'DOMINAR':[1500,95,2050,110,2370]

                                          }
                        ,'AECS Layout - Kundalahalli':{
                                            'IRON 883':[500,35,700,45,850]
                                           ,'DESERT STORM - 500':[5000,418,8030,418,8580]
                                           ,'CLASSIC - 350':[500,30,650,40,800]
                                           ,'THUNDERBIRD - 350':[500,45,900,60,1200]
                                           ,'NINJA 650':[500,23,500,30,600]
                                           ,'DUKE 390':[2000,106,2080,106,2300]
                                           ,'DUKE 200':[500,30,650,40,800]
                                           ,'HIMALAYAN':[2000,96,1640,96,2080]
                                           ,'AVENGER':[500,35,700,45,850]
                                           ,'RC 390':[500,30,650,40,800]


                                            }
                        ,'Koramangala':{
                                            'IRON 883':[500,50,950,65,1300]
                                           ,'STREET 750':[500,30,650,40,800]
                                           ,'CLASSIC - 350':[500,23,350,25,400]
                                           ,'THUNDERBIRD - 350':[500,30,700,45,850]
                                           ,'TNT 600 GT':[500,37,850,50,950]
                                           ,'ELECTRA - 350':[500,30,700,45,850]
                                           ,'DUKE 200':[500,23,350,25,400]
                                           ,'TNT 600I':[500,30,700,45,850]
                                           ,'ENFIELD HIMALAYAN':[500,37,850,50,950]
                                           ,'AVENGER':[500,30,700,45,850]
                                           ,'RC 390':[500,23,350,25,400]
                            
                                            }
                        ,'Indiranagar 1st Block':{
                                           'IRON 883':[500,50,950,65,1300]
                                           ,'STREET 750':[500,30,650,40,800]
                                           ,'CLASSIC - 350':[500,23,350,25,400]
                                           ,'THUNDERBIRD - 350':[500,30,700,45,850]
                                           ,'TIGER 800 XR':[500,343,8232,343,8232]
                                           ,'DUKE 390':[500,62,1190,83,1992]
                                           ,'RC 200':[500,64,1228,86,2064]
                                           ,'MOJO':[500,51,979,69,1656]
                                           ,'HIMALAYAN':[500,37,850,50,950]
                                           ,'AVENGER':[500,30,700,45,850]
                                           ,'RC 390':[500,23,350,25,400]
                                           ,'HYPERSTRADA':[500,371,8000,495,11880]
                                            }
                        ,'Electronic City':{
                                           'CLASSIC - 350':[500,23,350,25,400]
                                           ,'BULLET 350':[500,35,700,45,850]
                                           ,'THUNDERBIRD - 350':[500,30,650,40,800]
                                           ,'BULLET ELECTRA - 350':[500,20,350,23,400]
                                           ,'DUKE 390':[500,20,350,23,400]
                                           ,'DUKE 200':[500,20,350,23,400]
                                           ,'HIMALAYAN':[500,20,350,23,400]
                                           ,'AVENGER':[500,30,700,45,850]
                                            }
                        
                        ,'Art of Living, Kanakapura Main Road':{
                                           'AVENGER':[500,45,900,60,1200]
                                           }
                                       
                        ,'Chandapura':{
                                           'THUNDERBIRD - 350':[500,45,900,60,1200]
                                           ,'AVENGER':[500,35,700,45,850]
                                            }
                        ,'OYO Rooms - Indiranagar':{
                                           'Classic 350':[500,45,900,60,1200]
                                           ,'THUNDERBIRD - 350':[500,35,700,45,850]
                                           ,'MOJO':[500,30,650,40,800]
                                           ,'HIMALAYAN':[500,20,350,23,400]
                                           ,'AVENGER':[500,30,700,45,850]
                                           ,'MONSTER 821':[500,30,700,45,850]
                                            }
                        ,'OYO Rooms - Marathahalli Innovative Multiplex':{
                                           'CLASSIC - 350':[500,45,900,60,1200]
                                           ,'650':[500,35,700,45,850]
                                           ,'RC 200':[500,30,650,40,800]
                                           ,'AVENGER':[500,20,350,23,400]
                                           ,'TNT 300':[500,20,350,23,400]
                                            }

                        ,'OYO Rooms - Kormangala Sony Signal':{
                                           'STREET 750':[500,45,900,60,1200]
                                           ,'CLASSIC - 350':[500,35,700,45,850]
                                           ,'NINJA ER-6N':[500,30,650,40,800]
                                           ,'VERSYS 650':[500,20,350,23,400]
                                           ,'HIMALAYAN':[500,20,350,23,400]
                                            }
                        ,'Hebbal (Sahakara Nagar)':{
                                           'Classic 350':[500,45,900,60,1200]
                                           ,'BULLET 350':[500,35,700,45,850]
                                           ,'DUKE 390':[500,30,650,40,800]
                                           ,'DUKE 200':[500,20,350,23,400]
                                           ,'VERSYS 650':[500,20,350,23,400]
                                           ,'AVENGER':[500,20,350,23,400]
                                            }

                                                                                
                        }
                    ,'Jaipur':{
                        'JLN MARG':         {
                                           'STREET 750':[500,45,900,60,1200]
                                           ,'BULLET 350':[500,35,700,45,850]
                                           ,'DUKE 390':[500,30,650,40,800]
                                           ,'DUKE 200':[500,20,350,23,400]
                                           ,'VERSYS 650':[500,20,350,23,400]
                                           ,'AVENGER':[500,20,350,23,400]
                                           }
                        ,'Hebbal (Sahakara Nagar)':{
                                           'Classic 350':[500,45,900,60,1200]
                                           ,'BULLET 350':[500,35,700,45,850]
                                           ,'DUKE 390':[500,30,650,40,800]
                                           ,'DUKE 200':[500,20,350,23,400]
                                           ,'VERSYS 650':[500,20,350,23,400]
                                           ,'AVENGER':[500,20,350,23,400]
                                            }

                        
                        }
                   
                   }
                    
    #print(dictWickedRide)
    return dictMetroBikes


    


pickUpTotal=datetime.strptime('02-03-2017 09', "%d-%m-%Y %H")                                                                            
dropTotal=datetime.strptime('03-03-2017 11', "%d-%m-%Y %H")
'''
pickUpDate=pickUpTotal.strftime('%d')                                                                            
dropDate=dropTotal.strftime('%d')

pickUpTime=pickUpTotal.strftime('%H')                                                                            
dropTime=dropTotal.strftime('%H')
'''

dateDefault(pickUpTotal,dropTotal)


'''
weekdayInitialBaseCost=1-4hr(weekday)
weekdayBaseRate=5-19 rate eg 41
weekendBaseRate=>24 rate eg55
weekdayFinalBase=above 24 base(weekday) cost eg 787
weekendFinalBase=above 24 base(weekend) cost eg 1200

steps:
1.Find current date and time from calnedar
2.find today is a weekday or a weekend
3.If weekday:
3.1 Find total rate for 1-4 hrs(weekdayInitialBaseCost)
3.2 Find hr rate from 5-19 hrs (weekdayBaseRate)
3.3 Find total rate from 20-24hr (weekdayFinalBase)
3.4 GoTo weekend and perform weekend steps
4.If weekend:
4.1 Find Total Rate for 1-24 hrs (weekendFinalBase)
4.2 find hr rate for above 24-44 hrs(weekendBaseRate)
4.3 GoTo weekday and perform weekday steps

'''



