from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import codecs
#from pyvirtualdisplay import Display
#from lxml import html
#from xvfbwrapper import Xvfb
import time

browser = webdriver.Chrome()
browser.get('https://www.bykemania.com/search?pass=a%3A30%3A%7Bs%3A7%3A%22model_1%22%3Bs%3A1%3A%221%22%3Bs%3A7%3A%22model_2%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_3%22%3Bs%3A1%3A%222%22%3Bs%3A7%3A%22model_4%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_5%22%3Bi%3A2%3Bs%3A7%3A%22model_6%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_7%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_8%22%3Bs%3A1%3A%220%22%3Bs%3A7%3A%22model_9%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_10%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_11%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_12%22%3Bi%3A0%3Bs%3A8%3A%22model_13%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_14%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22model_15%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_16%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_17%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_18%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_19%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_20%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_21%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_22%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_23%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_24%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_27%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_28%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22model_29%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_30%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_31%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22model_32%22%3Bs%3A1%3A%220%22%3B%7D&location=1000&dhour=30&ehour=0')
#time.sleep(5)
ps=browser.page_source
#print(ps)
#rawData=ps.encode('utf-8')
#testContent=html.fromstring(ps)
#print(testContent)
soup=BeautifulSoup(ps,"html.parser")
#rawDataSoup=soup.encode('utf-8')
#print(rawDataSoup)
#print(rawDataSoup.decode('utf-8'))

myContent=soup.find_all("div",{"class":"thumbnail col-xs-4 col-xs-offset-4 col-lg-4 col-lg-offset-4 col-md-4 col-md-offset-4 col-sm-4 col-sm-offset-4 "})

#print("\n \n \n")
print(len(myContent))


#browser.close()
