from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Azure App Service with Python! Let's add some more text and verify you're working now! Additional sample content"
