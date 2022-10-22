from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from time import sleep

console = Console()
layout = Layout()

layout.split(Layout(name="header", size=3),
             Layout(ratio=1, name="main"),
             Layout(size=10, name="footer"),)

# William McGugan's article must be updated
layout["main"].split_row(Layout(name='side'),
                         Layout(name="body", ratio=2))

layout["side"].split(Layout(), Layout())

console.print(layout)

with Live(layout, screen=True):
    while True:
        sleep(1)