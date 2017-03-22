from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def dateCalculation(N):
        dateReq = datetime.now() + timedelta(days=N)
        return (dateReq.strftime('%d-%m-%Y'))


def currentTime():
    if(datetime.now().isoweekday()):
        timeReq = datetime.now() + timedelta(hours=4)
        value=timeReq.strftime('%H')
        val=0
    else:
        timeReq = datetime.now() + timedelta(hours=10)
        timeHr=timeReq.strftime('%H')
        val=1

    return(timeHr,val)
        
def timeCalculation():
    value=""
    timeHr,val=currentTime()
    if(val==0):
        if(int(timeHr)<6):
            value="09:00 AM"
        elif(int(timeHr)==6):
            value="10:00 AM"    
        elif(int(timeHr)==7):
            value="11:00 AM"
        elif(int(timeHr)==8):
            value="12:00 PM"
        elif(int(timeHr)==9):
            value="01:00 PM"
        elif(int(timeHr)==10):
            value="02:00 PM"
        elif(int(timeHr)==11):
            value="03:00 PM"
        elif(int(timeHr)==12):
            value="04:00 PM"
        elif(int(timeHr)==13):
            value="05:00 PM"
        elif(int(timeHr)==14):
            value="06:00 PM"
        elif(int(timeHr)==15):
            value="07:00 PM"
        elif(int(timeHr)==16):
            value="08:00 PM"
        elif(int(timeHr)==17):
            value="09:00 PM"
        else:
            value="10:00 PM"
        print(int(currentTime()))
        print(value)
    else:
        if(int(timeHr)<0):
            value="09:00 AM"
        elif(int(timeHr)==0):
            value="10:00 AM"    
        elif(int(timeHr)==1):
            value="11:00 AM"
        elif(int(timeHr)==2):
            value="12:00 PM"
        elif(int(timeHr)==3):
            value="01:00 PM"
        elif(int(timeHr)==4):
            value="02:00 PM"
        elif(int(timeHr)==5):
            value="03:00 PM"
        elif(int(timeHr)==6):
            value="04:00 PM"
        elif(int(timeHr)==7):
            value="05:00 PM"
        elif(int(timeHr)==8):
            value="06:00 PM"
        elif(int(timeHr)==9):
            value="07:00 PM"
        elif(int(timeHr)==10):
            value="08:00 PM"
        elif(int(timeHr)==11):
            value="09:00 PM"
        else:
            value="10:00 PM"

    return value

def datePickerXpath():
    x=2
    y=6
    if(datetime.now().strftime('%A')=='Monday'):
        x=x+1
    if(datetime.now().strftime('%H')==0):
        y=y+1
    if(x>4):
        x=1
    if(y>7):
        y=1
    xpath="html/body/div[8]/div[1]/div[2]/table/tbody/tr[%d]/td[%d]/div"%(x,y)
    return (x,y)
def dayDuration():
        dateVal=0
        dayCount=0
        if(datetime.now().isoweekday() and int(datetime.now().strftime('%H')) in range(1,17)):
                dateVal=0
                dayCount=0
        elif(datetime.now().isoweekday() and int(datetime.now().strftime('%H')) not in range(1,17)):
                dateVal=1
                dayCount=0
        elif(not datetime.now().isoweekday() and int(datetime.now().strftime('%H')) in range(1,11)):
                dateVal=0
                dayCount=1
        elif(not datetime.now().isoweekday() and int(datetime.now().strftime('%H')) not in range(1,11)):
                dateVal=1
                dayCount=1
        return dateVal,dayCount        
class varStatic:
        startVal=int(datetime.now().strftime('%d'))
        endVal=startVal+1
        timeIn=0
        daysCount=0
        timeOut=0
        count=0
        timeElapsed=0
def ajaxContainer(url,cityId,cityIdNo,city,count):
    browser1.get(url)
    #findValues(browser1)    
    dateVal,dayCount=dayDuration()
    print(dateVal,dayCount)
    
    if(int(datetime.now().strftime('%H'))<6 or int(datetime.now().strftime('%H'))>16):
        varStatic.timeIn=9
        if(varStatic.timeOut==0):
            varStatic.timeOut=9
        print("1")
    
    if(dateVal==0):
        print("2")
        if(dayCount==0):
            varStatic.timeIn=int(datetime.now().strftime('%H'))+4
            if(varStatic.timeOut==0):
                varStatic.timeOut=varStatic.timeIn
            print("3")
        else:
            varStatic.timeIn=int(datetime.now().strftime('%H'))+10
            if(varStatic.timeOut==0):
                varStatic.timeOut=varStatic.timeIn
            print("4")
    elif(int(datetime.now().strftime('%H'))>16):
        varStatic.startVal=int(datetime.now().strftime('%d'))+1
        varStatic.endVal=varStatic.startVal+1
        varStatic.timeIn=9
        if(varStatic.timeOut==0):
            varStatic.timeOut=varStatic.timeIn+4
        print("5")


    
            
        
    while(varStatic.daysCount<2):

        if(varStatic.count==0):    
            findValues(browser1,city,str(varStatic.startVal),str(varStatic.endVal),str(varStatic.timeElapsed),varStatic.count,varStatic.timeOut)
            varStatic.count=varStatic.count+1    
        else:
            findValues(browser1,city,str(varStatic.startVal),str(varStatic.endVal),str(varStatic.timeElapsed),varStatic.count,varStatic.timeOut)


        varStatic.timeOut=varStatic.timeOut+4
        varStatic.timeElapsed=varStatic.timeElapsed+4
        print("6")
        if(varStatic.timeOut>17):
            varStatic.daysCount=varStatic.daysCount+1
            varStatic.timeOut=9    
            varStatic.endVal=varStatic.endVal+1
        print(varStatic.startVal,varStatic.timeIn,varStatic.endVal,varStatic.timeOut,varStatic.timeElapsed)
        ajaxContainer("http://www.wickedride.com/booking/choose-models?start_date="+str(varStatic.startVal)+"+Feb+2017&start_time="+str(varStatic.timeIn)+"%3A00&end_date="+str(varStatic.endVal)+"+Feb+2017&end_time="+str(varStatic.timeOut)+"%3A00&city_id="+cityIdNo+"&_token="+cityId,cityId,cityIdNo,city,0)
        print("7")
    if(varStatic.daysCount==2):
        print("8")
        varStatic.startVal=int(datetime.now().strftime('%d'))
        varStatic.endVal=varStatic.startVal+1
        varStatic.timeIn=0
        varStatic.daysCount=0
        varStatic.timeOut=0
        varStatic.timeElapsed=0
        print("9")
    	
	
def findValues(browser1,city,fromDate,toDate,priceForTimeDuration,count,timeOut):
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeTitleUL=soup.find_all("ul",{"class":"book_bike_fleet happy_customers item"})
    bikeTitleList=[]
    bikeImgSrcList=[]



    if(count==0):
        f=open("wickedRide.txt","w")
        print("count =%d"%count)
        f.write("\n")
        f.write("%s FromDate= %s - ToDate= %s Time Duration: %s TimeOut %s"%(city,fromDate,toDate,priceForTimeDuration,timeOut))
        f.write("\n")
    else:
        f=open("wickedRide.txt","a")
        f.write("\n")
        f.write("%s FromDate= %s - ToDate= %s Time Duration: %s TimeOut %s"%(city,fromDate,toDate,priceForTimeDuration,timeOut))
        print("count =%d"%count)
        f.write("\n")
    for value in bikeTitleUL:
        tempList=[]
        #print(value)
        for value2 in value.contents[0].contents:
            tempList.append(value2)
        #print(tempList[0].text,tempList[1].contents[0].get("src"))
        bikeTitleList.append(tempList[0].text.encode('utf8'))
        bikeImgSrcList.append(tempList[1].contents[0].get("src").encode('utf8'))
        bikeHourPriceList=soup.find_all("div",{"class":"price effective-price"})
        bikeTotalPriceList=soup.find_all("div",{"class":"price total-price"})
    
        #bikeSoldOut=soup.find_all("div",{"class":"sold-out-wrapper show"})

    for x in range(0,len(bikeTitleList)-1):
        #print(bikeTitleList[x],bikeImgSrcList[x],bikeHourPriceList[x].text.encode('utf8'),bikeTotalPriceList[x].text.encode('utf8'))
        f.write("%s,%s,%s,%s"%(bikeTitleList[x],bikeImgSrcList[x],bikeHourPriceList[x].text.encode('utf8'),bikeTotalPriceList[x].text.encode('utf8')))
        f.write("\n")
    f.close()
    
    #browser1.close()    	
		
	
'''	

    bikeImageList=soup.find_all("a",{"class":"media-link"})
    
    if(count==0):
        f=open("rentrip.txt","w")
        f.write("\n")
        f.write("%s FromDate= %s - ToDate= %s"%(city,fromDate,toDate))
        f.write("\n")
        
       
    else:
        f=open("rentrip.txt","a")
        f.write("\n")
        f.write("%s FromDate= %s - ToDate= %s"%(city,fromDate,toDate))
        f.write("\n")
    bikeImgSrcList=[]
    for value in bikeImageList:
        bikeImgSrcList.append(value.contents[1].get("src"))
       

    bikeTitleList=soup.find_all("h4",{"class":"caption-title"})
    bikeTitleContentList=[]
    for value in bikeTitleList:
        bikeTitleContentList.append(value.text)

    #countLeftList=soup.find_all("div",{"class":"row search-border"})
    priceOuterList=soup.find_all("h2",{"class":"caption-title-sub"})
    priceList=[]
    localLocationList=[]
    for value in priceOuterList:
        priceList.append(value.contents[0].decode('utf-8')+value.contents[1].text)
        localLocationList.append(value.contents[3].text)
        #print(priceList)
		
	

    print(bikeImgSrcList)
    print(bikeTitleContentList)
    print(priceList)
    print(localLocationList) 
    
	
	
    for value in range(0,len(bikeImgSrcList)-1):
        f.write("%s,%s,%s,%s"%(bikeImgSrcList[value].decode('utf-8'),bikeTitleContentList[value].decode('utf-8'),priceList[value].decode('utf-8'),localLocationList[value].decode('utf-8')))
        f.write("\n")
    f.close()
    #localLocationList=soup.find_all("a",{"class":"pull-right"})
    #bikeEngine=soup.find_all("a",{"class":"pull-right"})
    
  
    print(bikeImageList)
    print("\n")
    print(bikeTitleList)
    print("\n")
    print(priceList)
    print("\n")
    print(localLocationList)
    print("\n")

    

    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    myContent=soup.find_all("div",{"class":"row search-border"})
    if(count==0):
        f=open("spanbikes.txt","w")
        f.write("\n")
        f.write("%s FromDate= %s - ToDate= %s"%(city,fromDate,toDate))
       
    else:
        f=open("spanbikes.txt","a")
        f.write("\n")
        f.write("%s FromDate= %s - ToDate= %s"%(city,fromDate,toDate))
        
    for myMainDivList in myContent:
        subList=myMainDivList.contents
        bikeImage=subList[1].contents[1].get("src")
        bikeTitle=subList[3].contents[1].text
        bikeDescription=subList[3].contents[3]
        listItemDesc=[]
        listItemDescTotal=[]
        count=0
        #for bikeItem in bikeDescription:
        bikeCountItemStr=str(bikeDescription)
        value1=unicode(bikeCountItemStr, "utf-8") #change
        soup1=BeautifulSoup(value1,"html.parser")
        #print(soup1)
        ls=soup1.find_all("span")
        bikeEngine=ls[0].text.encode('ascii')
        bikeType=ls[1].text.encode('ascii')
        openTime=ls[2].text.encode('ascii')
        closeTime=ls[3].text.encode('ascii')
        #print "bikeEngine= ",bikeEngine.encode('ascii')," bikeType= ",bikeType.encode('ascii'),"  openTime= ",openTime.encode('ascii')," closeTime= ",closeTime.encode('ascii')
        
            
        
        bikesRemainingCount=subList[5]
        list1=[]
        bikeCountItemStr=str(bikesRemainingCount)
        value1=unicode(bikeCountItemStr, "utf-8") #change
        soup1=BeautifulSoup(value1,"html.parser")
        ls=soup1.find_all("span")
        countLeft=ls[0].text.encode('ascii')
        price=ls[1].text.encode('ascii')
        if(count==0):
            f.write("%s,%s,%s,%s,%s,%s,%s,%s"%(bikeTitle,bikeImage,bikeEngine,bikeType,openTime,closeTime,countLeft,price))
        else:
            f.write("%s,%s,%s,%s,%s,%s,%s,%s"%(bikeTitle,bikeImage,bikeEngine,bikeType,openTime,closeTime,countLeft,price))
    f.close()
    #browser1.close()            
'''
	
browser1=webdriver.Chrome()
baseURL="http://www.wickedride.com/booking/choose-models?"

ajaxContainer("http://www.wickedride.com/booking/choose-models?start_date=13+Feb+2017&start_time=10%3A00&end_date=14+Feb+2017&end_time=12%3A00&city_id=1&_token=b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw","b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw","1","Bangalore",0)
ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=2&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","2","Jaipur",1)

ajaxContainer("http://www.wickedride.com/booking/choose-models?start_date=13+Feb+2017&start_time=10%3A00&end_date=14+Feb+2017&end_time=12%3A00&city_id=3&_token=b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw","bXlNk9zXv1OB2EI9JcHsVeeC7v2PsjILr80qenHi","3","Udaipur",0)
ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=4&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","bXlNk9zXv1OB2EI9JcHsVeeC7v2PsjILr80qenHi","4","Mysuru",1)

ajaxContainer("http://www.wickedride.com/booking/choose-models?start_date=13+Feb+2017&start_time=10%3A00&end_date=14+Feb+2017&end_time=12%3A00&city_id=5&_token=b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw","bXlNk9zXv1OB2EI9JcHsVeeC7v2PsjILr80qenHi","5","Bhuj",0)
ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=6&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","6","Ahemedabad",1)

ajaxContainer("http://www.wickedride.com/booking/choose-models?start_date=13+Feb+2017&start_time=10%3A00&end_date=14+Feb+2017&end_time=12%3A00&city_id=7&_token=b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw","b3TzUROqD1ZI6KpvqAcfVgQkmp3ZNnUtPlx1s7cw","7","Hospet",0)
ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=8&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","8","belgavi",1)

ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=8&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","9","Jaisalmer",1)
ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=8&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","10","Manipal",1)

ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=8&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","12","Gokarna",1)
ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=8&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","13","Chikmanglur",1)


ajaxContainer("https://www.wickedride.com/booking/choose-models?start_date=14+Feb+2017&start_time=11%3A00&end_date=15+Feb+2017&end_time=14%3A00&city_id=8&_token=DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","DQDgP0qLWtnazTuOrnqmfBJsxhro8tEUtXHCKiBp","14","Tumkur",1)










