from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/index.html")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/<username>/<int:post_id>")
def blog(username = None, post_id = None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/blog/2022/dogs")
def blog2():
    return "<p>This is my second blog post about dog</p>"
