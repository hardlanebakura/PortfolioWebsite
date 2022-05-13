from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys

#configuration for the database
db = SQLAlchemy()

class Blog(db.Model):
    __bind_key__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return "Blog " + str(self.id)

class DanceDate(db.Model):
    __bind_key__ = "dates"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)

    @staticmethod
    def insert_one(data):
        DanceDate1 = DanceDate(date = data)
        db.session.add(DanceDate1)
        db.session.commit()

    @staticmethod
    def find_all_filter(data):
        search_matches = db.session.query(DanceDate).filter_by(date = data).all()
        if len(search_matches) > 0:
            return search_matches
        else: return None

    @staticmethod
    def find_all():
        search_matches = [vars(item) for item in DanceDate.query.all()]
        list1 = [item["date"].strftime("%d/%m/%Y/%H:%M:%S - {}:00:00".format(int(item["date"].strftime("%H")) + 1)) for item in search_matches]
        return list1

    @staticmethod
    def delete_all():
        db.session.query(DanceDate).delete()
        db.session.commit()

    @staticmethod
    def delete_one(data):
        DanceDate.query.filter_by(date = data).delete()
        db.session.commit()

#configuration for app
def set_config(dict, env):
    #setting app.config
    dict['SECRET_KEY'] = 'secretkey1'
    dict['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
    dict['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    dict['SQLALCHEMY_BINDS'] = {"avatars": "sqlite:///avatars.db", "blogs": "sqlite:///blogs.db", "dates": "sqlite:///dates.db"}
    dict['TEMPLATES_AUTO_RELOAD'] = True
    dict["CACHE_TYPE"] = "redis"
    dict['UPLOAD_PATH'] = "C:\\Users\dESKTOP I5\PycharmProjects\\PythonFlaskAsimov\\static\\uploads\\images"
    dict['UPLOAD_MUSIC_PATH'] = "C:\\Users\dESKTOP I5\PycharmProjects\\PythonFlaskAsimov\\static\\uploads\\music"
    dict['DEFAULT_AVATAR'] = "C:\\Users\dESKTOP I5\PycharmProjects\\PythonFlaskAsimov\\static\\images\\login-icon.jpg"
    dict['CORS_HEADERS'] = 'Content-Type'

    # setting jinja_env
    env.auto_reload = True
    env.cache = {}


#setting database operations
class Database(object):

    @staticmethod
    def insert_one(data):
        Blog1 = Blog(title = data[0], content = data[1], author = data[2])
        db.session.add(Blog1)
        db.session.commit()

    def __repr__(self):
        return

