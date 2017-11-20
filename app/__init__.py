from flask import Flask
import sqlite3

# Init database
db = sqlite3.connect('database.sql')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS creds(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Init flask app
app = Flask(__name__)

from app import main
