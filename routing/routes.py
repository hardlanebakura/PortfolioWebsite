from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from operator import itemgetter
import json
from db_models import *
from flask_paginate import Pagination, get_page_args
import math
import random

index_pages = Blueprint('api', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/")

@index_pages.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        selected_option = request.form.get("month_select")
        logging.info(selected_option)
        return redirect("/")
    dance_dates = DanceDate.find_all()
    json_file = open("data/quotes.json")
    data = json.load(json_file)["quotes"]
    quote = random.choice(data)
    return render_template("index.html", dance_dates = dance_dates, quote = quote)

def get_books(offset = 0, per_page = 10):
    return Book.find_all()[offset: offset + per_page]

@index_pages.route("/books")
def books():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    books = get_books(offset=offset, per_page=per_page)
    total = math.ceil(len(Book.find_all()) / 10) * 10
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')
    return render_template('books.html', books = books, page = page, per_page = 50, pagination = pagination, total = total)

@index_pages.route("/projects")
def projects():
    return render_template("projects.html")

@index_pages.route("/blog")
def blogs():
    data_file = open("data/blogs.json")
    blogs = json.load(data_file)["blogs"]
    logging.info(blogs)
    return render_template("blogs.html", blogs = blogs)

@index_pages.route("blog/<int:blog_id>")
def blog(blog_id):
    data_file = open("data/blogs.json")
    blogs = json.load(data_file)["blogs"]
    return render_template("blogs/{}.html".format(blogs[blog_id - 1]["template"]), blogs = blogs)

@index_pages.route("/dance_with_death")
def dance_with_death():
    if request.method == "POST":
        selected_option = request.form.get("month_select")
        logging.info(selected_option)
        return redirect("/dance_with_death")
    dance_dates = DanceDate.find_all()
    return render_template("dance_with_death.html", dance_dates = dance_dates)



