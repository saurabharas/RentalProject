'''
1.import All the webScrape Files
2.import the sqlite DB
3.import all priceStruct files
4.get all price Strut dictionaries
5.compare values from sqlite DB to price struct Dictionaries
6.cost retrived from step 6 to be added to a new dictionary of price struct
7.from new priceStructDictionaries/new sqlite DB echo values to php
'''
#Dummy scrape-SQLite
import sqlite3
dbData=[]
d1={'DR':{'mumbai':{'dadar':{'HondaActiva':[10,500]

                                    }






                        }

                }



    }

print(d1['DR'])

#Two things to work on connect(),cursor()
connection=sqlite3.connect('database2.db')
c=connection.cursor()
def createDB():
    c.execute('''CREATE TABLE IF NOT EXISTS t1(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                provider TEXT,
                                                city TEXT,
                                                sublocation TEXT,
                                                bikeName TEXT,
                                                pickUpDate TEXT,
                                                dropDate TEXT,
                                                Availability TEXT,
                                                pID INTEGER,
                                                bID INTEGER)''')
    connection.commit()

#Provider,city,sublocation,bikeName,pickUpDate,dropDate,Availability,pID,bID,aID
#DB types INTEGER,REAL,TEXT,CHAR,BLOB

def insertDB():
    #c.execute('INSERT INTO t1 VALUES(1,"sau","sajskjasd",82391893289389)')
    c.execute('INSERT INTO t1 VALUES(?,?,?,?,?,?,?,?,?,?)',
    (1,"bykeMania","mumbai","thane","HondaActiva","09-03-2017","09-03-2017","a",1,1))
    c.execute('INSERT INTO t1 VALUES(?,?,?,?,?,?,?,?,?,?)',
    (2,"RoadPanda","mumbai","dadar","HondaBike","09-03-2017","09-03-2017","a",2,1))
    c.execute('INSERT INTO t1 VALUES(?,?,?,?,?,?,?,?,?,?)',
    (3,"bykeMania","mumbai","thane","HondaNavi","09-03-2017","09-03-2017","u",2,1))
    c.execute('INSERT INTO t1 VALUES(?,?,?,?,?,?,?,?,?,?)',
    (4,"WR","bangalore","thane","CBZ","09-03-2017","09-03-2017","u",2,1))
    c.execute('INSERT INTO t1 VALUES(?,?,?,?,?,?,?,?,?,?)',
    (5,"DR","mumbai","thane","Pulsur","09-03-2017","09-03-2017","a",1,1))
    
    connection.commit()

def selectDB():
    c.execute("SELECT * FROM t1 ")
    dbData=c.fetchall()    
    for row in c.fetchall():
        #print(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),row[8],row[9])
        pass

def updateDB():
    c.execute("UPDATE t1 SET name='bubu' WHERE name='sau' ")
    connection.commit()
def deleteDB():
    c.execute("DELETE FROM T1 WHERE name='bubu' ")
    connection.commit()

def compareDbToDict():
    for row in dbData:
        #print(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),row[8],row[9])
        for row1 in d1:     
        if(row[1]==d1):
            
    


    

##createDB()
##insertDB()
##
##selectDB()
##compareDbToDict()


##updateDB()
##print('#'*100)
##selectDB()
c.close()
connection.close()





