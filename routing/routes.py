from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from operator import itemgetter
import json
from config import *

index_pages = Blueprint('api', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/")

@index_pages.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        selected_option = request.form.get("month_select")
        logging.info(selected_option)
        return redirect("/")
    dance_dates = DanceDate.find_all()
    return render_template("index.html", dance_dates = dance_dates)

