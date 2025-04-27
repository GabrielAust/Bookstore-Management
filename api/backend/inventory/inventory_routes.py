from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

inventory_bp = Blueprint('inventory', __name__)


# GET /inventory → list all
@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    cur = db.get_db().cursor(dictionary=True)
    cur.execute("SELECT * FROM Inventory;")
    data = cur.fetchall()
    return make_response(jsonify(data), 200)


# PUT /inventory/<book_id> → update stock
@inventory_bp.route('/<int:book_id>', methods=['PUT'])
def update_inventory(book_id):
    p = request.get_json()
    sql = """
      UPDATE Inventory
      SET StockQuantity=%s, LastRestockedDate=%s
      WHERE BookID=%s;
    """
    params = (p['stock_quantity'], p['last_restocked_date'], book_id)
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return make_response("Inventory updated", 200)
