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
import calendar
import numpy as np
from random import randint


browser1=webdriver.Chrome()
def dateNavigation():
    dateVar=datetime.now()+timedelta(days=1)
    td=0
    tr=0
    td=0
    td2=0
    timeVal1=0
    timeVal2=0
    for x in range(1,2):
        if(dateVar.weekday()<6):
            td=dateVar.weekday()+2
        if(dateVar.weekday()==6):
            td=1
        
        tr1=get_week_of_month(2017, dateVar.month,dateVar.day)    
        timeVal1=randint(1,12)
        timeVal2=randint(1,12)
        
        if(dateVar.weekday()==5):
            td2=1            
        else:
            td2=td+1
        tr2=get_week_of_month(2017, (dateVar+timedelta(days=1)).month,(dateVar+timedelta(days=1)).day)    


        print("tr=%d tr2=%d td=%d td2=%d timeVal1=%d timeVal2=%d"%(tr1,tr2,td,td2,timeVal1,timeVal2))        
        pageNavigation(tr1,tr2,td,td2,timeVal1,timeVal2)
        dateVar=dateVar+timedelta(days=1)
        
        
    

def pageNavigation(tr,tr2,td,td2,timeVal1,timeVal2):
    browser1.get("https://dryve.co.in/search/")
    
    time.sleep(4)
    dateOuter = browser1.find_element_by_xpath(".//*[@id='date-start']/span").click()
    

    pickElementDate = browser1.find_element_by_xpath(".//*[@id='page-top']/div[6]/div[3]/table/tbody/tr["+str(tr)+"]/td["+str(td)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='page-top']/div[6]/div[2]/table/tbody/tr/td/span["+str(timeVal1)+"]").click()

    pickElementDate = browser1.find_element_by_xpath(".//*[@id='page-top']/div[7]/div[3]/table/tbody/tr["+str(tr2)+"]/td["+str(td2)+"]").click()
    pickElementTime = browser1.find_element_by_xpath(".//*[@id='page-top']/div[7]/div[2]/table/tbody/tr/td/span["+str(timeVal2)+"]").click()

    searchButton =   browser1.find_element_by_xpath(".//*[@id='searchBikeBtn']").click()

    page_info()

    

       

    
def get_week_of_month(year, month, day):
    calendar.setfirstweekday(6)
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)


def page_info():
    ps=browser1.page_source
    soup=BeautifulSoup(ps,"html.parser")
    bikeImageHtml=soup.find_all("img",{"class":"img-responsive"})
    for value in bikeImageHtml:
         pass
#        print(value.get("src"))

    bike_title=soup.find_all("div",{"class":"bike-info"})
    #print bike_title
    print(len(bike_title))
    l=[]
    d={}
    for value in bike_title:       
        a=" ".join(value.text.split())
        k,v=a.split("Total Fare")
        d[k]=v.split(':')
        l.append(d)
       
    print(l)
    print(len(l))
   # print(len(myDict))

        

'''    bikeTitleList=[]
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

'''

dateNavigation()



    
'''
ps=browser1.page_source
soup=BeautifulSoup(ps,"html.parser")
bikeImageList=soup.find_all("a",{"class":"media-link"})
'''


'''
1.find weekday
2.for (!sunday)
    td=weekday+2
    tr=get_week_of_the_month(currentDate)
    findelementbyxpath(td,tr).click
if(sunday):
    td=0

    
'''
