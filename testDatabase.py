import pymysql
from database import *
# 建库和建表
con = None
cur = None

(cur,con)= initializeDB()
