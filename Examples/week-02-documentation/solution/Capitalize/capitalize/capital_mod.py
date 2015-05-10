#!/usr/bin/env python

"""
===================
capitalize_mod.py
===================

A really simple module, just to demonstrate packaging
"""

def capitalize_line(instr):
    """
    capitalizes each word of the input string

    :param instr: the string to capitalize it should be a single line.
    :type instr: string

    :returns: a capitalized version of instr

    **List of known Users**:
        - you
        - me
    
    :Example Usage:

    >>> capitalize_line( "abcd efgh" )
    "Abcd Efgh"

    .. note:: decide if we want doctests for this

    """

    return " ".join( word.capitalize() for word in instr.split() )


def capitalize(infilename, outfilename):
    """
    reads the contents of infilename, and writes it to outfilename, but with
    every word capitalized

    :param infilename: The file name you want to process
    :type infilename: string

    :param outfilename: the name of the new file that will be created
    :type outfilename: string

    :returns: None

    :raises: IOError if infilename doesn't exist.

    .. warning:: very primitive -- it will mess some files up!

    """
    infile = open(infilename, 'U')
    outfile = open(outfilename, 'w')

    for line in infile:
        outfile.write(capitalize_line(line))
        outfile.write("\n")

    return None


class Something(object):
    """
    this is the class docstring
    """
    def __init__(self, input):
        """
        the __init__ docstring

        :param input: someinput
        :type input: some_type
        """
        pass
