from flask import Flask, redirect, request, render_template, session
app = Flask(__name__)
app.secret_key ="TheDarkestNight"

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)