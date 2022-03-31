from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/works")
def works():
    return render_template('works.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/components")
def components():
    return render_template('components.html')
  
@app.route("/<username>/<int:post_id>")
def blog(username = None, post_id = None):
    return render_template('index.html', name=username, post_id=post_id)
  
@app.route("/blog/2022/dogs")
def blog2():
    return "<p>This is my second blog post about dog</p>"
