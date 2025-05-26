from flask import json


def configure_utils_cookie(response, value=None, key='data', max_age=86400):
    if value:
        # 设置cookie：将字典转换为JSON字符串存储
        import json
        response.set_cookie(
            key=key,  # Cookie的名称
            value=json.dumps(value),  # 将字典转为JSON字符串
            path='/',
            httponly=True,  # 防止XSS攻击
            max_age=max_age  # 有效期（秒）
        )
    else:
        # 删除cookie：key必须与设置时一致
        response.delete_cookie(
            key=key,  # 要删除的Cookie名称
            path='/',
            domain=None
        )
    return response


def get_user_cookie(request):
    data = request.cookies.get('data')
    if data:
        try:
            # 解析JSON字符串为字典
            return json.loads(data)
        except json.JSONDecodeError:
            # 解析失败时返回None
            return None
    return None
