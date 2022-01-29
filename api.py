from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from fastapi import FastAPI

app = FastAPI()

predict = SentimentIntensityAnalyzer()

#need input!

@app.get("/")
def hello():
    return "query format: fastapi-5gzezq4jcq-uc.a.run.app/predict?text="

@app.get("/predict")
def fetch_predictions(text: str):
    result = predict.polarity_scores(text)
    return result
