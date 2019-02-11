import logging

import click

logger = logging.getLogger(__name__)


@click.group()
@click.option('-v', '--verbose', count=True, help="Verbose logging")
@click.option('-d', '--debug', help="Debug logging")
def cli(verbose, debug):
    loglevel = logging.WARNING
    if verbose:
        loglevel = logging.INFO
    elif debug:
        loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)


@cli.command()
def subcommand():
    logger.debug("DEBUG log")
    logger.info("INFO log")
    logger.warning("WARN log")
    print("Subcommand")


if __name__ == '__main__':
    cli()
