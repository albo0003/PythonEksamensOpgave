import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")


def ask_ai(user_info, message):

    prompt = f"""
    User information:
    {user_info}

    User question:
    {message}

    Give fitness advice.
    """

    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-small-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

       # 🚨 STEP 1: check HTTP status
    if response.status_code != 200:
        return f"API error {response.status_code}: {response.text}"

    result = response.json()

    # 🚨 STEP 2: check structure
    if "choices" not in result:
        return f"Unexpected response: {result}"

    return result["choices"][0]["message"]["content"]