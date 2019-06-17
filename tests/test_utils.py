#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `f90nmlparse/utils.py` package."""
import pytest
import logging
from click.testing import CliRunner

from f90nmlparse import utils


def test_count_to_log_level():
    assert utils.count_to_log_level(0) == logging.ERROR
    assert utils.count_to_log_level(1) == logging.WARNING
    assert utils.count_to_log_level(2) == logging.INFO
    assert utils.count_to_log_level(3) == logging.DEBUG
