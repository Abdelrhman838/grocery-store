def get_uoms(connection):
    cursor = connection.cursor()
    query =("SELECT * FROM uom")
    cursor.execute(query)

    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    from sql_conection import get_sql_conector
    connection = get_sql_conector()
    print(get_uoms(connection))
