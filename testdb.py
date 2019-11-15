import pymysql
# 建库和建表
con = None
cur = None

def initializeDB():
    con = pymysql.connect(host='localhost', user='root',
                       charset='utf8')
    # passwd='memorology'
    cur = con.cursor()
    # b -> a list of all databases in the server
    cur.execute("SHOW DATABASES");
    b = cur.fetchall()

    print("print fetchall() - databases: ")
    print(b)
    a = ("test",) in b
    if not a:
        # database hasn't been created yet
        # create database
        cur.execute("create database test character set utf8;")
        # select database
        cur.execute("use test;")
        cur.execute("create table recordings(id text,audio mediumtext);")
        con.commit()
        print("first time creating database 'test' and table 'recordings'. ")
    else:
        cur.execute("use test;")
        print("already exist database 'test', use test. ")
    return(cur,con)
