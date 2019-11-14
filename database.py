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

    print("print fetchall(): ")
    print(b)
    a = ("memorology",) in b
    if not a:
        # database hasn't been created yet
        # create database
        cur.execute("create database memorology character set utf8;")
        # select database
        cur.execute("use memorology;")
        cur.execute("create table recording(id int,audio mediumtext);")
        con.commit()
        print("first time creating database 'memorology' and table 'recording'. ")
    else:
        cur.execute("use memorology;")
        print("already exist database 'memorology', use memorology. ")
    return(cur,con)
