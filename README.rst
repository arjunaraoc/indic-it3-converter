indic-it3-converter
===================

|Build Status| |Coverage Status| |CircleCI|

.. |Build Status| image:: https://travis-ci.org/arjunaraoc/indic-it3-converter.svg?branch=master 
   :target: https://travis-ci.org/arjunaraoc/indic-it3-converter

.. |Coverage Status| image:: https://coveralls.io/repos/github/arjunaraoc/indic-it3-converter/badge.svg?branch=master 
   :target: https://coveralls.io/github/arjunaraoc/indic-it3-converter?branch=master

.. |CircleCI| image:: https://circleci.com/gh/arjunaraoc/indic-it3-converter.svg?style=shield&circle-token=:circle-token 
    :target: https://circleci.com/gh/arjunaraoc/indic-it3-converter


Python library for IT3 to UTF conversion  for Indian languages.

Installation
------------

Download
^^^^^^^^

Download **indic-it3-converter**  from `github`_.

.. _`github`: https://github.com/irshadbhat/indic-it3-converter

Install
^^^^^^^

::

    Clone the repository:
        git clone https://github.com/arjunaraoc/indic-it3-converter

    Change to the cloned directory:
        cd indic-it3-converter
        pip install -r requirements.txt
        python setup.py install

Examples
--------

1. work with files:
^^^^^^^^^^^^^^^^^^^

.. parsed-literal::

    it3conv --f ssf --t intra --n --l hin --s utf --i hin-utf.ssf --o hin-it3.ssf

    -l , --language     select language (3 letter ISO-639 code)
                                        Hindi       : hin
                                        Telugu      : tel
                                        Tamil       : tam
                                        Malayalam   : mal
                                        Kannada     : kan
                                        Bengali     : ben
                                        Oriya       : ori
                                        Punjabi     : pan
                                        Marathi     : mar
                                        Nepali      : nep
                                        Gujarati    : guj
                                        Bodo        : bod
                                        Konkani     : kok
                                        Assamese    : asm
                                        Urdu        : urd
    -s , --source-enc   {utf, it3} select input-file encoding
    -f , --format       {text, ssf, conll, bio, tnt} select input-file format
    -t , --ssf-type     {inter, intra} specify ssf-type if file format (-f) is ssf
    -n, --nested        set this flag for nested ssf
    -m, --no-mask       set this flag to keep off masking of roman strings in Indic text
    -i , --input        <input-file>
    -o , --output       <output-file>
    -z, --normalize     set this flag for utf normalizations without WX-Conversion

2. utf to it3 (plain text):
^^^^^^^^^^^^^^^^^^^^^^^^^^

Not implemented

3. it3 to utf:
^^^^^^^^^^^^^

.. code:: python
    Example for Telugu it3 to Utf-8
    --------
    >>> from it3conv import IT3C
    >>> it3c = IT3C(lang='tel', order='it32utf')
    >>> tel_it3=u'''tirumala tirupati aan\'dhrulaku pavitra pund-ya kshheitramu'''
    >>> tel_utf_ = it3c.convert(tel_it3)
    >>> print(tel_utf_)
    తిరుమల తిరుపతి ఆంధ్రులకు పవిత్ర పుణ్య క్షేత్రము
    >>>




