# 引入控制器
from web.controllers.index import route_index
from application import app
from web.controllers.user.User import route_user
from web.interceptors.AuthInterceptor import *


"""
蓝图
"""

app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(route_user, url_prefix='/user')
