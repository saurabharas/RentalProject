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
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    
    bikeImageListOuter=soup.find_all("td",{"class":"bike-data-image"})
    bikeImageListMain=[]
    #print(bikeImageListOuter)
    for value in bikeImageListOuter:
        #print(value.contents[1].get('src'))
        bikeImageListMain.append(value.contents[1].get('src'))
        #print(value1)
    #print(bikeImageListMain)
    time.sleep(2)
    select=Select(browser1.find_element_by_xpath(".//*[@id='bike-data-main-content']/div[1]/table[1]/tbody/tr[3]/td[2]/table/tbody/tr/td/select"))
    selectOuter=soup.find_all("select",{"class":"select-location"})
    #print(select.select_by_index(0))
    for value in selectOuter:
        for x in range(1,len(value.contents)-1):
            print(value.contents[x].get('class'))
            print(value.contents[x].get('class')[0].decode('utf-8'))
            print(value.contents[x].get('class')[0].encode('utf-8'))
            '''
            if(value.contents[x].get('class')=='available'):
                print(value.contents[x].text)
            elif(value.contents[x].get('class')=='notavailable'):
                print("The bike is not availabel at - %s"%value.contents[x].text)
            '''
        
            
    

    
    browser1.close()
        
    #bikeImageListMain.append(value1.get('src'))
    #print(bikeImageListMain)
	
    '''
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

	for value in range(0,len(bikeImgSrcList)-1):
        f.write("%s,%s,%s,%s"%(bikeImgSrcList[value].decode('utf-8'),bikeTitleContentList[value].decode('utf-8'),priceList[value].decode('utf-8'),localLocationList[value].decode('utf-8')))
        f.write("\n")
    f.close()

	
	
	
	
	
	
	
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
1
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

	for value in range(0,len(bikeImgSrcList)-1):
        f.write("%s,%s,%s,%s"%(bikeImgSrcList[value].decode('utf-8'),bikeTitleContentList[value].decode('utf-8'),priceList[value].decode('utf-8'),localLocationList[value].decode('utf-8')))
        f.write("\n")
    f.close()


browser1=webdriver.Chrome()
ajaxContainer("https://www.rentrip.in/rent-bike/Ahmedabad","Ahemdabad",0)
ajaxContainer("https://www.rentrip.in/rent-bike/Bangalore","Bangalore",1)
ajaxContainer("https://www.rentrip.in/rent-bike/Indore","Indore",2)
ajaxContainer("https://www.rentrip.in/rent-bike/Chandigarh","Chandigarh",3)
ajaxContainer("https://www.rentrip.in/rent-bike/Chennai","Chennai",4)
ajaxContainer("https://www.rentrip.in/rent-bike/Coimbatore","Coimbatore",5)
ajaxContainer("https://www.rentrip.in/rent-bike/Jaipur","Jaipur",6)
ajaxContainer("https://www.rentrip.in/rent-bike/Guwahati","Guwahati",7)
	'''
	
	
	
browser1=webdriver.Chrome()
ajaxContainer("http://www.ziphop.in/bangalore/p/book-a-ride?pick=17.02.2017%205:00%20PM&&drop=18.02.2017%205:00%20PM","bangalore",0)
