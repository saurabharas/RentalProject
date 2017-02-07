from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
#from pyvirtualdisplay import Display
#from lxml import html
#from xvfbwrapper import Xvfb
import time
from datetime import datetime, timedelta


'''
browser1=webdriver.Chrome()
#mainContent(browser1,'https://www.bykemania.com/search?pass=a%3A30%3A%7Bs%3A7%3A%22model_1%22%3Bs%3A1%3A%221%22%3Bs%3A7%3A%22model_2%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_3%22%3Bs%3A1%3A%222%22%3Bs%3A7%3A%22model_4%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_5%22%3Bi%3A2%3Bs%3A7%3A%22model_6%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_7%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_8%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_9%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_10%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_11%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_12%22%3Bi%3A0%3Bs%3A8%3A%22model_13%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_14%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22model_15%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_16%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_17%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_18%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_19%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_20%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_21%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_22%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_23%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_24%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_27%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_28%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22model_29%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_30%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_31%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_32%22%3Bs%3A1%3A%220%22%3B%7D&location=1000&dhour=30&ehour=0',1)
#try:
    a=browser1.get('https://www.wikiposao.com')
    print(a)
except WebDriverException:
#    print("Oops!  That was no valid number.  Try again...")
    print(a)
expectedTitle = "Google"
expectedUrl = "https://www.google.com"
driver = webdriver.Chrome()
driver.get(expectedUrl)
print(driver.title)

browser1=webdriver.Chrome()
browser1.get('http://www.rentsetgo.co/mumbai/motorbikesonrent?brand=&commit=submit&delivery_type=&locality=&max=&max_disc=&min=&min_disc=&page=1&sort_by=&utf8=%E2%9C%93')
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
myContent=soup.find_all("div",{"class":"card-container"})
print(len(myContent))
browser1.get('http://www.rentsetgo.co/mumbai/motorbikesonrent?brand=&commit=submit&delivery_type=&locality=&max=&max_disc=&min=&min_disc=&page=2&sort_by=&utf8=%E2%9C%93')
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
myContent=soup.find_all("div",{"class":"card-container"})
print(len(myContent))
browser1.get('http://www.rentsetgo.co/mumbai/motorbikesonrent?brand=&commit=submit&delivery_type=&locality=&max=&max_disc=&min=&min_disc=&page=3&sort_by=&utf8=%E2%9C%93')
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
myContent=soup.find_all("div",{"class":"card-container"})
print(len(myContent))
browser1.get('http://www.rentsetgo.co/mumbai/motorbikesonrent?brand=&commit=submit&delivery_type=&locality=&max=&max_disc=&min=&min_disc=&page=4&sort_by=&utf8=%E2%9C%93')
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
myContent=soup.find_all("div",{"class":"card-container"})
print(len(myContent))
'''
#SnapBikes
#while(True):
browser1=webdriver.Chrome()



def dateCalculation(N):
    dateReq = datetime.now() + timedelta(days=N)
    return (dateReq.strftime('%d-%m-%Y'))

def ajaxContainer(cityXpath,city,count):

    browser1.get('http://www.snapbikes.in/Bike-Search.aspx?PickupDate=09-02-2017&DropOffDate=10-02-2017')
    browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']").click()
    browser1.find_element_by_xpath(cityXpath).click()
    
    '''
    browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_txtDropOff']").click()
    browser1.find_element_by_id("ctl00_ContentPlaceHolder1_CEPickup_day_1_4").click()

    browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_btnSearchChange']").click()
    browser1.find_element_by_id("ctl00_ContentPlaceHolder1_CEPickup_day_1_5").click()
    '''
    
    for N in range(0,4):
        inputElement = browser1.find_element_by_id("ctl00_ContentPlaceHolder1_txtPicUpdate")
        inputElement2 = browser1.find_element_by_id("ctl00_ContentPlaceHolder1_txtDropOff")
        inputElement.clear()
        inputElement.send_keys(dateCalculation(N))
        inputElement2.clear()
        inputElement2.send_keys(dateCalculation(N+1))
        browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_btnSearchChange']").click()
        findValues(browser1,city,count,dateCalculation(N),dateCalculation(N+1))

    '''        
        inputElement = browser1.find_element_by_id("ctl00_ContentPlaceHolder1_txtPicUpdate")
        inputElement2 = browser1.find_element_by_id("ctl00_ContentPlaceHolder1_txtDropOff")
        for N in range(0,4):
            inputElement.clear()
            inputElement.send_keys(dateCalculation(N))
            inputElement2.clear()
            inputElement2.send_keys(dateCalculation(N+1))   
            browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_btnSearchChange']").click()
            findValues(browser1,city,count,dateCalculation(N),dateCalculation(N+1))
    '''
         
    
def findValues(browser1,city,count,fromDate,toDate):
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



 

