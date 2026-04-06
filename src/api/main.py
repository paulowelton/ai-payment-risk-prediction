from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("models/model.pkl")
columns = joblib.load("models/columns.pkl")

@app.get("/")
def home():
    return {"message": "API de previsão de pagamento rodando"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return {"pagou_em_dia": int(prediction)}