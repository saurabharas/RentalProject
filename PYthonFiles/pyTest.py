import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *
from bs4 import BeautifulSoup
#import urllib.request
import sys  
import time  
class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
  
url = 'https://www.rentomojo.com/mumbai/bikes-on-rent'  
client_response = Client(url)
source = client_response.mainFrame().toHtml()
pyString=unicode(source)
soup=BeautifulSoup(pyString,"html.parser")
myContent=len(soup.find_all("div"))

print(myContent)


#print(soup)


#print(html.encode("UTF-8"))
