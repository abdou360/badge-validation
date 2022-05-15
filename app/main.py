from flask import Flask

app = Flask(__name__)

@app.route("/deploy")
def home_view():
		return "<h1>Welcomme to your app </h1>"
