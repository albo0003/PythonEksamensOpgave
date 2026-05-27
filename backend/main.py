from fastapi import FastAPI, HTTPException
from calculations import calculate_bmi, calorie_estimate
from database import sign_up_user, login_user
from infoDatabase import save_info
from ai import ask_ai

app = FastAPI()



@app.get("/info")
def info(username: str, weight: float, height: float):
    bmi_result = calculate_bmi(weight, height)

    save_info(username, weight, height, bmi_result)


    calories = calorie_estimate(weight)

    return {
        "BMI": bmi_result,
        "daily_calories": calories
    }

@app.get("/signup")
def signup(username: str, password: str):
    result = sign_up_user(username, password)

    if(not result):
        raise HTTPException(
                    status_code=401,
                    detail="username akready exists"
                )

    return{
        "username": username
    }

@app.get("/login")
def login(username: str, password: str):
    result = login_user(username, password)

    if(not result):
        raise HTTPException(
                    status_code=401,
                    detail="wrong username or password"
                )

    return{
        "username": username
    }

@app.get("/ai")
def ai(info: str, message: str):
    answer = ask_ai(info, message)

    return{
        "ai_answer": answer
    }