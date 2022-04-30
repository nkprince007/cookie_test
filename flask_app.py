from flask import Flask, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app, supports_credentials=True)


@app.route("/", methods=["GET"])
def index():
    response = make_response("Here take some cookie!")
    response.set_cookie(
        key='cookieKey',
        value='cookieValue',
        path='/',
        samesite='None',
        secure=True,
        max_age=24 * 60 * 60,
    )
    return response


@app.route("/about/", methods=["GET"])
def about():
    if 'cookieKey' in request.cookies:
        val = request.cookies.get('cookieKey')
        return f'Cookie received => cookieKey: {val}'
    return 'No cookie received!'
