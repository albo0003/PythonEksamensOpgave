import pandas as pd
import os

FILE_PATH = "/app/data/users.csv"


def sign_up_user(username, password):
    new_data = pd.DataFrame([{
        "username": username,
        "password": password
    }])

    if os.path.exists(FILE_PATH):
        df = pd.read_csv(FILE_PATH)

        # check if user already has name
        if username in df["username"].values:
            return False

        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_csv(FILE_PATH, index=False)
    return True

def login_user(username, password):
    if not os.path.exists(FILE_PATH):
        return False

    df = pd.read_csv(FILE_PATH)

    # check if user exists
    df["username"] = df["username"].astype(str)
    df["password"] = df["password"].astype(str)
    match = (df["username"] == username) & (df["password"] == password)

    return match.any()


