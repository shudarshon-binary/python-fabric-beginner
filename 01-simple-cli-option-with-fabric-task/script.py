#!/usr/bin/env python3
import configparser
import click
from fabric.api import local

config = configparser.ConfigParser()
config.read("config.ini")
host = config["DEFAULT"].get("host")
user = config["DEFAULT"].get("user")

@click.group()
@click.pass_context
def cli(ctx):
    """create a cli tool that will help running ad-hoc tasks"""
    return

def main():
    """execute main"""
    cli.add_command(deploy)
    cli()

@click.command()
@click.option(
    "-e",
    "--environment",
    required=True,
    prompt=True,
    type=click.Choice(["dev", "stage"]),
)
def deploy(environment):
    """deploy to defined environment"""
    click.confirm(f"Are you sure you want to deploy {environment}?", abort=True)

    if environment == "dev":
        deploy_develop()
    elif environment == "stage":
        deploy_staging()

    click.echo(f"Successfully started deployment for {environment}")

def deploy_develop():
    """ Run 'ping' on development hosts """
    local("pwd")
        
def deploy_staging():
    """ Run 'ping' on staging hosts"""
    local("hostname")

if __name__ == "__main__":
    main()
