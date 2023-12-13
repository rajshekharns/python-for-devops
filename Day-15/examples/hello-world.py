from flask import Flask

app = Flask(__name__)

@app.route('/')
#decorator is used to run action before the function execution
#for example if user enter ip:port then incorrect path then it will send error msg path not found
#before the execution of function decoraor is used perform certain actions.
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run("0.0.0.0")
