#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from testtools import TestCase

from it3conv import IT3C


class TestIT3(TestCase):

    def setUp(self):
        super(TestIT3, self).setUp()
        self.languages = 'hin urd ben guj mal pan tel tam kan ori'.split()
        self.test_dir = os.path.dirname(os.path.abspath(__file__))

    def test_tel_map(self):
        lang = "tel"
        telmap = {

            'a': 'అ', 'aa': 'ఆ', 'i': 'ఇ', 'ii': 'ఈ', 'u': 'ఉ', 'uu': 'ఊ',
            'e': 'ఎ', 'o': 'ఒ',
            'ei': 'ఏ', 'ai': 'ఐ', 'oo': 'ఓ', 'au': 'ఔ',
            'rx': 'ఋ',
            # 'rx-': 'ఋూ',
            # 'lx': 'ఌ',
            'ka': 'క',
            'kha': 'ఖ', 'ga': 'గ', 'gha': 'ఘ',
            'ng-a': 'ఙ',
            'cha': 'చ', 'chha': 'ఛ', 'ja': 'జ', 'jha': 'ఝ',
            'nj-a': 'ఞ',
            't\'a': 'ట', 't\'ha': 'ఠ', 'd\'a': 'డ', 'd\'ha': 'ఢ',
            'nd-a': 'ణ',
            'ta': 'త', 'tha': 'థ', 'da': 'ద', 'dha': 'ధ',
            'na': 'న',
            'pa': 'ప', 'pha': 'ఫ', 'ba': 'బ', 'bha': 'భ', 'ma': 'మ',
            'ya': 'య', 'ra': 'ర', 'r\'a': 'ఱ', 'la': 'ల', 'l\'a': 'ళ',
            'va': 'వ', 'sha': 'శ',
            'shha': 'ష',
            'sa': 'స', 'ha': 'హ',

            'an\'': 'అం', 'aan\'': 'ఆం',
            'a:': 'అః',
            'ayitei eimit\'i': 'అయితే ఏమిటి',

            'k': 'క్', 'kaa': 'కా', 'ki': 'కి', 'kii': 'కీ', 'ku': 'కు',
            'kuu': 'కూ', 'krx': 'కృ',
            'ke': 'కె', 'kei': 'కే', 'kai': 'కై', 'ko': 'కొ', 'koo': 'కో',
            'kau': 'కౌ',
            'kan\'': 'కం', 'ka:': 'కః',
            # 'krx-':'కౄ',
            'kh': 'ఖ్', 'khaa': 'ఖా', 'khi': 'ఖి', 'khii': 'ఖీ', 'khu': 'ఖు',
            'khuu': 'ఖూ', 'khrx': 'ఖృ',
            'khe': 'ఖె', 'khei': 'ఖే', 'khai': 'ఖై', 'kho': 'ఖొ', 'khoo': 'ఖో',
            'khau': 'ఖౌ',
            'khan\'': 'ఖం', 'kha:': 'ఖః',
            # 'khrx-':'ఖౄ',

            't\'h': 'ఠ్', 't\'haa': 'ఠా', 't\'hi': 'ఠి', 't\'hii': 'ఠీ',
            't\'hu': 'ఠు', 't\'huu': 'ఠూ', 't\'hrx': 'ఠృ',
            't\'he': 'ఠె', 't\'hei': 'ఠే', 't\'hai': 'ఠై', 't\'ho': 'ఠొ',
            't\'hoo': 'ఠో', 't\'hau': 'ఠౌ',
            't\'han\'': 'ఠం', 't\'ha:': 'ఠః',
            # 't\'hrx-':'ఠౄ',

            'kaan\'': 'కాం', 'kin\'': 'కిం',

            'kaayaka': 'కాయక',
            'nan\'danan\'': 'నందనం',
            'kautukan\'': 'కౌతుకం',
            'Harinarayan Apte': 'హరినరయన్ అప్తె',
            'Karandikar M.E.': 'కరన్దికర్ మ్.ఎ.',
            'aan\'dhrulaku pund-ya kshheitramu': 'ఆంధ్రులకు పుణ్య క్షేత్రము',
            'shaivaaya:': 'శైవాయః',
            'vidyuchchhakti': 'విద్యుచ్ఛక్తి',
            'patrashreishht\'amu': 'పత్రశ్రేష్టము',
            'dussvapnamu': 'దుస్స్వప్నము',
            'shleishhmajyooshht\'amu': 'శ్లేష్మజ్యోష్టము',
            'and-vastramu': 'అణ్వస్త్రము',
            # 'Vein\'kat\'a':'వేంకట',
            '.': '.',
            ',': ',', '?': '?', '0': '0', '1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6', '7': '7',
            '8': '8', '9': '9', ';': ';', '-': '-', '\\': '\\', '<': '<',
            '>': '>', '/': '/', '[': '[',
            ']': ']', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%',
            '^': '^', '&': '&', '*': '*',
            '(': '(', ')': ')',
            # '_':'_',
            '+': '+', '|': '|'
        }

        utf_con = IT3C(order='it32utf', lang=lang)

        for item in telmap.keys():
            exp_text = telmap.get(item)
            conv_text = utf_con.convert(item)
            self.assertEqual(conv_text, exp_text)
