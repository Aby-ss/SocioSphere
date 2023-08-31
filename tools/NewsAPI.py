import json
import requests

url = "https://api.apilayer.com/financelayer/news?apikey=EHw0Ndjb26EG0xvAK5uNSO5oNkgp5w73&tickers=blk&tickers=btc&tickers=VOO&tickers=STT&tags=News&tags=Business&sources=forbes.com&sources=investing.com&sources=bloomberg.com&sort=desc&offset=5&limit=7&keywords=news&keywords=stock%20prices&fallback=on&date=thismonth"

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

