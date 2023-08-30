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


    
layout["Header"].update(Header())
layout["Footer"].update(Footer())

print(layout)