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
    '''
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
    '''
    def test_tel_map(self):
        lang="tel"
        telmap={


                'a':'అ', 'aa':'ఆ', 'i':'ఇ', 'ii':'ఈ', 'u':'ఉ', 'uu':'ఊ',
                   'e':'ఎ', 'o':'ఒ',
                'ei': 'ఏ', 'ai': 'ఐ', 'oo': 'ఓ', 'au': 'ఔ',
                'rx': 'ఋ',
            #'lx': 'ఌ',
                     'ka':'క',
                     'kha':'ఖ', 'ga':'గ', 'gha':'ఘ',
                 'ng~a':'ఙ',
                 'cha':'చ', 'chha':'ఛ', 'ja':'జ', 'jha':'ఝ',
                'nj~a':'ఞ',
                't:a': 'ట', 't:ha':'ఠ', 'd:a':'డ', 'd:ha':'ఢ',
                'nd~a':'ణ',
                    'ta':'త', 'tha':'థ', 'da':'ద', 'dha':'ధ',
                     'na':'న',
                     'pa':'ప', 'pha':'ఫ', 'ba':'బ', 'bha':'భ', 'ma':'మ', 'ya':'య',
                 'ra':'ర','r:a':'ఱ','la':'ల','l:a':'ళ','va':'వ', 'sha': 'శ',
                 'shha':'ష',
                 'sa':'స', 'ha':'హ',

                'an:':'అం','aan:':'ఆం',
                #'a:' : 'అః',
                 'ayitei eimit:i':'అయితే ఏమిటి',

                    'k': 'క్',  'kaa':'కా','ki':'కి', 'kii':'కీ', 'ku':'కు', 'kuu':'కూ','krx':'కృ',
                    'ke': 'కె','kei':'కే','kai':'కై', 'ko':'కొ', 'koo':'కో', 'kau':'కౌ',
                    'kan:': 'కం',  # 'ka:':'కః',
                    #'krxx':'కౄ',
            'kh': 'ఖ్', 'khaa': 'ఖా', 'khi': 'ఖి', 'khii': 'ఖీ', 'khu': 'ఖు', 'khuu': 'ఖూ', 'khrx': 'ఖృ',
            'khe': 'ఖె', 'khei': 'ఖే', 'khai': 'ఖై', 'kho': 'ఖొ', 'khoo': 'ఖో', 'khau': 'ఖౌ',
            'khan:': 'ఖం',  # 'kha:':'ఖః',
            # 'khrxx':'ఖౄ',
                    

                    'kaan:':'కాం','kin:':'కిం',
            
            
                    'kaayaka':'కాయక',
                    'nan:danan:':'నందనం',
                    'kautukan:':'కౌతుకం',
                    'tirumala tirupati aan:drulaku pavitra pund~yaa kshheitramu':'తిరుమల తిరుపతి ఆంద్రులకు పవిత్ర పుణ్యా క్షేత్రము',
                     'shaivaaya':'శైవాయ',

                     '.':'.',
                     ',':',', '?':'?', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7',
                     '8':'8', '9':'9', ';':';', '-':'-', '\\':'\\', '<':'<', '>':'>', '/':'/', '[':'[',
                      ']':']', '!':'!', '@':'@', '#':'#', '$':'$', '%':'%', '^':'^', '&':'&', '*':'*',
                      '(':'(', ')':')',
                        #'_':'_',
                        '+':'+', '|':'|'
                }

        utf_con = IT3C(order='it32utf', lang=lang)

        for item in telmap.keys():
            self.assertEqual( utf_con.convert(item), telmap.get(item))