from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort, make_response
from jinja2 import TemplateNotFound
from log_config import logging
from operator import itemgetter
from config import *
from db_models import *
import json

api_pages = Blueprint('index', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/api")

@api_pages.route("/")
def api():

    json_file = open("data/books.json")
    data = json.load(json_file)
    return jsonify(DanceDate.find_all())

@api_pages.route("/", methods = ["POST"])
def api_post():
    # receiving request asynchronously in JSON
    if request.headers.get("Content-Type") == "application/json":
        scheduled_date = request.get_json()
        time = datetime(2022, datetime.strptime(scheduled_date["month"], "%B").month,
                        int(scheduled_date["day"]), int(scheduled_date["hour"].split(":")[0]), 0, 0)
        if DanceDate.find_all_filter(time) == None:
            logging.info(time)
            DanceDate.insert_one(time)
        logging.info(time)
    return jsonify({"success":True, "response":"Date added"})

@api_pages.route("/", methods = ["PUT"])
def api_put():
    if request.headers.get("Content-Type") == "application/json":
        scheduled_dates = request.get_json()
    return jsonify({"success":True, "response":"Date updated"})

@api_pages.route("/", methods = ["DELETE"])
def api_delete():
    if request.headers.get("Content-Type") == "application/json":
        scheduled_date = request.get_json()
        time = datetime(2022, datetime.strptime(scheduled_date["month"], "%B").month,
                        int(scheduled_date["day"]), int(scheduled_date["hour"].split(":")[0]), 0, 0)
        DanceDate.delete_one(time)
        return jsonify({"success": True, "response": "Date deleted"})

@api_pages.route("/delete_all")
def api_delete_all():
    DanceDate.delete_all()
    return jsonify({"success": True, "response": "All is deleted"})