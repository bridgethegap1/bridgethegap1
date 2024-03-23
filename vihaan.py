import sqlite3
import random
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
cursor=sqlite3.connect('app.db')
db=conn.cursor()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET","POST"])
def login():
  if request.method=="GET"
    session.clear()
    username=request.form.get("username")
    password=request.form.get("password")
    subject=request.form.get("subject")
    rows=db.execute("Select * from accounts")
    account_info=db.execute("SELECT username from accounts WHERE username=? AND password=?",(username,password))
    accounts=db.fetchall()
    logged_in_user=accounts[0][0]
    return render_template("/index.html",logged_in_user=logged_in_user)
  else 
    return render_template("/login.html")
@app.route("/discussion",methods=["POST"]
def post():
  
  
    
  
  
