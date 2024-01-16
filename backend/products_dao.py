from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()
    query = "SELECT p.product_id, p.name, p.price_per_unit, p.uom_id, u.uom_name FROM gs.products p inner join gs.uom u on p.uom_id = u.uom_id;"
    cursor.execute(query)
    response = []
    for (product_id, name, price_per_unit , uom_id, uom_name) in cursor:
        response.append({
            'product_id' : product_id,
            'name' : name,
            'price_per_unit' : price_per_unit,
            'uom_id' : uom_id,
            'uom_name' : uom_name
        })

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into gs.products" "(name, uom_id, price_per_unit)" "values (%s, %s, %s)");
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM gs.products where product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 9))