from flask import Flask, session,request, redirect, render_template, url_for, flash
from Controller_User import ControllerUser

from Controller_Riddle import ControllerRiddle


app = Flask(__name__)
app.debug = True
app.secret_key = 'chavesecreta'

controllerUser = ControllerUser()

controllerRiddle = ControllerRiddle()



@app.route("/")
def home():
	users = controllerUser.get_list_dict_users()
	return render_template("home.html", data=users)


@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == 'POST':

		user = request.form['name']
		password = request.form['password']
		

		login_sucess,errors = controllerUser.check_login(user,password)

		if not login_sucess:
			return render_template('login.html', errors = errors)

		#session.permanent = True	
		# session["user"] = user

		flash("Login Sucessful!")
		return redirect(url_for("user", user=user))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("user"))		
		return render_template('login.html')





@app.route("/signup", methods=['POST','GET'])
def signup():
	error = None
	if request.method == 'POST':
		user = request.form['nm']
		password = request.form['password']


		if not controllerUser.check_user_signed(user):
			controllerUser.create_user(user,password)
			flash("User created with sucess!")
			return redirect(url_for("user"))
		else:
			error = 'User already signed-up! Please log in.'
			return redirect(url_for('login'))
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


