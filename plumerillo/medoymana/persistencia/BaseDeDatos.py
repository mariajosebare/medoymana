import pymysql


__cursor = pymysql.connect(
    host = "127.0.0.1",
    user="root",
    password="Y106954h",
    db="mdm3",
    cursorclass=pymysql.cursors.DictCursor
).cursor()


def correr_sql(query):
    __cursor.execute(query)
    return __cursor.fetchall()

