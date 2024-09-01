import mysql.connector

cnx = None
def get_sql_conector():
    global cnx 
    if cnx is None:
        cnx = mysql.connector.connect(user='root', password='1B12o202r*',
                                    host='localhost',
                                    database='grocery_store')
    return cnx