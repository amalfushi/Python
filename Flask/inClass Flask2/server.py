from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="BugleHorn"

@app.route('/')
def index():
    if not session.has_key('count'):
        session['count'] = 0
    return render_template('index.html', count = session['count'])

@app.route('/validate')
def validate():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('reset')
    return redirect('/')
app.run(debug=True)