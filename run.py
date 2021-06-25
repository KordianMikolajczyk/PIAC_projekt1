from flask import Flask, render_template, request, abort, redirect, url_for, make_response
from flask_dance.contrib.github import make_github_blueprint, github
from AzureDB import AzureDB
import secrets
import os



app = Flask(__name__)

app.secret_key=secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT']='1'

github_blueprint = make_github_blueprint(
    client_id = '96341b6972481700e117',
    client_secret = '895af5173650317127f92bec911b5dea68604f8e',
)
app.register_blueprint(github_blueprint, url_prefix='/login')

@app.route('/home')
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/guest")
def guest():
    with AzureDB() as a:
        data = a.azureAddData()
       # data = a.azureDeleteData()
        data = a.azureGetData()
    return render_template("guest.html", data=data)


@app.route('/error_denied')
def error_denied():
    abort(401)


@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template('index.html')
            #return '<h1>Your Github name is {}'.format(account_info_json['login'])
    return '<h1>Request failed!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
