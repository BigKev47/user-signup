from flask import Flask, request, redirect, render_template
import cgi
#~
app = Flask(__name__)
#~
app.config['DEBUG'] = True      # displays runtime errors in the browser..

@app.route("/submit", methods=["POST"])
def process_form():
    user = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    results = [is_valid(user),is_valid(password),password_match(password, verify),valid_email(email)]
    if results == ["","","",""]:
        return render_template('welcome.html', username = user)
    else:
        return render_template('signup.html', results = results, username = user, email = email)
    

def is_valid(response):
    if response != "":
        if " " not in response:
            if 2<len(response)<21:
                return ""
            return "Field must be between 3-20 characters."
        return "Field cannot contain spaces."
    else:
        return "No input"

def valid_email(email):
    if is_valid(email) == "No input":
                return ""
    if email.count("@") != 1 or email.count(".") != 1:
        return "email must contain on '.', one '@', and be between 3-20 characters long."
    else:
        return is_valid(email)
        
def password_match(first_PW,conf):
    if first_PW == conf:
        return ""
    else:
        return "Passwords do not match."
    
@app.route("/", methods=["GET","POST"])
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html', results = [], error=encoded_error and cgi.escape(encoded_error, quote=True))
    #~
    

app.run()
