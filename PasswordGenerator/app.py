from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    if length < 8:
        length = 8

    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    password_chars = list(lower + upper + digit + special + ''.join(remaining))
    random.shuffle(password_chars)
    return ''.join(password_chars)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password')
def get_password():
    password = generate_password()
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
