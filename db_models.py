from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

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

class Book(db.Model):
    __bind_key__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(70))
    rating = db.Column(db.Integer)
    img = db.Column(db.String)
    review = db.Column(db.String)

    @staticmethod
    def insert_one(data):
        Book1 = Book(name = data["name"], author = data["author"], rating = data["rating"], img = data["img"], review = data["review"])
        db.session.add(Book1)
        db.session.commit()

    @staticmethod
    def find_all():
        search_matches = [{"name":vars(item)["name"], "author":vars(item)["author"], "rating":vars(item)["rating"], "img":vars(item)["img"], "review":vars(item)["review"]} for item in Book.query.all()]
        return search_matches

    @staticmethod
    def delete_all():
        db.session.query(Book).delete()
        db.session.commit()

    @staticmethod
    def delete_one(data):
        Book.query.filter_by(name = data["name"]).delete()
        db.session.commit()

    def __repr__(self):
        return "Book " + str(self.id)