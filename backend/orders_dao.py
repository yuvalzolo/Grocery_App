from sql_connection import get_sql_connection

import datetime

def insert_order(connection, order):
    cursor = connection.cursor()
    query = "INSERT INTO Orders (customer_name, total, datetime) values (%s, %s, %s)"
    order_data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(query, order_data)
    order_id = cursor.lastrowid

    order_details_query = "INSERT INTO order_details (order_id, product_id, quantity, total_price) values (%s, %s, %s, %s)"
    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_details_data['quantity']),
            float(order_details_data['total_price'])
        ])

    cursor.executemany(order_details_query, order_details_data)


    connection.commit()
    return order_id
if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, 9))