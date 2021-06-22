import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from . import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app.db import get_db
from flask import request

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

#links ending in ("/") will redirect to the file within the ()
#The same style applies to the following methods
#This allows multiple pages to interact through links.
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/health', methods=['GET'])
def health():
    return "200"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    ## Return a register page
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418

    ## Return a login page
    return render_template('login.html')

@app.route("/mamnuya")
def Rinki():
        return render_template('Rinki.html')

@app.route("/nandhini")
def Nandhini():
        return render_template('Webp.html')

@app.route("/ixchel")
def Marcela():
        return render_template('ixchel.html')

if __name__ == '__main__':
    app.run(debug=True)
