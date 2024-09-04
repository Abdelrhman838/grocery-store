from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from sql_conection import get_sql_conector
import product_dao ,uom_dao, order_dao
import json

file = Flask(__name__)
file.secret_key = 'mano22'  # Change this to a random secret key
connection = get_sql_conector()

@file.route('/', methods=['GET'])
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@file.route('/login', methods=['GET', 'POST'])
def login():
    print("Login route hit")
    if request.method == 'POST':
        print("POST request received")
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}, Password: {password}")
        
        if username and password:
            session['username'] = username
            print("Redirecting to dashboard")
            return redirect(url_for('dashboard'))
        else:
            print("Missing username or password")
            return render_template('login.html', error="Please provide both username and password")
    return render_template('login.html')

@file.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@file.route('/manage-product')
def manage_products():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('manage-product.html')

@file.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@file.route('/order')
def order():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('order.html')
@file.route( '/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = order_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@file.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = order_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@file.route('/getProducts', methods=["GET"])
def get_products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@file.route('/getUOM', methods=["GET"])
def get_uom():
    products = uom_dao.get_uoms(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@file.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@file.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data']) 
    product_id = product_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id' : product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    file.run( debug=True, port=5000)


