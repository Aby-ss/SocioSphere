import json
import requests

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
