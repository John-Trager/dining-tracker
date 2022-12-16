# app.py

from flask import Flask, redirect, render_template, request
from database import Database, user_params

app = Flask(__name__)
db = Database('users.csv')

def parse_user(user):
    return user.replace('[', '').replace(']', '').replace("'", "").replace('"','').replace(' ', '').split(',')

@app.route('/')
def index():
    users = db.read_users()
    return render_template('index.html', users=users, user_params=user_params)

@app.route('/add', methods=['POST'])
def add_user():
    if request.form['name'] == '':
        return redirect('/')
    
    name = request.form['name']
    created_ip = request.remote_addr

    db.add_user([name] + [0]*(len(user_params)-2))
    return redirect('/')

@app.route('/modify', methods=['POST'])
def modify_user():
    #if request.remote_addr != request.form['user_ip'] or request.remote_addr != "35.3.118.88":
    #    return redirect('/')

    user = parse_user(request.form['user'])
    change = int(request.form['change'])
    param = request.form['param']

    db.modify_user(user,change,param)
        
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_user():
    #if request.remote_addr != request.form['user_ip'] or request.remote_addr != "35.3.118.88":
    #    return redirect('/')
    user = parse_user(request.form['user'])
    print(user[0])
    db.delete_user(user[0])
    return redirect('/')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True, port=65535)