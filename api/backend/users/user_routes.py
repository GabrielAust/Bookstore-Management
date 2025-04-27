from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

auth_bp = Blueprint('users', __name__)


# POST /users/login → authenticate
@auth_bp.route('/login', methods=['POST'])
def login_user():
    p = request.get_json()
    email = p.get('email')
    password = p.get('password')
    conn = db.get_db();
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT CustomerID, Password FROM Customer WHERE Email=%s;",
        (email,)
    )
    user = cur.fetchone()
    if user and user['Password'] == password:
        return make_response(jsonify({
            'message': 'Login successful',
            'user_id': user['CustomerID']
        }), 200)
    else:
        return make_response(jsonify({'message': 'Invalid credentials'}), 401)
