import unittest
from watchlist import app, db
from watchlist.models import Movie, User
app.app_context().push()

class WatchlistTestCase(unittest.TestCase):

    def setUp(self):
        # 更新配置
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        db.create_all()
        user = User(name='Test',username='test username')
        user.set_password('123456')
        movie = Movie(title='test movie title', year='2019')
        db.session.add_all([user,movie])
        db.session.commit()

        self.client = app.test_client() # 创建测试客户端
        self.runner = app.test_cli_runner() # 创建测试命令运行器

        def tearDown(self):
            db.session.remove() # 清除数据库会话
            db.drop_all() # 删除数据库表

    def test_app_exist(self):
        self.assertIsNotNone(app)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()
