# ------------------------------------------------------------
# This file creates a shared DB connection resource
# ------------------------------------------------------------
# api/backend/db_connection/__init__.py

import mysql.connector
from flask import g


class DB:
    def __init__(self):
        self.config = None

    def init_app(self, app):
        # Capture MySQL settings from Flask config
        self.config = {
            'host': app.config['MYSQL_DATABASE_HOST'],
            'user': app.config['MYSQL_DATABASE_USER'],
            'password': app.config['MYSQL_DATABASE_PASSWORD'],
            'database': app.config['MYSQL_DATABASE_DB'],
            'port': app.config['MYSQL_DATABASE_PORT'],
        }

        # Ensure connection closes at request end
        @app.teardown_appcontext
        def close_db(exc):
            db_conn = g.pop('db_connection', None)
            if db_conn is not None:
                db_conn.close()

    def get_db(self):
        # Reuse one connection per request
        if 'db_connection' not in g:
            g.db_connection = mysql.connector.connect(**self.config)
        return g.db_connection


# Expose a single shared DB instance
db = DB()
