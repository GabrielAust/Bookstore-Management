from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

customers = Blueprint('customers', __name__)


@customers.route('/', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT id, company, last_name, first_name, job_title, business_phone
        FROM customers
    ''')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


@customers.route('/', methods=['PUT'])
def update_customer():
    current_app.logger.info('PUT /customers route')
    cust_info = request.json
    cust_id = cust_info['id']
    first = cust_info['first_name']
    last = cust_info['last_name']
    company = cust_info['company']
    query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s WHERE id = %s'
    data = (first, last, company, cust_id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return 'customer updated!'


@customers.route('/<int:userID>', methods=['GET'])
def get_customer(userID):
    current_app.logger.info('GET /customers/<userID> route')
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT id, first_name, last_name FROM customers WHERE id = %s',
        (userID,)
    )
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


@customers.route('/prediction/<var01>/<var02>', methods=['GET'])
def predict_value(var01, var02):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')
    returnVal = predict(var01, var02)
    return_dict = {'result': returnVal}
    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
