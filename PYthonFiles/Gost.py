import ghost
from bs4 import BeautifulSoup
g = ghost.Ghost()
with g.start() as session:
    resources = session.open('https://www.rentomojo.com/bangalore/bikes-on-rent')
    #page, resources = ghost.wait_for_page_loaded()
    #wait_while_selector("rm-category__desc", timeout=None)
    session.wait_for_text('Honda Activa 3G',timeout=100)
    #session.wait_while_selector("div.rm-category__desc", timeout=None)
    #session.wait_timeout=50
    html=session.content
    soup=BeautifulSoup(html,"html.parser")
    #print(soup)
    myContent=soup.find_all("div")
    print(len(myContent))



