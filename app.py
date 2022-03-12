#from crypt import methods
from flask import Flask, request, render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)

#Run py file for 192, run commend "python -m flask run" for default

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('login1.html')

@app.route('/land/')
def land():
    return render_template('landingPage.html')

@app.route('/land/', methods=['post'])
def landform():
    return render_template('landingPage.html')

@app.route('/reg/')
def createProfile():
    return render_template('registration.html')

@app.route('/reg/', methods=['post'])
def regform():
    form = RegistrationForm(request.form)
    #validate data here when we use db
    #if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
        #            form.password.data)
        #db_session.add(user)
        #flash('Thanks for registering')
        #return redirect(url_for('login'))
    return render_template('registration.html', form=form)

##########################################################
@app.route('/profile/')
def profile():
    return render_template('profile.html')

   
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