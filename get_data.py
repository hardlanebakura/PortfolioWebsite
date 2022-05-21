#supply the hangman with the json data
from log_config import logging
from mongo_collections import DatabaseAtlas
import json

logging.info(DatabaseAtlas.db.list_collection_names())


def is_english(s):
    if not isinstance(s, str):
        raise TypeError("Expected string input")
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def movies_check(s):
    if not isinstance(s, str):
        raise TypeError("Expected string input")
    if "\\" in s:
        return False
    elif (s.isalpha() or " " in s):
        return True

all_movies = [item for item in DatabaseAtlas.findAll("movies2", {}) if is_english(item["original_title"]) and movies_check(item["original_title"])]

for item in all_movies:
    item["title"] = item["original_title"].replace(":", "")
    item["genre"] = "movies"
    item["question"] = item["title"]
    logging.info(item["title"])

d = {}
d["questions"] = all_movies
with open("data/quiz_questions.json", "w") as data_file:
    json.dump(d, data_file, indent = 4)