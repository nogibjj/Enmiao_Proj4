from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from fastapi import FastAPI

app = FastAPI()

predict = SentimentIntensityAnalyzer()

#need input!

@app.get("/")
def hello():
    return "query format: 0.0.0.0:8000/predict?text="

@app.get("/predict")
def fetch_predictions(text: str):
    result = predict.polarity_scores(text)
    return result
