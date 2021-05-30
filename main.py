from flask import Flask, request, render_template, redirect, session, url_for
from datetime import timedelta

app = Flask(__name__)
#Use secrect key to enable session
app.secret_key = "flask auth"
app.permanent_session_lifetime = timedelta(hours=1)

#Root Route
@app.route('/',methods=['POST','GET'])
def home():   
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if email == "anirudh@gmail.com" and password == "abcdef":
            return render_template('index.html',username=email)
        return redirect(url_for('login'))
    else:
        if "username" in session:
            return render_template('index.html',username=session['username'])
        return redirect(url_for('login'))

#Login Route
@app.route('/login')
def login():
    if "username" in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    if "username" in session:
        session.pop("username",None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)