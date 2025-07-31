# scrape.py
import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(query, max_results=100):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == max_results:
            break
        tweets.append([tweet.date, tweet.content, tweet.user.username])
    df = pd.DataFrame(tweets, columns=["Date", "Tweet", "User"])
    return df

if __name__ == "__main__":
    df = scrape_tweets("LeapScholar since:2023-07-01")
    df.to_csv("tweets.csv", index=False)
    print("Scraped and saved tweets.")
