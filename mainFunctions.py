from difflib import SequenceMatcher
import itertools
import ast
from PyQt5 import QtCore
from dictionaryMaker import dictionaryMaker
import ast


#Calls the makeDictionary on start.

dictionaryMaker.makeDictionary()

gardinersCodetoSymbolsf = {'A1':'𓀀',
'A2':'𓀁',
'A3':'𓀂',
'A4':'𓀃',
'A5':'𓀄',
'A5A':'𓀅',
'A6':'𓀆',
'A6A':'𓀇',
'A6B':'𓀈',
'A7':'𓀉',
'A8':'𓀊',
'A9':'𓀋',
'A10':'𓀌',
'A11':'𓀍',
'A12':'𓀎',
'A13':'𓀏',
'A14':'𓀐',
'A14A':'𓀑',
'A15':'𓀒',
'A16':'𓀓',
'A17':'𓀔',
'A17A':'𓀕',
'A18':'𓀖',
'A19':'𓀗',
'A20':'𓀘',
'A21':'𓀙',
'A22':'𓀚',
'A23':'𓀛',
'A24':'𓀜',
'A25':'𓀝',
'A26':'𓀞',
'A27':'𓀟',
'A28':'𓀠',
'A29':'𓀡',
'A30':'𓀢',
'A31':'𓀣',
'A32':'𓀤',
'A32A':'𓀥',
'A33':'𓀦',
'A34':'𓀧',
'A35':'𓀨',
'A36':'𓀩',
'A37':'𓀪',
'A38':'𓀫',
'A39':'𓀬',
'A40':'𓀭',
'A40A':'𓀮',
'A41':'𓀯',
'A42':'𓀰',
'A42A':'𓀱',
'A43':'𓀲',
'A43A':'𓀳',
'A44':'𓀴',
'A45':'𓀵',
'A45A':'𓀶',
'A46':'𓀷',
'A47':'𓀸',
'A48':'𓀹',
'A49':'𓀺',
'A50':'𓀻',
'A51':'𓀼',
'A52':'𓀽',
'A53':'𓀾',
'A54':'𓀿',
'A55':'𓁀',
'A56':'𓁁',
'A57':'𓁂',
'A58':'𓁃',
'A59':'𓁄',
'A60':'𓁅',
'A61':'𓁆',
'A62':'𓁇',
'A63':'𓁈',
'A64':'𓁉',
'A65':'𓁊',
'A66':'𓁋',
'A67':'𓁌',
'A68':'𓁍',
'A69':'𓁎',
'A70':'𓁏',
'B1':'𓁐',
'B2':'𓁑',
'B3':'𓁒',
'B4':'𓁓',
'B5':'𓁔',
'B5A':'𓁕',
'B6':'𓁖',
'B7':'𓁗',
'B8':'𓁘',
'B9':'𓁙',
'C1':'𓁚',
'C2':'𓁛',
'C2A':'𓁜',
'C2B':'𓁝',
'C2C':'𓁞',
'C3':'𓁟',
'C4':'𓁠',
'C5':'𓁡',
'C6':'𓁢',
'C7':'𓁣',
'C8':'𓁤',
'C9':'𓁥',
'C10':'𓁦',
'C10A':'𓁧',
'C11':'𓁨',
'C12':'𓁩',
'C13':'𓁪',
'C14':'𓁫',
'C15':'𓁬',
'C16':'𓁭',
'C17':'𓁮',
'C18':'𓁯',
'C19':'𓁰',
'C20':'𓁱',
'C21':'𓁲',
'C22':'𓁳',
'C23':'𓁴',
'C24':'𓁵',
'D1':'𓁶',
'D2':'𓁷',
'D3':'𓁸',
'D4':'𓁹',
'D5':'𓁺',
'D6':'𓁻',
'D7':'𓁼',
'D8':'𓁽',
'D8A':'𓁾',
'D9':'𓁿',
'D10':'𓂀',
'D11':'𓂁',
'D12':'𓂂',
'D13':'𓂃',
'D14':'𓂄',
'D15':'𓂅',
'D16':'𓂆',
'D17':'𓂇',
'D18':'𓂈',
'D19':'𓂉',
'D20':'𓂊',
'D21':'𓂋',
'D22':'𓂌',
'D23':'𓂍',
'D24':'𓂎',
'D25':'𓂏',
'D26':'𓂐',
'D27':'𓂑',
'D27A':'𓂒',
'D28':'𓂓',
'D29':'𓂔',
'D30':'𓂕',
'D31':'𓂖',
'D31A':'𓂗',
'D32':'𓂘',
'D33':'𓂙',
'D34':'𓂚',
'D34A':'𓂛',
'D35':'𓂜',
'D36':'𓂝',
'D37':'𓂞',
'D38':'𓂟',
'D39':'𓂠',
'D40':'𓂡',
'D41':'𓂢',
'D42':'𓂣',
'D43':'𓂤',
'D44':'𓂥',
'D45':'𓂦',
'D46':'𓂧',
'D46A':'𓂨',
'D47':'𓂩',
'D48':'𓂪',
'D48A':'𓂫',
'D49':'𓂬',
'D50':'𓂭',
'D50A':'𓂮',
'D50B':'𓂯',
'D50C':'𓂰',
'D50D':'𓂱',
'D50E':'𓂲',
'D50F':'𓂳',
'D50G':'𓂴',
'D50H':'𓂵',
'D50I':'𓂶',
'D51':'𓂷',
'D52':'𓂸',
'D52A':'𓂹',
'D53':'𓂺',
'D54':'𓂻',
'D54A':'𓂼',
'D55':'𓂽',
'D56':'𓂾',
'D57':'𓂿',
'D58':'𓃀',
'D59':'𓃁',
'D60':'𓃂',
'D61':'𓃃',
'D62':'𓃄',
'D63':'𓃅',
'D64':'𓃆',
'D65':'𓃇',
'D66':'𓃈',
'D67':'𓃉',
'D67A':'𓃊',
'D67B':'𓃋',
'D67C':'𓃌',
'D67D':'𓃍',
'D67E':'𓃎',
'D67F':'𓃏',
'D67G':'𓃐',
'D67H':'𓃑',
'E1':'𓃒',
'E2':'𓃓',
'E3':'𓃔',
'E4':'𓃕',
'E5':'𓃖',
'E6':'𓃗',
'E7':'𓃘',
'E8':'𓃙',
'E8A':'𓃚',
'E9':'𓃛',
'E9A':'𓃜',
'E10':'𓃝',
'E11':'𓃞',
'E12':'𓃟',
'E13':'𓃠',
'E14':'𓃡',
'E15':'𓃢',
'E16':'𓃣',
'E16A':'𓃤',
'E17':'𓃥',
'E17A':'𓃦',
'E18':'𓃧',
'E19':'𓃨',
'E20':'𓃩',
'E20A':'𓃪',
'E21':'𓃫',
'E22':'𓃬',
'E23':'𓃭',
'E24':'𓃮',
'E25':'𓃯',
'E26':'𓃰',
'E27':'𓃱',
'E28':'𓃲',
'E28A':'𓃳',
'E29':'𓃴',
'E30':'𓃵',
'E31':'𓃶',
'E32':'𓃷',
'E33':'𓃸',
'E34':'𓃹',
'E34A':'𓃺',
'E36':'𓃻',
'E37':'𓃼',
'E38':'𓃽',
'F1':'𓃾',
'F1A':'𓃿',
'F2':'𓄀',
'F3':'𓄁',
'F4':'𓄂',
'F5':'𓄃',
'F6':'𓄄',
'F7':'𓄅',
'F8':'𓄆',
'F9':'𓄇',
'F10':'𓄈',
'F11':'𓄉',
'F12':'𓄊',
'F13':'𓄋',
'F13A':'𓄌',
'F14':'𓄍',
'F15':'𓄎',
'F16':'𓄏',
'F17':'𓄐',
'F18':'𓄑',
'F19':'𓄒',
'F20':'𓄓',
'F21':'𓄔',
'F21A':'𓄕',
'F22':'𓄖',
'F23':'𓄗',
'F24':'𓄘',
'F25':'𓄙',
'F26':'𓄚',
'F27':'𓄛',
'F28':'𓄜',
'F29':'𓄝',
'F30':'𓄞',
'F31':'𓄟',
'F31A':'𓄠',
'F32':'𓄡',
'F33':'𓄢',
'F34':'𓄣',
'F35':'𓄤',
'F36':'𓄥',
'F37':'𓄦',
'F37A':'𓄧',
'F38':'𓄨',
'F38A':'𓄩',
'F39':'𓄪',
'F40':'𓄫',
'F41':'𓄬',
'F42':'𓄭',
'F43':'𓄮',
'F44':'𓄯',
'F45':'𓄰',
'F45A':'𓄱',
'F46':'𓄲',
'F46A':'𓄳',
'F47':'𓄴',
'F47A':'𓄵',
'F48':'𓄶',
'F49':'𓄷',
'F50':'𓄸',
'F51':'𓄹',
'F51A':'𓄺',
'F51B':'𓄻',
'F51C':'𓄼',
'F52':'𓄽',
'F53':'𓄾',
'G1':'𓄿',
'G2':'𓅀',
'G3':'𓅁',
'G4':'𓅂',
'G5':'𓅃',
'G6':'𓅄',
'G6A':'𓅅',
'G7':'𓅆',
'G7A':'𓅇',
'G7B':'𓅈',
'G8':'𓅉',
'G9':'𓅊',
'G10':'𓅋',
'G11':'𓅌',
'G11A':'𓅍',
'G12':'𓅎',
'G13':'𓅏',
'G14':'𓅐',
'G15':'𓅑',
'G16':'𓅒',
'G17':'𓅓',
'G18':'𓅔',
'G19':'𓅕',
'G20':'𓅖',
'G20A':'𓅗',
'G21':'𓅘',
'G22':'𓅙',
'G23':'𓅚',
'G24':'𓅛',
'G25':'𓅜',
'G26':'𓅝',
'G26A':'𓅞',
'G27':'𓅟',
'G28':'𓅠',
'G29':'𓅡',
'G30':'𓅢',
'G31':'𓅣',
'G32':'𓅤',
'G33':'𓅥',
'G34':'𓅦',
'G35':'𓅧',
'G36':'𓅨',
'G36A':'𓅩',
'G37':'𓅪',
'G37A':'𓅫',
'G38':'𓅬',
'G39':'𓅭',
'G40':'𓅮',
'G41':'𓅯',
'G42':'𓅰',
'G43':'𓅱',
'G43A':'𓅲',
'G44':'𓅳',
'G45':'𓅴',
'G45A':'𓅵',
'G46':'𓅶',
'G47':'𓅷',
'G48':'𓅸',
'G49':'𓅹',
'G50':'𓅺',
'G51':'𓅻',
'G52':'𓅼',
'G53':'𓅽',
'G54':'𓅾',
'H1':'𓅿',
'H2':'𓆀',
'H3':'𓆁',
'H4':'𓆂',
'H5':'𓆃',
'H6':'𓆄',
'H6A':'𓆅',
'H7':'𓆆',
'H8':'𓆇',
'I1':'𓆈',
'I2':'𓆉',
'I3':'𓆊',
'I4':'𓆋',
'I5':'𓆌',
'I5A':'𓆍',
'I6':'𓆎',
'I7':'𓆏',
'I8':'𓆐',
'I9':'𓆑',
'I9A':'𓆒',
'I10':'𓆓',
'I10A':'𓆔',
'I11':'𓆕',
'I11A':'𓆖',
'I12':'𓆗',
'I13':'𓆘',
'I14':'𓆙',
'I15':'𓆚',
'K1':'𓆛',
'K2':'𓆜',
'K3':'𓆝',
'K4':'𓆞',
'K5':'𓆟',
'K6':'𓆠',
'K7':'𓆡',
'K8':'𓆢',
'L1':'𓆣',
'L2':'𓆤',
'L2A':'𓆥',
'L3':'𓆦',
'L4':'𓆧',
'L5':'𓆨',
'L6':'𓆩',
'L6A':'𓆪',
'L7':'𓆫',
'L8':'𓆬',
'M1':'𓆭',
'M1A':'𓆮',
'M1B':'𓆯',
'M2':'𓆰',
'M3':'𓆱',
'M3A':'𓆲',
'M4':'𓆳',
'M5':'𓆴',
'M6':'𓆵',
'M7':'𓆶',
'M8':'𓆷',
'M9':'𓆸',
'M10':'𓆹',
'M10A':'𓆺',
'M11':'𓆻',
'M12':'𓆼',
'M12A':'𓆽',
'M12B':'𓆾',
'M12C':'𓆿',
'M12D':'𓇀',
'M12E':'𓇁',
'M12F':'𓇂',
'M12G':'𓇃',
'M12H':'𓇄',
'M13':'𓇅',
'M14':'𓇆',
'M15':'𓇇',
'M15A':'𓇈',
'M16':'𓇉',
'M16A':'𓇊',
'M17':'𓇋',
'M17A':'𓇌',
'M18':'𓇍',
'M19':'𓇎',
'M20':'𓇏',
'M21':'𓇐',
'M22':'𓇑',
'M22A':'𓇒',
'M23':'𓇓',
'M24':'𓇔',
'M24A':'𓇕',
'M25':'𓇖',
'M26':'𓇗',
'M27':'𓇘',
'M28':'𓇙',
'M28A':'𓇚',
'M29':'𓇛',
'M30':'𓇜',
'M31':'𓇝',
'M31A':'𓇞',
'M32':'𓇟',
'M33':'𓇠',
'M33A':'𓇡',
'M33B':'𓇢',
'M34':'𓇣',
'M35':'𓇤',
'M36':'𓇥',
'M37':'𓇦',
'M38':'𓇧',
'M39':'𓇨',
'M40':'𓇩',
'M40A':'𓇪',
'M41':'𓇫',
'M42':'𓇬',
'M43':'𓇭',
'M44':'𓇮',
'N1':'𓇯',
'N2':'𓇰',
'N3':'𓇱',
'N4':'𓇲',
'N5':'𓇳',
'N6':'𓇴',
'N7':'𓇵',
'N8':'𓇶',
'N9':'𓇷',
'N10':'𓇸',
'N11':'𓇹',
'N12':'𓇺',
'N13':'𓇻',
'N14':'𓇼',
'N15':'𓇽',
'N16':'𓇾',
'N17':'𓇿',
'N18':'𓈀',
'N18A':'𓈁',
'N18B':'𓈂',
'N19':'𓈃',
'N20':'𓈄',
'N21':'𓈅',
'N22':'𓈆',
'N23':'𓈇',
'N24':'𓈈',
'N25':'𓈉',
'N25A':'𓈊',
'N26':'𓈋',
'N27':'𓈌',
'N28':'𓈍',
'N29':'𓈎',
'N30':'𓈏',
'N31':'𓈐',
'N32':'𓈑',
'N33':'𓈒',
'N33A':'𓈓',
'N34':'𓈔',
'N34A':'𓈕',
'N35':'𓈖',
'N35A':'𓈗',
'N36':'𓈘',
'N37':'𓈙',
'N37A':'𓈚',
'N38':'𓈛',
'N39':'𓈜',
'N40':'𓈝',
'N41':'𓈞',
'N42':'𓈟',
'NL1':'𓈠',
'NL2':'𓈡',
'NL3':'𓈢',
'NL4':'𓈣',
'NL5':'𓈤',
'NL5a':'𓈥',
'NL6':'𓈦',
'NL7':'𓈧',
'NL8':'𓈨',
'NL9':'𓈩',
'NL10':'𓈪',
'NL11':'𓈫',
'NL12':'𓈬',
'NL13':'𓈭',
'NL14':'𓈮',
'NL15':'𓈯',
'NL16':'𓈰',
'NL17':'𓈱',
'NL17a':'𓈲',
'NL18':'𓈳',
'NL19':'𓈴',
'NL20':'𓈵',
'NU1':'𓈶',
'NU2':'𓈷',
'NU3':'𓈸',
'NU4':'𓈹',
'NU5':'𓈺',
'NU6':'𓈻',
'NU7':'𓈼',
'NU8':'𓈽',
'NU9':'𓈾',
'NU10':'𓈿',
'NU10a':'𓉀',
'NU11':'𓉁',
'NU11a':'𓉂',
'NU12':'𓉃',
'NU13':'𓉄',
'NU14':'𓉅',
'NU15':'𓉆',
'NU16':'𓉇',
'NU17':'𓉈',
'NU18':'𓉉',
'NU18a':'𓉊',
'NU19':'𓉋',
'NU20':'𓉌',
'NU21':'𓉍',
'NU22':'𓉎',
'NU22a':'𓉏',
'O1':'𓉐',
'O1A':'𓉑',
'O2':'𓉒',
'O3':'𓉓',
'O4':'𓉔',
'O5':'𓉕',
'O5A':'𓉖',
'O6':'𓉗',
'O6A':'𓉘',
'O6B':'𓉙',
'O6C':'𓉚',
'O6D':'𓉛',
'O6E':'𓉜',
'O6F':'𓉝',
'O7':'𓉞',
'O8':'𓉟',
'O9':'𓉠',
'O10':'𓉡',
'O10A':'𓉢',
'O10B':'𓉣',
'O10C':'𓉤',
'O11':'𓉥',
'O12':'𓉦',
'O13':'𓉧',
'O14':'𓉨',
'O15':'𓉩',
'O16':'𓉪',
'O17':'𓉫',
'O18':'𓉬',
'O19':'𓉭',
'O19A':'𓉮',
'O20':'𓉯',
'O20A':'𓉰',
'O21':'𓉱',
'O22':'𓉲',
'O23':'𓉳',
'O24':'𓉴',
'O24A':'𓉵',
'O25':'𓉶',
'O25A':'𓉷',
'O26':'𓉸',
'O27':'𓉹',
'O28':'𓉺',
'O29':'𓉻',
'O29A':'𓉼',
'O30':'𓉽',
'O30A':'𓉾',
'O31':'𓉿',
'O32':'𓊀',
'O33':'𓊁',
'O33A':'𓊂',
'O34':'𓊃',
'O35':'𓊄',
'O36':'𓊅',
'O36A':'𓊆',
'O36B':'𓊇',
'O36C':'𓊈',
'O36D':'𓊉',
'O37':'𓊊',
'O38':'𓊋',
'O39':'𓊌',
'O40':'𓊍',
'O41':'𓊎',
'O42':'𓊏',
'O43':'𓊐',
'O44':'𓊑',
'O45':'𓊒',
'O46':'𓊓',
'O47':'𓊔',
'O48':'𓊕',
'O49':'𓊖',
'O50':'𓊗',
'O50A':'𓊘',
'O50B':'𓊙',
'O51':'𓊚',
'P1':'𓊛',
'P1A':'𓊜',
'P2':'𓊝',
'P3':'𓊞',
'P3A':'𓊟',
'P4':'𓊠',
'P5':'𓊡',
'P6':'𓊢',
'P7':'𓊣',
'P8':'𓊤',
'P9':'𓊥',
'P10':'𓊦',
'P11':'𓊧',
'Q1':'𓊨',
'Q2':'𓊩',
'Q3':'𓊪',
'Q4':'𓊫',
'Q5':'𓊬',
'Q6':'𓊭',
'Q7':'𓊮',
'R1':'𓊯',
'R2':'𓊰',
'R2A':'𓊱',
'R3':'𓊲',
'R3A':'𓊳',
'R3B':'𓊴',
'R4':'𓊵',
'R5':'𓊶',
'R6':'𓊷',
'R7':'𓊸',
'R8':'𓊹',
'R9':'𓊺',
'R10':'𓊻',
'R10A':'𓊼',
'R11':'𓊽',
'R12':'𓊾',
'R13':'𓊿',
'R14':'𓋀',
'R15':'𓋁',
'R16':'𓋂',
'R16A':'𓋃',
'R17':'𓋄',
'R18':'𓋅',
'R19':'𓋆',
'R20':'𓋇',
'R21':'𓋈',
'R22':'𓋉',
'R23':'𓋊',
'R24':'𓋋',
'R25':'𓋌',
'R26':'𓋍',
'R27':'𓋎',
'R28':'𓋏',
'R29':'𓋐',
'S1':'𓋑',
'S2':'𓋒',
'S2A':'𓋓',
'S3':'𓋔',
'S4':'𓋕',
'S5':'𓋖',
'S6':'𓋗',
'S6A':'𓋘',
'S7':'𓋙',
'S8':'𓋚',
'S9':'𓋛',
'S10':'𓋜',
'S11':'𓋝',
'S12':'𓋞',
'S13':'𓋟',
'S14':'𓋠',
'S14A':'𓋡',
'S14B':'𓋢',
'S15':'𓋣',
'S16':'𓋤',
'S17':'𓋥',
'S17A':'𓋦',
'S18':'𓋧',
'S19':'𓋨',
'S20':'𓋩',
'S21':'𓋪',
'S22':'𓋫',
'S23':'𓋬',
'S24':'𓋭',
'S25':'𓋮',
'S26':'𓋯',
'S26A':'𓋰',
'S26B':'𓋱',
'S27':'𓋲',
'S28':'𓋳',
'S29':'𓋴',
'S30':'𓋵',
'S31':'𓋶',
'S32':'𓋷',
'S33':'𓋸',
'S34':'𓋹',
'S35':'𓋺',
'S35A':'𓋻',
'S36':'𓋼',
'S37':'𓋽',
'S38':'𓋾',
'S39':'𓋿',
'S40':'𓌀',
'S41':'𓌁',
'S42':'𓌂',
'S43':'𓌃',
'S44':'𓌄',
'S45':'𓌅',
'S46':'𓌆',
'T1':'𓌇',
'T2':'𓌈',
'T3':'𓌉',
'T3A':'𓌊',
'T4':'𓌋',
'T5':'𓌌',
'T6':'𓌍',
'T7':'𓌎',
'T7A':'𓌏',
'T8':'𓌐',
'T8A':'𓌑',
'T9':'𓌒',
'T9A':'𓌓',
'T10':'𓌔',
'T11':'𓌕',
'T11A':'𓌖',
'T12':'𓌗',
'T13':'𓌘',
'T14':'𓌙',
'T15':'𓌚',
'T16':'𓌛',
'T16A':'𓌜',
'T17':'𓌝',
'T18':'𓌞',
'T19':'𓌟',
'T20':'𓌠',
'T21':'𓌡',
'T22':'𓌢',
'T23':'𓌣',
'T24':'𓌤',
'T25':'𓌥',
'T26':'𓌦',
'T27':'𓌧',
'T28':'𓌨',
'T29':'𓌩',
'T30':'𓌪',
'T31':'𓌫',
'T32':'𓌬',
'T32A':'𓌭',
'T33':'𓌮',
'T33A':'𓌯',
'T34':'𓌰',
'T35':'𓌱',
'T36':'𓌲',
'U1':'𓌳',
'U2':'𓌴',
'U3':'𓌵',
'U4':'𓌶',
'U5':'𓌷',
'U6':'𓌸',
'U6A':'𓌹',
'U6B':'𓌺',
'U7':'𓌻',
'U8':'𓌼',
'U9':'𓌽',
'U10':'𓌾',
'U11':'𓌿',
'U12':'𓍀',
'U13':'𓍁',
'U14':'𓍂',
'U15':'𓍃',
'U16':'𓍄',
'U17':'𓍅',
'U18':'𓍆',
'U19':'𓍇',
'U20':'𓍈',
'U21':'𓍉',
'U22':'𓍊',
'U23':'𓍋',
'U23A':'𓍌',
'U24':'𓍍',
'U25':'𓍎',
'U26':'𓍏',
'U27':'𓍐',
'U28':'𓍑',
'U29':'𓍒',
'U29A':'𓍓',
'U30':'𓍔',
'U31':'𓍕',
'U32':'𓍖',
'U32A':'𓍗',
'U33':'𓍘',
'U34':'𓍙',
'U35':'𓍚',
'U36':'𓍛',
'U37':'𓍜',
'U38':'𓍝',
'U39':'𓍞',
'U40':'𓍟',
'U41':'𓍠',
'U42':'𓍡',
'V1':'𓍢',
'V1A':'𓍣',
'V1B':'𓍤',
'V1C':'𓍥',
'V1D':'𓍦',
'V1E':'𓍧',
'V1F':'𓍨',
'V1G':'𓍩',
'V1H':'𓍪',
'V1I':'𓍫',
'V2':'𓍬',
'V2A':'𓍭',
'V3':'𓍮',
'V4':'𓍯',
'V5':'𓍰',
'V6':'𓍱',
'V7':'𓍲',
'V7A':'𓍳',
'V7B':'𓍴',
'V8':'𓍵',
'V9':'𓍶',
'V10':'𓍷',
'V11':'𓍸',
'V11A':'𓍹',
'V11B':'𓍺',
'V11C':'𓍻',
'V12':'𓍼',
'V12A':'𓍽',
'V12B':'𓍾',
'V13':'𓍿',
'V14':'𓎀',
'V15':'𓎁',
'V16':'𓎂',
'V17':'𓎃',
'V18':'𓎄',
'V19':'𓎅',
'V20':'𓎆',
'V20A':'𓎇',
'V20B':'𓎈',
'V20C':'𓎉',
'V20D':'𓎊',
'V20E':'𓎋',
'V20F':'𓎌',
'V20G':'𓎍',
'V20H':'𓎎',
'V20I':'𓎏',
'V20J':'𓎐',
'V20K':'𓎑',
'V20L':'𓎒',
'V21':'𓎓',
'V22':'𓎔',
'V23':'𓎕',
'V23A':'𓎖',
'V24':'𓎗',
'V25':'𓎘',
'V26':'𓎙',
'V27':'𓎚',
'V28':'𓎛',
'V28A':'𓎜',
'V29':'𓎝',
'V29A':'𓎞',
'V30':'𓎟',
'V30A':'𓎠',
'V31':'𓎡',
'V31A':'𓎢',
'V32':'𓎣',
'V33':'𓎤',
'V33A':'𓎥',
'V34':'𓎦',
'V35':'𓎧',
'V36':'𓎨',
'V37':'𓎩',
'V37A':'𓎪',
'V38':'𓎫',
'V39':'𓎬',
'V40':'𓎭',
'V40A':'𓎮',
'W1':'𓎯',
'W2':'𓎰',
'W3':'𓎱',
'W3A':'𓎲',
'W4':'𓎳',
'W5':'𓎴',
'W6':'𓎵',
'W7':'𓎶',
'W8':'𓎷',
'W9':'𓎸',
'W9A':'𓎹',
'W10':'𓎺',
'W10A':'𓎻',
'W11':'𓎼',
'W12':'𓎽',
'W13':'𓎾',
'W14':'𓎿',
'W14A':'𓏀',
'W15':'𓏁',
'W16':'𓏂',
'W17':'𓏃',
'W17A':'𓏄',
'W18':'𓏅',
'W18A':'𓏆',
'W19':'𓏇',
'W20':'𓏈',
'W21':'𓏉',
'W22':'𓏊',
'W23':'𓏋',
'W24':'𓏌',
'W24A':'𓏍',
'W25':'𓏎',
'X1':'𓏏',
'X2':'𓏐',
'X3':'𓏑',
'X4':'𓏒',
'X4A':'𓏓',
'X4B':'𓏔',
'X5':'𓏕',
'X6':'𓏖',
'X6A':'𓏗',
'X7':'𓏘',
'X8':'𓏙',
'X8A':'𓏚',
'Y1':'𓏛',
'Y1A':'𓏜',
'Y2':'𓏝',
'Y3':'𓏞',
'Y4':'𓏟',
'Y5':'𓏠',
'Y6':'𓏡',
'Y7':'𓏢',
'Y8':'𓏣',
'Z1':'𓏤',
'Z2':'𓏥',
'Z2A':'𓏦',
'Z2B':'𓏧',
'Z2C':'𓏨',
'Z2D':'𓏩',
'Z3':'𓏪',
'Z3A':'𓏫',
'Z3B':'𓏬',
'Z4':'𓏭',
'Z4A':'𓏮',
'Z5':'𓏯',
'Z5A':'𓏰',
'Z6':'𓏱',
'Z7':'𓏲',
'Z8':'𓏳',
'Z9':'𓏴',
'Z10':'𓏵',
'Z11':'𓏶',
'Z12':'𓏷',
'Z13':'𓏸',
'Z14':'𓏹',
'Z15':'𓏺',
'Z15A':'𓏻',
'Z15B':'𓏼',
'Z15C':'𓏽',
'Z15D':'𓏾',
'Z15E':'𓏿',
'Z15F':'𓐀',
'Z15G':'𓐁',
'Z15H':'𓐂',
'Z15I':'𓐃',
'Z16':'𓐄',
'Z16A':'𓐅',
'Z16B':'𓐆',
'Z16C':'𓐇',
'Z16D':'𓐈',
'Z16E':'𓐉',
'Z16F':'𓐊',
'Z16G':'𓐋',
'Z16H':'𓐌',
'Aa1':'𓐍',
'Aa2':'𓐎',
'Aa3':'𓐏',
'Aa4':'𓐐',
'Aa5':'𓐑',
'Aa6':'𓐒',
'Aa7':'𓐓',
'Aa7A':'𓐔',
'Aa7B':'𓐕',
'Aa8':'𓐖',
'Aa9':'𓐗',
'Aa10':'𓐘',
'Aa11':'𓐙',
'Aa12':'𓐚',
'Aa13':'𓐛',
'Aa14':'𓐜',
'Aa15':'𓐝',
'Aa16':'𓐞',
'Aa17':'𓐟',
'Aa18':'𓐠',
'Aa19':'𓐡',
'Aa20':'𓐢',
'Aa21':'𓐣',
'Aa22':'𓐤',
'Aa23':'𓐥',
'Aa24':'𓐦',
'Aa25':'𓐧',
'Aa26':'𓐨',
'Aa27':'𓐩',
'Aa28':'𓐪',
'Aa29':'𓐫',
'Aa30':'𓐬',
'Aa31':'𓐭',
'Aa32':'𓐮'}

def similar(a, b):

    #Using the SequenceMatcher function, return the similarity ratio.

    return SequenceMatcher(None, a, b).ratio()

def gardinersMultiDirect (incode):

    #This function just takes gardiners code, and turns it into symbols using the dictionary.
     
    founding = ""

    if "}" in incode:
        incode = incode.replace("}"," ")

    for word in incode.split("  "):
        for c in word.split(" "):
            
            for code, sym in gardinersCodetoSymbolsf.items():

                if c.lower() == code.lower():
                    founding += ( sym + " ")

            if c.lower() == "-":
                founding += ("-")


        founding += "  "

    return founding
  
def newSearchForEng(sen,dictionaryFull):

    #This function translates English to Hieroglyphs, Transliteration, and Gardiner's code, and it returns then and moreinfo variable.

    #Making some variables to store values in to return later.

    temp = []
    newWord = ""
    codeper = {}
    foundings = ""
    foundforgard = ""
    moreinfo = ""
    ogsen = []

    foundcheck = False

    for word in sen.lower().split(" "):
        ogsen.append(word)

    for word in sen.lower().split(" "):
        temp.append(word)
    
    while len(ogsen) != 0:
        
        foundcheck = False

        while len(temp) != 0:
            newWord = ""
            for i in range(len(temp)):
                if temp[i] != temp[-1]:
                    newWord += temp[i] + " "
                else: newWord += temp[i]


            for code, trans in dictionaryFull.items():

                #if list

                if isinstance(trans, list):

                    #loop to clean the word from its surrounding

                    for word in trans:

                    #if it matches we add it to a temp dictionary

                        if ")" in word and "(" in word:
                            b1 = word.index("(")
                            b2 = word.index(")")
                            sb = word.index("]")
                            if (b1-2) == sb:
                                word = word[b2+1:]
                            elif (b1-2) != sb:
                                word = word[sb+1:]
                        elif "]" in word:
                            sb = word.index("]")
                            word = word[sb+1:]

                        #if it matches we add it to a temp dictionary

                        if newWord == word.lower().strip() and len(word) != 0 and len(newWord) != 0:
                            per = (len(newWord)/len(word.lower().strip())*100) + 5
                            codeper[code] = per
                            foundcheck = True

                        elif newWord in word.lower().strip() and len(word) != 0 and len(newWord) != 0:
                            per = (len(newWord)/len(word.lower().strip())*100)
                            codeper[code] = per
                            foundcheck = True
                        else:
                            per = 0
                            codeper["{-}"] = per


                #else if not list

                elif isinstance(trans, str):

                    #cleans word

                    if ")" in trans:
                        b1 = trans.index("(")
                        b2 = trans.index(")")
                        sb = trans.index("]")
                        if (b1-2) == sb:
                            trans = trans[b2+1:]
                        elif (b1-2) != sb:
                            trans = trans[sb+1:]
                    elif "]" in trans:
                        sb = trans.index("]")
                        trans = trans[sb+1:]

                    #if it matches we add it to a temp dictionary

                    if newWord == trans.lower().strip() and len(trans) != 0 and len(newWord) != 0:
                        per = (len(newWord)/len(trans.lower().strip())*100) + 10
                        codeper[code] = per
                        foundcheck = True

                    elif newWord in trans.lower().strip() and len(trans) != 0 and len(newWord) != 0:
                        per = (len(newWord)/len(trans.lower().strip())*100) + 5
                        codeper[code] = per
                        foundcheck = True
                    else:
                        per = 0
                        codeper["{-}"] = per
                
            if foundcheck:
                for i in newWord.split(" "):
                    temp.remove(i)
                    ogsen.remove(i)
            else:
                temp.pop()
                        

            #if the temp dictionary isnt empty, it finds the max of the dictionary (the one with the best accuracy)
            # and returns it and adds it formatted to get translated into symbols using the Gardiner function.

            

        if len(codeper) != 0:
            maxv = max(codeper, key=codeper.get)
            if maxv != "{-}":

                result = maxv + " " +  str(codeper[maxv]) + "% (" + newWord + ")"
                print(result)
                moreinfo += ("More info: (" + str(codeper[maxv]) + "%) " + str(maxv) + ": " + str(dictionaryFull[maxv]) +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")
                codeper.clear()

            else:

                result = maxv + " Not found" + "% (" + newWord + ")"
                print(result)
                moreinfo += ("More info: " ": Not found" +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")
                codeper.clear()

        if not foundcheck:
            ogsen.remove(ogsen[0])

        temp = ogsen.copy()    
        #returns the stats for found words.



    transl = ""
    for i in foundforgard.split("} "):
        n = i+ "}"
        
        if n != "}":
            c = dictionaryFull.get(n,"notfound")

            if isinstance(c,list):
                for i in c:
                    if "notfound" not in i.lower():
                        if ")" and "(" in i.lower():
                            b = i.index("(")
                            e= i.index(")")
                            tr = i[b:e+1]
                            i = i.replace(tr,"")
                        if "notfound" not in i.lower():
                            tt = (i[i.index("["):i.index("]")+1])
                            transl += tt +" "
                            break
                        else: transl += "[-] "
                
            if isinstance(c, str):
                if ")" and "(" in c.lower():
                            b = c.index("(")
                            e= c.index(")")
                            tr = c[b:e+1]
                            c = c.replace(tr,"")
                if "notfound" not in c.lower():
                    tt = (c[c.index("["):c.index("]")+1])
                    transl += tt+ " "
                else: transl += "[-] "


    
    res = foundforgard.replace("{", "")
    hiero = gardinersMultiDirect(res)
    print("\n" + moreinfo)
    print(foundforgard)
    print(transl)
    print(hiero)
    return moreinfo,foundforgard,transl,hiero

    #calls function to translate to symbols using gardiners code.

def newSearchForTransl(sen,dictionaryFull):
    temp = []
    newWord = ""

    codeper = {}
    foundings = ""
    foundforgard = ""
    moreinfo = ""

    ogsen = []

    foundcheck = False

    for word in sen.split(" "):
        ogsen.append(word)

    for word in sen.split(" "):
        temp.append(word)
    
    while len(ogsen) != 0:
        
        foundcheck = False

        while len(temp) != 0:
            newWord = ""
            for i in range(len(temp)):
                if temp[i] != temp[-1]:
                    newWord += temp[i] + " "
                else: newWord += temp[i]

            #if found --------

            for code, trans in dictionaryFull.items():

                #if list

                if isinstance(trans, list):

                    #loop to clean the word from its surrounding

                    for word in trans:

                    #if it matches we add it to a temp dictionary

                        if "]" in word and "[" in word:
                            esb = word.index("]")
                            bsb = word.index("[")
                            word = word[bsb:esb+1]

                        #if it matches we add it to a temp dictionary

                        if newWord == word.strip():
                            #per = (len(newWord)/len(word.lower().strip())*100) + 5
                            newWordp = "[" +newWord +"]"
                            per = similar(newWordp,word.strip())*100 +5
                            #print("sure match (", per, ")", code)
                            codeper[code] = per
                            foundcheck = True

                        elif newWord in word.strip():
                            #per = (len(newWord)/len(word.lower().strip())*100)
                            newWordp = "[" +newWord +"]"
                            per = similar(newWordp,word.strip())*100
                            #print("not accurate (", per, ")", code)
                            codeper[code] = per
                            foundcheck = True
                            #or word.lower().strip() in newWord
                        else:
                            per = 0
                            codeper["-"] = per


                #else if not list

                elif isinstance(trans, str):

                    #cleans word

                    if "]" in trans and "[" in trans:
                        esb = trans.index("]")
                        bsb = trans.index("[")

                        trans = trans[bsb:esb+1]

                    #if it matches we add it to a temp dictionary

                    if newWord == trans.strip():
                        #per = (len(newWord)/len(trans.lower().strip())*100) + 10
                        newWordp = "[" +newWord +"]"
                        per = similar(newWordp,trans.strip())*100+10
                        #print("sure match (", per, ")", code)
                        codeper[code] = per
                        foundcheck = True

                    elif newWord in trans.strip():
                        #per = (len(newWord)/len(trans.lower().strip())*100) + 5
                        newWordp = "[" +newWord +"]"
                        per = similar(newWordp,trans.strip())*100 +5
                        #print("not accurate (", per, ")", code)
                        codeper[code] = per
                        foundcheck = True
                    else:
                        per = 0
                        codeper["{-}"] = per
                
            if foundcheck:
                for i in newWord.split(" "):
                    temp.remove(i)
                    ogsen.remove(i)
            else:
                temp.pop()
                        

            #if the temp dictionary isnt empty, it finds the max of the dictionary (the one with the best accuracy)
            # and returns it and adds it formatted to get translated into symbols using the Gardiner function.

            

        if len(codeper) != 0:
            #print(codeper)
            #print(len(codeper))
            maxv = max(codeper, key=codeper.get)
            if maxv != "-":

                result = maxv + " " +  str(codeper[maxv]) + "% (" + newWord + ")"
                    
                print(result)
                moreinfo += ("More info: (" + str(codeper[maxv]) + "%) " + str(maxv) + ": " + str(dictionaryFull[maxv]) +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")

                codeper.clear()
            else:
                result = maxv + " Not found" + "% (" + newWord + ")"
                    
                print(result)
                moreinfo += ("More info: " ": Not found" +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")

                codeper.clear()

        if not foundcheck:
            ogsen.remove(ogsen[0])

        temp = ogsen.copy()    
        #returns the stats for found words.
        #print(foundings)

    eng = ""

    for i in foundforgard.split("} "):
        n = i+ "}"
        
        if n != "}":
            c = dictionaryFull.get(n,"Not found.")

            


            if isinstance(c,list):
                #eng += c[0][c[0].index("["):c[0].index("]")]
                for i in c:
                    if "not found" not in i.lower():
                        if ")" and "(" in i.lower():
                            b = i.index("(")
                            e= i.index(")")
                            tr = i[b:e+1]
                            i = i.replace(tr,"")
                            xczxca= i[i.index("[")+1:i.index("]")].strip().lower()
                        if i[i.index("[")+1:i.index("]")].strip().lower() in sen:
                            tt = (i[i.index("]")+1:])
                            eng += tt +" "
                            break
                
            if isinstance(c, str):
                if ")" and "(" in c.lower():
                            b = c.index("(")
                            e= c.index(")")
                            tr = c[b:e+1]
                            c = c.replace(tr,"")
                if "not found" not in c.lower():
                    #eng += c[c.index("["):c.index("]")]
                    tt = (c[c.index("]")+1:])
                    eng += tt +" "


    
    res = foundforgard.replace("{", "")
    hiero = gardinersMultiDirect(res)
    #res = res.replace("}", " ")
    print("\n" + moreinfo)
    print(foundforgard)
    print(eng)
    print(hiero)

    return moreinfo, foundforgard, eng, hiero
    
def newSearchForGard(sen,dictionaryFull):

    newsen = ""
    for i in sen.split(" "):
        
        #value = {v for v in gardinersCodetoSymbolsf if gardinersCodetoSymbolsf[v]==i}
        if i in gardinersCodetoSymbolsf.values():
            if i != "":
                value = list(gardinersCodetoSymbolsf.keys())[list(gardinersCodetoSymbolsf.values()).index(i)]
                newsen += value + " "
        else:
            if i != "":
                newsen += "{-}"

    sen = newsen



    temp = []
    newWord = ""

    codeper = {}
    foundings = ""
    foundforgard = ""
    moreinfo = ""

    ogsen = []

    foundcheck = False

    if len(sen) != 0:
        if sen.lower()[-1] == " ":
            sen = sen[:-1]

    for word in sen.lower().split(" "):

        ogsen.append(word)

    for word in sen.lower().split(" "):

        temp.append(word)
    
    while len(ogsen) != 0:
        
        foundcheck = False

        while len(temp) != 0:
            newWord = ""
            for i in range(len(temp)):
                if len(temp) > 1:
                    newWord += temp[i] + " "
                elif len(temp) == 1:
                    newWord += temp[i]
                else: newWord += temp[i]
            
            if len(newWord) != 0:
                if newWord[-1] == " ":
                    newWord = newWord[:-1]

            #if found --------

            for code, trans in dictionaryFull.items():

                #if it matches we add it to a temp dictionary
                codew = code.replace("{","")
                codew = codew.replace("}","")

                if newWord == codew.lower().strip():
                    #per = (len(newWord)/len(codew.lower().strip())*100) + 10
                    per = similar(newWord,codew.lower().strip())*100
                    if per > 80:
                        #print("sure match (", per, ")", code)
                        codeper[code] = per
                        foundcheck = True

                elif newWord in codew.lower().strip():
                    #per = (len(newWord)/len(codew.lower().strip())*100) + 5
                    per = similar(newWord,codew.lower().strip())*100
                    if per > 80:
                        #print("not accurate (", per, ")", code)
                        codeper[code] = per
                        foundcheck = True
                else:
                    per = 0
                    codeper["{-}"] = per
                
            if foundcheck:
                for i in newWord.split(" "):
                    if len(temp) != 0:
                        temp.remove(i)
                    if len(ogsen) != 0:
                        ogsen.remove(i)
            else:
                temp.pop()
                        

            #if the temp dictionary isnt empty, it finds the max of the dictionary (the one with the best accuracy)
            # and returns it and adds it formatted to get translated into symbols using the Gardiner function.

            

        if len(codeper) != 0:
            #print(codeper)
            #print(len(codeper))
            maxv = max(codeper, key=codeper.get)
            if maxv != "{-}":

                result = maxv + " " +  str(codeper[maxv]) + "% (" + newWord + ")"
                    
                print(result + "Line 1609")
                moreinfo += ("More info: (" + str(codeper[maxv]) + "%) " + str(maxv) + ": " + str(dictionaryFull[maxv]) +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")

                codeper.clear()
            else:
                result = maxv + " Not found" + "% (" + newWord + ")"
                    
                print(result + "Line 1618")
                moreinfo += ("More info: {" + newWord + "} Not found" +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")

                codeper.clear()

        if not foundcheck:
            ogsen.remove(ogsen[0])

        temp = ogsen.copy()    
        #returns the stats for found words.
        #print(foundings)

    transl = ""

    for i in foundforgard.split("} "):
        n = i+ "}"
        
        if n != "}":
            c = dictionaryFull.get(n,"Not found.")

            


            if isinstance(c,list):
                #transl += c[0][c[0].index("["):c[0].index("]")]
                for i in c:
                    if "not found" not in i.lower():
                        if ")" and "(" in i.lower():
                            b = i.index("(")
                            e= i.index(")")
                            tr = i[b:e+1]
                            i = i.replace(tr,"")
                        if "not found" not in i.lower():
                            tt = (i[i.index("["):i.index("]")+1])
                            transl += tt +" "
                            break
                
            if isinstance(c, str):
                if ")" and "(" in c.lower():
                            b = c.index("(")
                            e= c.index(")")
                            tr = c[b:e+1]
                            c = c.replace(tr,"")
                if "not found" not in c.lower():
                    #transl += c[c.index("["):c.index("]")]
                    tt = (c[c.index("["):c.index("]")+1])
                    transl += tt+ " "


    allpossiblesen = []
    tt = []
    nffg = foundforgard.replace("} {","}.{")
    nffg = nffg[:-1]
    for words in nffg.split("."):
        
        if words != "{-}" :
            if words!= "":
                print(words + "Line 1677")
                curr = dictionaryFull[words]

                if isinstance(curr, list):
                    tt = []
                    for i in curr:
                        
                        if "]" in i and "[" in i:
                            bs = i.index("]")
                            es = i.index("[")
                            t = i[es:bs+1]
                            i = i.replace(t,"")
                            
                        if ")" in i and "(" in i:
                            bb = i.index(")")
                            eb = i.index("(")
                            t = i[eb:bb+1]
                            i = i.replace(t,"")
                            

                        tt.append(i)
                    allpossiblesen.append(tt)

                if isinstance(curr, str):
                    tt = []

                    if "]" in curr:
                        bs = curr.index("]")
                        curr = curr[bs+1:]
                        #curr = curr.replace(" ", "")
                    if ")" in curr and "(" in curr:
                        bb = curr.index("(")
                        be = curr.index(")")
                        test = curr[bb:be+1]
                        curr = curr.replace(curr[bb:be+1],"")
                        #curr = curr.replace(" ", "")

                    tt.append(curr)
                    allpossiblesen.append(tt)


        moreresults = ""
        if len(allpossiblesen) <= 5:

            bbbb = (list(itertools.product(*allpossiblesen)))
            tsa = ""
            listtsa = []
            sentoprint = ""
            #print(allpossiblesen)
            for l in bbbb:
                for b in l:
                    tsa += b + " "
                tsa += "\n"

            for line in tsa.split("\n"):
                if line != "":
                    listtsa.append(line)
            
            if len(listtsa) != 0:
                sentoprint = (listtsa[0])

            for count,l in enumerate(listtsa):
                moreresults += str(count) + ")> "+ l + "\n"


    """
    print(tsa)
    tool = language_tool_python.LanguageTool('en-US')

    finlist = []

    for i in listtsa:
        matches = tool.check(i)
        if len(matches) == 0:
            print(i)
            finlist.append(i)
            print(len(matches))
    
    for i in finlist:
        corrected_text = GingerIt().parse(i)
        print(corrected_text) """
    
    finalsen = ""
    for i in allpossiblesen:
        if len(i) >0:
            blankspace = "  "
            tt = ""
            for blankspace in i[0]:
                tt= i[0].replace("   "," ")
            finalsen += tt + " "



    
    res = foundforgard.replace("{", "")
    hiero = gardinersMultiDirect(res)
    #res = res.replace("}", " ")
    print("\n" + moreinfo)
    print(finalsen)
    
    print(foundforgard)
    #print(sentoprint)
    print(transl)
    print(hiero)
    return moreinfo,foundforgard,transl,hiero,finalsen,moreresults

    #calls function to translate to symbols using gardiners code.

def newSearchForHiero(sen,dictionaryFull):


    newsen = ""
    for i in sen.split(" "):
        #value = {v for v in gardinersCodetoSymbolsf if gardinersCodetoSymbolsf[v]==i}
        if i in gardinersCodetoSymbolsf.values():
            if i != "":
                value = list(gardinersCodetoSymbolsf.keys())[list(gardinersCodetoSymbolsf.values()).index(i)]
                newsen += value + " "
        else:
            if i != "":
                newsen += "{-}"

    sen = newsen



    temp = []
    newWord = ""

    codeper = {}
    foundings = ""
    foundforgard = ""
    moreinfo = ""

    ogsen = []

    foundcheck = False

    if sen.lower()[-1] == " ":
        sen = sen[:-1]

    for word in sen.lower().split(" "):
        ogsen.append(word)

    for word in sen.lower().split(" "):
        temp.append(word)
    
    while len(ogsen) != 0:
        
        foundcheck = False

        while len(temp) != 0:
            newWord = ""
            for i in range(len(temp)):
                if len(temp) > 1:
                    newWord += temp[i] + " "
                elif len(temp) == 1:
                    newWord += temp[i]
                else: newWord += temp[i]
            
            if len(newWord) != 0:
                if newWord[-1] == " ":
                    newWord = newWord[:-1]

            #if found --------

            for code, trans in dictionaryFull.items():

                #if it matches we add it to a temp dictionary
                codew = code.replace("{","")
                codew = codew.replace("}","")

                if newWord == codew.lower().strip():
                    #per = (len(newWord)/len(codew.lower().strip())*100) + 10
                    per = similar(newWord,codew.lower().strip())*100
                    if per > 80:
                        #print("sure match (", per, ")", code)
                        codeper[code] = per
                        foundcheck = True

                elif newWord in codew.lower().strip():
                    #per = (len(newWord)/len(codew.lower().strip())*100) + 5
                    per = similar(newWord,codew.lower().strip())*100
                    if per > 80:
                        #print("not accurate (", per, ")", code)
                        codeper[code] = per
                        foundcheck = True
                else:
                    per = 0
                    codeper["{-}"] = per
                
            if foundcheck:
                for i in newWord.split(" "):
                    if len(temp) != 0:
                        temp.remove(i)
                    if len(ogsen) != 0:
                        ogsen.remove(i)
            else:
                temp.pop()
                        

            #if the temp dictionary isnt empty, it finds the max of the dictionary (the one with the best accuracy)
            # and returns it and adds it formatted to get translated into symbols using the Gardiner function.

            

        if len(codeper) != 0:
            #print(codeper)
            #print(len(codeper))
            maxv = max(codeper, key=codeper.get)
            if maxv != "{-}":

                result = maxv + " " +  str(codeper[maxv]) + "% (" + newWord + ")"
                    
                print(result)
                moreinfo += ("More info: (" + str(codeper[maxv]) + "%) " + str(maxv) + ": " + str(dictionaryFull[maxv]) +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")

                codeper.clear()
            else:
                result = maxv + " Not found" + "% (" + newWord + ")"
                    
                print(result)
                moreinfo += ("More info: {" + newWord + "} Not found" +"\n")
                foundings += (result + " ")
                foundforgard += (str(maxv) + " ")

                codeper.clear()

        if not foundcheck:
            ogsen.remove(ogsen[0])

        temp = ogsen.copy()    
        #returns the stats for found words.
        #print(foundings)

    transl = ""

    for i in foundforgard.split("} "):
        n = i+ "}"
        
        if n != "}":
            c = dictionaryFull.get(n,"Not found.")

            


            if isinstance(c,list):
                #transl += c[0][c[0].index("["):c[0].index("]")]
                for i in c:
                    if "not found" not in i.lower():
                        if ")" and "(" in i.lower():
                            b = i.index("(")
                            e= i.index(")")
                            tr = i[b:e+1]
                            i = i.replace(tr,"")
                        if "not found" not in i.lower():
                            tt = (i[i.index("["):i.index("]")+1])
                            transl += tt +" "
                            break
                
            if isinstance(c, str):
                if ")" and "(" in c.lower():
                            b = c.index("(")
                            e= c.index(")")
                            tr = c[b:e+1]
                            c = c.replace(tr,"")
                if "not found" not in c.lower():
                    #transl += c[c.index("["):c.index("]")]
                    tt = (c[c.index("["):c.index("]")+1])
                    transl += tt+ " "


    allpossiblesen = []
    tt = []
    nffg = foundforgard.replace("} {","}.{")
    nffg = nffg[:-1]
    for words in nffg.split("."):
        
        if words != "{-}":
            curr = dictionaryFull[words]

            if isinstance(curr, list):
                tt = []
                for i in curr:
                    
                    if "]" in i and "[" in i:
                        bs = i.index("]")
                        es = i.index("[")
                        t = i[es:bs+1]
                        i = i.replace(t,"")
                        
                    if ")" in i and "(" in i:
                        bb = i.index(")")
                        eb = i.index("(")
                        t = i[eb:bb+1]
                        i = i.replace(t,"")
                        

                    tt.append(i)
                allpossiblesen.append(tt)

            if isinstance(curr, str):
                tt = []

                if "]" in curr:
                    bs = curr.index("]")
                    curr = curr[bs+1:]
                    #curr = curr.replace(" ", "")
                if ")" in curr and "(" in curr:
                    bb = curr.index("(")
                    be = curr.index(")")
                    test = curr[bb:be+1]
                    curr = curr.replace(curr[bb:be+1],"")
                    #curr = curr.replace(" ", "")

                tt.append(curr)
                allpossiblesen.append(tt)


    moreresults = ""
    if len(allpossiblesen) <= 5:

        bbbb = (list(itertools.product(*allpossiblesen)))
        tsa = ""
        listtsa = []
        sentoprint = ""
        #print(allpossiblesen)
        for l in bbbb:
            for b in l:
                tsa += b + " "
            tsa += "\n"

        for line in tsa.split("\n"):
            if line != "":
                listtsa.append(line)
        
        if len(listtsa) != 0:
            sentoprint = (listtsa[0])

        for count,l in enumerate(listtsa):
            moreresults += str(count) + ")> "+ l + "\n"


    """
    print(tsa)
    tool = language_tool_python.LanguageTool('en-US')

    finlist = []

    for i in listtsa:
        matches = tool.check(i)
        if len(matches) == 0:
            print(i)
            finlist.append(i)
            print(len(matches))
    
    for i in finlist:
        corrected_text = GingerIt().parse(i)
        print(corrected_text) """
    
    finalsen = ""
    for i in allpossiblesen:
        if len(i) >0:
            blankspace = "  "
            tt = ""
            for blankspace in i[0]:
                tt= i[0].replace("   "," ")
            finalsen += tt + " "



    
    res = foundforgard.replace("{", "")
    hiero = gardinersMultiDirect(res)
    #res = res.replace("}", " ")
    print("\n" + moreinfo)
    print(finalsen)
    
    print(foundforgard)
    #print(sentoprint)
    print(transl)
    print(hiero)
    return moreinfo,foundforgard,transl,hiero,finalsen,moreresults

    #calls function to translate to symbols using gardiners code.

def formater():

    #Formats by making elements of every single category of the gardiners codes.

    a,b,c,d,e,f,g,h,i,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
    

    for gard, sign in gardinersCodetoSymbolsf.items():
        
        if gard[0] == "A" and gard[1] != "a":
            a[gard] = sign
        if gard[0] == "B":
            b[gard] = sign
        if gard[0] == "C":
            c[gard] = sign
        if gard[0] == "D":
            d[gard] = sign
        if gard[0] == "E":
            e[gard] = sign
        if gard[0] == "F":
            f[gard] = sign
        if gard[0] == "G":
            g[gard] = sign
        if gard[0] == "H":
            h[gard] = sign
        if gard[0] == "I":
            i[gard] = sign
        if gard[0] == "K":
            k[gard] = sign
        if gard[0] == "L":
            l[gard] = sign
        if gard[0] == "M":
            m[gard] = sign
        if gard[0] == "N":
            n[gard] = sign
        if gard[0] == "O":
            o[gard] = sign
        if gard[0] == "P":
            p[gard] = sign
        if gard[0] == "Q":
            q[gard] = sign
        if gard[0] == "R":
            r[gard] = sign
        if gard[0] == "S":
            s[gard] = sign
        if gard[0] == "T":
            t[gard] = sign
        if gard[0] == "U":
            u[gard] = sign
        if gard[0] == "V":
            v[gard] = sign
        if gard[0] == "W":
            w[gard] = sign
        if gard[0] == "X":
            x[gard] = sign
        if gard[0] == "Y":
            y[gard] = sign
        if gard[0] == "Z":
            z[gard] = sign
        if gard[0] == "A" and gard[1] == "a":
            aa[gard] = sign 

    return a,b,c,d,e,f,g,h,i,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa
    
def useDir(dir):

    #Takes a directory and returns the dictionary after using literal eval on it.

    st = ""
    with open(dir) as f:
        text = f.readlines()
    for i in text:
        st += i
    
    tdict = ast.literal_eval(st)

    return tdict

def saveLog(text):

    #Saves the log using the date and time, and it takes a text as the only arguement.

    time = QtCore.QTime.currentTime().toString("h:mm:ss AP")
    date = QtCore.QDate.currentDate().toString('dd/MM/yyyy')

    st = "[" + date + " " + time + "] " + text + "\n"

    with open("Log.txt","a+",encoding='utf-8') as file:
        file.write(st)




dictionaryForNamesEn = """{
    'a':'𓄿',
    'b':'𓃀',
    'c':'𓎡',
    'd':'𓂧',
    'e':'𓂝',
    'f':'𓆑',
    'g':'𓎼',
    'h':'𓉔',
    'i':'𓇋',
    'j':'𓆓',
    'k':'𓎡',
    'l':'𓃭',
    'm':'𓅓',
    'n':'𓈖',
    'o':'𓍯',
    'p':'𓊪',
    'q':'𓏘',
    'r':'𓂋',
    's':'𓋴',
    't':'𓏏',
    'u':'𓅱',
    'v':'𓆑',
    'w':'𓅱',
    'x':'𓄡',
    'y':'𓇌',
    'z':'𓊃'
}"""

dictionaryForNamesAr = """{
    'ا':'𓄿',
    'ب':'𓃀',
    'ت':'𓏏',
    'ث':'𓍿',
    'ج':'𓎼',
    'ح':'𓎛',
    'خ':'𓐍',
    'د':'𓂧',
    'ذ':'𓍿',
    'ر':'𓂋',
    'ز':'𓊃',
    'س':'𓋴',
    'ش':'𓈙',
    'ص':'𓋴',
    'ض':'𓂧',
    'ط':'𓏏',
    'ظ':'𓊃',
    'ع':'𓂝',
    'غ':'𓄡',
    'ف':'𓆑',
    'ق':'𓏘',
    'ك':'𓎡',
    'ل':'𓃭',
    'م':'𓅓',
    'ن':'𓈖',
    'ه':'𓉔',
    'و':'𓅱',
    'ي':'𓇌'
}"""


dictionaryForNamesEn = ast.literal_eval(dictionaryForNamesEn)
dictionaryForNamesAr = ast.literal_eval(dictionaryForNamesAr)

def namefinder(uinp, dictionaryfornames):

    newword = ""

    for i in uinp:
        if i in dictionaryfornames.keys():
            newword+=dictionaryfornames[i] + " "

            
    print(newword)
    return newword
    
""" mainDictionary = ast.literal_eval (dictionaryMaker.defaultDictionary)

uinp = input("Enter name: ")
newSearchForGard(uinp,mainDictionary) """