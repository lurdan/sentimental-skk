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



class MouseMode():

    protocol = 0
    encoding = 0

    def set_on(self, s):
        s.write(u"\x1b[?1000h")
        s.write(u"\x1b[?1002h")
        s.write(u"\x1b[?1003h")
        s.write(u"\x1b[?1015h")
        s.write(u"\x1b[?1006h")

    def set_off(self, s):
        if self.protocol == 0:
            s.write(u"\x1b[?1000l")
        else:
            s.writestring(u"\x1b[?%dl" % self.protocol)
            if self.encoding != 0:
                s.writestring(u"\x1b[?%dl" % self.encoding)


def test():
    import StringIO
    s = StringIO.StringIO()
    mouse_mode = MouseMode()
    mouse_mode.set_on(s)
    print s.getvalue().replace("\x1b", "<ESC>")
    s.truncate(0)
    mouse_mode.set_on(s)
    print s.getvalue().replace("\x1b", "<ESC>")
    s.truncate(0)

if __name__ == "__main__":
    print "MouseMode test."
    test()
