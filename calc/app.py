# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div
app = Flask(__name__)
function_list = [add,sub,mult,div]

@app.route('/math/<func>')
def math(func):
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    function_string = ["add", "sub", "mult", "div"]
    idx = function_string.index(func)
    return f"{function_list[idx](a,b)}"
    

