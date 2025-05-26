from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from dotenv import load_dotenv
import os
from app.utils.config_utils_cookie import configure_utils_cookie, get_user_cookie

# 加载 .env 文件中的环境变量
load_dotenv()
from app.utils.sql_util import MysqlUtils

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route('/allIndex', methods=['POST', 'GET'])
def allIndex():
    if request.method == "GET":
        # 获取所以 issue
        sql = "SELECT q.id id,q.title title,q.content content,q.views views,q.created_at created_at,u.username username FROM questions q JOIN users u ON q.user_id = u.id ORDER BY created_at DESC"
        with MysqlUtils() as db:
            all_data = db.fetch_all(sql, )
        return render_template('index_all_issue.html',all_data=all_data,user_data=get_user_cookie(request))


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # 检查请求中的 cookie（而非响应中的）
        if get_user_cookie(request) is None:
            # 重定向到登录视图（假设登录视图函数名为 'login'）
            return redirect(url_for('login'))
    # 根据id来查
    sql = "SELECT id,title,content,views,created_at FROM questions WHERE user_id = %s ORDER BY created_at DESC"
    with MysqlUtils() as db:
        user_issue = db.fetch_all(sql, (get_user_cookie(request)['id'],))
        print(user_issue)
        print(user_issue[0]['title'])
        # 处理 POST 请求或已登录用户
    return render_template('index.html', user_data=get_user_cookie(request), user_issue=user_issue)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # POST 登录请求
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
            if users and users["password_hash"] == password_hash and users['username'] == username:
                # 密码正确
                # flash('密码正确', 'success')
                # 创建响应对象并设置Cookie
                return configure_utils_cookie(response=make_response(redirect(url_for('index'))),
                                              value={
                                                  'id': users['id'],
                                                  'username': users['username'],
                                                  'score': users['score'],
                                                  'email': users['email']
                                              },
                                              max_age=3600)
            else:
                flash('用户名或密码错误', 'error')
                return redirect(url_for('login'))

    return redirect(url_for('login'))


@app.route('/self', methods=['GET', 'POST'])
def self():
    if request.method == 'GET':
        return render_template('self.html',user_data=get_user_cookie(request))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        response = make_response(redirect(url_for('login')))
        configure_utils_cookie(response, value=None)  # 删除Cookie
        return response


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


@app.route('/user/issue/<int:article_id>')
def user_issue(article_id):
    sql = "SELECT title,content,views,created_at FROM questions WHERE id = %s ORDER BY created_at DESC"
    with MysqlUtils() as db:
        user_data = db.fetch_one(sql, ((article_id),))
        # 处理 POST 请求或已登录用户
    return render_template('issue.html', user_data=user_data, coociks=get_user_cookie(request))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
