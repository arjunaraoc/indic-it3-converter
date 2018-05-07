#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import re

from testtools import TestCase

from it3conv import IT3C


class TestIT3(TestCase):

    def setUp(self):
        super(TestIT3, self).setUp()
        self.languages = 'hin urd ben guj mal pan tel tam kan ori'.split()
        self.test_dir = os.path.dirname(os.path.abspath(__file__))

    def test_raw_text(self):
        for lang in self.languages:
            it3_con = IT3C(order='utf2it3', lang=lang)
            utf_con = IT3C(order='it32utf', lang=lang)
            with io.open('%s/plain_text/%s.txt' % (self.test_dir, lang),
                         encoding='utf-8') as fp:
                for line in fp:
                    it3 = it3_con.convert(line)
                    utf = utf_con.convert(it3)
                    it3_ = it3_con.convert(utf)
                    self.assertEqual(it3, it3_)

    def test_other(self):
        for ext in ['ssf', 'conll', 'tnt']:
            it3_con = IT3C(
                order='utf2it3',
                lang='hin',
                format_=ext,
                ssf_type='intra',
                rmask=False)
            utf_con = IT3C(
                order='it32utf',
                lang='hin',
                format_=ext,
                ssf_type='intra',
                rmask=False)
            with io.open('%s/%s/hin.%s' % (self.test_dir, ext, ext),
                         encoding='utf-8') as fp:
                if ext == "ssf":
                    sentences = re.finditer(
                        "(<Sentence id=.*?>)(.*?)</Sentence>", fp.read(), re.S)
                    for sid_sentence in sentences:
                        sentence = sid_sentence.group(2).strip()
                        it3 = it3_con.convert(sentence)
                else:
                    for line in fp:
                        it3 = it3_con.convert(line)
                        utf = utf_con.convert(it3)
                        it3_ = it3_con.convert(utf)
                        self.assertEqual(it3, it3_)
