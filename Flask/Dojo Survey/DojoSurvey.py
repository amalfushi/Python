from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
# app.secret_key = "jibba jabba"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    thisName = request.form['your_name']
    dojoLoc = request.form['dojo_location']
    favLang = request.form['fav_language']
    thisComment = request.form['comment']
    return render_template('result.html', name=thisName, dojo_location = dojoLoc, fav_language=favLang, comment=thisComment)

@app.route('/go_back', methods=['POST'])
def go_back():
    return render_template('index.html')
app.run(debug=True)