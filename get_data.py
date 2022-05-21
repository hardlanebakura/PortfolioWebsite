#supply the hangman with the json data
from log_config import logging
from mongo_collections import DatabaseAtlas
import json

logging.info(DatabaseAtlas.db.list_collection_names())


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

all_movies = [item for item in DatabaseAtlas.findAll("movies2", {}) if "\\" not in item["original_title"] and "'" not in item["original_title"] and is_english(item["original_title"]) and (item["original_title"].isalpha() or " " in item["original_title"])]

logging.info([item["original_title"] for item in all_movies])
for item in all_movies:
    item["title"] = item["original_title"]
    item["title"] = item["title"].replace(":", "")
    logging.info(item["title"])

for item in all_movies:
    item["genre"] = "movies"
    item["question"] = item["title"]

d = {}
d["questions"] = all_movies
with open("data/quiz_questions.json", "w") as data_file:
    json.dump(d, data_file, indent = 4)