'''
So I'm basically just going through the quickstart guide 
for Flask and adding my own notes as comments below.
After that, I plan on diving a bit deeper into the docs
before rebuilding my 'portfolio' page or another NUBC 
project with Flask running the routing. 
'''



from flask import Flask

from markupsafe import escape #This is to prevent injection attacks
                              #Escape causes the route input to be rendered as text
                              #Prevents someone from running unwanted <script> in the browser
                              #HTML templates from Jinja do this automatically

app = Flask(__name__) 

# @app.route defines page routing
# like node, not nodemon. server must be restarted to show changes
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test_page():
    return 'This is a test'


#Escaping Example
@app.route('/<name>-<age>')  #Variables passed into routing function need to be separted, most likely with '-'
def hello(name, age):
    return f'Hello, {escape(name)}. You are {escape(age)}' #New String Formatting, with escape
    # return 'Hello %s.' % (name) #Old String Formatting


#Variable Rules -> Used in Escaping Example
#Variables marked in the url are denoted by <variable_name>
#Can have type converters attached with <converter:<variable>
'''
Variable Converters:
string: string
int: integers
float: positive floating points
path: string, but with slashes
uuid: uuid strings -> IETF Paper on UUIDs (https://datatracker.ietf.org/doc/html/rfc4122)
'''
#examples
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'  #I'm assuming this doesn't need escape bc of the int converter

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'





