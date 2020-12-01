"""Console script for teamcity_rest_client."""
import sys
import click
from teamcity_rest_client.rest_api import start_build


@click.group()
def main():
    return 0


@main.command()
@click.option('--server', prompt='server url',
              help='server url.')
@click.option('--user', prompt='user',
              help='teamcity login.')
@click.option('--token', prompt='token',
              help='teamcity token.')
@click.option('--build-id', prompt='build id',
              help='teamcity build id.')
@click.option('--commit', prompt='commit hash to build',
              help='commit hash to build.')
@click.option('--parameter', '-p', multiple=True)
@click.option('--tag', '-t', multiple=True)
def build(server, user, token, build_id, commit, parameter, tag):
    """Console script for teamcity_build."""
    success = start_build(server=server, user=user, token=token, build_id=build_id,
                          properties=[p.split('=') for p in parameter], change=commit, tags=tag)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
