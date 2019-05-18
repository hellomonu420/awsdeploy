from flask import Flask
import os
 
application = Flask(__name__)

@application.route('/')
def hello_world():
    message = "Hello, world!"
    return "hello world"
 
if __name__ == '__main__':
    application.run(host='0.0.0.0')

