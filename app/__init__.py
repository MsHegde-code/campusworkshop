"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq1i02qv2dcb92a5hg-a.oregon-postgres.render.com",
        database="mshtodo",
        user="mshtodo_user",
        password="HR56cEP6jPSY6x2K5p18JCPA6uO3J2Wl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
