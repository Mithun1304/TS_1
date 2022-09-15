# save this as app.py
from flask import Flask
app = Flask(name_1)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if name_1 == 'main':
    app.run()