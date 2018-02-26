from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "merlin and the goats"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)