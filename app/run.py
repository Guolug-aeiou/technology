from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #  查数据库比对登录信息是否正确
        if (True):
            # 密码正确 跳转到首页
            # 比对数据库创建用户成功
            # 写入cookie
            print(request.form.get('username'))
            print(request.form.get('password'))
            return redirect(url_for('index'))
        else:
            # 密码错误 跳转到登录页面

            pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        if (request.form.get('username') != '' and
                request.form.get('email') != '' and
                request.form.get('password') != '' and
                request.form.get('confirm_password') != '' and
                request.form.get('confirm_password') == request.form.get('password')):
            # 密码正确 跳转到首页
            # 比对数据库创建用户成功
            print(request.form.get('username'))
            print(request.form.get('email'))
            print(request.form.get('password'))
            print(request.form.get('confirm_password'))
        return redirect(url_for('login'))
        pass
    else:
        #  创建用户失败
        pass
    return redirect(url_for('index'))


@app.route('/user/issue/<id>')
def user_issue(id):
    print(id)
    return render_template('issue.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
