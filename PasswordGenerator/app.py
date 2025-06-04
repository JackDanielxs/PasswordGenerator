from flask import Flask, render_template, jsonify
import random
import string

# Flask web application instance
app = Flask(__name__)

def generate_password(length=12):
    # Enforce a minimum length of 8 characters
    if length < 8:
        length = 8

    # Ensure the password includes at least one character from each category
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Combine all character types for remaining characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    # Create the password list and shuffle it to ensure randomness
    password_chars = list(lower + upper + digit + special + ''.join(remaining))
    random.shuffle(password_chars)
    return ''.join(password_chars)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for generating a password via a JSON response
@app.route('/generate-password')
def get_password():
    password = generate_password()
    return jsonify({'password': password})

# Run the application in debug mode when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
