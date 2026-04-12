import os
from datetime import datetime
import json

if not os.path.exists("log_folder"):
    os.mkdir("log_folder")

current_time = datetime.now()

data = {
    "date": current_time.strftime("%d.%m.%Y"),
    "time": current_time.strftime("%H:%M:%S"),
    "status": "success"
}

with open("log_folder/log.json", "w", encoding="utf-8") as log_json:
    json.dump(data, log_json, ensure_ascii=False, indent=4)