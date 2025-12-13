import json
import os
from utils.config import DATA_PATH

def read_json(filename):
    file_path = os.path.join(DATA_PATH, filename)
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


