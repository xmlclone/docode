import click

from waitress import serve
from xflask import create_app


@click.group()
def main():
    ...


@click.command()
@click.option('-h', '--host', type=str, default='0.0.0.0', show_default=True, help="Hostname or IP address on which to listen, default is '0.0.0.0',which means all IP addresses on this host.")
@click.option('-p', '--port', type=str, default=51127, show_default=True, help="TCP port on which to listen, default is '51127'.")
@click.option('-e', '--env', type=click.Choice(['prod', 'test', 'dev']), default='prod', show_default=True)
def run_server(host, port, env):
    serve(create_app(env), host=host, port=port)


main.add_command(run_server)