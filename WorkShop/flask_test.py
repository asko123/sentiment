# Flask_test
from flask import Flask, request

# initializes a new Flask application. __name__ holds the name of the current module
app = Flask(__name__)

# route() decorator tells Flask the entry points for the application
@app.route('/')
def hello_world():
    return '<H1> Hello, World! </H1>'

@app.route('/add')
def add():
    a1 = request.args.get('a')
    b1 = request.args.get('b')
    s = "<H1>" + str(int(a1) + int(b1)) + "</H1>"   
    return s

if __name__ == '__main__':
    app.run()



