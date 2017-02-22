import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from bs4 import BeautifulSoup

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
   # self.frame = self.mainFrame()
    self.app.quit()




url = 'http://pycoders.com/archive/'
r = Render("https://www.rentomojo.com/bangalore/bikes-on-rent")
#html = r.frame.totml()
html = r.mainFrame().toHtml()
#formatted_result = str(html.encode("utf-8"))
#print(html)
#print(html.encode("utf-8"))
soup=BeautifulSoup(html,"lxml")
#print(soup)
#test=soup.find_all("div",{"class","rm_container"})
#test2=soup.find_all("a")
#print(test[0])
#print(soup.prettify())
#for i in range(30):
#  print("\n \n ")
# print(test[i])
print(datetime.now().isoweekday())
print(int(datetime.now().strftime('%H'))==range(1,17))
