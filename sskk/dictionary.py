#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ***** BEGIN LICENSE BLOCK *****
# Copyright (C) 2012-2013  Hayaki Saito <user@zuse.jp>
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

import os
import thread
import inspect
import re
import logging

_TIMEOUT = 1.0

homedir = os.path.expanduser('~')
rcdir = os.path.join(homedir, '.sskk')
dictdir = os.path.join(rcdir, 'dict')
if not os.path.exists(dictdir):
    os.makedirs(dictdir)

_userdb = {}
_tangodb = {}
_okuridb = {}
_compdb = {}
_encoding = 0
_encoding_list = [u'eucjp', u'utf-8']

def _register(db, key, value):
    current = db
    for c in key:
        if c in current:
            current = current[c]
        else:
            new_current = {}
            current[c] = new_current
            current = new_current

_control_chars = re.compile('[\x00-\x1f\x7f\x80-\x9f\xff]')

def feedback(key, value):
    _register(_compdb, key, value)
    if key in _userdb:
        _userdb[key].append(value)
    else:
        _userdb[key] = [value]

def _escape(s):
    '''
    >>> _escape('abc')
    'abc'
    >>> _escape('lda\\x1baa\x10laa')
    'ldaaalaa'
    '''
    return _control_chars.sub('', s)


def _decode_line(line):
    global _encoding
    try:
        return unicode(line, _encoding_list[_encoding])
    except:
        _encoding = 1 - _encoding # flip
    return unicode(line, _encoding_list[_encoding])


def _load_dict(filename):
    p = re.compile('^(?:([0-9a-z.]+?)|(.+?)([a-z])?) /(.+)/')

    try:
        for line in open(filename):
            if len(line) < 4 or line[1] == ';':
                continue
            line = _decode_line(line)
            match = p.match(line)
            if not match:
                template = '_load_dict: can\'t load the entry: %s'
                logging.message(template % line)
            alphakey, key, okuri, value = match.groups()
            if key:
                if okuri:
                    key += okuri
                else:
                    _register(_compdb, key, value)
                if key in _tangodb:
                    _tangodb[key] += value.split('/')
                else:
                    _tangodb[key] = value.split('/')
            else:
                _register(_compdb, alphakey, value)
                if alphakey in _tangodb:
                    _tangodb[alphakey] += value.split('/')
                else:
                    _tangodb[alphakey] = value.split('/')
    except:
        template = '_load_dict: loading process failed. filename: %s'
        logging.exception(template % filename)


def _get_fallback_dict_path(name):
    filename = inspect.getfile(inspect.currentframe())
    dirpath = os.path.abspath(os.path.dirname(filename))
    return os.path.join(dirpath, name)


def _load():
    dict_list = os.listdir(dictdir)
    _load_dict(_get_fallback_dict_path('SKK-JISYO.builtin'))
    _load_dict(_get_fallback_dict_path('SKK-JISYO.L'))
    _load_dict(_get_fallback_dict_path('SKK-JISYO.JIS2'))
    _load_dict(_get_fallback_dict_path('SKK-JISYO.assoc'))
    _load_dict(_get_fallback_dict_path('SKK-JISYO.geo'))
    _load_dict(_get_fallback_dict_path('SKK-JISYO.jinmei'))
    if dict_list:
        for f in dict_list:
            _load_dict(os.path.join(dictdir, f))


def gettango(key):
    result = set()
    if key in _userdb:
        result.update(_userdb[key])
    if key in _tangodb:
        result.update(_tangodb[key])
    return result


def getokuri(key):
    if key in _tangodb:
        return _tangodb[key]
    return None

def _expand_all(key, current, candidate):
    for c, value in current:
        if value == {}:
            candidate.append(key + c)
        else:
            _expand_all(key + c, (x for x in value.items()), candidate)

def _expand_sparse(key, current, candidate, generators):
    for c, value in current:
        if value == {}:
            candidate.append(key + c)
            return True
        generator = (x for x in value.items())
        if _expand_sparse(key + c, generator, candidate, generators):
            generators.append((key, current))
            return True
    return False

def _expand(key, current, candidate):
    generators = []
    for c in current:
        generator = (x for x in current[c].items())
        _expand_sparse(key + c, generator, candidate, generators)
        if len(candidate) > 10:
            break
    else:
        if len(candidate) < 10:
            for k, v in generators:
                _expand_all(k, v, candidate)
            if len(candidate) < 10:
                for c in current:
                    if current[c] == {}:
                        candidate.append(c)
            if current == {}:
                candidate.append(key)

def suggest(key, comp):

    _current = _compdb
    for _c in key:
        if _c in _current:
            _current = _current[_c]
        else:
            return None

    candidate = []
    if not comp:
        _expand(u'', _current, candidate)
    else:
        for _key in comp:
            key_len = len(_key)
            if key_len == 1:
                if _key in _current:
                    _expand(_key, _current[_key], candidate)
            elif key_len == 2:
                first, second = _key[0], _key[1]
                if first in _current:
                    if second in _current[first]:
                        _expand(_key, _current[first][second], candidate)
    return candidate


###############################################################################
#
# Clause
#
class Clause():

    def __init__(self, key, candidates):
        self._key = _escape(key)
        self._values = []
        self._remarks = []
        for candidate in candidates:
            row = candidate.split(';')
            if len(row) == 2:
                value, remark = row
            else:
                value, remark = candidate, u''
            self._values.append(_escape(value))
            self._remarks.append(_escape(remark))
        self._index = 0

    def getkey(self):
        return self._key

    def getcurrentvalue(self):
        return self._values[self._index]

    def getcurrentremark(self):
        return self._remarks[self._index]

    def getcandidates(self):
        return self._values

    def select(self, index):
        self._index = index


###############################################################################
#
# Clauses
#
class Clauses:

    def __init__(self):
        self._clauses = []
        self._index = 0

    def __iter__(self):
        for clause in self._clauses:
            yield clause

    def add(self, clause):
        self._clauses.append(clause)

    def getkey(self):
        word = u''
        for clause in self._clauses:
            word += clause.getkey()
        return word

    def length(self):
        return len(self._clauses)

    def getvalue(self):
        word = u''
        for clause in self._clauses:
            word += clause.getcurrentvalue()
        return word

    def getcurrentclause(self):
        return self._clauses[self._index]

    def getcurrentvalue(self):
        return self._clauses[self._index].getcurrentvalue()

    def getcurrentremark(self):
        return self._clauses[self._index].getcurrentremark()

    def getcandidates(self):
        return self._clauses[self._index].getcandidates()

    def select(self, index):
        self._index = index

    def movenext(self):
        self._index = (self._index + 1) % self.length()

    def moveprev(self):
        self._index = (self._index - 1) % self.length()

    def _retry_google(self, words):
        response = call_cgi_api(','.join(words))
        if response:
            self._clauses = []
            for clauseinfo in response:
                key, candidates = clauseinfo
                clause = Clause(key, candidates)
                self.add(clause)
            if self._index >= len(self._clauses):
                self._index = len(self._clauses) - 1

    def shift_left(self):

        words = []
        for clause in self._clauses:
            words.append(clause.getkey())

        index = self._index
        surplus = words[index][-1:] + ''.join(words[index + 1:])
        words[index] = words[index][:-1]
        words = words[0:index + 1] + [surplus]

        self._retry_google(words)

    def shift_right(self):

        words = []
        for clause in self._clauses:
            words.append(clause.getkey())

        index = self._index
        if index == len(words) - 1:
            words = words[:index] + [words[index][0], words[index][1:]]
        else:
            words[index] += words[index + 1][0]
            surplus = (''.join(words[index + 1:])[1:])
            words = words[:index + 1] + [surplus]

        self._retry_google(words)


def call_cgi_api(key):
    import json
    import urllib
    import urllib2
    params = urllib.urlencode({'langpair': 'ja-Hira|ja',
                               'text': key.encode('UTF-8')})
    escaped_params = str(params)
    url = 'http://www.google.com/transliterate?' + escaped_params
    try:
        response = urllib2.urlopen(url, None, 0.5)
        json_response = response.read()
        if not json_response:
            logging.exception('call_cgi_api failed. %s' % key)
            return None
        response = json.loads(json_response)
    except:
        logging.exception('call_cgi_api failed. key: %s' % key)
        return None
    return response


def get_from_google_cgi_api(clauses, key):
    response = call_cgi_api(key)
    if not response:
        return None
    try:
        for clauseinfo in response:
            key, candidates = clauseinfo
            clause = Clause(key, candidates)
            clauses.add(clause)
    except:
        logging.exception('get_from_google_cgi_api failed. key: %s' % key)
        return None
    return clauses

thread.start_new_thread(_load, ())
#_load()


def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
