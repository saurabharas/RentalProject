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
    
      

def ajaxContainer(url,city,count):
    browser1.get(url)
    #findValues(browser1)
    dateVal=0
    if(datetime.now().isoweekday() and datetime.now().strftime('%H')==range(1,17)):
        dateVal=0
    elif(datetime.now().isoweekday() and datetime.now().strftime('%H')!=range(1,17)):
        dateVal=1
    elif(not datetime.now().isoweekday() and datetime.now().strftime('%H')==range(1,11)):
        dateVal=0
    elif(not datetime.now().isoweekday() and datetime.now().strftime('%H')!=range(1,11)):
        dateVal=1
    

    startVal=0
    endVal=4
    if(dateVal==1):
        startVal=1    
        endVal=5
    print(startVal,endVal)

    for N in range(0,1):
        x,y=datePickerXpath()
        print(x,y)
        browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[4]/span").click()
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_pick_time']/option[7]")).click().perform()
        #browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[4]/span").click()
        
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[1]/div[1]/input")).click().perform()
        #time.sleep(3)
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath("html/body/div[8]/div[1]/div[2]/table/tbody/tr[2]/td[7]/div")).click().perform()
        #browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[1]/div[2]/input").click()
        
        
        #browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[1]/div[2]/input").click()
        #browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[1]/div[2]/input").click()
        
        
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[3]/div[1]/input")).click().perform()
        #time.sleep(3)
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath("html/body/div[8]/div[1]/div[2]/table/tbody/tr[2]/td[7]/div")).click().perform()
        #browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[1]/div[2]/input").click()     
        browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[1]/div[2]/input").click()
        browser1.find_element_by_xpath("html/body/div[9]/div[2]/div/div[1]/div[1]").click()
        browser1.find_element_by_xpath(".//*[@id='show-bikes']/form[1]/ul/li[2]/div[1]/div/div[3]/div[2]/input").click()
        browser1.find_element_by_xpath("html/body/div[6]/div[2]/div/div[1]/div[2]").click()
        
        
'''
        presentDayVal=6
        presentWeekVal=3
        for x in range(1,8):
            presentDayVal=x
            x=x+1
            if(x==7):
                presentWeekVal=presentWeekVal+1
            if(x==7 and presentWeekVal):
                presentWeekVal=1
            #print(x,presentWeekVal)
                
'''         


        
        
        #inputElement.send_keys(dateCalculation(N))

        #select=Select(browser1.find_element_by_id("_pick_time"))
        #select.select_by_visible_text(timeCalculation())
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_pick_time']/option[7]")).click().perform()
        
'''		

        
        inputElement2.clear()
        inputElement2.send_keys(dateCalculation(N+1))

        #use for select options
        select=Select(browser1.find_element_by_id("_drop_time"))
        select.select_by_visible_text(timeCalculation())
        
'''

        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_drop_time']")).click().perform()
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_drop_time']/option[2]")).click().perform()
        

        #browser1.find_element_by_xpath(".//*[@id='_drop_time']").click()
        #browser1.find_element_by_xpath(".//*[@id='_drop_time']/option[12]").click()
        
        #Use when element is not clickable
'''
        ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='datesbtn']")).click().perform()
        
        if(count==0):
            findValues(browser1,city,count,dateCalculation(N),dateCalculation(N+1))
            count=count+1
        else:
            findValues(browser1,city,count,dateCalculation(N),dateCalculation(N+1))
'''    
'''
	
	
def findValues(browser1):
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeTitleUL=soup.find_all("ul",{"class":"book_bike_fleet happy_customers item"})
    bikeTitleList=[]
    bikeImgSrcList=[]
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
        
        print(bikeTitleList[x],bikeImgSrcList[x],bikeHourPriceList[x].text.encode('utf8'),bikeTotalPriceList[x].text.encode('utf8'))
        print("\n \n")

    
        #for value in tempList[0].contents:
            #print(value)
            #print("\n \n")
            #tempList.append(value2)
        #bikeTitle=tempList[0].text
        #bikeSrc=tempList[1].contents[0].get("src")
        #print(bikeTitle,bikeSrc)

    browser1.close()    	
		
	
	

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
		
'''	
'''
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
'''
    
'''
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
ajaxContainer("http://www.wickedride.com/booking/choose-models?start_date=13+Feb+2017&start_time=09%3A00&end_date=14+Feb+2017&end_time=22%3A00&city_id=1&_token=2OsO0ddkOdnsCY91cxxT8z3bQmJHC5ARvtDeAVZ9","Bangalore",0)
'''
ajaxContainer("https://www.rentrip.in/rent-bike/Bangalore","Bangalore",1)
ajaxContainer("https://www.rentrip.in/rent-bike/Indore","Indore",2)
ajaxContainer("https://www.rentrip.in/rent-bike/Chandigarh","Chandigarh",3)
ajaxContainer("https://www.rentrip.in/rent-bike/Chennai","Chennai",4)
ajaxContainer("https://www.rentrip.in/rent-bike/Coimbatore","Coimbatore",5)
ajaxContainer("https://www.rentrip.in/rent-bike/Jaipur","Jaipur",6)
ajaxContainer("https://www.rentrip.in/rent-bike/Guwahati","Guwahati",7)
'''
