
from flask import Flask, session,request, redirect, render_template, url_for, flash



app = Flask(__name__)
app.debug = True
app.secret_key = 'chavesecreta'


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == 'POST':	
		session.permanent = True	
		user = request.form['nm']
		session["user"] = user

		flash("Login Sucessful!")
		return redirect(url_for("user", user=user))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("user"))		
		return render_template('login.html')


@app.route("/user", methods= ["POST", "GET"])
def user():
	email = None

	if "user" in session:

		user = session["user"]
		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
			flash("Email registered")
		else:
			if "email" in session:
				email = session["email"]


		return render_template("user.html", email=email)
	else:
		flash("You are not logged in!")
		return redirect(url_for('login'))


@app.route("/logout")
def logout():
	flash("You have logged off!")
	session.pop("user",None)
	session.pop("email", None)
	return redirect(url_for('login.html'))

if __name__ == '__main__':
	app.run()
