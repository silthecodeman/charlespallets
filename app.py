from flask import Flask, render_template, redirect, request
from sendEmail import sendEmail

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

@app.route('/EmailForm', methods=["GET", "POST"])
def EmailForm():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        sendEmail(email, name, message)
        return redirect('/about')
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run()
