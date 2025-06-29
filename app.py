from flask import Flask, request, render_template, redirect, url_for, session, get_flashed_messages, flash

app = Flask(__name__)
app.secret_key = '.'

data = {
	"name" : [],
	"latitude" : [],
	"longitude" : []
}

@app.route('/form', methods = ["GET", "POST"])
def form():
	if request.method == "POST":
		name = request.form.get("name")
		latitude = request.form.get("lat")
		longitude = request.form.get("long")
		
		if name and latitude and longitude:
			data["name"].append(name)
			data["latitude"].append(latitude)
			data["longitude"].append(longitude)
		else:
			flash('Please fill in all information')
		return redirect(url_for("form"))
	return render_template("form.html", data=data, len=len(data["name"]))

@app.route('/submit', methods = ["GET", "POST"])
def submit():
	if request.method == "POST":
		print(data)
		return render_template("submit.html")
	return redirect(url_for("form"))

@app.route('/edit', methods = ["GET", "POST"])
def edit():
	global data
	if request.method == "POST":
		num = int(request.form.get("edit_num"))
	else:
		num = session['num_data']
	return render_template("edit.html", num=num, data=data)

@app.route('/update', methods = ["GET", "POST"])
def update():
	if request.method == "POST":
		print("update")
		num = int(request.form.get("num"))
		name = request.form.get("new_name")
		latitude = request.form.get("new_lat")
		longitude = request.form.get("new_long")
		global data
	
		if name and latitude and longitude:
			data["name"][num] = name
			data["latitude"][num] = latitude
			data["longitude"][num] = longitude
			return redirect(url_for("form"))
		else:
			flash('Please fill in all information')
			session['num_data'] = num
			return redirect(url_for("edit"))
	return redirect(url_for("form"))

@app.route('/')
def index():
	return redirect(url_for("form"))

if __name__ == '__main__':
	app.run(debug=True)
