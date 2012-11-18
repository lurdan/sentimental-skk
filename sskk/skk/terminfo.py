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

import curses

curses.setupterm()

sc = curses.tigetstr('sc')
if sc is None:
    sc = u'\x1b7'

rc = curses.tigetstr('rc')
if rc is None:
    rc = u'\x1b8'

civis = curses.tigetstr('civis')
if civis is None:
    civis = u'\x1b[?25l'
 
cvvis = curses.tigetstr('cvvis')
if cvvis is None:
    cvvis = u'\x1b[?25h'

sgr0 = curses.tigetstr('sgr0')
if sgr0 is None:
    sgr0 = u'\x1b[0;10m'

setab = curses.tigetstr('setab')
if setab is None:
    setab = u'\x1b[4%p1%dm'

setaf = curses.tigetstr('setaf')
if setaf is None:
    setaf = u'\x1b[3%p1%dm'
