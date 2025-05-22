import pymysql
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()


class MysqlUtils:
    def __init__(
            self,
            host: str = os.environ.get("MYSQL_HOST"),
            port: int = int(os.environ.get("MYSQL_PORT")),
            user: str = os.environ.get("MYSQL_USER"),
            password: str = os.environ.get("MYSQL_PASSWORD"),
            database: str = os.environ.get("MYSQL_DATABASE"),
            charset: str = os.environ.get("MYSQL_CHARSET"),
    ):
        """
        初始化数据库连接参数
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.connection = None

    def connect(self):
        """建立数据库连接"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset,
                cursorclass=pymysql.cursors.DictCursor  # 返回字典格式结果
            )
            print("数据库连接成功")
        except pymysql.MySQLError as e:
            raise Exception(f"数据库连接失败：{e}")

    def close(self):
        """关闭数据库连接"""
        if self.connection and self.connection.open:
            self.connection.close()
            print("数据库连接已关闭")

    def fetch_one(self, sql: str, params: tuple = None) -> Optional[Dict]:
        """查询单条记录"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchone()

    def fetch_all(self, sql: str, params: tuple = None) -> List[Dict]:
        """查询所有记录"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    def execute(self, sql: str, params: tuple = None) -> int:
        """执行插入/更新/删除语句，返回影响行数"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            return cursor.rowcount

    def insert(self, sql: str, params: tuple = None) -> int:
        """插入一条数据，并返回自增主键"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            return cursor.lastrowid

    def __enter__(self):
        """用于上下文管理器 with"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时自动关闭连接"""
        self.close()


if __name__ == '__main__':
    with MysqlUtils() as db:
        user = db.fetch_one("select * from users where id=%s", (1,))
        db.insert("INSERT INTO users(`username` ,`email`,`password_hash`) VALUES(%s,%s,%s) ", ("121", "123", "1234",))
        print(user)
