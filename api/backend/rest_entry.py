from flask import Flask
from dotenv import load_dotenv
import os

from backend.db_connection import db
from backend.customers.customer_routes import customers
from backend.products.products_routes import products
from backend.simple.simple_routes import simple_routes
from backend.orders.order_routes import orders_bp
from backend.inventory.inventory_routes import inventory_bp
from backend.users.user_routes import auth_bp
from backend.vendors.vendors_routes import vendors_bp


def create_app():
    # load .env
    load_dotenv()

    app = Flask(__name__)

    # security & DB config
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT').strip())
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME').strip()

    # init DB
    app.logger.info('Starting DB connection')
    db.init_app(app)

    # register all blueprints
    app.logger.info('Registering blueprints')
    app.register_blueprint(simple_routes, url_prefix='/')
    app.register_blueprint(customers, url_prefix='/customers')
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(auth_bp, url_prefix='/users')
    app.register_blueprint(vendors_bp, url_prefix='/vendors')

    return app
