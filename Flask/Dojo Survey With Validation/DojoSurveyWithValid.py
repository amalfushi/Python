from flask import Flask, flash, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "jibba jabba"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    #form validation
    errors = False
    #could add these to session['errors'] and check for it's lenghth instead of using errors variable
    if len(request.form['your_name']) <1:
        #display error
        flash('Please Enter Your Name')
        errors = True

    if len(request.form['dojo_location']) <1:
        flash('Please Choose A Location')
        errors = True

    if len(request.form['fav_language']) <1:
        flash('Please Choose A Language')
        errors = True

    if len(request.form['comment']) > 120:
        flash('Comments can only be 120 characters')
        errors = True

    #if there are errors, show som errors
    if errors:
        return redirect('/')

    #otherwise, serve the results page
    else:
        #retrieves info from form(could be condensed into the return statement)
        thisName = request.form['your_name']
        dojoLoc = request.form['dojo_location']
        favLang = request.form['fav_language']
        thisComment = request.form['comment']

        #renders result page with the info above
        return render_template('result.html', name=thisName, dojo_location = dojoLoc, fav_language=favLang, comment=thisComment)

@app.route('/go_back', methods=['POST'])
def go_back():
    return render_template('index.html')
app.run(debug=True)