from flask import Flask, request, jsonify, Response
import json
from flask.templating import render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body> 
    <ul>
        <li><a href="/member/form">멤버 추가</a></li> 
        <li><a href="/members">멤버 목록 불러오기</a></li> 
    </ul>
    </body>
    </html>
    '''


@app.route('/save', methods=['POST'])
def save():
    if(request.method == 'POST'):
        # JSON 형식으로 서버에 전달
        data = request.form
        url = "http://localhost:8080/data/save"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = requests.post(url,
                            json=data,
                            headers=headers)
    else:
        data = {}
    return '''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body> 
        <h3> Welcome, {}</h3>
        <a href="/">메인으로</a>
    </body>
    </html>'''.format(data['username'])


@app.route('/member/form')
def register_form():
    # register form
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body> 
    <form action="/save" method="post">
        username: <input type="text" name="username" />
        age: <input type="text" name="age" />
        <button type="submit">전송</button>
    </form>
    </body>
    </html>
    '''


@app.route('/members')
def members():
    # show member lists
    # data get
    url = "http://localhost:8080/members"
    res = requests.get(url)
    data = json.loads(res.text)

    for i in data:
        print(i)
    return render_template("members.html", data=data)
