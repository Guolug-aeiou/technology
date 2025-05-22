from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from dotenv import load_dotenv
import os

from app.utils.config_utils_cookie import configure_utils_cookie

# 加载 .env 文件中的环境变量
load_dotenv()
from app.utils.sql_util import MysqlUtils

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # 检查请求中的 cookie（而非响应中的）
        if request.cookies.get('username') is None:
            # 重定向到登录视图（假设登录视图函数名为 'login'）
            return redirect(url_for('login'))

    # 处理 POST 请求或已登录用户
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.cookies.get('username'):
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password_hash = request.form.get('password_hash')
        # 输入框不为空
        if not username or not password_hash:
            flash('用户名或密码不为空', 'error')
            return render_template('login.html')

        # 数据库插入数据,先比是否用户名一致的
        sql = "SELECT * FROM users WHERE username = %s"
        with MysqlUtils() as db:
            users = db.fetch_one(sql, (request.form.get('username'),))
            if users and users["password_hash"] == password_hash:
                # 密码正确
                flash('密码正确', 'success')
                # 创建响应对象并设置Cookie
                return configure_utils_cookie(response=make_response(redirect(url_for('index'))),
                                              username=users["username"],
                                              max_age=3600)

            else:
                flash('用户名或密码错误', 'error')
                return redirect(url_for('login'))

    return redirect(url_for('login'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        return configure_utils_cookie(make_response(redirect(url_for('index'))), username=None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        if (request.form.get('username') != '' and
                request.form.get('email') != '' and
                request.form.get('password_hash') != '' and
                request.form.get('password_again') != '' and
                request.form.get('password_hash') == request.form.get('password_again')):
            # 数据库插入数据,先比是否用户名一致的
            with MysqlUtils() as db:
                # 用户名或邮箱不存在则执行插入数据
                if (db.fetch_one("SELECT * FROM users WHERE username = %s", (request.form.get('username'),)) is None
                        and db.fetch_one("SELECT * FROM users WHERE email = %s", (request.form.get('email'),)) is None):
                    print("不存在用户名和邮箱,可以注册")
                    db.insert("INSERT INTO users(`username` ,`email`,`password_hash`) VALUES(%s,%s,%s) ",
                              (request.form.get('username'),
                               request.form.get('email'),
                               request.form.get('password_hash')))
                    flash('注册成功，请登录', 'success')  # 注册成功 添加成功消息
                else:
                    flash('用户名或邮箱已存在', 'error')  # 注册失败 添加错误消息
                    # 从定向到注册页面
                    return redirect(url_for('register'))
    return redirect(url_for('register'))


@app.route('/user/issue/<id>')
def user_issue(id):
    print(id)
    return render_template('issue.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
