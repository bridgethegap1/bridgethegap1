import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
conn = sqlite3.connect('app.db')
db = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        account_info = db.execute("SELECT username FROM accounts WHERE username=? AND password=?", (username, password))
        account = account_info.fetchone()
        if account:
            logged_in_user = account[0]
            return render_template("/index.html", logged_in_user=logged_in_user)
        else:
            return render_template("/login.html")

@app.route("/discussion", methods=["POST", "GET"])
def discussion():
    if request.method == "POST":
        message = request.form.get("message")
        username = request.form.get("username")
        db.execute("INSERT INTO posts (message, username) VALUES (?, ?)", (message, username))
        conn.commit()
        return render_template("/discussion.html")
    else:
        past_posts_info = db.execute("SELECT username, message FROM posts")
        past_posts = past_posts_info.fetchall()
        return render_template("/discussion.html", past_posts=past_posts)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        db.execute("INSERT INTO accounts (name, username, password) VALUES (?, ?, ?)", (name, username, password))
        conn.commit()
        return render_template("/index.html")
    else:
        return render_template("/create_account.html")
