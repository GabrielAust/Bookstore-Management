from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

vendors_bp = Blueprint('vendors', __name__)


# GET /vendors/<vid>/books → list their books
@vendors_bp.route('/<int:vendor_id>/books', methods=['GET'])
def get_vendor_books(vendor_id):
    cur = db.get_db().cursor(dictionary=True)
    cur.execute(
        "SELECT * FROM Book WHERE VendorID=%s;",
        (vendor_id,)
    )
    data = cur.fetchall()
    return make_response(jsonify(data), 200)


# POST /vendors/<vid>/books → add a book
@vendors_bp.route('/<int:vendor_id>/books', methods=['POST'])
def add_vendor_book(vendor_id):
    p = request.get_json()
    sql = """
      INSERT INTO Book
        (Title, Author, ISBN, Price, Description, CoverImage, CategoryID, VendorID)
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    params = (
        p['title'], p['author'], p['isbn'],
        p['price'], p['description'],
        p['cover_image'], p['category_id'],
        vendor_id
    )
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return make_response(jsonify({'book_id': cur.lastrowid}), 201)


# PUT /vendors/<vid>/books/<bid> → update
@vendors_bp.route('/<int:vendor_id>/books/<int:book_id>', methods=['PUT'])
def update_vendor_book(vendor_id, book_id):
    p = request.get_json()
    sql = """
      UPDATE Book
      SET Title=%s, Author=%s, Price=%s, Description=%s, CoverImage=%s
      WHERE BookID=%s AND VendorID=%s;
    """
    params = (
        p['title'], p['author'], p['price'],
        p['description'], p['cover_image'],
        book_id, vendor_id
    )
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return make_response("Book updated", 200)


# DELETE /vendors/<vid>/books/<bid> → remove
@vendors_bp.route('/<int:vendor_id>/books/<int:book_id>', methods=['DELETE'])
def delete_vendor_book(vendor_id, book_id):
    conn = db.get_db();
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM Book WHERE BookID=%s AND VendorID=%s;",
        (book_id, vendor_id)
    )
    conn.commit()
    return make_response("Book deleted", 200)
