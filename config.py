from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys

#configuration for the database
db = SQLAlchemy()

#configuration for app
def set_config(dict, env):
    #setting app.config
    dict['SECRET_KEY'] = 'secretkey1'
    dict['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
    dict['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    dict['SQLALCHEMY_BINDS'] = {"avatars": "sqlite:///avatars.db", "blogs": "sqlite:///blogs.db", "dates": "sqlite:///dates.db", "books":"sqlite:///books.db"}
    dict['TEMPLATES_AUTO_RELOAD'] = True
    dict["CACHE_TYPE"] = "redis"
    dict['UPLOAD_PATH'] = "C:\\Users\dESKTOP I5\PycharmProjects\\PythonFlaskAsimov\\static\\uploads\\images"
    dict['UPLOAD_MUSIC_PATH'] = "C:\\Users\dESKTOP I5\PycharmProjects\\PythonFlaskAsimov\\static\\uploads\\music"
    dict['DEFAULT_AVATAR'] = "C:\\Users\dESKTOP I5\PycharmProjects\\PythonFlaskAsimov\\static\\images\\login-icon.jpg"
    dict['CORS_HEADERS'] = 'Content-Type'

    # setting jinja_env
    env.auto_reload = True
    env.cache = {}


