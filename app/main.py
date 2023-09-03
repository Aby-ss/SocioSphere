from datetime import datetime
import csv
import time
import requests
from time import sleep
import math
import keyboard
import numpy as np
import wbgapi as wb
import matplotlib.pyplot as plt
import asciichartpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from rich import print
from rich import box
from rich.tree import Tree
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name = "Header", size=3),
    Layout(name = "Body"),
    Layout(name = "Footer", size=3)
)

layout["Body"].split_row(
    Layout(name="Left"),
    Layout(name="Right")
)


layout["Left"].split_column(
    Layout(name="Sentiment Analysis"), #📝
    Layout(name="Entity Profilling"), #✅
    Layout(name="Power Dynamics") #📝
)

layout["Right"].split_column(
    Layout(name="News"), #✅
    Layout(name="Political / Economical Influences") #✅
)


class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "🗃", "[b]InfluenceGraph Insights: Mapping Power Dynamics and Political Relationships[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white", box=box.SQUARE)
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row("[b]Mapping Influence, Unveiling Power: See Beyond the Surface[/]")
        return Panel(grid, style="white on black", box=box.SQUARE)


def worldBank_API():
    # Data Retrieval
    indicators = [
        "FP.CPI.TOTL.ZG",     # Inflation
        "NE.EXP.GNFS.CD",     # Expenses
        "NY.GDP.MKTP.CD",     # GDP
        "NY.GDP.MKTP.KD.ZG",  # GDP Growth
        "NY.GNS.ICTR.CD",     # Gross Savings
        "NE.EXP.GNFS.CD"      # Exports
    ]

    countries = "USA"

    data = [wb.data.DataFrame(indicator, countries).transpose() for indicator in indicators]

    # Set up colors
    colors = ['b', 'g', 'r', 'c', 'm', 'y']

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot each indicator with a different color
    for i, indicator_data in enumerate(data):
        ax.plot(indicator_data.index, indicator_data.values, label=indicators[i], color=colors[i])

    # Set axis labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    ax.set_title("Multiple Indicators Over Time")

    # Add a legend
    ax.legend(loc='upper left')

    # Rotate the x-axis labels by 90 degrees
    ax.tick_params(axis='x', rotation=90)

    # Show the plot
    plt.show()   

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

# Analyze sentiment for a given text
def analyze_text_sentiment(text):
    sentiment = analyze_sentiment(text)
    sentiment_score = sentiment["compound"]
    return sentiment_score

def news_main():
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
        sentiment_score = analyze_text_sentiment(description)

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
    return news_panel

def wiki_main():
    # Get the Wikipedia summary for a political figure (Barack Obama in this case)
    political_figure = "Hitler"
    topic_summary = get_wikipedia_summary(political_figure)

    # Analyze sentiment of the Wikipedia summary
    wikipedia_sentiment_score = analyze_text_sentiment(topic_summary)

    # Get sentiment label with color formatting for Wikipedia summary
    wikipedia_sentiment_label = get_sentiment_label(wikipedia_sentiment_score)

    # Create a panel to display the Wikipedia topic summary with sentiment
    wikipedia_panel_content = (
        f"Title: Wikipedia Summary for {political_figure}\n"
        f"Summary: {topic_summary}\n"
        f"Sentiment: {wikipedia_sentiment_label} (Score: {wikipedia_sentiment_score})\n\n"
    )
    wikipedia_panel = Panel(wikipedia_panel_content, title="Entity Profiling", border_style="bold white", box=box.SQUARE)
    return wikipedia_panel


layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["News"].update(news_main())
layout["Entity Profilling"].update(wiki_main())
layout["Political / Economical Influences"].update(Panel("Charts shown separately.", padding=(8,25), border_style="bold white", box=box.SQUARE))
worldBank_API()

print(layout)