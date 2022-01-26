from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from fastapi import FastAPI

app = FastAPI()

predict = SentimentIntensityAnalyzer()

@app.get("/")
def fetch_predictions(text: str):
    result = predict.polarity_scores(text)
    return result