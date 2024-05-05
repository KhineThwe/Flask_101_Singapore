from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("11.jinja.html")

@app.route("/<name>")
def welcome(name):
    return render_template("11.welcome.html",name=name)

@app.route("/home")
def home():
    return render_template("11.home.html")

@app.route("/about")
def about():
    sites = ['twitter','facebook','instagram','whatsapp']
    return render_template("11.about.html",site=sites)

@app.route("/contact/<role>")
def test(role):
	return render_template("11.contact.html", person=role)


if __name__ == "__main__":
    app.run()
    
