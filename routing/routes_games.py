from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from operator import itemgetter
import json
from db_models import *
from flask_paginate import Pagination, get_page_args
import math
import random

games_pages = Blueprint('games', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/games")


@games_pages.route("/")
def games():
    return render_template("games/games.html")

@games_pages.route("/hangman")
def hangman():
    data_file = open("data/quiz_questions.json")
    quiz = json.load(data_file)["questions"]
    return render_template("games/hangman.html", quiz = quiz)

@games_pages.route("/memory")
def memory():
    return render_template("games/memory.html")

