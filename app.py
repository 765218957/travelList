import os
from flask import Flask, render_template, flash, redirect, url_for, Markup

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# the minimal Flask application
@app.route('/')
def index():
    return render_template('travel.html')


if __name__ == '__main__':
    app.run(debug=False)
