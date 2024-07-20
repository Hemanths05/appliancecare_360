from flask import Flask, render_template, request
from temp import store_data,fetch_data
from users import User


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user_type = request.form['userType']
    user=User(username,email,password,user_type)
    isUserAvailable=fetch_data(user)
    if(not isUserAvailable):
        store_data(user)
    else:
        return "user exits"
    return "singup"

@app.route('/signin', methods=['POST'])
def signin():
    password = request.form['password']
    email = request.form['email']
    user_type = request.form['userType1']
    user=User(email,password,user_type)
    isUserAvailable=fetch_data(user)
    if isUserAvailable:
        return "Signin successful."
    else:
        return "User does not exist. Create an account."

if __name__ == '__main__':
     app.run(debug=True)