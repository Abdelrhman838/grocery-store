import mysql.connector

cnx = mysql.connector.connect(user='root', password='1B12o202r*',
                              host='localhost',
                              database='grocery_store')

cursor =cnx.cursor()


cursor.execute("SELECT * FROM grocery_store.orders")

cnx.close()