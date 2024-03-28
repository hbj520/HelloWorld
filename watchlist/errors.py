from watchlist import app
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.filter_by(name='Lebron Han').first()
    return render_template('errors/404.html'), 404 # 返回模板和状态码
