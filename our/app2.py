# from flask import Flask, request, render_template,redirect,session, url_for
# import sqlite3 as sql
# import os
# from os.path import join, dirname, realpath
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage

# UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\images')

# app = Flask(__name__)           
# app.config['SECRET_KEY'] = 'super secret key'

# @app.route("/")
# def index():
#     return render_template("signinup.html")

# @app.route("/regAction", methods = ["GET","POST"])
# def regAction():
#     msg=None
#     if(request.method=="POST"):
#         if (request.form["username"]!="" and request.form["email"]!="" and request.form["password"]!=""):
#             username = request.form["username"]
#             email = request.form["email"]
#             password = request.form["password"]
            
                
#             with sql.connect("our.db") as con:
#                 c=con.cursor()
#                 c.execute("INSERT INTO  register(username, email, password) VALUES('"+username+"','"+email+"','"+password+"')")
#                 msg = "Register Details submitted successfully "
                

#                 con.commit()
#         else:
#             msg="Something went wrong"
#     return render_template("signinup.html", msg=msg)
    
# @app.route('/loginAction',methods=['GET','POST'])
# def loginAction():
#     msg=None
#     if (request.method == "POST"):
#         username = request.form['username']
      
#         password = request.form['password']
        
#         with sql.connect("our.db") as con:
#             c=con.cursor()
#             c.execute("SELECT username,password  FROM register WHERE username = '"+username+"' and password ='"+password+"'")
#             r=c.fetchall()
#             for i in r:
#                 if(username==i[1] and password==i[1]):
#                     session["logedin"]=True
#                     session["ausername"]=username
#                     session["password"]=password
#                     return redirect(url_for("secondpg"))
#                 else:
#                     msg= "please enter valid username and password"

#     return render_template("secondpg.html",msg=msg)

# @app.route("/secondpg")
# def secondpg():
#     return render_template("secondpg.html")

# @app.route("/girl")
# def girl():
#     return render_template("girl.html")

# @app.route("/home")
# def home():
#     return render_template("home.html")

# @app.route("/blog")
# def blog():
#     return render_template("blog.html")
    
# @app.route("/haircut")
# def haircut():
#     return render_template("haircut.html")

# @app.route("/coloring")
# def coloring():
#     return render_template("coloring.html")

# @app.route("/facial")
# def facial():
#     return render_template("facial.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")



# @app.route('/viewreg')
# def viewreg():
#     con=sql.connect("our.db")
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     cur.execute("select username, email, password from register")
#     rows=cur.fetchall()
#     print(rows)
#     return render_template("viewreg.html",rows=rows)


# if __name__ == "__main__":
#     app.run(debug=True)












    