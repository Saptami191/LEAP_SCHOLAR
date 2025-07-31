# sentiment.py
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    compound = score["compound"]
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def tag_sentiment(csv_path):
    df = pd.read_csv(csv_path)
    df["Sentiment"] = df["Tweet"].apply(analyze_sentiment)
    df.to_csv("labeled_tweets.csv", index=False)
    print("Sentiment analysis complete.")

if __name__ == "__main__":
    tag_sentiment("tweets.csv")
