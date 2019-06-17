#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `f90nmlparse` package."""
import pytest
from click.testing import CliRunner

from f90nmlparse import cli


def test_command_line_interface():
    """Test the CLI."""
    infile = "tests/data/letkf_c"
    runner = CliRunner()
    result = runner.invoke(cli.main, ['-f', 'nml', infile])
    assert result.exit_code == 0
    assert '&report\n    excl_bnd = 0.67\n    height_t = 300.0\n/' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output
    dry_run_result = runner.invoke(cli.main, ['-n', infile])
    assert dry_run_result.exit_code == 0
    assert 'Is dry run' in dry_run_result.output
    version_result = runner.invoke(cli.main, ['-V', infile])
    assert version_result.exit_code == 0
    assert cli.__version__ in version_result.output
