# -*- coding: utf-8 -*-
"""Main module."""
import os
import sys
import f90nml
import json
import yaml
import logging


def nmlparse(infile: str):
    # parse namelist and store it in dict
    nml = f90nml.read(infile)
    return (nml)


def nmlwrite(nml, **kwargs):

    output_fmt = kwargs.get("format")

    _out = kwargs.get("_out", sys.stdout)
    # determine output format
    valid_formats = ('json', 'yaml', 'nml')
    if output_fmt and output_fmt not in valid_formats:
        raise ValueError(
            "Error: format must be one of: {0}".format(valid_formats))

    if _out != sys.stdout:
        output_file = open(_out, 'w')
        output_fname = _out
    else:
        output_file = _out
        output_fname = None

    # Get output format from out_file name
    if not output_fmt:
        if output_fname:
            _, output_ext = os.path.splitext(output_fname)
            if output_ext == '.json':
                output_fmt = 'json'
            elif output_ext in ('.yaml', '.yml'):
                output_fmt = 'yaml'
            else:
                output_fmt = 'nml'
        else:
            output_fmt = 'nml'

    # write nml to output_file
    if output_fmt == "json":
        json.dump(nml, output_file, indent=4, separators=(',', ': '))
        output_file.write('\n')
    elif output_fmt == "yaml":
        input_data = nml.todict(complex_tuple=True)
        yaml.dump(input_data, output_file, default_flow_style=False)
    else:
        f90nml.write(nml, output_file)

    # Cleanup
    if _out != sys.stdout:
        output_file.close()
