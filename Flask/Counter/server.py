from flask import Flask, redirect, session, render_template

app = Flask(__name__)
app.secret_key ="jisaopjasip"

@app.route('/')
def index():
    session['count']+=1
    print session['count']
    return render_template('index.html', count = session['count'])

app.run(debug=None)