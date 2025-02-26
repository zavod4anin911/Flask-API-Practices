from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my API!"
@app.route('/about')
def about():
    return "This is a simple Flask API."
@app.route('/new')
def new():
    return "This is a new endpoint for PR!!"

if __name__ == "__main__":
    app.run(debug=True) 
