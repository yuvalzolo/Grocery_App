from flask import Flask, request, jsonify, json
import products_dao
import orders_dao
import uom_dao
from sql_connection import get_sql_connection

app = Flask(__name__)
connection = get_sql_connection()


@app.route('/getProducts', methods = ['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods = ['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    return_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    return_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods = ['GET'])
def get_ums():
    uoms = uom_dao.get_uoms(connection)
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == "__main__":
    print("Starting Python Flask")
    app.run(port=5000)


