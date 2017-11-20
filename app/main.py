"""
Author: Ben Bornholm
Date: 11-20-17
Description: Default web server
"""
from app import app, cursor, db
from flask import Flask, render_template, request, url_for
from config import slack_webhook
import sqlite3

"""
Slack messager
"""
def slack_message(text):
    from urllib2 import Request, urlopen
    #from urlparse import urlparse
    #from urllib.request import urlopen, Request
    #from urllib import parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = Request(slack_webhook, data=json_data.encode('ascii'), headers={'Content-Type': 'application/json'})
        resp = urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))


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
@app.route('/wp-login', methods=['GET', 'POST'])
@app.route('/adminlogin', methods=['GET', 'POST'])
def login():
    error = 'Invalid Credentials. Please try again.'
    if request.method == 'POST':
        add_entry(request.form['username'], request.form['password'])
        slack_message("Web login with username: {0} and password: {1}".format(request.form['username'], request.form['password']))

    return render_template('login.html', error=error)
