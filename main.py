from flask import Flask, request, redirect, render_template
import cgi
#~
app = Flask(__name__)
#~
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def process_form():
    user = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    results = [is_valid(user),isvalid(password),password_match(verify),valid_email(email)]
    if results == ["","","",""]:
        return True
    else:
        return results
    

def is_valid(response):
    if response != "":
        if " " not in response:
            if 2<len(response)<21:
                return True
            return "Field must be between 3-20 characters."
        return "Field cannot contain spaces."
    return "No input"

def valid_email(email):
    if email.count("@") == 1:
        if email.count(".") == 1:
            if is_valid(email) == "No input":
                return True
            return is_valid(email)
        return "email must contain on '.', one '@', and be between 3-20 characters long."
        
def password_match(first_PW,conf):
    if first_pw == conf:
        return ""
    else:
        return "Passwords do not match."
    
@app.route("/")
def main():
    #encoded_error = request.args.get("error")
    return render_template('signup.html', results = process_form(), usernamep=request.form['username'], error=encoded_error and cgi.escape(encoded_error, quote=True))
    #~
    print(valid_email("kevin@unionmaccom"))

main()
