from flask import Flask, session,request, redirect, render_template, url_for, flash
from Controller_User import ControllerUser


app = Flask(__name__)
app.debug = True
app.secret_key = 'chavesecreta'

controller = ControllerUser()



@app.route("/")
def home():
	users = controller.get_list_users()
	return render_template("home.html", data=users)


@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == 'POST':
		#session.permanent = True	
		user = request.form['nm']
		session["user"] = user

		flash("Login Sucessful!")
		return redirect(url_for("user", user=user))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("user"))		
		return render_template('login.html')





@app.route("/signup", methods=['POST','GET'])
def signup():
	if request.method == 'POST':
		user = request.form['nm']
		password = request.form['password']

		controller.create_user(user,password)
		flash("User created with sucess!")
		return redirect(url_for("user"))
	else:
		return render_template('signup.html')


@app.route("/user", methods= ["POST", "GET"])
def user():
	if True:
		return render_template("user.html")
	else:
		flash("You are not logged in!")
		return redirect(url_for('login'))


@app.route("/logout")
def logout():
	flash("You have logged off!")
	session.pop("user",None)
	session.pop("email", None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()


