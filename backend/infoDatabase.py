import pandas as pd
import os
from datetime import datetime

FILE_PATH = "/app/data/info.csv"


def save_info(username, weight, height, bmi):
    new_row = pd.DataFrame([{
        "date": datetime.now().strftime("%Y-%m-%d"),
        "username": username,
        "weight": weight,
        "height": height,
        "bmi": bmi
    }])

    if os.path.exists(FILE_PATH):
        df = pd.read_csv(FILE_PATH)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(FILE_PATH, index=False)