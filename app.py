from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This application is running inside Azure Container Apps."

@app.route("/about")
def about():
    return "This container was built and deployed using Azure."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
