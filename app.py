from database import *
from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "lkasjjsa;ijcz;/osidjc;zsdicm;z/sdijc;z/sdijc;zsod/icjml"

 
##### Code here ######
 

@app.route('/DeleverySign',methods=['GET','POST'])
def signD():

    if request.method=='GET':
         return render_template("signAsdelevery.html")

    if request.method=='POST':
        if Check_DUsername(request.form['Name'])==None:
            
            add_Delevery(request.form['Name'],request.form['password'],request.form['Email'],request.form['Phone'],request.form['city'],request.form['Cost'])
            
            return render_template("signAsdelevery.html")
         
    return "try another UserName"



@app.route('/',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        user = check_username(request.form['Name'])
        if user!=None and user.verify_password(request.form["password"]):
             
            return "logedin Coustmer"
        user=Check_DUsername(request.form['Name'])
        if user!=None and user.verify_password(request.form["password"]):
            return render_template("delevery.html",name=request.form['Name'])
             
        
    return "wrong password or username"
        

@app.route('/sign',methods=['GET','POST'])

def sign():
    if request.method=="GET":
        return render_template("sign.html")
    
    if request.method=="POST":
        print("we posted")
        if check_username(request.form['Name'])==None:
            print("you got here")
            add_user(request.form['Name'],request.form['password'],request.form['Email'],request.form['Phone'],request.form['city'])
            return render_template('sign.html')
    return "use another username"
    print("you get here")


if __name__ == '__main__':
    app.run(debug=True)