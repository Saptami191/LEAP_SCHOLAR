import pandas as pd
import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

        # Streamlit page setup
st.set_page_config(layout="wide")
st.title("📊 Leap Brand Pulse - Sentiment Dashboard")

# Load data
df = pd.read_csv("labeled_tweets.csv")

# Debug: show column names
st.write("🧪 Debug: Columns in your data:", df.columns.tolist())

# Validate required columns
if not all(col in df.columns for col in ["text", "sentiment"]):
    st.error("⚠️ Required columns 'text' and 'sentiment' not found.")
    st.stop()

#  Sentiment Distribution Pie Chart
sentiment_count = df["sentiment"].value_counts().reset_index()
sentiment_count.columns = ["Sentiment", "Count"]
fig1 = px.pie(sentiment_count, names="Sentiment", values="Count", title="Sentiment Distribution")
st.plotly_chart(fig1)

#  Word Cloud
text = " ".join(df["text"].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
st.subheader("Word Cloud of All Tweets")
fig_wc, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig_wc)

#  Top Tweets by Sentiment
st.subheader("Top Tweets by Sentiment")
for sentiment in ["positive", "neutral", "negative"]:
    st.markdown(f"### {sentiment.capitalize()} Tweets")
    sample = df[df["sentiment"] == sentiment].head(5)
    for i, row in sample.iterrows():
        st.markdown(f"- {row['text']}")


