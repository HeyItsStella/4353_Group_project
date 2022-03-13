from flask import Flask
from flask import request
from flask import render_template, session , redirect
import os

app = Flask(__name__, template_folder='static')

app.secret_key = os.urandom(24)

users = {'test': 'Abc12345'}
profiles = {}
histories= {}


# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# landing page
@app.route('/land', methods=['GET', 'POST'])
def land():
    return render_template('pages/landingPage.html')

# registration form
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template("pages/registration.html")

# login form
@app.route('/login', methods=['GET'])
def login_form():
    return render_template("pages/login1.html")

# process login form
@app.route('/login', methods=['POST'])
def login():
    name = request.form['username']
    password = request.form['psw']
    
    if len(name) == 0:
        return "please enter username"
    
    if len(password) == 0:
        return "please enter password"
    
    if not name in users:
        return "username dost not exist"
    
    if users[name] != password:
        return "username and password dost not match"
    
    session['user'] = name
    return redirect("/land")
    

@app.route('/registration', methods=['POST'])
def registration():
    name = request.form['name']
    password = request.form['password']
    password_confirm = request.form['password_confirm']
    
    # make sure password satisfy requirements
    if password != password_confirm:
        return "password dost not match"
    
    if name in users:
        return "name is exists"
    
    if len(password) < 8 or len(password) > 64:
        return "password should be 8-64 characters"
    
    if password.isalnum() and not password.isdigit() and not password.isalpha():
        users[name] = password
        return redirect('/land')
    else:
        return "password must include a capital letter and a number"
        
  
    
# manage user profile
@app.route('/profile', methods=['GET'])
def profile_page():
    if not 'user' in session:
        return redirect('/login')
    profile = {'username': '', 'address1': '', 'address2': '', 'city': '', 'zipcode': '', 'state': ''}
    if session['user'] in profiles:
        profile = profiles[session['user']]
        
    return render_template("pages/profile.html", profile=profile)


# process profile form
@app.route('/profile', methods=['POST'])
def update_profile():
    name = request.form['name']
    address1 = request.form['address1']
    address2 = request.form['address2']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zipcode']
    
    if len(zipcode) < 5:
        return "Zipcode is too short"
    
    if not 'user' in session:
        return redirect('/login')
    profile = {'username': name, 'address1': address1, 'address2': address2, 'city': city, 'zipcode': zipcode, 'state': state}
    
    profiles[session['user']] = profile
    
    return redirect("/land")

# manage  quote
@app.route('/quote', methods=['GET'])
def quote_page():
    if not 'user' in session:
        return redirect('/login')
    
    address = ''
    if session['user'] in profiles:
        address = profiles[session['user']]['address1'] + profiles[session['user']]['address2']
        
    return render_template("pages/quote_form.html", address=address)


# manage  quote
@app.route('/quote', methods=['POST'])
def process_quote():
    if not 'user' in session:
        return redirect('/login')
    
    number = request.form['number']
    date = request.form['date']
    address = request.form['address']
    
    user = session['user']
    if user in histories:
        histories[user].append((number, address, date))
    else:
        histories[user] = [(number, address, date)]
        
    return redirect('/quote_history')

@app.route('/quote_history', methods=['GET'])
def quote_history():
    if not 'user' in session:
        return redirect('/login')
    
    history = []
    
    user = session['user']
    if user in histories:
        history = histories[user]
        
    return render_template("pages/quote_history.html", history=history)




if __name__ == '__main__':
    app.run()