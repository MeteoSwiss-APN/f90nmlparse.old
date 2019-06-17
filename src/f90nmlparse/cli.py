# -*- coding: utf-8 -*-
"""Console script for f90nmlparse."""
import os
import sys
import click
import logging

from f90nmlparse.f90nmlparse import nmlparse, nmlwrite
from f90nmlparse.utils import count_to_log_level

__version__ = '0.1.0'


@click.command()
@click.option(
    '--dry-run',
    '-n',
    flag_value='dry_run',
    default=False,
    help="Perform a trial run with no changes made")
@click.option(
    '--verbose',
    '-v',
    count=True,
    help="Increase verbosity (specify multiple times for more)")
@click.option('--version', '-V', is_flag=True, help="Print version")
@click.option('--format', '-f', help="Output format (json, nml or yaml)")
@click.option('--out_file', '-o', help="Output file")
@click.argument('infile', type=click.File('rb'), nargs=1)
def main(*args, **kwargs):
    """Parse fortran namelist and print it in json format"""

    logging.basicConfig(level=count_to_log_level(kwargs['verbose']))

    logging.warning("This is a warning.")
    logging.info("This is an info message.")
    logging.debug("This is a debug message.")

    if kwargs['version']:
        click.echo(__version__)
        return 0

    if kwargs['dry_run']:
        click.echo("Is dry run")
        return 0

    if kwargs["out_file"]:
        output_file = kwargs["out_file"]
    else:
        output_file = sys.stdout

    # read input file name from command line
    infile = kwargs["infile"].name

    mynml = nmlparse(infile)

    if kwargs["format"]:
        output_fmt = kwargs["format"]
    else:
        output_fmt = "json"

    nmlwrite(mynml, _out=output_file, format=output_fmt)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover47
