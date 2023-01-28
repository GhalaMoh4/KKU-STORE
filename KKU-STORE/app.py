from flask import Flask, render_template, request
import datetime
import qrcode

app = Flask(__name__)

@app.route("/")
def index():
    
    name = "ghala"
    return render_template("index.html", name=name)

@app.route("/loginpage")
def date():
    
    
    return render_template("loginpage.html")


@app.route("/cart")
def cart():
   
    return render_template("cart.html")


if __name__ == "__main__":
    app.run(debug= True)