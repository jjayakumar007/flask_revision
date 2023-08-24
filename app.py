from flask import Flask,request,render_template


app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to flask"

@app.route('/cal',method=['GET'])
def math_operator():
    operation=request.jason['operation']
    number1=request.jason['number1']
    number2=request.jason['number2']

    if operation == "add":
        result=number1+number2

    elif operation == "multuplication":
        result=number1*number2

    elif operation == "division":
        result=number1/number2

    else:
        result=number1-number2
    
    return result






print (__name__)

if __name__ == '__main__':
    app.run()
