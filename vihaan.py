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
    rows=db.execute("Select * from accounts")
    account_info=db.execute("SELECT username from accounts WHERE username=? AND password=?",(username,password))
    accounts=db.fetchall()
    logged_in_user=accounts[0][0]
    return render_template("/index.html",logged_in_user=logged_in_user)
  else 
    return render_template("/login.html")
@app.route("/discussion",methods=["POST","GET"])
def discussion():
  if request.method == "POST":
    message=request.form.get("message")
    username=request.form.get("username")
    discussion_post=db.execute("INSERT into posts (message,username) VALUES(?,?)",(message,username))
    return render_template("/discussion.html")
  else:
    past_posts=db.execute("SELECT username from posts")
    past_posts_usernames=db.fetchall()
    past_posts=db.execute("SELECT message from posts")
    past_posts_messages=db.fetchall()
    past_posts_count=db.execute("SELECT COUNT(*) as n from posts")
    count=db.fetchall()
    return render_template("/discussion.html",past_posts_usernames=past_posts_usernames,past_posts_messages=past_posts_messages,count=count)
@app.route("/register",methods=["POST","GET"])
def register():
  if request.method=="POST":
    name=request.form.get("name")
    username=request.form.get("username")
    password=request.form.get("password")
    db.execute("INSERT INTO accounts(name,username,password) VALUES(?,?,?)",name,username,password)
    return render_template("/index.html")
  else:
    return render_template("/register.html")
