from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

def about():
    return '<h1>About us, text</h1>'

@app.route('/txt')
def txt():
    return render_template('txt.html')


@app.route('/<name>')
def user(name):
    return render_template('user.html', my_name=input())


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'

@app.route('/admin')
def admin():
    # return redirect('https://www.google.com/')
    # return redirect('/')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
