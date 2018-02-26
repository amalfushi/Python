from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key="excelcior"

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about_me')
def about():
    return render_template('about_me.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

app.run(debug=True)