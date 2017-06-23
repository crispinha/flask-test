from flask import Flask, render_template, request, redirect, url_for, abort, make_response
import random
app = Flask(__name__)

user_message = []


@app.route("/", methods=["GET", "POST"])
def message():
	global user_message
	if request.method == 'POST':
		if "message" in request.form:
			user_message.append(request.form["message"])
			return redirect(url_for('message'))
		else:
			abort(422)

	return render_template("index.html", message=user_message)


@app.route("/set_cookie/")
def set_cookie():
	resp = make_response(render_template("done.html"))
	resp.set_cookie("number", str(random.randint(0, 100000)))
	return resp


@app.route("/get_cookie/")
def get_cookie():
	return render_template("show_cookie.html", number=request.cookies.get('number'))

if __name__ == "__main__":
	app.run()
