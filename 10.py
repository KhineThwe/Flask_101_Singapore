from flask import Flask,redirect,url_for,render_template,request,abort

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template("10.login.html")

@app.route('/success')
def success():
    return "logged in successfully"

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST" and request.form["username"] == "admin":
        return redirect(url_for("success"))
    return redirect(url_for('index'))

@app.route('/<uname>')
def abortDemo(uname):
    if uname[0].isdigit():
        abort(400)
    return '<h1>Good Username</h1>'

if __name__ == '__main__':
    app.run(debug=True)