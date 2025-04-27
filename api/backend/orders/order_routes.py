from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

orders_bp = Blueprint('orders', __name__)


# GET /orders → list all
@orders_bp.route('/', methods=['GET'])
def get_orders():
    cur = db.get_db().cursor(dictionary=True)
    cur.execute("SELECT * FROM `Order`;")
    data = cur.fetchall()
    return make_response(jsonify(data), 200)


# GET /orders/<id> → one
@orders_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    cur = db.get_db().cursor(dictionary=True)
    cur.execute("SELECT * FROM `Order` WHERE OrderID=%s;", (order_id,))
    data = cur.fetchone()
    return make_response(jsonify(data), 200)


# POST /orders → create
@orders_bp.route('/', methods=['POST'])
def create_order():
    p = request.get_json()
    sql = """
      INSERT INTO `Order` (CustomerID, OrderDate, TotalAmount, Status)
      VALUES (%s, %s, %s, %s);
    """
    params = (p['customer_id'], p['order_date'], p['total_amount'], p['status'])
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return make_response(jsonify({'order_id': cur.lastrowid}), 201)


# PUT /orders/<id> → update
@orders_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    p = request.get_json()
    sql = """
      UPDATE `Order`
      SET Status=%s, TotalAmount=%s
      WHERE OrderID=%s;
    """
    params = (p['status'], p['total_amount'], order_id)
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return make_response("Order updated", 200)


# DELETE /orders/<id> → delete
@orders_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute("DELETE FROM `Order` WHERE OrderID=%s;", (order_id,))
    conn.commit()
    return make_response("Order deleted", 200)
