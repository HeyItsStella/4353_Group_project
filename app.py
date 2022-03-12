from flask import Flask, request, render_template
app = Flask(__name__)

#Run py file for 192, run commend "python -m flask run" for default
@app.route('/')
def index():
    return render_template('login1.html')

@app.route('/land/')
def land():
    return render_template('landingPage.html')

##########################################################
@app.route('/profile/')
def profile():
    return render_template('profile.html')

@app.route('/reg/')
def createProfile():
    return render_template('registration.html')
   
##########################################################
@app.route('/getQuote/')
def getQuote():
    return render_template('quote_form.html')

@app.route('/submitQuote/', methods = ['POST'])
def quote():
    if request.method == 'POST':
        date = request.form['date']
        gallons = request.form['gallons']
        fuel = request.form['fuel']
    else:
        return render_template('quote_form.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000, threaded=True, debug=True)