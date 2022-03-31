from flask import Flask, flash
from flask import request
from flask import render_template, session , redirect

import os
import os.path
import sqlite3
import hashlib

#这么import文件夹下的db !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
logindb = os.path.join(PROJECT_ROOT, 'db', 'loginInfo.db')

currentdirectory = os.path.dirname(os.path.abspath(__file__))

#use "python -m flask run" for ip 127, run file for pc ip
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
    if not 'user' in session:
        return redirect('/login')
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
        flash("Please enter a username!")
        return redirect(request.url)
    
    if len(password) == 0:
        flash("Please enter a password!")
        return redirect(request.url)
    
    #if not name in users:
    #    return "username dost not exist"
    #if users[name] != password:
    #    return "username and password dost not match"
    #Nani1234
    
    #session['user'] = name
    
    conn = sqlite3.connect(logindb)
    cur = conn.cursor()

    currentUser = name
    txtPassword = password
    currentPassword = hashlib.sha256(str(txtPassword).encode('utf-8')).hexdigest()

    statement = f"SELECT UsrName from loginInfo WHERE UsrName='{currentUser}' AND Pasword = '{currentPassword}';"
    cur.execute(statement)
    
    if not cur.fetchone():  # An empty result evaluates to False.
        flash("This account does not exist or username and password do not match!!!")
        return redirect(request.url)
    else:
        #print("Welcome")
        session['user'] = name
        return redirect("/land")
    
#nani Nani1234
    
@app.route('/registration', methods=['POST', 'GET'])
def registration():
    #password_confirm = request.form['psw_con']
        
    # make sure password satisfy requirements
    #if password != password_confirm:
    #    return "password dost not match"
    if request.method == "POST":  
        name = request.form['usrname']
        password = request.form['psw']
        GETITLATER = ''
        #if name in users:
        #    flash('this shit exist man wtf')
        #    return redirect(request.url)
        
        #if len(password) < 8 or len(password) > 64:
        #    flash('password should be 8-64 characters')
        #    return redirect(request.url)

        #if password.isalnum() and not password.isdigit() and not password.isalpha():
        #users[name] = password Nani1234
        
        con = sqlite3.connect(logindb)
        # create cursor object
        cur = con.cursor()
        #------------------------------------------------------------------------------
        currentUser = name
        txtPassword = password
        currentPassword = hashlib.sha256(str(txtPassword).encode('utf-8')).hexdigest()
        #------------------------------------------------------------------------------
        #Check if STUDENT table exists in the database
        listOfTables = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table'
        AND name='loginInfo'; """).fetchall()
        if listOfTables == []:
            #Table not found!
            #TABLE IS CREATED HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            con.execute('''CREATE TABLE loginInfo(UsrName, Pasword, yourstate, email, phone);''')
            #------------------------------------------------------------------------------
            currentUser = name
            txtPassword = password
            currentPassword = hashlib.sha256(str(txtPassword).encode('utf-8')).hexdigest()
            statement = f"SELECT UsrName from loginInfo WHERE UsrName='{currentUser}' AND Pasword = '{currentPassword}';"
            cur.execute(statement)
            if not cur.fetchone():  # An empty result evaluates to False.
                session['user'] = name
                con.execute("insert into loginInfo values (?,?,?,?,?)", (currentUser, currentPassword,str(GETITLATER),str(GETITLATER),str(GETITLATER)))
                con.commit()
                con.close()
                return redirect("/land")
            else:
                #print("Nah")
                flash("Account already exist, Please login!!!")
                return redirect(request.url)
        else:
            #Table found!
            currentUser = name
            txtPassword = password
            currentPassword = hashlib.sha256(str(txtPassword).encode('utf-8')).hexdigest()
            statement = f"SELECT UsrName from loginInfo WHERE UsrName='{currentUser}' AND Pasword = '{currentPassword}';"
            cur.execute(statement)
            if not cur.fetchone():  # An empty result evaluates to False.
                session['user'] = name
                con.execute("insert into loginInfo values (?,?,?,?,?)", (currentUser, currentPassword,str(GETITLATER),str(GETITLATER),str(GETITLATER)))
                con.commit()
                con.close()
                return redirect("/land")
            else:
                #print("Nah")
                flash("Account already exist, Please login!!!")
                return redirect(request.url)
        #return redirect('/land')
        #else:
            #return "password must include a capital letter and a number"
        #    return redirect('/land')
        #------------------------------------------------------------------------------
    return render_template("pages/registration.html")
        
  
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