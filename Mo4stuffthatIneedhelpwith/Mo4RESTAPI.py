# I am unable to check this since I can not import

from flask import Flask
app = Flasck(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))


    def __repr__(self):
        return f"{self.name} - {self.description}"


# in the consle
# python3
# from application import db
# from application import Book
# book = Book(book_name = "id", author = "I don't remember" , publisher = "I don't remember part two" )
