from flask import Flask, request, render_template, send_from_directory
import sqlite3 as sql
import os
from os.path import join, dirname, realpath

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

# Ensure the uploads directory exists
os.makedirs(UPLOADS_PATH, exist_ok=True)        

# Function to create the users and images tables
def create_table():
    with sql.connect('our.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS images')  # Drop the table if it exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image TEXT NOT NULL,
                feedback TEXT
            )
        ''')
        conn.commit()

# Call create_table function to create the tables
create_table()

@app.route("/")
def index():
    return render_template("signinup.html")

@app.route('/loginAction', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = check_user(username, password)
    if user:
        msg = "You are successfully logged in!"
        return render_template("secondpg.html", msg=msg)
    else:
        msg = "Invalid username or password"
        return render_template("signinup.html", msg=msg)

def check_user(username, password):
    with sql.connect('our.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
    return user

@app.route('/regAction', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    msg = insert_user(username, email, password)
    return render_template("secondpg.html", msg=msg)

def insert_user(username, email, password):
    try:
        with sql.connect('our.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
        return "Registration successful. You are now logged in!"
    except sql.IntegrityError:
        return "Username already exists"

@app.route("/secondpg")
def secondpg():
    return render_template("secondpg.html")

@app.route("/girl")
def girl():
    return render_template("girl.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/haircut")
def haircut():
    return render_template("haircut.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/booking2")
def booking2():
    return render_template("booking2.html")

@app.route("/coloring")
def coloring():
    return render_template("coloring.html")

@app.route("/facial")
def facial():
    return render_template("facial.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route('/viewreg')
def viewreg():
    with sql.connect("our.db") as conn:
        conn.row_factory = sql.Row
        cursor = conn.cursor()
        cursor.execute("SELECT username, email, password FROM users")
        rows = cursor.fetchall()
    return render_template("viewreg.html", rows=rows)

@app.route('/submit_image', methods=['POST'])
def submit_image():
    feedback = request.form.get('feedback', '')  # Get feedback from form data
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Save the image to the uploads folder
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

            # Store image information in SQLite3 database
            with sql.connect('our.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO images (image, feedback) VALUES (?, ?)', (image.filename, feedback))
                conn.commit()

            return '<section background-color:black; > <b style="font-size:80px;color: orange; "> Image and feedback uploaded successfully!</b> <br>  <h1 style="font-size:49px;color: orange;"> THANKS FOR YOUR PRESENCE <span > 💌 </span> </h1> </section>'

    return 'Failed to upload image and feedback'

@app.route('/viewfeed')
def viewfeed():
    with sql.connect("our.db") as conn:
        conn.row_factory = sql.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM images")
        rows = cursor.fetchall()
    return render_template("viewfeed.html", rows=rows)

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
