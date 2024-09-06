from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    return render_template("home.html")

@app.route("/about/")
def person():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()