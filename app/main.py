from datetime import datetime
import csv
import time
import requests
from time import sleep
import math
import keyboard
import numpy as np
import asciichartpy

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
    Layout(name="Sentiment Analysis"),
    Layout(name="Entity Profilling"),
    Layout(name="Power Dynamics")
)

layout["Right"].split_column(
    Layout(name="News"),
    Layout(name="Political / Economical Influences")
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

def news():
    url = "https://api.apilayer.com/financelayer/news?apikey=EHw0Ndjb26EG0xvAK5uNSO5oNkgp5w73&tickers=blk&tickers=btc&tickers=VOO&tickers=STT&tags=News&tags=Business&sources=forbes.com&sources=investing.com&sources=bloomberg.com&sort=desc&offset=5&limit=7&keywords=news&keywords=economy&keywords=politics&keywords=Blackrock&keywords=stock%20prices&fallback=on&date=thismonth"

    response = requests.get(url)
    data = response.json()

    news_objects = data["data"]

    # Create a layout to organize panels
    layout = Layout(name="root")

    # Create a single panel to hold all news articles
    news_panel_content = ""

    for news in news_objects:
        title = news["title"]
        description = news["description"]
        url = news["url"]
        source = news["source"]
        published_at = news["published_at"]
        
        # Add each news article's information to the aggregated content
        news_panel_content += (
            f"Title: [link={url}]{title}[/link]\n"
            f"Description: {description}\n"
            f"Source: {source}\n"
            f"Published At: {published_at}\n\n"
        )

    # Create the panel with aggregated content
    news_panel = Panel(news_panel_content, title="Aggregated News", border_style="bold white", box=box.SQUARE)

    # Print the layout to display the news panel
    return news_panel

def get_wikipedia_summary(topic):
    base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    full_url = base_url + topic
    response = requests.get(full_url)
    data = response.json()
    summary = data.get("extract", "No summary available.")
    return summary

def wikipedia_main():
    political_figure = "Barack_Obama"
    topic_summary = get_wikipedia_summary(political_figure)
    
    return Panel(topic_summary, title="Entity profilling", border_style="bold white", box=box.SQUARE)


layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["News"].update(news())
layout["Entity Profilling"].update(wikipedia_main())

print(layout)