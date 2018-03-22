#!/usr/bin/env python3
from collections import OrderedDict
import os
import pprint

langCode = OrderedDict([
    ('"English"','EN'),
    ('"German"','DE'),
    ('"French"','FR'),
    ('"ChineseTraditional"','ZH'),
    ('"Japanese"','JA'),
    ('"Spanish"','ES'),
    ('"Italian"','IT'),
    ('"Korean"','KO'),
    ('"BrazilianPortuguese"','PT')
    ])

newNamesPy = """from collections import defaultdict

from . import sanitized as conf

language = conf.LANGUAGE.upper()[:2]
"""

assetsPath = "."

with open(os.path.join(assetsPath,"moves.txt"),"r") as f:
    lines = []
    for line in f:
        lines.append(line)

moves_dict = OrderedDict()
for k in lines[0].rstrip().split('\t'):
    moves_dict[k] = {}

moves_dict_keys = list(moves_dict.keys())

for l in lines[1:]:
    l = l.rstrip()
    splitL = l.split("\t")
    splitL[0] = int(splitL[0].replace('"','').split("_")[2])
    for k in range(len(moves_dict_keys))[1:]:
        moves_dict[moves_dict_keys[k]][splitL[0]] = splitL[k].replace('"','')

with open(os.path.join(assetsPath,"pokemon.txt"),"r") as f:
    lines = []
    for line in f:
        lines.append(line)

pokes_dict = OrderedDict()
for k in lines[0].rstrip().split('\t'):
    pokes_dict[k] = {}

pokes_dict_keys = list(pokes_dict.keys())

for l in lines[1:]:
    l = l.rstrip()
    splitL = l.split("\t")
    if splitL[0] == '"pokemon_desc_0000"':
        break
    splitL[0] = int(splitL[0].replace('"','').split("_")[2])
    for k in range(len(pokes_dict_keys))[1:]:
        pokes_dict[pokes_dict_keys[k]][splitL[0]] = splitL[k].replace('"','')

pp  = pprint.PrettyPrinter(indent=4)
pp8 = pprint.PrettyPrinter(indent=8)
for k in langCode.keys():
    if langCode[k] == 'EN':
        newNamesPy += "POKEMON = defaultdict(lambda: '?', {\n"
        ppformat = pp.pformat(pokes_dict[k]).replace("{"," ").replace("}","")
        newNamesPy += ppformat
        newNamesPy += "\n})\n"
        newNamesPy += "MOVES = defaultdict(lambda: '?', {\n"
        ppformat = pp.pformat(moves_dict[k]).replace("{"," ").replace("}","")
        newNamesPy += ppformat
        newNamesPy += "\n})\n"
        newNamesPy += "if language == 'EN':\n    pass\n"
        del pokes_dict[k][0]
    elif k in langCode.keys():
        del pokes_dict[k][0]
        newNamesPy += "elif language == '{}':\n".format(langCode[k])
        if pokes_dict[k] == pokes_dict['"English"']:
            newNamesPy += "    # Pokémon names are the same as English\n"
        else:
            newNamesPy += "    POKEMON = defaultdict(lambda: '?', {\n"
            ppformat = pp8.pformat(pokes_dict[k]).replace("{"," ").replace("}","")
            newNamesPy += ppformat
            newNamesPy += "\n    })\n"
        newNamesPy += "    MOVES = defaultdict(lambda: '?', {\n"
        ppformat = pp8.pformat(moves_dict[k]).replace("{"," ").replace("}","")
        newNamesPy += ppformat
        newNamesPy += "\n    })\n"
    else:
        print("Unknown language: {}".format(k))
        raise ValueError

newNamesPy += """else:
    raise ValueError('Language must be EN, DE, ES, FR, IT, JA, KO, PT, or ZH. You set {}.'.format(conf.LANGUAGE))

DAMAGE = defaultdict(lambda: '?', {
    13: 60,
    14: 150,
    16: 80,
    18: 50,
    20: 35,
    21: 60,
    22: 90,
    24: 70,
    26: 100,
    28: 50,
    30: 70,
    31: 120,
    32: 100,
    33: 50,
    34: 40,
    35: 65,
    36: 100,
    38: 60,
    39: 90,
    40: 130,
    42: 95,
    45: 55,
    46: 80,
    47: 110,
    48: 25,
    49: 90,
    50: 35,
    51: 50,
    53: 45,
    54: 60,
    56: 40,
    57: 45,
    58: 50,
    59: 55,
    60: 65,
    62: 70,
    63: 70,
    64: 80,
    65: 80,
    66: 50,
    67: 40,
    69: 50,
    70: 100,
    72: 70,
    74: 60,
    75: 25,
    77: 45,
    78: 100,
    79: 80,
    80: 45,
    82: 90,
    83: 50,
    84: 70,
    85: 60,
    86: 100,
    87: 130,
    88: 90,
    89: 40,
    90: 80,
    91: 110,
    92: 130,
    94: 40,
    95: 80,
    96: 55,
    99: 75,
    100: 45,
    101: 70,
    102: 70,
    103: 140,
    104: 60,
    105: 70,
    106: 80,
    107: 130,
    108: 100,
    109: 100,
    111: 60,
    114: 50,
    115: 55,
    116: 180,
    117: 70,
    118: 90,
    121: 60,
    122: 110,
    123: 40,
    125: 60,
    126: 40,
    127: 55,
    129: 80,
    131: 50,
    132: 50,
    133: 35,
    134: 50,
    135: 90,
    136: 25,
    137: 25,
    200: 3,
    201: 5,
    202: 6,
    203: 7,
    204: 6,
    205: 5,
    206: 6,
    207: 6,
    208: 8,
    209: 10,
    210: 8,
    211: 10,
    212: 5,
    213: 9,
    214: 7,
    215: 13,
    216: 5,
    217: 12,
    218: 10,
    219: 8,
    220: 6,
    221: 5,
    222: 7,
    223: 5,
    224: 10,
    225: 9,
    226: 5,
    227: 12,
    228: 8,
    229: 9,
    230: 5
})
"""

f = open("names.py_generated","w")
f.write(newNamesPy)
f.close()
