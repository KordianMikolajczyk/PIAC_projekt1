from flask import Flask, render_template, request, abort, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return app.send_static_file('about.html')


@app.route("/gallery")
def gallery():
    return app.send_static_file('gallery.html')


@app.route("/contact")
def contact():
    return app.send_static_file('contact.html')


@app.route('/error_denied')
def error_denied():
    abort(401)


if __name__ == '__main__':
    app.run(debug=True)
