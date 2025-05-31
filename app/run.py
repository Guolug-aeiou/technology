from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from dotenv import load_dotenv
import os
from app.utils.config_utils_cookie import configure_utils_cookie, get_user_cookie
import random

# 加载环境变量配置
load_dotenv()
from app.utils.sql_util import MysqlUtils

# 初始化Flask应用
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route('/allIndex', methods=['POST', 'GET'])
def allIndex():
    """显示所有用户发布的问题列表"""
    if request.method == "GET":
        # 查询所有问题并关联用户信息
        sql = "SELECT q.tag tag,q.id id,q.title title,q.content content,q.views views,q.created_at created_at,u.username username " \
              "FROM questions q JOIN users u ON q.user_id = u.id ORDER BY created_at DESC"
        with MysqlUtils() as db:
            all_data = db.fetch_all(sql, )
        # 渲染所有问题页面，传递问题数据和当前用户信息
        return render_template('index_all_issue.html', all_data=all_data, user_data=get_user_cookie(request))


@app.route('/', methods=['POST', 'GET'])
def index():
    """用户主页 - 显示当前用户发布的问题"""
    if request.method == 'GET':
        # 检查用户是否已登录
        if get_user_cookie(request) is None:
            # 未登录则重定向到登录页面
            return redirect(url_for('login'))
    # 查询当前用户发布的问题
    sql = "SELECT id,title,content,views,created_at,tag FROM questions WHERE user_id = %s ORDER BY created_at DESC"
    with MysqlUtils() as db:
        user_issue = db.fetch_all(sql, (get_user_cookie(request)['id'],))
    # 渲染用户主页，传递用户信息和问题数据
    return render_template('index.html', user_data=get_user_cookie(request), user_issue=user_issue)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """用户登录处理"""
    if request.method == 'GET':
        # 显示登录页面
        return render_template('login.html')

    # 处理POST登录请求
    if request.method == 'POST':
        username = request.form.get('username')
        password_hash = request.form.get('password_hash')

        # 验证输入是否完整
        if not username or not password_hash:
            flash('用户名或密码不为空', 'error')
            return render_template('login.html')

        # 查询数据库验证用户
        sql = "SELECT * FROM users WHERE username = %s"
        with MysqlUtils() as db:
            users = db.fetch_one(sql, (request.form.get('username'),))
            if users and users["password_hash"] == password_hash and users['username'] == username:
                # 验证成功，设置用户Cookie并重定向到主页
                return configure_utils_cookie(response=make_response(redirect(url_for('index'))),
                                              value={
                                                  'id': users['id'],
                                                  'username': users['username'],
                                                  'score': users['score'],
                                                  'email': users['email'],
                                                  'created_at': str(users['created_at']),
                                                  'avatar': users['avatar']
                                              },

                                              max_age=3600)
            else:
                # 验证失败，显示错误信息
                flash('用户名或密码错误', 'error')
                return redirect(url_for('login'))

    return redirect(url_for('login'))


@app.route('/self', methods=['GET', 'POST'])
def self():
    sql = "SELECT id,title,content,views,created_at,tag FROM questions WHERE user_id = %s ORDER BY created_at DESC"
    """用户个人中心页面"""
    if request.method == 'GET':
        # 渲染个人中心页面，传递用户信息
        with MysqlUtils() as db:
            user_issue = db.fetch_all(sql, (get_user_cookie(request)['id'],))
            counts = db.fetch_one("SELECT count(*) as counts FROM questions WHERE user_id = %s",
                                  (get_user_cookie(request)['id'],))
        return render_template('self.html', user_data=get_user_cookie(request), user_issue=user_issue, counts=counts)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """用户登出处理"""
    if request.method == 'GET':
        # 创建重定向响应并清除用户Cookie
        response = make_response(redirect(url_for('login')))
        configure_utils_cookie(response, value=None)  # 删除Cookie
        return response


@app.route('/register', methods=['GET', 'POST'])
def register():
    avatars = ['img1.png', 'img2.png', 'img3.png', 'img4.png', 'img5.png']
    random_avatar = random.choice(avatars)
    """用户注册处理"""
    if request.method == 'GET':
        # 显示注册页面
        return render_template('register.html')

    if request.method == 'POST':
        # 验证表单输入完整性和一致性
        if (request.form.get('username') != '' and
                request.form.get('email') != '' and
                request.form.get('password_hash') != '' and
                request.form.get('password_again') != '' and
                request.form.get('password_hash') == request.form.get('password_again')):

            # 检查用户名和邮箱是否已存在
            with MysqlUtils() as db:
                if (db.fetch_one("SELECT * FROM users WHERE username = %s", (request.form.get('username'),)) is None
                        and db.fetch_one("SELECT * FROM users WHERE email = %s", (request.form.get('email'),)) is None):

                    # 用户名和邮箱均不存在，执行注册
                    print("不存在用户名和邮箱,可以注册")
                    db.insert("INSERT INTO users(`username` ,`email`,`password_hash`,`avatar`) VALUES(%s,%s,%s,%s)",
                              (request.form.get('username'),
                               request.form.get('email'),
                               request.form.get('password_hash'),
                               random_avatar
                               ))
                    flash('注册成功，请登录', 'success')  # 注册成功 添加成功消息
                else:
                    flash('用户名或邮箱已存在', 'error')  # 注册失败 添加错误消息
                    return redirect(url_for('register'))

    return redirect(url_for('register'))


@app.route('/user/issue/<int:article_id>')
def user_issue(article_id):
    """显示单个问题的详情页面"""
    sql2 = "SELECT id FROM questions WHERE user_id = %s and id = %s"
    sql = "SELECT id,title,content,views,created_at,tag FROM questions WHERE id = %s ORDER BY created_at DESC"
    with MysqlUtils() as db:
        issue_data = db.fetch_one(sql, ((article_id),))
    with MysqlUtils() as db:
        isMyIssue = db.fetch_one(sql2, (get_user_cookie(request)['id'], article_id))
    # 渲染问题详情页面，传递问题数据和用户信息
    return render_template('issue.html', issue_data=issue_data, user_data=get_user_cookie(request), isMyIssue=isMyIssue)


@app.route('/add/issue/frompage', methods=['GET'])
def add_issue():
    """<UNK>"""
    return render_template('add_issue.html', user_data=get_user_cookie(request))


@app.route("/add/issue/submit", methods=['POST'])
def add_issue_submit():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('description')
        sql = "INSERT INTO questions(`title`, `content`,`user_id`, `views`) VALUES(%s,%s,%s,%s)"
        with MysqlUtils() as db:
            db.insert(sql, (title, content, get_user_cookie(request).get('id'), 0))
            return redirect(url_for('index'))
    return render_template('add_issue.html', user_data=get_user_cookie(request))


@app.route('/profile/edit', methods=['GET', 'POST'])
def profile_edit():
    if request.method == 'POST':
        sql = "UPDATE users SET username = %s,email=%s WHERE id = %s"
        with MysqlUtils() as db:
            db.execute(sql,
                       (request.form.get('username'), request.form.get('email'), get_user_cookie(request).get('id')))
        return redirect(url_for('logout'))
    if request.method == 'GET':
        return render_template('profile.html', user_data=get_user_cookie(request))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    with MysqlUtils() as db:
        question_data = db.fetch_one("SELECT * FROM questions WHERE id = %s", (id,))
    if request.method == 'POST':
        sql = "UPDATE questions SET title = %s,content=%s,tag=%s WHERE id = " + str(id)
        with MysqlUtils() as db:
            db.execute(sql,
                       (request.form.get('title'), request.form.get('content'), request.form.get('tag')))
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('edit.html', user_data=get_user_cookie(request), question_data=question_data)


if __name__ == '__main__':
    # 启动应用，开启调试模式
    app.run(debug=True, port=5000)
