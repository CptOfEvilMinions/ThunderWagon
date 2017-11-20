"""
Author: Ben Bornholm
Date: 11-20-17
Description: Default web server
"""
from app import app
from flask import Flask, render_template, request, url_for
import sqlite3

"""
Slack messager
"""

"""
Store usernames and passwords to database
"""

"""
Default route and routes to login page
"""
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    error = 'Invalid Credentials. Please try again.'
    if request.method == 'POST':
        print request.form['username']
        print request.form['password']
    return render_template('login.html', error=error)
