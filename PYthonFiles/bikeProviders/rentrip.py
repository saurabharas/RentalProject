from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
#from pyvirtualdisplay import Display
#from lxml import html
#from xvfbwrapper import Xvfb
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def dateCalculation(N):
    dateReq = datetime.now() + timedelta(days=N)
    return (dateReq.strftime('%d-%m-%Y'))


def currentTime():
    timeReq = datetime.now() + timedelta(hours=3)
    return (timeReq.strftime('%H'))

def timeCalculation():
    value=""
    if(int(currentTime())<7):
        value="09:00 AM"
    elif(int(currentTime())==7):
        value="10:00 AM"    
    elif(int(currentTime())==8):
        value="11:00 AM"
    elif(int(currentTime())==9):
        value="12:00 PM"
    elif(int(currentTime())==10):
        value="01:00 PM"
    elif(int(currentTime())==11):
        value="02:00 PM"
    elif(int(currentTime())==12):
        value="03:00 PM"
    elif(int(currentTime())==13):
        value="04:00 PM"
    elif(int(currentTime())==14):
        value="05:00 PM"
    elif(int(currentTime())==15):
        value="06:00 PM"
    elif(int(currentTime())==16):
        value="07:00 PM"
    elif(int(currentTime())==17):
        value="08:00 PM"
    else:
        value="09:00 PM"
    print(int(currentTime()))
    print(value)
    return value    
      

def ajaxContainer(url,city,count):
    browser1.get(url)
    startVal=0
    endVal=4
    if(int(currentTime())<7 or int(currentTime())>=18):
        startVal=1    
        endVal=5
    print(startVal,endVal)
    for N in range(startVal,endVal):
        inputElement = browser1.find_element_by_xpath(".//*[@id='pickDate']")
        inputElement2 = browser1.find_element_by_xpath(".//*[@id='dropDate']")
        
        inputElement.clear()
        inputElement.send_keys(dateCalculation(N))

        select=Select(browser1.find_element_by_id("_pick_time"))
        select.select_by_visible_text(timeCalculation())
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_pick_time']/option[7]")).click().perform()
        
       

        
        inputElement2.clear()
        inputElement2.send_keys(dateCalculation(N+1))

        #use for select options
        select=Select(browser1.find_element_by_id("_drop_time"))
        select.select_by_visible_text(timeCalculation())
        


        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_drop_time']")).click().perform()
        #ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='_drop_time']/option[2]")).click().perform()
        

        #browser1.find_element_by_xpath(".//*[@id='_drop_time']").click()
        #browser1.find_element_by_xpath(".//*[@id='_drop_time']/option[12]").click()
        
        #Use when element is not clickable
        ActionChains(browser1).move_to_element(browser1.find_element_by_xpath(".//*[@id='datesbtn']")).click().perform()
        
        if(count==0):
            findValues(browser1,city,count,dateCalculation(N),dateCalculation(N+1))
            count=count+1
        else:
            findValues(browser1,city,count,dateCalculation(N),dateCalculation(N+1))
    
def findValues(browser1,city,count,fromDate,toDate):
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
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
    print(bikeImgSrcList)
    print(bikeTitleContentList)
    print(priceList)
    print(localLocationList) 
    '''
    for value in range(0,len(bikeImgSrcList)-1):
        f.write("%s,%s,%s,%s"%(bikeImgSrcList[value].decode('utf-8'),bikeTitleContentList[value].decode('utf-8'),priceList[value].decode('utf-8'),localLocationList[value].decode('utf-8')))
        f.write("\n")
    f.close()
    #localLocationList=soup.find_all("a",{"class":"pull-right"})
    #bikeEngine=soup.find_all("a",{"class":"pull-right"})
    
    '''
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

'''
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[4]","Delhi",0)

ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[2]","Pune",1)

ajaxContainer("/html/body/form/div[6]/div[2]/div/div[2]/div/div/div/select/option[6]","Shimla",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[5]","Kolkata",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[7]","Manali",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[8]","Goa",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[9]","Dharamshala",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[10]","Shrinagar",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[11]","Nainital",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[12]","Mount Abu",2)
ajaxContainer(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[3]","Mumbai",2)
'''


browser1=webdriver.Chrome()
ajaxContainer("https://www.rentrip.in/rent-bike/Ahmedabad","Ahemdabad",0)
ajaxContainer("https://www.rentrip.in/rent-bike/Bangalore","Bangalore",1)
ajaxContainer("https://www.rentrip.in/rent-bike/Indore","Indore",2)
ajaxContainer("https://www.rentrip.in/rent-bike/Chandigarh","Chandigarh",3)
ajaxContainer("https://www.rentrip.in/rent-bike/Chennai","Chennai",4)
ajaxContainer("https://www.rentrip.in/rent-bike/Coimbatore","Coimbatore",5)
ajaxContainer("https://www.rentrip.in/rent-bike/Jaipur","Jaipur",6)
ajaxContainer("https://www.rentrip.in/rent-bike/Guwahati","Guwahati",7)
