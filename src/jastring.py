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

import romaji
import kana
import thumb

from segment import unichar_half_to_full

HalfSymbolTable = {}
for i in range(32, 127):
    if not chr(i).isalnum():
        HalfSymbolTable[unichar_half_to_full(chr(i))] = chr(i)

HalfNumberTable = {}
for i in range(10):
    HalfNumberTable[unichar_half_to_full(str(i))] = str(i)

PeriodTable = {'。': '．', '、': '，', '｡': '.', '､': ','}

SymbolTable = {}
SymbolTable[0] = {'「': '「', '」': '」', '／': '／'}
SymbolTable[1] = {'「': '「', '」': '」', '／': '・'}
SymbolTable[2] = {'「': '［', '」': '］', '／': '／'}
SymbolTable[3] = {'「': '［', '」': '］', '／': '・'}

TYPING_MODE_ROMAJI, \
TYPING_MODE_KANA, \
TYPING_MODE_THUMB_SHIFT = list(range(3))

class JaString:
    _prefs = None
    _mode = TYPING_MODE_ROMAJI
    _shift = False
    _unshift = False

    def __init__(self, mode=TYPING_MODE_ROMAJI, latin_with_shift=True):
        self._init_mode(mode)
        if mode == TYPING_MODE_ROMAJI:
            romaji.RomajiSegment.SET_LATIN_WITH_SHIFT(latin_with_shift)

    @classmethod
    def _init_mode(cls, mode):
        cls._mode = mode
        cls._shift = False
        cls._unshift = False
        cls.__cursor = 0
        cls.__segments = list()
        if mode == TYPING_MODE_ROMAJI:
            romaji.RomajiSegment.INIT_ROMAJI_TYPING_RULE(cls._prefs)
        elif mode == TYPING_MODE_KANA:
            kana.KanaSegment.INIT_KANA_TYPING_RULE(cls._prefs)
        elif mode == TYPING_MODE_THUMB_SHIFT:
            thumb.ThumbShiftSegment.INIT_THUMB_TYPING_RULE(cls._prefs)

    @classmethod
    def SET_PREFS(cls, prefs):
        cls._prefs = prefs

    @classmethod
    def RESET(cls, prefs, section, key, value):
        cls._prefs = prefs
        if section == 'kana-typing-rule':
            mode = TYPING_MODE_KANA
            kana.KanaSegment.RESET(prefs, section, key, value)
            cls._init_mode(mode)
        if section == 'common' and key == 'latin-with-shift':
            romaji.RomajiSegment.SET_LATIN_WITH_SHIFT(value)

    def set_shift(self, shift):
        self._shift = shift

    def set_hiragana_katakana(self, mode):
        if mode and self._mode == TYPING_MODE_ROMAJI:
            self._unshift = True

    def insert(self, c):
        segment_before = None
        segment_after = None
        new_segments = None

        if self.__cursor >= 1:
            segment_before = self.__segments[self.__cursor - 1]
        if self.__cursor < len(self.__segments):
            segment_after = self.__segments[self.__cursor]
        if segment_before and not segment_before.is_finished():
            if type(segment_before) == romaji.RomajiSegment:
                new_segments = segment_before.append(c,
                                                     self._shift,
                                                     self._unshift)
                self._unshift = False
            else:
                new_segments = segment_before.append(c)
        elif segment_after and not segment_after.is_finished():
            if type(segment_after) == romaji.RomajiSegment:
                new_segments = segment_after.prepend(c,
                                                     self._shift,
                                                     self._unshift)
                self._unshift = False
            else:
                new_segments = segment_after.prepend(c)
        else:
            if c != '\0' and c != '':
                if self._mode == TYPING_MODE_ROMAJI:
                    new_segments = [romaji.RomajiSegment(c,
                                                         '',
                                                         self._shift,
                                                         self._unshift)]
                    self._unshift = False
                elif self._mode == TYPING_MODE_KANA:
                    # kana mode doesn't have shift latin in MS.
                    new_segments = [kana.KanaSegment(c)]
                elif self._mode == TYPING_MODE_THUMB_SHIFT:
                    new_segments = [thumb.ThumbShiftSegment(c)]
        if new_segments:
            self.__segments[self.__cursor:self.__cursor] = new_segments
            self.__cursor += len(new_segments)

    def remove_before(self):
        index = self.__cursor - 1
        if index >= 0:
            segment = self.__segments[index]
            segment.pop()
            if segment.is_empty():
                del self.__segments[index]
                self.__cursor = index
            return True

        return False

    def remove_after(self):
        index = self.__cursor
        if index < len(self.__segments):
            segment = self.__segments[index]
            segment.pop()
            if segment.is_empty():
                del self.__segments[index]
            return True

        return False

    def get_string(self, type):
        pass

    def move_cursor(self, delta):
        self.__cursor += delta
        if self.__cursor < 0:
            self.__cursor = 0
        elif self.__cursor > len(self.__segments):
            self.__cursor = len(self.__segments)

    # hiragana segments are not char lengths.
    # e.g. 'ya' is 1 segment and 1 char and 'kya' is 1 segment and 2 chars.
    def move_cursor_hiragana_length(self, length):
        delta = length
        if delta < 0:
            if self.__cursor >= len(self.__segments):
                delta = delta + (self.__cursor - len(self.__segments) + 1)
                self.__cursor = len(self.__segments) - 1
            while delta < 0:
                text = str(self.__segments[self.__cursor].to_hiragana())
                if len(text) > -delta:
                    break
                delta = delta + len(text)
                self.__cursor = self.__cursor - 1
        else:
            if self.__cursor >= len(self.__segments):
                self.__cursor = len(self.__segments)
                return
            while delta > 0:
                text = str(self.__segments[self.__cursor].to_hiragana())
                if len(text) > delta:
                    break
                delta = delta - len(text)
                self.__cursor = self.__cursor + 1

    def move_cursor_katakana_length(self, length):
        delta = length
        if delta < 0:
            if self.__cursor >= len(self.__segments):
                delta = delta + (self.__cursor - len(self.__segments) + 1)
                self.__cursor = len(self.__segments) - 1
            while delta < 0:
                text = str(self.__segments[self.__cursor].to_katanaka())
                if len(text) > -delta:
                    break
                delta = delta + len(text)
                self.__cursor = self.__cursor - 1
        else:
            if self.__cursor >= len(self.__segments):
                self.__cursor = len(self.__segments)
                return
            while delta > 0:
                text = str(self.__segments[self.__cursor].to_katanaka())
                if len(text) > delta:
                    break
                delta = delta - len(text)
                self.__cursor = self.__cursor + 1

    def move_cursor_half_with_katakana_length(self, length):
        delta = length
        if delta < 0:
            if self.__cursor >= len(self.__segments):
                delta = delta + (self.__cursor - len(self.__segments) + 1)
                self.__cursor = len(self.__segments) - 1
            while delta < 0:
                text = str(self.__segments[self.__cursor].to_half_width_katakana())
                if len(text) > -delta:
                    break
                delta = delta + len(text)
                self.__cursor = self.__cursor - 1
        else:
            if self.__cursor >= len(self.__segments):
                self.__cursor = len(self.__segments)
                return
            while delta > 0:
                text = str(self.__segments[self.__cursor].to_half_width_katakana())
                if len(text) > delta:
                    break
                delta = delta - len(text)
                self.__cursor = self.__cursor + 1

    def _chk_text(self, s):
        period = self._prefs.get_value('common', 'period-style')
        symbol = self._prefs.get_value('common', 'symbol-style')
        half_symbol = self._prefs.get_value('common', 'half-width-symbol')
        half_number = self._prefs.get_value('common', 'half-width-number')
        ret = ''
        for c in s:
            c = c if not period else PeriodTable.get(c, c)
            # thumb_left + '2' and '/' are different
            if self._mode != TYPING_MODE_THUMB_SHIFT:
                c = c if not symbol else SymbolTable[symbol].get(c, c)
            c = c if not half_symbol else HalfSymbolTable.get(c, c)
            c = c if not half_number else HalfNumberTable.get(c, c)
            ret += c
        return ret

    def get_hiragana(self, commit=False):
        conv = lambda s: s.to_hiragana()
        R = lambda s: s if not (commit and s[-1:] == 'n') else s[:-1] + 'ん'
        text_before = R(''.join(map(conv, self.__segments[:self.__cursor])))
        text_after = R(''.join(map(conv, self.__segments[self.__cursor:])))
        return self._chk_text(text_before + text_after), len(text_before)

    def get_katakana(self, commit=False):
        conv = lambda s: s.to_katakana()
        R = lambda s: s if not (commit and s[-1:] == 'n') else s[:-1] + 'ン'
        text_before = R(''.join(map(conv, self.__segments[:self.__cursor])))
        text_after = R(''.join(map(conv, self.__segments[self.__cursor:])))
        return self._chk_text(text_before + text_after), len(text_before)

    def get_half_width_katakana(self, commit=False):
        conv = lambda s: s.to_half_width_katakana()
        R = lambda s: s if not (commit and s[-1:] == 'n') else s[:-1] + 'ﾝ'
        text_before = R(''.join(map(conv, self.__segments[:self.__cursor])))
        text_after = R(''.join(map(conv, self.__segments[self.__cursor:])))
        return self._chk_text(text_before + text_after), len(text_before)

    def get_latin(self):
        conv = lambda s: s.to_latin()
        text_before = ''.join(map(conv, self.__segments[:self.__cursor]))
        text_after = ''.join(map(conv, self.__segments[self.__cursor:]))
        return text_before + text_after, len(text_before)

    def get_wide_latin(self):
        conv = lambda s: s.to_wide_latin()
        text_before = ''.join(map(conv, self.__segments[:self.__cursor]))
        text_after = ''.join(map(conv, self.__segments[self.__cursor:]))
        return text_before + text_after, len(text_before)

    def is_empty(self):
        return all([s.is_empty() for s in self.__segments])

    def get_raw(self, start, end):
        i = 0
        r = ''
        for s in self.__segments:
            if i >= end:
                break
            elif start <= i:
                r += s.to_latin()
            i += len(s.to_hiragana())
        return r
