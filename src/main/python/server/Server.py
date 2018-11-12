from flask import Flask
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect('UserDB')


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()


