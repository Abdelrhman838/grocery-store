import product_dao
from sql_conection import get_sql_conector
connection = get_sql_conector()
cursor = connection.cursor()

query = ("select * from orders")