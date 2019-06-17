#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `f90nmlparse` package."""
import pytest
from pathlib import Path
from f90nmlparse.f90nmlparse import nmlparse, nmlwrite



def test_nmlparse():
    infile="tests/data/letkf_c"

    # test values of namelist
    mynml = nmlparse(infile)
    assert(mynml["report"]["excl_bnd"] == 0.67)
    assert(mynml["report"]["height_t"] == 300.0)
    assert(mynml["rules"]["t"]["use"] == 7)

    # test for inexistant file
    with pytest.raises(FileNotFoundError) as excinfo:
        mynml = nmlparse("gugus")

    assert("No such file or directory: 'gugus'" 
           in str(excinfo.value))

def test_nmlwrite():
    infile="tests/data/letkf_c"

    # test values different formats
    mynml = nmlparse(infile)
    for fmt in ["json", "yaml", "nml"]:
        outfile = "test_nml." + fmt
        nmlwrite(mynml, _out=outfile)
        assert(Path(outfile).exists())
        Path(outfile).unlink()

    # test for wrong format
    with pytest.raises(ValueError):
        nmlwrite(mynml, format="txt")
    
        

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
