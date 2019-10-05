# vim:set et sts=4 sw=4:
# -*- coding: utf-8 -*-
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2010-2017 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2007-2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys

from tables import *
import segment

def romaji_correction_rule_get(k, d):
    return ('ん', k[1:2]) if k[0:1] == 'n' and not k[1:2] in "aiueony'" else d

class RomajiSegment(segment.Segment):
    _prefs = None
    _romaji_typing_rule_method = None
    _latin_with_shift = True
    _shift_mode = False

    def __init__(self, enchars='', jachars='', shift=False, unshift=False):
        if self._latin_with_shift:
            # If Shift key is pressed, Latin mode.
            # If Hiragana_Katakana key is pressed, Hiragana mode.
            if shift:
                self._shift_mode = True
            if unshift:
                self._shift_mode = False

        enchars_orig = enchars
        # Even if the chars are capital with CapsLock, Hiragana
        # should be converted. E.g. 'SA'
        enchars = enchars.lower()

        if not jachars and not shift:
            jachars = self.__get_romaji_typing_rule(enchars, None)
            if jachars == None:
                jachars = symbol_rule.get(enchars, '')
        super(RomajiSegment, self).__init__(enchars_orig, jachars)

    @classmethod
    def INIT_ROMAJI_TYPING_RULE(cls, prefs):
        cls._prefs = prefs
        if prefs == None:
            cls._romaji_typing_rule_method = None
            return
        method = prefs.get_value('romaji-typing-rule', 'method')
        if method == None:
            method = 'default'
        cls._romaji_typing_rule_method = method
        keymap = prefs.get_value('romaji-typing-rule', 'list')
        if cls._romaji_typing_rule_method not in keymap.keys():
            cls._romaji_typing_rule_method = None

    @classmethod
    def SET_LATIN_WITH_SHIFT(cls, latin_with_shift):
        # Do not use IBus.Config in every conversion for the performance.
        cls._latin_with_shift = latin_with_shift

    def __get_romaji_typing_rule(self, enchars, retval=None):
        prefs = self._prefs
        value = None
        method = self._romaji_typing_rule_method
        if method != None:
            # Need to send Unicode to typing_to_config_key instead of UTF-8
            # not to separate U+A5
            gkey = prefs.typing_to_config_key(enchars)
            if gkey == '':
                return None
            keymap = prefs.get_value('romaji-typing-rule', 'list')[method]
            value = keymap.get(gkey)
            if value == '':
                value = None
            if value == None:
                value = retval 
        else:
            value = romaji_typing_rule_static.get(enchars, retval)
        return value

    def is_finished(self):
        return self._jachars != ''

    def append(self, enchar, shift=False, unshift=False):
        if self.is_finished():
            if enchar == '' and enchar == '\0':
                return []
            return [RomajiSegment(enchar)]

        text_orig = self._enchars + enchar
        text = text_orig.lower()

        if self._latin_with_shift:
            # If Shift key is pressed, Latin mode.
            # If Hiragana_Katakana key is pressed, Hiragana mode.
            if shift:
                self._shift_mode = True
            if unshift:
                self._shift_mode = False
            if self._shift_mode:
                self._enchars = text_orig
                return []

        if shift:
            self._enchars = text_orig
            return []

        jachars = self.__get_romaji_typing_rule(text, None)
        if jachars == None:
            jachars = symbol_rule.get(text, None)
        if jachars:
            self._enchars = text_orig
            self._jachars = jachars
            return []

        jachars, c = romaji_double_consonat_typing_rule.get(text, (None, None))
        if jachars:
            self._enchars = text_orig[0]
            self._jachars = jachars
            return [RomajiSegment(c)]

#        jachars, c = romaji_correction_rule.get(text, (None, None))
        jachars, c = romaji_correction_rule_get(text, (None, None))
        if jachars:
            self._enchars = text_orig[0]
            self._jachars = jachars
            return [RomajiSegment(c)]

        for i in range(-min(4, len(text)), 0):
            enchars = text[i:]

            jachars = self.__get_romaji_typing_rule(enchars, None)
            if jachars == None:
                jachars = symbol_rule.get(enchars, None)
            if jachars:
                jasegment = RomajiSegment(enchars, jachars)
                self._enchars = text_orig[:i]
                return [jasegment]

            jachars, c = romaji_double_consonat_typing_rule.get(enchars, (None, None))
            if jachars:
                jasegment = RomajiSegment(enchars[:-len(c)], jachars)
                self._enchars = text_orig[:i]
                if c:
                    return [jasegment, RomajiSegment(c)]
                return [jasegment]

#            jachars, c = romaji_correction_rule.get(enchars, (None, None))
            jachars, c = romaji_correction_rule_get(enchars, (None, None))
            if jachars:
                jasegment = RomajiSegment(enchars[:-len(c)], jachars)
                self._enchars = text_orig[:i]
                if c:
                    return [jasegment, RomajiSegment(c)]
                return [jasegment]

        self._enchars = text_orig
        return []

    def prepend(self, enchar, shift=False, unshift=False):
        if enchar == '' or enchar == '\0':
            return []

        if self.is_finished():
            return [RomajiSegment(enchar)]

        text_orig  = enchar + self._enchars
        text  = text_orig.lower()

        if self._latin_with_shift:
            if shift:
                self._shift_mode = True
            if unshift:
                self._shift_mode = False
            if self._shift_mode:
                self._enchars = text_orig
                return []

        if shift:
            self._enchars = text_orig
            return []

        jachars = self.__get_romaji_typing_rule(text, None)
        if jachars == None:
            jachars = symbol_rule.get(text, None)
        if jachars:
            self._enchars = text_orig
            self._jachars = jachars
            return []

        jachars, c = romaji_double_consonat_typing_rule.get(text, (None, None))
        if jachars:
            self._enchars = c
            return [RomajiSegment(text_orig[0], jachars)]

#        jachars, c = romaji_correction_rule.get(text, (None, None))
        jachars, c = romaji_correction_rule_get(text, (None, None))
        if jachars:
            self._enchars = c
            return [RomajiSegment(text_orig[0], jachars)]

        for i in range(min(4, len(text)), 0, -1):
            enchars = text[:i]

            jachars = self.__get_romaji_typing_rule(enchars, None)
            if jachars == None:
                jachars = symbol_rule.get(enchars, None)
            if jachars:
                jasegment = RomajiSegment(enchars, jachars)
                self._enchars = text_orig[i:]
                return [jasegment]

            jachars, c = romaji_double_consonat_typing_rule.get(enchars, (None, None))
            if jachars:
                self._enchars = c + text_orig[i:]
                return [RomajiSegment(enchars[:-len(c)], jachars)]

#            jachars, c = romaji_correction_rule.get(enchars, (None, None))
            jachars, c = romaji_correction_rule_get(enchars, (None, None))
            if jachars:
                self._enchars = c + text_orig[i:]
                return [RomajiSegment(enchars[:-len(c)], jachars)]

        self._enchars = text_orig
        return []

    def pop(self, index=-1):
        if index == -1:
            index = len(self._enchars) - 1
        if index < 0 or index >= len(self._enchars):
            raise IndexError('Out of bound')
        if self.is_finished():
            self._enchars = ''
            self._jachars = ''
        else:
            enchars = list(self._enchars)
            del enchars[index]
            self._enchars = ''.join(enchars)
            jachars = self.__get_romaji_typing_rule(self._enchars, None)
            if jachars == None:
                jachars = symbol_rule.get(self._enchars, '')
            self._jachars = jachars


