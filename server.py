from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
  
@app.route("/blog")
def blog():
    return "<p>This is my first blog post</p>"
  
@app.route("/blog/2022/dogs")
def blog2():
    return "<p>This is my second blog post about dog</p>"