from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Alex Hanson"
role="Google Cloud Engineering Fellow"
phone="N/A"
email="oOoUxDeveloperoOoxUoOo@gmail.com"
location="Los Angeles, CA, United States"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email,
    location=location
    )

if __name__ == "__main__":
    app.run(debug=True)