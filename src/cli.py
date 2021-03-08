# cli.py
import click
from pyGEDI import *

try:
    import click
except ImportError:
    sys.exit("""The following module is required: click""")


@click.group()
def main():
    """
    A simple CLI for searcing and downloading data from the 
    Global Ecosystem Dynamics Investigation (GEDI) mission.
    """

@main.command()
@click.argument('username')
@click.argument('password')
@click.argument('bbox')
def search(username, password, bbox):
    """Searches and returns GEDI data within given bounding box"""
    click.echo(username)
    click.echo(password)
    click.echo(bbox)

    session = sessionNASA(username, password)
    ul_lat= 2.96845  
    ul_lon=-73.32586
    lr_lat=-1.26845
    lr_lon=-70.23869  

    bbox=[ul_lat,ul_lon,lr_lat,lr_lon]

@main.command()
@click.argument('username')
@click.argument('password')
@click.argument('bbox')
@click.argument('path')
def download(username, password, bbox, path):
    """
    Searches and downloads GEDI data within given bounding box
    """

    click.echo(username)
    click.echo(password)
    click.echo(bbox)
    click.echo(path)

if __name__ == "__main__":
    main()