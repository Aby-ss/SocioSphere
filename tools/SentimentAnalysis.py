import json
import requests
from rich.traceback import install
install(show_locals=True)
from rich.panel import Panel
from rich import box, print
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to get news data
def get_news_data():
    url = "https://api.apilayer.com/financelayer/news?apikey=EHw0Ndjb26EG0xvAK5uNSO5oNkgp5w73&tickers=blk&tickers=btc&tickers=VOO&tickers=STT&tags=News&tags=Business&sources=forbes.com&sources=investing.com&sources=bloomberg.com&sort=desc&offset=5&limit=7&keywords=news&keywords=stock%20prices&fallback=on&date=thismonth"
    response = requests.get(url)
    data = response.json()
    return data.get("data", [])

# Function to analyze sentiment
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    return vs

# Function to get sentiment label with color formatting
def get_sentiment_label(sentiment_score):
    if sentiment_score > 0:
        return "[green]Positive[/]"
    elif sentiment_score < 0:
        return "[red]Negative[/]"
    else:
        return "[yellow]Neutral[/]"

# Function to get Wikipedia summary
def get_wikipedia_summary(topic):
    base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    full_url = base_url + topic
    response = requests.get(full_url)
    data = response.json()
    summary = data.get("extract", "No summary available.")
    return summary

# Get news data
news_data = get_news_data()

# Initialize a panel to hold news content
news_panel_content = ""

# Iterate through news articles
for news in news_data:
    title = news["title"]
    description = news["description"]
    url = news["url"]
    source = news["source"]
    published_at = news["published_at"]

    # Analyze sentiment of the description
    sentiment = analyze_sentiment(description)
    sentiment_score = sentiment["compound"]

    # Get sentiment label with color formatting
    sentiment_label = get_sentiment_label(sentiment_score)

    # Add each news article's information to the aggregated content
    news_panel_content += (
        f"Title: [link={url}]{title}[/link]\n"
        f"Description: {description}\n"
        f"Source: {source}\n"
        f"Published At: {published_at}\n"
        f"Sentiment: {sentiment_label} (Score: {sentiment_score})\n\n"
    )

# Create the panel with aggregated news content
news_panel = Panel(news_panel_content, title="Aggregated News", border_style="bold white", box=box.SQUARE)

# Get the Wikipedia summary for a political figure (Barack Obama in this case)
political_figure = "Barack_Obama"
topic_summary = get_wikipedia_summary(political_figure)

# Create a panel to display the Wikipedia topic summary
wikipedia_panel = Panel(topic_summary, title="Entity Profiling", border_style="bold white", box=box.SQUARE)

# Print the news panel and Wikipedia panel
print(news_panel)
print(wikipedia_panel)