import os
import requests

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from functools import wraps
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///todo.db")
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

from datetime import datetime

@app.route("/")
@login_required
def index():
    today = datetime.today().date()  # Bugünün tarihi

    # Kullanıcının tamamlanmamış ve geçerli tarihe sahip görevlerini çekiyoruz
    user_tasks = db.execute(
        "SELECT * FROM tasks WHERE user_id = ? AND completed = 0 AND date >= ? ORDER BY date",
        session["user_id"],
        today
    )

    # Görevleri gruplamak için bir sözlük oluşturuyoruz
    grouped_tasks = {}
    for task in user_tasks:
        task_date = task["date"].split(" ")[0]  # Sadece tarihi alıyoruz (saat olmadan)
        if task_date not in grouped_tasks:
            grouped_tasks[task_date] = []
        grouped_tasks[task_date].append({"description": task["description"], "id": task["id"]})

    # Sözlüğü bir listeye çevirip, her grup için 'date' ve 'tasks' alanlarını oluşturuyoruz
    tasks = [{"date": date, "tasks": tasks} for date, tasks in grouped_tasks.items()]

    return render_template("index.html", tasks=tasks)




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)


        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )


        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)


        session["user_id"] = rows[0]["id"]


        return redirect("/")


    else:
        return render_template("login.html")
@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if (request.method == "POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        if not username:
            return apology('Username is required!')
        elif not password:
            return apology('Password is required!')
        elif not confirmation:
            return apology('Password confirmation is required!')
        if password != confirmation:
            return apology('Password do not match!')
        hash = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username,hash) VALUES(?,?)", username, hash)
            return redirect('/')
        except:
            return apology('Username has already been registered!')
    else:
        return render_template("register.html")

@app.route("/addcard", methods=["GET", "POST"])
@login_required
def addcard():
    user_id = session["user_id"]
    if request.method == "POST":
        task_description = request.form.get("task_description")
        task_date = request.form.get("task_date")
        if not task_description:
            return apology("Task description is required!")
        if not task_date:
            return apology("Task date is required!")

        db.execute("INSERT INTO tasks (user_id, description,date, completed) VALUES (?, ?, ?,?)", user_id, task_description,task_date, False)
        return redirect('/')
    else:
        return render_template("addcard.html")
@app.route("/complete_task", methods=["POST"])
@login_required
def complete_task():
    task_id = request.form.get("task_id")

    if not task_id:
        return redirect("/")

    db.execute("UPDATE tasks SET completed = 1 WHERE id = ?", task_id)
    return redirect("/")
@app.route("/history")
@login_required
def history():
    completed_tasks = db.execute(
        "SELECT description, date FROM tasks WHERE user_id = ? AND completed = 1 ORDER BY date DESC",
        session["user_id"]
    )
    return render_template("history.html", tasks=completed_tasks)

@app.route("/update_task", methods=["POST"])
@login_required
def update_task():
    task_id = request.form.get("task_id")
    description = request.form.get("description")
    date = request.form.get("date")

    if not task_id or not description or not date:
        return apology("Please fill all")

    db.execute("UPDATE tasks SET description = ?, date = ? WHERE id = ?", description, date, task_id)

    return redirect("/")
@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_id = request.form['task_id']
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    return redirect("/")





