from flask import Flask, flash, request, render_template, session , redirect, jsonify
from flask_session import Session
from datetime import datetime

import project_price
from project_price import *

import os
import os.path
import sqlite3
import hashlib


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#test price modeule evan写的在这里
#使用这个方式传入数据,class名字是Price
#testcase1 = Price(1500, True, True)
#testcase1.show()
#testcase1.getSuggested()
#print(testcase1.totalDue())

currentdirectory = os.path.dirname(os.path.abspath(__file__))
#这样import文件夹下的db !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
quote_app = os.path.join(PROJECT_ROOT, 'db', 'quote_app.db')

#Initialize the loginInfo.db database
co = sqlite3.connect(quote_app)
c = co.cursor()
ckTableExist = c.execute("""SELECT name FROM sqlite_master WHERE type='table'AND name='login_customer_info'; """).fetchall()

if ckTableExist == []:
    ###创建table的statement，需要完善+修改
    c.execute('''CREATE TABLE "login_customer_info" (
	"UsrName"	TEXT NOT NULL CHECK(length(UsrName)>0) UNIQUE COLLATE BINARY,
	"Pasword"	TEXT NOT NULL CHECK(length(Pasword)>=8) COLLATE BINARY,
	"address1"	TEXT CHECK(length(address1)<=100) COLLATE NOCASE,
	"address2"	TEXT CHECK(length(address2)<=100) COLLATE NOCASE,
	"City"	TEXT CHECK(length(City)<=100) COLLATE NOCASE,
	"stateName"	TEXT CHECK(length(stateName)=2) COLLATE NOCASE,
	"zip_code"	TEXT CHECK(length(zip_code)<=9),
	PRIMARY KEY("UsrName")
    )''') 
else:
    pass

co.commit()
co.close()

#use "python -m flask run" for ip 127, run file for pc ip
app = Flask(__name__, template_folder='static')
app.secret_key = os.urandom(24)

#有新的session管理了，这下面三行应该可以删掉，但是删了貌似JACK你的part不工作
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

#Login, Logout, Sign in, and register done by Evan----------------------------------------------------
#session管理 /log out Nani1234 Evan1234
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('user');
    return render_template('index.html')

# login form
@app.route('/login', methods=['GET'])
def login_form():
    return render_template("pages/login1.html")

# process login form
@app.route('/login', methods=['POST'])
def login():
    name = request.form['username']
    password = request.form['psw']
    
    conn = sqlite3.connect(quote_app)
    cur = conn.cursor()

    currentUser = name
    txtPassword = password
    currentPassword = hashlib.sha256(str(txtPassword).encode('utf-8')).hexdigest()

    statement = f"SELECT UsrName from login_customer_info WHERE UsrName='{currentUser}' AND Pasword = '{currentPassword}';"
    cur.execute(statement)
    
    if not cur.fetchone():  # An empty result evaluates to False.
        flash("This account does not exist or username and password do not match!!!")
        return redirect(request.url)
    else:
        session['user'] = name
        return redirect("/land")
    
@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == "POST":
        name = request.form['usrname']
        password = request.form['psw']
        con = sqlite3.connect(quote_app)
        cur = con.cursor()
        currentUser = name
        txtPassword = password
        currentPassword = hashlib.sha256(str(txtPassword).encode('utf-8')).hexdigest()
        statement = f"SELECT UsrName from login_customer_info WHERE UsrName='{currentUser}';"
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            session['user'] = name
            con.execute("insert into login_customer_info(UsrName,Pasword) values (?,?)", (currentUser, currentPassword))
            con.commit()
            con.close()
            return redirect("/land")
        else:
            flash("Account With that name already exist, Please login!!!")
            return redirect(request.url)
    return render_template("pages/registration.html")

#User Profile management done by Jack---------------------------------------------------------------------------------
# manage user profile
@app.route('/profile', methods=['GET'])
def profile_page():
    if not 'user' in session:
        return redirect('/login')

    username =  session['user']
    con = sqlite3.connect(quote_app)
    cur=con.cursor()
    statement = f"SELECT * from login_customer_info where UsrName='{username}';"
    cur.execute(statement)
    data=cur.fetchone()
    
    profile = {'username': data[7], 'address1': data[2], 'address2':  data[3], 'city': data[4], 'zipcode': data[6], 'state': data[5]}
      
    #if session['user'] in profiles:
    #    profile = profiles[session['user']]
    
    return render_template("pages/profile.html", profile=profile)
#-------------------------------------------分割线
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
    
    user = session['user']
    
    con = sqlite3.connect(quote_app)
    cur=con.cursor()
    statement = f"UPDATE login_customer_info SET full_name ='{name}',address1='{address1}', address2='{address2}', City='{city}', State='{state}', zip_code='{zipcode}' WHERE UsrName='{user}';"
    cur.execute(statement)
    con.commit()
    
    
    return redirect("/land")
    #profile = {'username': name, 'address1': address1, 'address2': address2, 'city': city, 'zipcode': zipcode, 'state': state}
    #profiles[session['user']] = profile
    #return redirect("/land")

#Quote management done by Stella---------------------------------------------------------------------------------
# manage  quote

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#test price modeule evan我写的在这里
#使用这个方式传入数据，class名字是Price
#需要数据的时候就用这个
#testcase1 = Price(1500, True, True)
#testcase1.show()
#testcase1.getSuggested()
#print(testcase1.totalDue())


#process suggest price module
@app.route('/process_suggest', methods=['POST','GET']) 
def process_suggest_price():
    if request.method=="POST":
        suggest_data=request.get_json()
        print(suggest_data)
        
    results ={'processed': 'true'}
    return jsonify(results)

    
@app.route('/quote', methods=['GET'])
def quote_page():
    if not 'user' in session:
        return redirect('/login')
    username = session['user']
    address = ''
    con = sqlite3.connect(quote_app)
    cur = con.cursor()
    statement = f"SELECT * from login_customer_info where UsrName='{username}';"
    cur.execute(statement)
    data_login=cur.fetchone()
    
    x = str(data_login[5])
    if len(x) != 2:
        return redirect('/profile')
    
    if data_login[5] == "TX":
        inout = True
    else:
        inout = False

    statement = f"SELECT * from quote_history where UsrName='{username}';"
    cur.execute(statement)
    if not cur.fetchone():
        requestb4 = False
    else:
        requestb4 = True
    return render_template("pages/quote_form.html", address=data_login[2] + " " + data_login[3] + " " + data_login[4] + " " + data_login[5] + " " +  data_login[6], inoutstate=inout,reqb4=requestb4)


# manage quote
@app.route('/quote', methods=['POST'])
def process_quote():
    if not 'user' in session:
        return redirect('/login')
    
    number = request.form['number']
    date = request.form['date']
    address = request.form['address']
    
    user = session['user']
    #if user in histories:
    #    histories[user].append((number, address, date))
    #else:
    #    histories[user] = [(number, address, date)]
        
    con = sqlite3.connect(quote_app)

    inputData = Price(number, True, True)
    #inputData.show()
    inputData.getSuggested()
    inputData.totalDue()
    #inputData.totalDue() 就可以知道需要多少钱了，param也可以从Price里改

    con.execute("insert into quote_history(UsrName,delivery_date,address,num_gallon,price_pergal,final_price) values (?,?,?,?,?);", (user,date,address,number,'60'))
    con.commit()
    con.close()
        
    return redirect('/quote_history')


##need to install datetime module
@app.route('/quote_history', methods=['GET'])
def quote_history():
    if not 'user' in session:
        return redirect('/login')
    
    history = []
    
    user = session['user']
    #if user in histories:
    #    history = histories[user]
        
    #####   connecting to db
    con = sqlite3.connect(quote_app)
    con.row_factory = sqlite3.Row
    # create cursor object
    cur = con.cursor()
    statement =f"select num_gallon, address, date(delivery_date), price_pergal from quote_history as q, login_customer_info as i where q.UsrName=i.UsrName and q.UsrName='{user}';"
    cur.execute(statement)
    
    rows = cur.fetchall()
    
    return render_template("pages/quote_history.html", history=rows)


if __name__ == '__main__': app.run(host='0.0.0.0',port=5000, debug=True)
