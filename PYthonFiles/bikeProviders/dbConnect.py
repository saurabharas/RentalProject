import sqlite3

#Two things to work on connect(),cursor()
connection=sqlite3.connect('database1.db')
c=connection.cursor()
def createDB():
    c.execute('CREATE TABLE IF NOT EXISTS t1(id REAL,name TEXT,addr TEXT,phoneNo REAL)')
    connection.commit()


#DB types INT,REAL,TEXT,CHAR
def insertDB():
    #c.execute('INSERT INTO t1 VALUES(1,"sau","sajskjasd",82391893289389)')
    i=2
    while(i in range(2,500)):
        c.execute('INSERT INTO t1 VALUES(?,?,?,?)',
        (i,"sau","sajs",82391893289389))
        i=i+1
    connection.commit()

def selectDB():
    c.execute("SELECT * FROM t1 ")
    for row in c.fetchall():
        print(row[0],str(row[1]),str(row[2]),row[3])


def updateDB():
    c.execute("UPDATE t1 SET name='bubu' WHERE name='sau' ")
    connection.commit()
def deleteDB():
    c.execute("DELETE FROM T1 WHERE name='bubu' ")
    connection.commit()
    

##createDB()
##insertDB()

selectDB()
updateDB()
print('#'*100)
selectDB()
c.close()
connection.close()
