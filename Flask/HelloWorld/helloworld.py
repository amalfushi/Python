from flask import Flask, session, request, render_template, redirect
app = Flask(__name__)
app.secret_key = "tacocat"

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)