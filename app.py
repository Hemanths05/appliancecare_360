from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Add your backend logic for authentication here
    print(username)
    print(password)
    print(email)
    return f'Username: {username}, Password: {password} Email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
