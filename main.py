from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

user_message = ""


@app.route("/", methods=["GET", "POST"])
def message():
	global user_message
	if request.method == 'POST':
		if "message" in request.form:
			user_message = request.form["message"]
			return redirect(url_for('message'))
		else:
			user_message = user_message
			raise KeyError
	return render_template("index.html", message=user_message)

if __name__ == "__main__":
	app.run()
