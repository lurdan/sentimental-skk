#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ***** BEGIN LICENSE BLOCK *****
# Copyright (C) 2012  Hayaki Saito <user@zuse.jp>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ***** END LICENSE BLOCK *****

import kanadb
import logging

_rule_normal = {'a': u'あ',
                'i': u'い',
                'u': u'う',
                'e': u'え',
                'o': u'お',
                'xa': u'ぁ',
                'xi': u'ぃ',
                'xu': u'ぅ',
                'xe': u'ぇ',
                'xo': u'ぉ',
                'va': u'う゛ぁ',
                'vi': u'う゛ぃ',
                'vu': u'う゛',
                've': u'う゛ぇ',
                'vo': u'う゛ぉ',
                'ka': u'か',
                'ki': u'き',
                'ku': u'く',
                'ke': u'け',
                'ko': u'こ',
                'ga': u'が',
                'gi': u'ぎ',
                'gu': u'ぐ',
                'ge': u'げ',
                'go': u'ご',
                'kya': u'きゃ',
                'kyi': u'きぃ',
                'kyu': u'きゅ',
                'kye': u'きぇ',
                'kyo': u'きょ',
                'gya': u'ぎゃ',
                'gyi': u'ぎぃ',
                'gyu': u'ぎゅ',
                'gye': u'ぎぇ',
                'gyo': u'ぎょ',
                'sa': u'さ',
                'si': u'し',
                'su': u'す',
                'se': u'せ',
                'so': u'そ',
                'za': u'ざ',
                'zi': u'じ',
                'zu': u'ず',
                'ze': u'ぜ',
                'zo': u'ぞ',
                'sya': u'しゃ',
                'syi': u'しぃ',
                'syu': u'しゅ',
                'sye': u'しぇ',
                'syo': u'しょ',
                'sha': u'しゃ',
                'shi': u'し',
                'shu': u'しゅ',
                'she': u'しぇ',
                'sho': u'しょ',
                'ja': u'じゃ',
                'ji': u'じ',
                'ju': u'じゅ',
                'je': u'じぇ',
                'jo': u'じょ',
                'jya': u'じゃ',
                'jyi': u'じぃ',
                'jyu': u'じゅ',
                'jye': u'じぇ',
                'jyo': u'じょ',
                'zya': u'じゃ',
                'zyi': u'じぃ',
                'zyu': u'じゅ',
                'zye': u'じぇ',
                'zyo': u'じょ',
                'ta': u'た',
                'ti': u'ち',
                'tu': u'つ',
                'te': u'て',
                'to': u'と',
                'da': u'だ',
                'di': u'ぢ',
                'du': u'づ',
                'de': u'で',
                'do': u'ど',
                'cha': u'ちゃ',
                'chi': u'ち',
                'chu': u'ちゅ',
                'che': u'ちぇ',
                'cho': u'ちょ',
                'tya': u'ちゃ',
                'tyi': u'ちぃ',
                'tyu': u'ちゅ',
                'tye': u'ちぇ',
                'tyo': u'ちょ',
                'tha': u'てぁ',
                'thi': u'てぃ',
                'thu': u'てゅ',
                'the': u'てぇ',
                'tho': u'てょ',
                'dya': u'ぢゃ',
                'dyi': u'ぢぃ',
                'dyu': u'ぢゅ',
                'dye': u'ぢぇ',
                'dyo': u'ぢょ',
                'dha': u'でゃ',
                'dhi': u'でぃ',
                'dhu': u'でゅ',
                'dhe': u'でぇ',
                'dho': u'でょ',
                'na': u'な',
                'ni': u'に',
                'nu': u'ぬ',
                'ne': u'ね',
                'no': u'の',
                'nya': u'にゃ',
                'nyi': u'にぃ',
                'nyu': u'にゅ',
                'nye': u'にぇ',
                'nyo': u'にょ',
                'ha': u'は',
                'hi': u'ひ',
                'hu': u'ふ',
                'he': u'へ',
                'ho': u'ほ',
                'pa': u'ぱ',
                'pi': u'ぴ',
                'pu': u'ぷ',
                'pe': u'ぺ',
                'po': u'ぽ',
                'ba': u'ば',
                'bi': u'び',
                'bu': u'ぶ',
                'be': u'べ',
                'bo': u'ぼ',
                'fa': u'ふぁ',
                'fi': u'ふぃ',
                'fu': u'ふ',
                'fe': u'ふぇ',
                'fo': u'ふぉ',
                'hya': u'ひゃ',
                'hyi': u'ひぃ',
                'hyu': u'ひゅ',
                'hye': u'ひぇ',
                'hyo': u'ひょ',
                'fya': u'ふゃ',
                'fyi': u'ふぃ',
                'fyu': u'ふゅ',
                'fye': u'ふぇ',
                'fyo': u'ふょ',
                'bya': u'びゃ',
                'byi': u'びぃ',
                'byu': u'びゅ',
                'bye': u'びぇ',
                'byo': u'びょ',
                'pya': u'ぴゃ',
                'pyi': u'ぴぃ',
                'pyu': u'ぴゅ',
                'pye': u'ぴぇ',
                'pyo': u'ぴょ',
                'ma': u'ま',
                'mi': u'み',
                'mu': u'む',
                'me': u'め',
                'mo': u'も',
                'mya': u'みゃ',
                'myi': u'みぃ',
                'myu': u'みゅ',
                'mye': u'みぇ',
                'myo': u'みょ',
                'ya': u'や',
                'yi': u'い',
                'yu': u'ゆ',
                'ye': u'いぇ',
                'yo': u'よ',
                'ra': u'ら',
                'ri': u'り',
                'ru': u'る',
                're': u'れ',
                'ro': u'ろ',
                'rya': u'りゃ',
                'ryi': u'りぃ',
                'ryu': u'りゅ',
                'rye': u'りぇ',
                'ryo': u'りょ',
                'wa': u'わ',
                'wi': u'うぃ',
                'wu': u'う',
                'we': u'うぇ',
                'wo': u'を',
                'nn': u'ん',
                'tsu': u'つ',
                'xtu': u'っ',
                'xtsu': u'っ',
                '-': u'ー',
                ',': u'、',
                '.': u'。',
                'z:': u'：',
                'z;': u'；',
                'zh': u'←',
                'zj': u'↓',
                'zk': u'↑',
                'zl': u'→',
                'z-': u'〜',
                'z,': u'‥',
                'z.': u'…',
                'z/': u'・',
                'z[': u'『',
                'z]': u'』',
                'z?': u'？',
                'z(': u'（',
                'z)': u'）',
                'z{': u'【',
                'z}': u'】',
                'zL': u'⇒',
                'z ': u'　',
                '[': u'「',
                ']': u'」',
                ':': u'：',
                ';': u'；'}


_rule_azik = {'a': u'あ',
              'i': u'い',
              'u': u'う',
              'e': u'え',
              'o': u'お',
              'va': u'う゛ぁ',
              'vi': u'う゛ぃ',
              'vu': u'う゛',
              've': u'う゛ぇ',
              'vo': u'う゛ぉ',
              'ka': u'か',
              'ki': u'き',
              'ku': u'く',
              'ke': u'け',
              'ko': u'こ',
              'ga': u'が',
              'gi': u'ぎ',
              'gu': u'ぐ',
              'ge': u'げ',
              'go': u'ご',
              'kya': u'きゃ',
              'kyi': u'きぃ',
              'kyu': u'きゅ',
              'kye': u'きぇ',
              'kyo': u'きょ',
              'gya': u'ぎゃ',
              'gyi': u'ぎぃ',
              'gyu': u'ぎゅ',
              'gye': u'ぎぇ',
              'gyo': u'ぎょ',
              'sa': u'さ',
              'si': u'し',
              'su': u'す',
              'se': u'せ',
              'so': u'そ',
              'za': u'ざ',
              'zi': u'じ',
              'zu': u'ず',
              'ze': u'ぜ',
              'zo': u'ぞ',
              'xa': u'しゃ',
              'xi': u'し',
              'xu': u'しゅ',
              'xe': u'しぇ',
              'xo': u'しょ',
              'sya': u'しゃ',
              'syi': u'しぃ',
              'syu': u'しゅ',
              'sye': u'しぇ',
              'syo': u'しょ',
              'ja': u'じゃ',
              'ji': u'じ',
              'ju': u'じゅ',
              'je': u'じぇ',
              'jo': u'じょ',
              'jya': u'じゃ',
              'jyi': u'じぃ',
              'jyu': u'じゅ',
              'jye': u'じぇ',
              'jyo': u'じょ',
              'zya': u'じゃ',
              'zyi': u'じぃ',
              'zyu': u'じゅ',
              'zye': u'じぇ',
              'zyo': u'じょ',
              'ta': u'た',
              'ti': u'ち',
              'tu': u'つ',
              'te': u'て',
              'to': u'と',
              'da': u'だ',
              'di': u'ぢ',
              'du': u'づ',
              'de': u'で',
              'do': u'ど',
              'cha': u'ちゃ',
              'chi': u'ち',
              'chu': u'ちゅ',
              'che': u'ちぇ',
              'cho': u'ちょ',
              'tya': u'ちゃ',
              'tyi': u'ちぃ',
              'tyu': u'ちゅ',
              'tye': u'ちぇ',
              'tyo': u'ちょ',
              'tha': u'てぁ',
              'thi': u'てぃ',
              'thu': u'てゅ',
              'the': u'てぇ',
              'tho': u'てょ',
              'dya': u'ぢゃ',
              'dyi': u'ぢぃ',
              'dyu': u'ぢゅ',
              'dye': u'ぢぇ',
              'dyo': u'ぢょ',
              'dha': u'でゃ',
              'dhi': u'でぃ',
              'dhu': u'でゅ',
              'dhe': u'でぇ',
              'dho': u'でょ',
              'na': u'な',
              'ni': u'に',
              'nu': u'ぬ',
              'ne': u'ね',
              'no': u'の',
              'nya': u'にゃ',
              'nyi': u'にぃ',
              'nyu': u'にゅ',
              'nye': u'にぇ',
              'nyo': u'にょ',
              'ha': u'は',
              'hi': u'ひ',
              'hu': u'ふ',
              'he': u'へ',
              'ho': u'ほ',
              'pa': u'ぱ',
              'pi': u'ぴ',
              'pu': u'ぷ',
              'pe': u'ぺ',
              'po': u'ぽ',
              'ba': u'ば',
              'bi': u'び',
              'bu': u'ぶ',
              'be': u'べ',
              'bo': u'ぼ',
              'fa': u'ふぁ',
              'fi': u'ふぃ',
              'fu': u'ふ',
              'fe': u'ふぇ',
              'fo': u'ふぉ',
              'hya': u'ひゃ',
              'hyi': u'ひぃ',
              'hyu': u'ひゅ',
              'hye': u'ひぇ',
              'hyo': u'ひょ',
              'fya': u'ふゃ',
              'fyi': u'ふぃ',
              'fyu': u'ふゅ',
              'fye': u'ふぇ',
              'fyo': u'ふょ',
              'bya': u'びゃ',
              'byi': u'びぃ',
              'byu': u'びゅ',
              'bye': u'びぇ',
              'byo': u'びょ',
              'pya': u'ぴゃ',
              'pyi': u'ぴぃ',
              'pyu': u'ぴゅ',
              'pye': u'ぴぇ',
              'pyo': u'ぴょ',
              'ma': u'ま',
              'mi': u'み',
              'mu': u'む',
              'me': u'め',
              'mo': u'も',
              'mya': u'みゃ',
              'myi': u'みぃ',
              'myu': u'みゅ',
              'mye': u'みぇ',
              'myo': u'みょ',
              'ya': u'や',
              'yi': u'い',
              'yu': u'ゆ',
              'ye': u'いぇ',
              'yo': u'よ',
              'ra': u'ら',
              'ri': u'り',
              'ru': u'る',
              're': u'れ',
              'ro': u'ろ',
              'rya': u'りゃ',
              'ryi': u'りぃ',
              'ryu': u'りゅ',
              'rye': u'りぇ',
              'ryo': u'りょ',
              'wa': u'わ',
              'wi': u'うぃ',
              'wu': u'う',
              'we': u'うぇ',
              'wo': u'を',
              'nn': u'ん',
              'tsu': u'つ',
              'xtu': u'っ',
              'xtsu': u'っ',
              'x;': u';',
              '-': u'ー',
              ',': u'、',
              '.': u'。',
              'z:': u'：',
              'z;': u'；',
              'zh': u'←',
              'zj': u'↓',
              'zk': u'↑',
              'zl': u'→',
              'z-': u'〜',
              'z,': u'‥',
              'z.': u'…',
              'z/': u'・',
              'z[': u'『',
              'z]': u'』',
              'z?': u'？',
              'z(': u'（',
              'z)': u'）',
              'z{': u'【',
              'z}': u'】',
              'zL': u'⇒',
              'z ': u'　',
              '[': u'「',
              ']': u'」',
              ':': u'：',
              ';': u'っ',
              'bd': u'べん',
              'bh': u'ぶう',
              'bj': u'ぶん',
              'bk': u'びん',
              'bl': u'ぼん',
              'bn': u'ばん',
              'bp': u'ぼう',
              'bq': u'ばい',
              'br': u'ばら',
              'bt': u'びと',
              'bw': u'べい',
              'bx': u'べい',
              'byd': u'びぇん',
              'byh': u'びゅう',
              'byj': u'びゅん',
              'byl': u'びょん',
              'byn': u'びゃん',
              'byp': u'びょう',
              'byq': u'びゃい',
              'byw': u'びぇい',
              'byz': u'びゃん',
              'bz': u'ばん',
              'ca': u'ちゃ',
              'cc': u'ちゃ',
              'cd': u'ちぇん',
              'ce': u'ちぇ',
              'cf': u'ちぇ',
              'ch': u'ちゅう',
              'ci': u'ち',
              'cj': u'ちゅん',
              'ck': u'ちん',
              'cl': u'ちょん',
              'cn': u'ちゃん',
              'co': u'ちょ',
              'cp': u'ちょう',
              'cq': u'ちゃい',
              'cu': u'ちゅ',
              'cv': u'ちゃい',
              'cw': u'ちぇい',
              'cx': u'ちぇい',
              'cz': u'ちゃん',
              'dch': u'でゅー',
              'dci': u'でぃ',
              'dck': u'でぃん',
              'dcp': u'どぅー',
              'dcu': u'でゅ',
              'dd': u'でん',
              'df': u'で',
              'dg': u'だが',
              'dh': u'づう',
              'dj': u'づん',
              'dk': u'ぢん',
              'dl': u'どん',
              'dm': u'でも',
              'dn': u'だん',
              'dp': u'どう',
              'dq': u'だい',
              'dr': u'である',
              'ds': u'です',
              'dt': u'だち',
              'dv': u'でん',
              'dw': u'でい',
              'dy': u'でぃ',
              'dz': u'だん',
              'fd': u'ふぇん',
              'fh': u'ふう',
              'fj': u'ふん',
              'fk': u'ふぃん',
              'fl': u'ふぉん',
              'fm': u'ふむ',
              'fn': u'ふぁん',
              'fp': u'ふぉー',
              'fq': u'ふぁい',
              'fr': u'ふる',
              'fs': u'ふぁい',
              'fw': u'ふぇい',
              'fz': u'ふぁん',
              'gd': u'げん',
              'gh': u'ぐう',
              'gj': u'ぐん',
              'gk': u'ぎん',
              'gl': u'ごん',
              'gn': u'がん',
              'gp': u'ごう',
              'gq': u'がい',
              'gr': u'がら',
              'gt': u'ごと',
              'gw': u'げい',
              'gyd': u'ぎぇん',
              'gyh': u'ぎゅう',
              'gyj': u'ぎゅん',
              'gyl': u'ぎょん',
              'gyn': u'ぎゃん',
              'gyp': u'ぎょう',
              'gyq': u'ぎゃい',
              'gyw': u'ぎぇい',
              'gyz': u'ぎゃん',
              'gz': u'がん',
              'hd': u'へん',
              'hf': u'ふ',
              'hga': u'ひゃ',
              'hgd': u'ひぇん',
              'hge': u'ひぇ',
              'hgh': u'ひゅう',
              'hgj': u'ひゅん',
              'hgl': u'ひょん',
              'hgn': u'ひゃん',
              'hgo': u'ひょ',
              'hgp': u'ひょう',
              'hgq': u'ひゃい',
              'hgu': u'ひゅ',
              'hgw': u'ひぇい',
              'hgz': u'ひゃん',
              'hh': u'ふう',
              'hj': u'ふん',
              'hk': u'ひん',
              'hl': u'ほん',
              'hn': u'はん',
              'hp': u'ほう',
              'hq': u'はい',
              'ht': u'ひと',
              'hw': u'へい',
              'hyd': u'ひぇん',
              'hyh': u'ひゅう',
              'hyl': u'ひょん',
              'hyp': u'ひょう',
              'hyq': u'ひゃい',
              'hyw': u'ひぇい',
              'hyz': u'ひゃん',
              'hz': u'はん',
              'jd': u'じぇん',
              'jf': u'じゅ',
              'jh': u'じゅう',
              'jj': u'じゅん',
              'jk': u'じん',
              'jl': u'じょん',
              'jn': u'じゃん',
              'jp': u'じょう',
              'jq': u'じゃい',
              'jv': u'じゅう',
              'jw': u'じぇい',
              'jz': u'じゃん',
              'kA': u'ヵ',
              'kE': u'ヶ',
              'kd': u'けん',
              'kf': u'き',
              'kga': u'きゃ',
              'kgd': u'きぇん',
              'kge': u'きぇ',
              'kgh': u'きゅう',
              'kgl': u'きょん',
              'kgn': u'きゃん',
              'kgo': u'きょ',
              'kgp': u'きょう',
              'kgq': u'きゃい',
              'kgu': u'きゅ',
              'kgw': u'きぇい',
              'kgz': u'きゃん',
              'kh': u'くう',
              'kj': u'くん',
              'kk': u'きん',
              'kl': u'こん',
              'km': u'かも',
              'kn': u'かん',
              'kp': u'こう',
              'kq': u'かい',
              'kr': u'から',
              'kt': u'こと',
              'kv': u'きん',
              'kw': u'けい',
              'kyd': u'きぇん',
              'kyh': u'きゅう',
              'kyj': u'きゅん',
              'kyl': u'きょん',
              'kyn': u'きゃん',
              'kyp': u'きょう',
              'kyq': u'きゃい',
              'kyw': u'きぇい',
              'kyz': u'きゃん',
              'kz': u'かん',
              'md': u'めん',
              'mf': u'む',
              'mga': u'みゃ',
              'mgd': u'みぇん',
              'mge': u'みぇ',
              'mgh': u'みゅう',
              'mgj': u'みゅん',
              'mgl': u'みょん',
              'mgn': u'みゃん',
              'mgo': u'みょ',
              'mgp': u'みょう',
              'mgq': u'みゃい',
              'mgu': u'みゅ',
              'mgw': u'みぇい',
              'mgz': u'みゃん',
              'mh': u'むう',
              'mj': u'むん',
              'mk': u'みん',
              'ml': u'もん',
              'mn': u'もの',
              'mp': u'もう',
              'mq': u'まい',
              'mr': u'まる',
              'ms': u'ます',
              'mt': u'また',
              'mv': u'むん',
              'mw': u'めい',
              'myd': u'みぇん',
              'myh': u'みゅう',
              'myj': u'みゅん',
              'myl': u'みょん',
              'myn': u'みゃん',
              'myp': u'みょう',
              'myq': u'みゃい',
              'myw': u'みぇい',
              'myz': u'みゃん',
              'mz': u'まん',
              'nb': u'ねば',
              'nd': u'ねん',
              'nf': u'ぬ',
              'nga': u'にゃ',
              'ngd': u'にぇん',
              'nge': u'にぇ',
              'ngh': u'にゅう',
              'ngj': u'にゅん',
              'ngl': u'にょん',
              'ngn': u'にゃん',
              'ngo': u'にょ',
              'ngp': u'にょう',
              'ngq': u'にゃい',
              'ngu': u'にゅ',
              'ngw': u'にぇい',
              'ngz': u'にゃん',
              'nh': u'ぬう',
              'nj': u'ぬん',
              'nk': u'にん',
              'nl': u'のん',
              'np': u'のう',
              'nq': u'ない',
              'nr': u'なる',
              'nt': u'にち',
              'nv': u'ぬん',
              'nw': u'ねい',
              'nyd': u'にぇん',
              'nyh': u'にゅう',
              'nyj': u'にゅん',
              'nyl': u'にょん',
              'nyn': u'にゃん',
              'nyp': u'にょう',
              'nyq': u'にゃい',
              'nyw': u'にぇい',
              'nyz': u'にゃん',
              'nz': u'なん',
              'pd': u'ぺん',
              'pf': u'ぽん',
              'pga': u'ぴゃ',
              'pgd': u'ぴぇん',
              'pge': u'ぴぇ',
              'pgh': u'ぴゅう',
              'pgj': u'ぴゅん',
              'pgl': u'ぴょん',
              'pgn': u'ぴゃん',
              'pgo': u'ぴょ',
              'pgp': u'ぴょう',
              'pgq': u'ぴゃい',
              'pgu': u'ぴゅ',
              'pgw': u'ぴぇい',
              'pgz': u'ぴゃん',
              'ph': u'ぷう',
              'pj': u'ぷん',
              'pk': u'ぴん',
              'pl': u'ぽん',
              'pn': u'ぱん',
              'pp': u'ぽう',
              'pq': u'ぱい',
              'pv': u'ぽう',
              'pw': u'ぺい',
              'pyd': u'ぴぇん',
              'pyh': u'ぴゅう',
              'pyj': u'ぴゅん',
              'pyl': u'ぴょん',
              'pyn': u'ぴゃん',
              'pyp': u'ぴょう',
              'pyq': u'ぴゃい',
              'pyw': u'ぴぇい',
              'pyz': u'ぴゃん',
              'pz': u'ぱん',
              'q': u'ん',
              'rd': u'れん',
              'rh': u'るう',
              'rj': u'るん',
              'rk': u'りん',
              'rl': u'ろん',
              'rn': u'らん',
              'rp': u'ろう',
              'rq': u'らい',
              'rr': u'られ',
              'rw': u'れい',
              'ryd': u'りぇん',
              'ryh': u'りゅう',
              'ryj': u'りゅん',
              'ryk': u'りょく',
              'ryl': u'りょん',
              'ryn': u'りゃん',
              'ryp': u'りょう',
              'ryq': u'りゃい',
              'ryw': u'りぇい',
              'ryz': u'りゃん',
              'rz': u'らん',
              'sd': u'せん',
              'sf': u'さい',
              'sh': u'すう',
              'sj': u'すん',
              'sk': u'しん',
              'sl': u'そん',
              'sm': u'しも',
              'sn': u'さん',
              'sp': u'そう',
              'sq': u'さい',
              'sr': u'する',
              'ss': u'せい',
              'st': u'した',
              'sv': u'さい',
              'sw': u'せい',
              'syd': u'しぇん',
              'syh': u'しゅう',
              'syj': u'しゅん',
              'syl': u'しょん',
              'syp': u'しょう',
              'syq': u'しゃい',
              'syw': u'しぇい',
              'syz': u'しゃん',
              'sz': u'さん',
              'tU': u'っ',
              'tb': u'たび',
              'td': u'てん',
              'tgh': u'てゅー',
              'tgi': u'てぃ',
              'tgk': u'てぃん',
              'tgp': u'とぅー',
              'tgu': u'てゅ',
              'th': u'つう',
              'tj': u'つん',
              'tk': u'ちん',
              'tl': u'とん',
              'tm': u'ため',
              'tn': u'たん',
              'tp': u'とう',
              'tq': u'たい',
              'tr': u'たら',
              'tsU': u'っ',
              'tsa': u'つぁ',
              'tse': u'つぇ',
              'tsi': u'つぃ',
              'tso': u'つぉ',
              'tt': u'たち',
              'tw': u'てい',
              'tyd': u'ちぇん',
              'tyh': u'ちゅう',
              'tyj': u'ちゅん',
              'tyl': u'ちょん',
              'tyn': u'ちゃん',
              'typ': u'ちょう',
              'tyq': u'ちゃい',
              'tyw': u'ちぇい',
              'tyz': u'ちゃん',
              'tz': u'たん',
              'vd': u'う゛ぇん',
              'vk': u'う゛ぃん',
              'vl': u'う゛ぉん',
              'vn': u'う゛ぁん',
              'vp': u'う゛ぉー',
              'vq': u'う゛ぁい',
              'vw': u'う゛ぇい',
              'vya': u'う゛ゃ',
              'vye': u'う゛ぇ',
              'vyo': u'う゛ょ',
              'vyu': u'う゛ゅ',
              'vz': u'う゛ぁん',
              'wA': u'ゎ',
              'wd': u'うぇん',
              'wf': u'わい',
              'wha': u'うぁ',
              'whe': u'うぇ',
              'whi': u'うぃ',
              'who': u'うぉ',
              'whu': u'う',
              'wk': u'うぃん',
              'wl': u'うぉん',
              'wn': u'わん',
              'wp': u'うぉー',
              'wq': u'わい',
              'wr': u'われ',
              'wso': u'うぉ',
              'wt': u'わた',
              'wz': u'わん',
              'xa': u'しゃ',
              'xc': u'しゃ',
              'xd': u'しぇん',
              'xe': u'しぇ',
              'xf': u'しぇい',
              'xh': u'しゅう',
              'xi': u'し',
              'xj': u'しゅん',
              'xk': u'しん',
              'xl': u'しょん',
              'xn': u'しゃん',
              'xo': u'しょ',
              'xp': u'しょう',
              'xq': u'しゃい',
              'xt': u'しゅつ',
              'xu': u'しゅ',
              'xv': u'しゃい',
              'xw': u'しぇい',
              'xxa': u'ぁ',
              'xxe': u'ぇ',
              'xxi': u'ぃ',
              'xxo': u'ぉ',
              'xxu': u'ぅ',
              'xxh': u'←',
              'xxj': u'↓',
              'xxk': u'↑',
              'xxl': u'→',
              'xz': u'しゃん',
              'y<': u'←',
              'y>': u'→',
              'y^': u'↑',
              'yf': u'ゆ',
              'yh': u'ゆう',
              'yi': u'ゐ',
              'yj': u'ゆん',
              'yl': u'よん',
              'yn': u'やん',
              'yp': u'よう',
              'yq': u'やい',
              'yr': u'よる',
              'yv': u'ゆう',
              'yz': u'やん',
              'zc': u'ざ',
              'zd': u'ぜん',
              'zf': u'ぜ',
              'zh': u'ずう',
              'zj': u'ずん',
              'zk': u'じん',
              'zl': u'ぞん',
              'zn': u'ざん',
              'zp': u'ぞう',
              'zq': u'ざい',
              'zr': u'ざる',
              'zv': u'ざい',
              'zw': u'ぜい',
              'zx': u'ぜい',
              'zyd': u'じぇん',
              'zyh': u'じゅう',
              'zyj': u'じゅん',
              'zyl': u'じょん',
              'zyn': u'じゃん',
              'zyp': u'じょう',
              'zyq': u'じゃい',
              'zyw': u'じぇい',
              'zyz': u'じゃん',
              'zz': u'ざん'}

SKK_ROMAN_VALUE = 0
SKK_ROMAN_NEXT = 1
SKK_ROMAN_PREV = 2
SKK_ROMAN_BUFFER = 3


def _maketree(rule, s):
    """ makes try-tree """
    tree = {}
    for key, value in rule.items():
        buf = u''
        context = tree
        for code in [ord(c) for c in key]:
            if not code in context:
                context[code] = {SKK_ROMAN_PREV: context}
            context = context[code]
            buf += chr(code)
            context[SKK_ROMAN_BUFFER] = buf
        context[SKK_ROMAN_VALUE] = value
        first = key[0]
        if first in s:
            key = first + key
            value = rule['xtu'] + value
            buf = u''
            context = tree
            for code in [ord(c) for c in key]:
                if not code in context:
                    context[code] = {SKK_ROMAN_PREV: context}
                context = context[code]
                if buf == chr(code):
                    buf = rule['xtu']
                buf += chr(code)
                context[SKK_ROMAN_BUFFER] = buf

            context[SKK_ROMAN_VALUE] = value

    for key, value in tree.items():
        context = tree
        if key == 0x6e:  # 'n'
            for code in [ord(c) for c in s]:
                value[code] = {SKK_ROMAN_VALUE: rule['nn'],
                               SKK_ROMAN_NEXT: tree[code]}
    tree[SKK_ROMAN_BUFFER] = ''
    tree[SKK_ROMAN_PREV] = tree
    return tree


def compile_normal():
    ''' make hiragana/katakana input state trie-tree
    >>> t = makekatatree()
    >>> t[ord('k')][ord('y')][ord('a')][SKK_ROMAN_VALUE]
    u'\u30ad\u30e3'
    >>> t = makehiratree()
    >>> t[ord('k')][ord('y')][ord('a')][SKK_ROMAN_VALUE]
    u'\u304d\u3083'
    '''
    hira_rule = _rule_normal
    kata_rule = {}
    for key, value in hira_rule.items():
        kata_rule[key] = kanadb.to_kata(value)

    _hira_tree = _maketree(hira_rule, 'bcdfghjkmprstvwxz')
    _kata_tree = _maketree(kata_rule, 'bcdfghjkmprstvwxz')
    return (_hira_tree, _kata_tree)


def compile_azik():
    ''' make hiragana/katakana input state trie-tree
    >>> t = makekatatree()
    >>> t[ord('k')][ord('y')][ord('a')][SKK_ROMAN_VALUE]
    u'\u30ad\u30e3'
    >>> t = makehiratree()
    >>> t[ord('k')][ord('y')][ord('a')][SKK_ROMAN_VALUE]
    u'\u304d\u3083'
    '''
    hira_rule = _rule_azik
    kata_rule = {}
    for key, value in hira_rule.items():
        kata_rule[key] = kanadb.to_kata(value)

    _hira_tree = _maketree(hira_rule, 'bcdfghjkmprstvwxz')
    _kata_tree = _maketree(kata_rule, 'bcdfghjkmprstvwxz')
    #_hira_tree = _maketree(hira_rule, 'w')
    #_kata_tree = _maketree(kata_rule, 'w')
    return (_hira_tree, _kata_tree)


def compile(method="normal"):
    if method == "azik":
        return compile_azik()
    elif method == "normal":
        return compile_normal()
    elif method is None:
        return compile_normal()
    else:
        logging.warning("Unknown Roman Rule: " + method)

def test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test()
