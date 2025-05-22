def configure_utils_cookie(response, username=None, max_age=86400):
    if username:
        # 设置cookie：key固定为'username'，值为用户名字符串
        response.set_cookie(
            key='username',  # 固定为'username'
            value=username,
            path='/',
            httponly=True,  # 防止XSS
            max_age=max_age
        )
    else:
        # 删除cookie：key必须与设置时一致
        response.delete_cookie(
            key='username',  # 固定为'username'
            path='/',
            domain=None,
            httponly=True
        )
    return response