from flask import Flask, session, redirect, render_template, request
import random

app = Flask(__name__)
app.secret_key="sanic"

@app.route('/')
def index():
    if not session.has_key('number'):
        session['number'] = random.randint(1,100)
        print session['number']
    if not session.has_key('msg'):
        session['message'] = ''
    return render_template('index.html', message=session['message'], color = session['color'])

@app.route('/verify', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    # print session['guess']
    # print session['number']
    if(session['guess'] ==  session['number']):
        session['message'] = 'Your guess is correct.  The  number was ' +str(session['number'])+'!'
    elif(session['guess'] > session['number']):
        session['message'] = 'Too High.'
    else:
        session['message'] = 'Too Low.'
    return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
	session.pop('number') 
	session.pop('guess')
	return redirect('/')

app.run(debug=True)
