from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
#from pyvirtualdisplay import Display
#from lxml import html
#from xvfbwrapper import Xvfb
import time
#from datetime import datetime, timedelta
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

#SnapBikes
#while(True):
browser1=webdriver.Chrome()
browser1.get('http://www.snapbikes.in/Bike-Search.aspx?PickupDate=09-02-2017&DropOffDate=10-02-2017')
browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']").click()
browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_ddlCity']/option[4]").click()
browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_txtDropOff']").click()
browser1.find_element_by_id("ctl00_ContentPlaceHolder1_CEPickup_day_1_4").click()

browser1.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_btnSearchChange']").click()
browser1.find_element_by_id("ctl00_ContentPlaceHolder1_CEPickup_day_1_5").click()
'''

'''
#i=datetime.datetime.now()
#i.strftime('%d/%m/%Y')


N = 2

#date_N_days_ago = datetime.now() + timedelta(days=N)
dateReq = datetime.now() + timedelta(days=2)
    
print datetime.now()
print date_N_days_ago.strftime('%d-%m-%Y')
'''
a=u'Rs. 400.00'.decode('utf-8')
st=a.encode('ascii', 'xmlcharrefreplace')
print(isinstance("hhjdashjsa", basestring))
print(isinstance(a, basestring))


