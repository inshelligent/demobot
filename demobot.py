# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)

# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World! Works now :) Fun codings!'

# When people visit '/ncss' use the ncss function
@app.route('/ncss')
def ncss():
    return '<h1>NCSS Rocks!</h1>'

# You can access demobot’s greet command via <your website>/greet
@app.route('/greet', methods=['GET','POST'])
def greet_person():
    # Get the value of the 'text' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('text')
    # This bot says hi to every name it gets sent!
    return f'hi {name}!'

@app.route('/weather')
def weather():
    # Get the value of the 'temp' query parameter
    temp = request.values.get('temp')
    # check to see if it is >30
    if int(temp) > 30:
        return "It's so hot!!"
    else:
        return f"the temperature is {temp}"


if __name__ == '__main__':
    # Start the web server!
    app.run(debug=true)
