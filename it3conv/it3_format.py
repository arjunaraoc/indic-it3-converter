#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Copyright Arjuna Rao Chavala 2018
#  Thanks to Irshad Ahmad Bhat 2015 for his WX converter code.

"""IT3 convertor: converts Indic scripts to ASCII and vice-versa

IT3 notation is a transliteration scheme for representing Indian languages
in ASCII. For more details on IT3 go to:
<https://en.wikipedia.org/wiki/WX_notation>.

This module is a UTF (Indian Scripts) to Roman (IT3) convertor and vice-versa:
    - converts text in 1 Indian languages Telugu,
    - handles 1 data formats viz. plain-text,
"""

from __future__ import unicode_literals

import re
import sys

from .it3 import IT3
from .ssf_reader import SSFReader


class IT3C():
    """IT3-converter for UTF to IT3 conversion of Indic (Telugu) scripts and vice-versa.

    Parameters
    ----------
    lang : str, default: tel
        Input script

    order : str, default: it32utf
        Order of conversion

    format_ : str, default: text
        Text file format (text)


    rmask : bool, default: True
        If True masks/unmasks Roman text in Indic scripts

    norm : bool, default: False
        If True returns normalized text without IT3-Conversion

    Example for Telugu it3 to Utf-8
    --------
    >>> from it3conv import IT3C
    >>> it3c = IT3C(lang='tel', order='it32utf')
    >>> tel_it3=u'''tirumala tirupati aan\'dhrulaku pavitra pund-ya kshheitramu'''
    >>> tel_utf_ = it3c.convert(tel_it3)
    >>> print(tel_utf_)
    తిరుమల తిరుపతి ఆంధ్రులకు పవిత్ర పుణ్య క్షేత్రము
    """

    def __init__(self, order="utf2it3", format_="text", lang="hin",
                 ssf_type="intra", nested=False, rmask=True, norm=False):
        self.lang = lang
        self.nested = nested
        self.format_ = format_
        self.ssf_type = ssf_type
        it3p = IT3(self.lang, order, rmask, norm)
        self.transform = it3p.it32utf if order == "it32utf" else it3p.utf2it3

    def convert(self, line):
        if self.format_ == "text":
            return self.transform(line)
        else:
            sys.stderr("FormatError: invalid format :: %s\n" % self.format_)
            sys.exit(0)
