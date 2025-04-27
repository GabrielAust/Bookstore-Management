from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

products = Blueprint('products', __name__)


@products.route('/', methods=['GET'])
def get_products():
    query = '''
        SELECT id, product_code, product_name, list_price, category
        FROM products
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@products.route('/<int:id>', methods=['GET'])
def get_product_detail(id):
    query = f'''
        SELECT id, product_name, description, list_price, category
        FROM products
        WHERE id = {id}
    '''
    current_app.logger.info(f'GET /products/{id} query={query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@products.route('/mostExpensive', methods=['GET'])
def get_most_pop_products():
    query = '''
        SELECT product_code, product_name, list_price, reorder_level
        FROM products
        ORDER BY list_price DESC
        LIMIT 5
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@products.route('/tenMostExpensive', methods=['GET'])
def get_10_most_expensive_products():
    query = '''
        SELECT product_code, product_name, list_price, reorder_level
        FROM products
        ORDER BY list_price DESC
        LIMIT 10
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@products.route('/', methods=['POST'])
def add_new_product():
    the_data = request.json
    current_app.logger.info(the_data)
    name = the_data['product_name']
    description = the_data['product_description']
    price = the_data['product_price']
    category = the_data['product_category']
    query = f'''
        INSERT INTO products (product_name, description, category, list_price)
        VALUES ('{name}', '{description}', '{category}', {price})
    '''
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response("Successfully added product")
    response.status_code = 200
    return response


@products.route('/categories', methods=['GET'])
def get_all_categories():
    query = '''
        SELECT DISTINCT category AS label, category AS value
        FROM products
        WHERE category IS NOT NULL
        ORDER BY category
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@products.route('/', methods=['PUT'])
def update_product():
    product_info = request.json
    current_app.logger.info(product_info)
    # TODO: actually perform UPDATE here
    return "Success"
