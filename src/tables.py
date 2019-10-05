# vim:set et sts=4 sw=4:
# -*- coding: utf-8 -*-
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2010-2014 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2007-2014 Red Hat, Inc.
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

# string, result, cont
romaji_typing_rule_static = {
    '-' : 'ー',
    'a' : 'あ',
    'i' : 'い',
    'u' : 'う',
    'e' : 'え',
    'o' : 'お',
    'xa' : 'ぁ',
    'xi' : 'ぃ',
    'xu' : 'ぅ',
    'xe' : 'ぇ',
    'xo' : 'ぉ',
    'la' : 'ぁ',
    'li' : 'ぃ',
    'lu' : 'ぅ',
    'le' : 'ぇ',
    'lo' : 'ぉ',
    'wha' : 'うぁ',
    'whi' : 'うぃ',
    'whe' : 'うぇ',
    'who' : 'うぉ',
    'va' : 'ヴぁ',
    'vi' : 'ヴぃ',
    'vu' : 'ヴ',
    've' : 'ヴぇ',
    'vo' : 'ヴぉ',
    'ka' : 'か',
    'ki' : 'き',
    'ku' : 'く',
    'ke' : 'け',
    'ko' : 'こ',
    'lka' : 'ヵ',
    'lke' : 'ヶ',
#    u'xka' : u'ゕ',
    'xka' : 'ヵ',
#    u'xke' : u'ゖ',
    'xke' : 'ヶ',
    'ga' : 'が',
    'gi' : 'ぎ',
    'gu' : 'ぐ',
    'ge' : 'げ',
    'go' : 'ご',
    'kya' : 'きゃ',
    'kyi' : 'きぃ',
    'kyu' : 'きゅ',
    'kye' : 'きぇ',
    'kyo' : 'きょ',
    'kwa' : 'くぁ',
    'gya' : 'ぎゃ',
    'gyi' : 'ぎぃ',
    'gyu' : 'ぎゅ',
    'gye' : 'ぎぇ',
    'gyo' : 'ぎょ',
    'gwa' : 'ぐぁ',
    'sa' : 'さ',
    'si' : 'し',
    'su' : 'す',
    'se' : 'せ',
    'so' : 'そ',
    'za' : 'ざ',
    'zi' : 'じ',
    'zu' : 'ず',
    'ze' : 'ぜ',
    'zo' : 'ぞ',
    'sya' : 'しゃ',
    'syi' : 'しぃ',
    'syu' : 'しゅ',
    'sye' : 'しぇ',
    'syo' : 'しょ',
    'sha' : 'しゃ',
    'shi' : 'し',
    'shu' : 'しゅ',
    'she' : 'しぇ',
    'sho' : 'しょ',
    'zya' : 'じゃ',
    'zyi' : 'じぃ',
    'zyu' : 'じゅ',
    'zye' : 'じぇ',
    'zyo' : 'じょ',
    'ja' : 'じゃ',
    'jya' : 'じゃ',
    'ji' : 'じ',
    'jyi' : 'じぃ',
    'ju' : 'じゅ',
    'jyu' : 'じゅ',
    'je' : 'じぇ',
    'jye' : 'じぇ',
    'jo' : 'じょ',
    'jyo' : 'じょ',
    'ta' : 'た',
    'ti' : 'ち',
    'tu' : 'つ',
    'tsu' : 'つ',
    'te' : 'て',
    'to' : 'と',
    'da' : 'だ',
    'di' : 'ぢ',
    'du' : 'づ',
    'de' : 'で',
    'do' : 'ど',
    'xtu' : 'っ',
    'xtsu' : 'っ',
    'ltu' : 'っ',
    'ltsu' : 'っ',
    'tya' : 'ちゃ',
    'tyi' : 'ちぃ',
    'tyu' : 'ちゅ',
    'tye' : 'ちぇ',
    'tyo' : 'ちょ',
    'cya' : 'ちゃ',
    'cyi' : 'ちぃ',
    'cyu' : 'ちゅ',
    'cye' : 'ちぇ',
    'cyo' : 'ちょ',
    'cha' : 'ちゃ',
    'chi' : 'ち',
    'chu' : 'ちゅ',
    'che' : 'ちぇ',
    'cho' : 'ちょ',
    'dya' : 'ぢゃ',
    'dyi' : 'ぢぃ',
    'dyu' : 'ぢゅ',
    'dye' : 'ぢぇ',
    'dyo' : 'ぢょ',
    'tsa' : 'つぁ',
    'tsi' : 'つぃ',
    'tse' : 'つぇ',
    'tso' : 'つぉ',
    'tha' : 'てゃ',
    'thi' : 'てぃ',
    'thu' : 'てゅ',
    'the' : 'てぇ',
    'tho' : 'てょ',
    'twu' : 'とぅ',
    'dha' : 'でゃ',
    'dhi' : 'でぃ',
    'dhu' : 'でゅ',
    'dhe' : 'でぇ',
    'dho' : 'でょ',
    'dwu' : 'どぅ',
    'na' : 'な',
    'ni' : 'に',
    'nu' : 'ぬ',
    'ne' : 'ね',
    'no' : 'の',
    'nya' : 'にゃ',
    'nyi' : 'にぃ',
    'nyu' : 'にゅ',
    'nye' : 'にぇ',
    'nyo' : 'にょ',
    'ha' : 'は',
    'hi' : 'ひ',
    'hu' : 'ふ',
    'he' : 'へ',
    'ho' : 'ほ',
    'ba' : 'ば',
    'bi' : 'び',
    'bu' : 'ぶ',
    'be' : 'べ',
    'bo' : 'ぼ',
    'pa' : 'ぱ',
    'pi' : 'ぴ',
    'pu' : 'ぷ',
    'pe' : 'ぺ',
    'po' : 'ぽ',
    'hya' : 'ひゃ',
    'hyi' : 'ひぃ',
    'hyu' : 'ひゅ',
    'hye' : 'ひぇ',
    'hyo' : 'ひょ',
    'bya' : 'びゃ',
    'byi' : 'びぃ',
    'byu' : 'びゅ',
    'bye' : 'びぇ',
    'byo' : 'びょ',
    'pya' : 'ぴゃ',
    'pyi' : 'ぴぃ',
    'pyu' : 'ぴゅ',
    'pye' : 'ぴぇ',
    'pyo' : 'ぴょ',
    'fa' : 'ふぁ',
    'fi' : 'ふぃ',
    'fu' : 'ふ',
    'fe' : 'ふぇ',
    'fo' : 'ふぉ',
    'fya' : 'ふゃ',
    'fyi' : 'ふぃ',
    'fyu' : 'ふゅ',
    'fye' : 'ふぇ',
    'fyo' : 'ふょ',
    'ma' : 'ま',
    'mi' : 'み',
    'mu' : 'む',
    'me' : 'め',
    'mo' : 'も',
    'mya' : 'みゃ',
    'myi' : 'みぃ',
    'myu' : 'みゅ',
    'mye' : 'みぇ',
    'myo' : 'みょ',
    'ya' : 'や',
    'yi' : 'い',
    'yu' : 'ゆ',
    'ye' : 'いぇ',
    'yo' : 'よ',
    'lya' : 'ゃ',
    'lyi' : 'ぃ',
    'lyu' : 'ゅ',
    'lye' : 'ぇ',
    'lyo' : 'ょ',
    'xya' : 'ゃ',
    'xyi' : 'ぃ',
    'xyu' : 'ゅ',
    'xye' : 'ぇ',
    'xyo' : 'ょ',
    'ra' : 'ら',
    'ri' : 'り',
    'ru' : 'る',
    're' : 'れ',
    'ro' : 'ろ',
    'rya' : 'りゃ',
    'ryi' : 'りぃ',
    'ryu' : 'りゅ',
    'rye' : 'りぇ',
    'ryo' : 'りょ',
    'wa' : 'わ',
    'wi' : 'うぃ',
    'wu' : 'う',
    'we' : 'うぇ',
    'wo' : 'を',
    'lwa' : 'ゎ',
    'xwa' : 'ゎ',
    'n\'' : 'ん',
    'nn' : 'ん',
    'wyi' : 'ゐ',
    'wye' : 'ゑ',
}

symbol_rule = {
    # symbols
    ' '  : '　',
    ','  : '、',
    '.'  : '。',
    '!'  : '！',
    '"' : '\u201d',
    '#'  : '＃',
    '$'  : '＄',
    '%'  : '％',
    '&'  : '＆',
    '\''  : '\u2019',
    '('  : '（',
    ')'  : '）',
    '~'  : '\uff5e',
    '-'  : 'ー',
    '='  : '＝',
    '^'  : '＾',
    '\\' : '＼',
    '|'  : '｜',
    '`'  : '\u2018',
    '@'  : '＠',
    '{'  : '｛',
    '['  : '「',
    '+'  : '＋',
    ';'  : '；',
    '*'  : '＊',
    ':'  : '：',
    '}'  : '｝',
    ']'  : '」',
    '<'  : '＜',
    '>'  : '＞',
    '?'  : '？',
    '/'  : '／',
    '_'  : '＿',
    '¥'  : '￥',

    # numbers
    '0': '０',
    '1': '１',
    '2': '２',
    '3': '３',
    '4': '４',
    '5': '５',
    '6': '６',
    '7': '７',
    '8': '８',
    '9': '９',
}

# this is only used with romaji_typing_rule
romaji_double_consonat_typing_rule = {
    # double consonant rule
    'bb' : ('っ', 'b'),
    'cc' : ('っ', 'c'),
    'dd' : ('っ', 'd'),
    'ff' : ('っ', 'f'),
    'gg' : ('っ', 'g'),
    'hh' : ('っ', 'h'),
    'jj' : ('っ', 'j'),
    'kk' : ('っ', 'k'),
    'mm' : ('っ', 'm'),
    'pp' : ('っ', 'p'),
    'rr' : ('っ', 'r'),
    'ss' : ('っ', 's'),
    'tt' : ('っ', 't'),
    'vv' : ('っ', 'v'),
    'ww' : ('っ', 'w'),
    'xx' : ('っ', 'x'),
    'yy' : ('っ', 'y'),
    'zz' : ('っ', 'z'),
}

# this is only used with romaji_typing_rule
romaji_correction_rule = {
    'nb' : ('ん', 'b'),
    'nc' : ('ん', 'c'),
    'nd' : ('ん', 'd'),
    'nf' : ('ん', 'f'),
    'ng' : ('ん', 'g'),
    'nh' : ('ん', 'h'),
    'nj' : ('ん', 'j'),
    'nk' : ('ん', 'k'),
    'nl' : ('ん', 'l'),
    'nm' : ('ん', 'm'),
    'np' : ('ん', 'p'),
    'nr' : ('ん', 'r'),
    'ns' : ('ん', 's'),
    'nt' : ('ん', 't'),
    'nv' : ('ん', 'v'),
    'nw' : ('ん', 'w'),
    'nx' : ('ん', 'x'),
    'nz' : ('ん', 'z'),
    'n\0' : ('ん', ''),
    'n,' : ('ん', ','),
    'n.' : ('ん', '.'),
}

# EUC-JP and SJIS do not have the chars
romaji_utf8_rule = {
    'う゛' : ['ゔ'],
}

# Hiragana normalization is needed for the personal dict.
romaji_normalize_rule = {
    'ヴ' : ['う゛'],
}

# a port of 101kana.sty from scim-anthy
kana_typing_rule_static = {
    # no modifiers keys
    '1' : 'ぬ',
    '2' : 'ふ',
    '3' : 'あ',
    '4' : 'う',
    '5' : 'え',
    '6' : 'お',
    '7' : 'や',
    '8' : 'ゆ',
    '9' : 'よ',
    '0' : 'わ',
    '-' : 'ほ',
    '^' : 'へ',

    'q' : 'た',
    'w' : 'て',
    'e' : 'い',
    'r' : 'す',
    't' : 'か',
    'y' : 'ん',
    'u' : 'な',
    'i' : 'に',
    'o' : 'ら',
    'p' : 'せ',
    '@' : '゛',
    '[' : '゜',

    'a' : 'ち',
    's' : 'と',
    'd' : 'し',
    'f' : 'は',
    'g' : 'き',
    'h' : 'く',
    'j' : 'ま',
    'k' : 'の',
    'l' : 'り',
    ';' : 'れ',
    ':' : 'け',
    ']' : 'む',

    'z' : 'つ',
    'x' : 'さ',
    'c' : 'そ',
    'v' : 'ひ',
    'b' : 'こ',
    'n' : 'み',
    'm' : 'も',
    ',' : 'ね',
    '.' : 'る',
    '/' : 'め',
    # u'\\' : u'ー',
    '\\' : 'ろ',

    # shift modifiered keys
    '!' : 'ぬ',
    '"' : 'ふ',
    '#' : 'ぁ',
    '$' : 'ぅ',
    '%' : 'ぇ',
    '&' : 'ぉ',
    '\'' : 'ゃ',
    '(' : 'ゅ',
    ')' : 'ょ',
    '~' : 'を',
    '=' : 'ほ',
    '|' : 'ー',

    'Q' : 'た',
    'W' : 'て',
    'E' : 'ぃ',
    'R' : 'す',
    'T' : 'ヵ',
    'Y' : 'ん',
    'U' : 'な',
    'I' : 'に',
    'O' : 'ら',
    'P' : 'せ',
    '`' : '゛',

    '{' : '「',

    'A' : 'ち',
    'S' : 'と',
    'D' : 'し',
    'F' : 'ゎ',
    'G' : 'き',
    'H' : 'く',
    'J' : 'ま',
    'K' : 'の',
    'L' : 'り',
    '+' : 'れ',
    '*' : 'ヶ',

    '}' : '」',

    'Z' : 'っ',
    'X' : 'さ',
    'C' : 'そ',
    'V' : 'ゐ',
    'B' : 'こ',
    'M' : 'も',
    'N' : 'み',
    '<' : '、',
    '>' : '。',

    '?' : '・',
    '_' : 'ろ',

    '¥' : 'ー',
}

kana_voiced_consonant_no_rule = {
    'か' : 'が',
    'き' : 'ぎ',
    'く' : 'ぐ',
    'け' : 'げ',
    'こ' : 'ご',
    'さ' : 'ざ',
    'し' : 'じ',
    'す' : 'ず',
    'せ' : 'ぜ',
    'そ' : 'ぞ',
    'た' : 'だ',
    'ち' : 'ぢ',
    'つ' : 'づ',
    'て' : 'で',
    'と' : 'ど',
    'は' : 'ば',
    'ひ' : 'び',
    'ふ' : 'ぶ',
    'へ' : 'べ',
    'ほ' : 'ぼ',
}

kana_semi_voiced_consonant_no_rule = {
    'は' : 'ぱ',
    'ひ' : 'ぴ',
    'ふ' : 'ぷ',
    'へ' : 'ぺ',
    'ほ' : 'ぽ',
}

# Create the table dynamically with kana_voiced_consonant_no_rule
#
#kana_voiced_consonant_rule = {
#    u'か@' : u'が',
#    u'き@' : u'ぎ',
#    u'く@' : u'ぐ',
#    u'け@' : u'げ',
#    u'こ@' : u'ご',
#    u'さ@' : u'ざ',
#    u'し@' : u'じ',
#    u'す@' : u'ず',
#    u'せ@' : u'ぜ',
#    u'そ@' : u'ぞ',
#    u'た@' : u'だ',
#    u'ち@' : u'ぢ',
#    u'つ@' : u'づ',
#    u'て@' : u'で',
#    u'と@' : u'ど',
#    u'は@' : u'ば',
#    u'ひ@' : u'び',
#    u'ふ@' : u'ぶ',
#    u'へ@' : u'べ',
#    u'ほ@' : u'ぼ',
#    u'か`' : u'が',
#    u'き`' : u'ぎ',
#    u'く`' : u'ぐ',
#    u'け`' : u'げ',
#    u'こ`' : u'ご',
#    u'さ`' : u'ざ',
#    u'し`' : u'じ',
#    u'す`' : u'ず',
#    u'せ`' : u'ぜ',
#    u'そ`' : u'ぞ',
#    u'た`' : u'だ',
#    u'ち`' : u'ぢ',
#    u'つ`' : u'づ',
#    u'て`' : u'で',
#    u'と`' : u'ど',
#    u'は`' : u'ば',
#    u'ひ`' : u'び',
#    u'ふ`' : u'ぶ',
#    u'へ`' : u'べ',
#    u'ほ`' : u'ぼ',
#    u'は[' : u'ぱ',
#    u'ひ[' : u'ぴ',
#    u'ふ[' : u'ぷ',
#    u'へ[' : u'ぺ',
#    u'ほ[' : u'ぽ',
#}
#
#kana_voiced_consonant_us_rule = {
#    u'か[' : u'が',
#    u'き[' : u'ぎ',
#    u'く[' : u'ぐ',
#    u'け[' : u'げ',
#    u'こ[' : u'ご',
#    u'さ[' : u'ざ',
#    u'し[' : u'じ',
#    u'す[' : u'ず',
#    u'せ[' : u'ぜ',
#    u'そ[' : u'ぞ',
#    u'た[' : u'だ',
#    u'ち[' : u'ぢ',
#    u'つ[' : u'づ',
#    u'て[' : u'で',
#    u'と[' : u'ど',
#    u'は[' : u'ば',
#    u'ひ[' : u'び',
#    u'ふ[' : u'ぶ',
#    u'へ[' : u'べ',
#    u'ほ[' : u'ぼ',
#    u'は]' : u'ぱ',
#    u'ひ]' : u'ぴ',
#    u'ふ]' : u'ぷ',
#    u'へ]' : u'ぺ',
#    u'ほ]' : u'ぽ',
#}

#hiragana, katakana, half_katakana
hiragana_katakana_table = {
    'あ' : ('ア', 'ｱ'),
    'い' : ('イ', 'ｲ'),
    'う' : ('ウ', 'ｳ'),
    'え' : ('エ', 'ｴ'),
    'お' : ('オ', 'ｵ'),
    'か' : ('カ', 'ｶ'),
    'き' : ('キ', 'ｷ'),
    'く' : ('ク', 'ｸ'),
    'け' : ('ケ', 'ｹ'),
    'こ' : ('コ', 'ｺ'),
    'が' : ('ガ', 'ｶﾞ'),
    'ぎ' : ('ギ', 'ｷﾞ'),
    'ぐ' : ('グ', 'ｸﾞ'),
    'げ' : ('ゲ', 'ｹﾞ'),
    'ご' : ('ゴ', 'ｺﾞ'),
    'さ' : ('サ', 'ｻ'),
    'し' : ('シ', 'ｼ'),
    'す' : ('ス', 'ｽ'),
    'せ' : ('セ', 'ｾ'),
    'そ' : ('ソ', 'ｿ'),
    'ざ' : ('ザ', 'ｻﾞ'),
    'じ' : ('ジ', 'ｼﾞ'),
    'ず' : ('ズ', 'ｽﾞ'),
    'ぜ' : ('ゼ', 'ｾﾞ'),
    'ぞ' : ('ゾ', 'ｿﾞ'),
    'た' : ('タ', 'ﾀ'),
    'ち' : ('チ', 'ﾁ'),
    'つ' : ('ツ', 'ﾂ'),
    'て' : ('テ', 'ﾃ'),
    'と' : ('ト', 'ﾄ'),
    'だ' : ('ダ', 'ﾀﾞ'),
    'ぢ' : ('ヂ', 'ﾁﾞ'),
    'づ' : ('ヅ', 'ﾂﾞ'),
    'で' : ('デ', 'ﾃﾞ'),
    'ど' : ('ド', 'ﾄﾞ'),
    'な' : ('ナ', 'ﾅ'),
    'に' : ('ニ', 'ﾆ'),
    'ぬ' : ('ヌ', 'ﾇ'),
    'ね' : ('ネ', 'ﾈ'),
    'の' : ('ノ', 'ﾉ'),
    'は' : ('ハ', 'ﾊ'),
    'ひ' : ('ヒ', 'ﾋ'),
    'ふ' : ('フ', 'ﾌ'),
    'へ' : ('ヘ', 'ﾍ'),
    'ほ' : ('ホ', 'ﾎ'),
    'ば' : ('バ', 'ﾊﾞ'),
    'び' : ('ビ', 'ﾋﾞ'),
    'ぶ' : ('ブ', 'ﾌﾞ'),
    'べ' : ('ベ', 'ﾍﾞ'),
    'ぼ' : ('ボ', 'ﾎﾞ'),
    'ぱ' : ('パ', 'ﾊﾟ'),
    'ぴ' : ('ピ', 'ﾋﾟ'),
    'ぷ' : ('プ', 'ﾌﾟ'),
    'ぺ' : ('ペ', 'ﾍﾟ'),
    'ぽ' : ('ポ', 'ﾎﾟ'),
    'ま' : ('マ', 'ﾏ'),
    'み' : ('ミ', 'ﾐ'),
    'む' : ('ム', 'ﾑ'),
    'め' : ('メ', 'ﾒ'),
    'も' : ('モ', 'ﾓ'),
    'や' : ('ヤ', 'ﾔ'),
    'ゆ' : ('ユ', 'ﾕ'),
    'よ' : ('ヨ', 'ﾖ'),
    'ら' : ('ラ', 'ﾗ'),
    'り' : ('リ', 'ﾘ'),
    'る' : ('ル', 'ﾙ'),
    'れ' : ('レ', 'ﾚ'),
    'ろ' : ('ロ', 'ﾛ'),
    'わ' : ('ワ', 'ﾜ'),
    'を' : ('ヲ', 'ｦ'),
    'ん' : ('ン', 'ﾝ'),
    'ぁ' : ('ァ', 'ｧ'),
    'ぃ' : ('ィ', 'ｨ'),
    'ぅ' : ('ゥ', 'ｩ'),
    'ぇ' : ('ェ', 'ｪ'),
    'ぉ' : ('ォ', 'ｫ'),
    'っ' : ('ッ', 'ｯ'),
    'ゃ' : ('ャ', 'ｬ'),
    'ゅ' : ('ュ', 'ｭ'),
    'ょ' : ('ョ', 'ｮ'),
    'ヵ' : ('ヵ', 'ｶ'),
    'ヶ' : ('ヶ', 'ｹ'),
    'ゎ' : ('ヮ', 'ﾜ'),
    'ゐ' : ('ヰ', 'ｨ'),
    'ゑ' : ('ヱ', 'ｪ'),
    'ヴ' : ('ヴ', 'ｳﾞ'),

    # symbols
    'ー' : ('ー', 'ｰ'),
    '、' : ('、', '､'),
    '。' : ('。', '｡'),
    '！' : ('！', '!'),
    '\u201d'  : ('\u201d', '"'),
    '＃' : ('＃', '#'),
    '＄' : ('＄', '$'),
    '％' : ('％', '%'),
    '＆' : ('＆', '&'),
    '\u2019'  : ('\u2019', '\''),
    '（' : ('（', '('),
    '）' : ('）', ')'),
    '\uff5e' : ('\uff5e', '~'),
    '＝' : ('＝', '='),
    '＾' : ('＾', '^'),
    '＼' : ('＼', '\\'),
    '｜' : ('｜', '|'),
    '\u2018'  : ('\u2018', '`'),
    '＠' : ('＠', '@'),
    '゛' : ('゛', 'ﾞ'),
    '｛' : ('｛', '{'),
    '゜' : ('゜', 'ﾟ'),
    '「' : ('「', '｢'),
    '＋' : ('＋', '+'),
    '；' : ('；', ';'),
    '＊' : ('＊', '*'),
    '：' : ('：', ':'),
    '｝' : ('｝', '}'),
    '」' : ('」', '｣'),
    '＜' : ('＜', '<'),
    '＞' : ('＞', '>'),
    '？' : ('？', '?'),
    '・' : ('・', '･'),
    '／' : ('／', '/'),
    '＿' : ('＿', '_'),
    '￥' : ('￥', '¥'),

    # numbers
    '０': ('０', '0'),
    '１': ('１', '1'),
    '２': ('２', '2'),
    '３': ('３', '3'),
    '４': ('４', '4'),
    '５': ('５', '5'),
    '６': ('６', '6'),
    '７': ('７', '7'),
    '８': ('８', '8'),
    '９': ('９', '9'),
}
