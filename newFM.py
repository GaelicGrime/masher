#!/usr/bin/python


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# FM.py is copied, along with the appropriate FMxxxxxx.py file from CONFIGDIR to local by pythonUnitsLink.py
# make sure if you change the modules, you also update the stored copy FMxxxxxx.py TBGLST file when you update FM.py
# CF.py is always linked, make sure to update CFTOP.py and SCTN0102 when FM.py or CF.py are changed
# all other units are loaded dynamically by pythonUnitsLink.py using the SCTN16 structure, FMSCTNENABLED.py file locally, etc.
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeAWideComment(comment_):
# * def makeCF():
# * def makeDO():
# * def makeFM():
# * def makeHBI():
# * def makeSP():
# * def parseTBGLST(FDTBGLST):
# * def readFileToStr(FILENAME_):
#
# * def __main__():


import hashlib as HL


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN001 _CHR_ _CONST_
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BKQT = "`"  # BACK TICK
BKSLSH = "\\"  # BACKSLASH
CBRCE = "}"  # CLOSEBRACE
CBRKT = "]"  # CLOSEBRACKET
CMNTLEN = 200
CONFIGDIR = "/rcr/0-units/python/"
CPAREN = ")"  # CLOSE PARENTHESIS
DBLQT = "\""  # DOUBLE QUOTE
ESC = "\x1b"
FOLDLEN = 200
NEWLINE = "\n"  # NEWLINE
OBRCE = "{"  # OPENBRACE
OBRKT = "["  # OPENBRACKET
OPAREN = "("  # OPENPAREN
SGLQT = "'"  # simple ' character
TABSTR = "\t"  # TAB

TRIQT = f"""{DBLQT}{DBLQT}{DBLQT}"""


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN002 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


BIN04 = lambda X: f"{X:04b}"
BIN08 = lambda X: f"{X:08b}"
BIN16 = lambda X: f"{X:016b}"
BIN32 = lambda X: f"{X:032b}"
BIN64 = lambda X: f"{X:064b}"
CF_NAME = "newCF.py"
CFTOP_NAME = f"{CONFIGDIR}CFTOP.py"
CLRALL = f"{ESC}[2J"
CLRDOWN = f"{ESC}[J"
CLREOL = f"{ESC}[K"
CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
DBSQLT_NAME = "newDBSQLT.py"
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
DO_NAME = "newDO.py"
DOTOP_NAME = f"{CONFIGDIR}DOTOP.py"
EEOL = "{ESC}[K"
EMPTY_DICT = {}
EMPTY_LIST = []
EMPTY_STR = ""
EMPTYSTRLST = [None, "", DBLQT, f"{DBLQT}{DBLQT}", SGLQT, f"{SGLQT}{SGLQT}", BKQT, "None", "\r", NEWLINE, "\r\n", "\n\r", ]
EMPTY_TUPLE = ()
FM_NAME = "newFM.py"
FMTOP_NAME = f"{CONFIGDIR}FMTOP.py"
FO_NAME = "newFO.py"
FOTOP_NAME = f"{CONFIGDIR}FOTOP.py"
FOLD1ENDHERE = f"""# fold here {"⥣1" * (FOLDLEN // 2)}"""
FOLD1ENDHERELN = f"""# fold here {"⥣1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD1STARTHERE = f"""# fold here {"⥥1" * (FOLDLEN // 2)}"""
FOLD1STARTHERELN = f"""# fold here {"⥥1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2ENDHERE = f"""# fold here {"⥣2" * (FOLDLEN // 2)}"""
FOLD2ENDHERELN = f"""# fold here {"⥣2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2STARTHERE = f"""# fold here {"⥥2" * (FOLDLEN // 2)}"""
FOLD2STARTHERELN = f"""# fold here {"⥥2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3ENDHERE = f"""# fold here {"⥣3" * (FOLDLEN // 2)}"""
FOLD3ENDHERELN = f"""# fold here {"⥣3" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3STARTHERE = f"""# fold here {"⥥3" * (FOLDLEN // 2)}"""
FOLD3STARTHERELN = f"""# fold here {"⥥3" * (FOLDLEN // 2)}{NEWLINE}"""
HBIBTM_NAME = f"{CONFIGDIR}HBIBTM.py"
HBI_NAME = "newHBI.py"
HBITOP_NAME = f"{CONFIGDIR}HBITOP.py"
HEX08 = lambda X_: f"{X_:02H}"  # {thisComment_}
HEX16 = lambda X_: f"{X_:04H}"  # {thisComment_}
HEX32 = lambda X_: f"{X_:08H}"  # {thisComment_}
HEX64 = lambda X_: f"{X_:016H}"  # {thisComment_}
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line\
LINESUP = lambda NUM_: f"{ESC}[{NUM_}A"
MARK1END = lambda TAG_: f"""# {"⥣1 " * (CMNTLEN // 3)} {TAG_}"""
MARK1ENDLN = lambda TAG_: f"""# {"⥣1 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK1MID = lambda TAG_: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK1MIDLN = lambda TAG_: f"""# {"⥣1⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK1START = lambda TAG_: f"""# {"1⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK1STARTLN = lambda TAG_: f"""# {"1⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK2END = lambda TAG_: f"""# {"⥣2 " * (CMNTLEN // 3)} {TAG_}"""
MARK2ENDLN = lambda TAG_: f"""# {"⥣2 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK2MID = lambda TAG_: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK2MIDLN = lambda TAG_: f"""# {"⥣2⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK2START = lambda TAG_: f"""# {"2⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK2STARTLN = lambda TAG_: f"""# {"2⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK3END = lambda TAG_: f"""# {"⥣3 " * (CMNTLEN // 3)} {TAG_}"""
MARK3ENDLN = lambda TAG_: f"""# {"⥣3 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK3MID = lambda TAG_: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK3MIDLN = lambda TAG_: f"""# {"⥣3⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK3START = lambda TAG_: f"""# {"3⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK3STARTLN = lambda TAG_: f"""# {"3⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK4END = lambda TAG_: f"""# {"⥣4 " * (CMNTLEN // 3)} {TAG_}"""
MARK4ENDLN = lambda TAG_: f"""# {"⥣4 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK4MID = lambda TAG_: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK4MIDLN = lambda TAG_: f"""# {"⥣4⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK4START = lambda TAG_: f"""# {"4⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK4STARTLN = lambda TAG_: f"""# {"4⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK5END = lambda TAG_: f"""# {"⥣5 " * (CMNTLEN // 3)} {TAG_}"""
MARK5ENDLN = lambda TAG_: f"""# {"⥣5 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK5MID = lambda TAG_: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK5MIDLN = lambda TAG_: f"""# {"⥣5⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK5START = lambda TAG_: f"""# {"5⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK5STARTLN = lambda TAG_: f"""# {"5⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK6END = lambda TAG_: f"""# {"⥣6 " * (CMNTLEN // 3)} {TAG_}"""
MARK6ENDLN = lambda TAG_: f"""# {"⥣6 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK6MID = lambda TAG_: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK6MIDLN = lambda TAG_: f"""# {"⥣6⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK6START = lambda TAG_: f"""# {"6⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK6STARTLN = lambda TAG_: f"""# {"6⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK7END = lambda TAG_: f"""# {"⥣7 " * (CMNTLEN // 3)} {TAG_}"""
MARK7ENDLN = lambda TAG_: f"""# {"⥣7 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK7MID = lambda TAG_: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK7MIDLN = lambda TAG_: f"""# {"⥣7⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK7START = lambda TAG_: f"""# {"7⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK7STARTLN = lambda TAG_: f"""# {"7⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK8END = lambda TAG_: f"""# {"⥣8 " * (CMNTLEN // 3)} {TAG_}"""
MARK8ENDLN = lambda TAG_: f"""# {"⥣8 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK8MID = lambda TAG_: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK8MIDLN = lambda TAG_: f"""# {"⥣8⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK8START = lambda TAG_: f"""# {"8⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK8STARTLN = lambda TAG_: f"""# {"8⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK9END = lambda TAG_: f"""# {"⥣9 " * (CMNTLEN // 3)} {TAG_}"""
MARK9ENDLN = lambda TAG_: f"""# {"⥣9 " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARK9MID = lambda TAG_: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {TAG_}"""
MARK9MIDLN = lambda TAG_: f"""# {"⥣9⥥ " * (CMNTLEN // 4)} {TAG_}{NEWLINE}"""
MARK9START = lambda TAG_: f"""# {"9⥥ " * (CMNTLEN // 3)} {TAG_}"""
MARK9STARTLN = lambda TAG_: f"""# {"9⥥ " * (CMNTLEN // 3)} {TAG_}{NEWLINE}"""
MARKLINES_NAME = f"{CONFIGDIR}MARKLINES.py"
MOVETO = lambda LN_, COL_: f"{ESC}[{LN_};{COL_}H"
NTAB = lambda NUM_: TABSTR * NUM_  # returns a string with _NUM_ TAB
QTSET = [DBLQT, SGLQT, BKQT]  # set of all quote characters
SCTN0102NAME = f"{CONFIGDIR}SCTN0102.py"
SCTNSNAME = f"{CONFIGDIR}SCTNS.py"
SP_NAME = "newSP.py"
SPTOP_NAME = f"{CONFIGDIR}SPTOP.py"
TBGLST_NAME = "TBGLST.py"


CODES2STRIP = [  # {'CODES2STRIP': "dict holding all of the things to strip from 'text' strings like color codes"}
	f"{ESC}[0m",  # entry for ESC-[0m
	f"{ESC}[1m",  # entry for ESC-[1m
	f"{ESC}[32m",  # entry for ESC-[32m
	f"{ESC}[35m",  # entry for ESC-[35m
	f"{ESC}[36m",  # entry for ESC-[36m
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN03 TYPEs and lambda
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
_ARRAY_ = "list"  # list or array, adjust for language
_AX_ = "_AX_"  # action involving a common key combination like ALT-D CTRL-W
_CHR_ = "varchar"  # character
_CONST_ = "_CONST_"  # constant in all uses
_DATETIME_ = "datetime"  # SQL datetime type
_DEC_ = "decimal"  # BCD like decimal sql value_
_DECIMAL_ = "decimal"  # BCD like decimal sql value_
_DEF_ = "_DEF_"  # define in all uses
_DICT_ = "dict"  # dict dictionary
_FLD_ = "varchar"  # field in all uses
_FLOAT_ = "float"  # standard floating point numbers
_INT_ = "int"  # integer any use
_KEY_ = "key"  # _DICT_ or DB key
_LIST_ = "list"  # list, table, etc.
_LST_ = "_LST_"  # list in all uses
_META_ = "metadata"  # metadata in all uses
_NUM_ = "NUMBER"  # number in all uses
_STR_ = "varchar"  # DB _STR_ to VARCHAR defined
_TUP_ = "tuple"  # define a tuple short method
_TUPLE_ = "tuple"  # define a tuple long method
_TYPE_ = "type"  # type in all uses
_TYPES_ = "types"  # types in all uses


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN04 BTNS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BTNGHAT_DN = "BTNGHAT_DN"  # artificial button for the hat on gamepads
BTNGHAT_DNLT = "BTNGHAT_DNLT"  # artificial button for the hat on gamepads
BTNGHAT_DNRT = "BTNGHAT_DNRT"  # artificial button for the hat on gamepads
BTNGHAT_LT = "BTNGHAT_LT"  # artificial button for the hat on gamepads
BTNGHAT_RLS = "BTNGHAT_RLS"  # artifical button release for hat on gamepads
BTNGHAT_RT = "BTNGHAT_RT"  # artificial button for the hat on gamepads
BTNGHAT_UP = "BTNGHAT_UP"  # artificial button for the hat on gamepads
BTNGHAT_UPLT = "BTNGHAT_UPLT"  # artificial button for the hat on gamepads
BTNGHAT_UPRT = "BTNGHAT_UPRT"  # artificial button for the hat on gamepads
BTNGLTSTK_DN = "BTNGLTSTK_DN"  # artificial button for left stick on gamepads
BTNGLTSTK_DNLT = "BTNGLTSTK_DNLT"  # artificial button for left stick on gamepads
BTNGLTSTK_DNRT = "BTNGLTSTK_DNRT"  # artificial button for left stick on gamepads
BTNGLTSTK_LT = "BTNGLTSTK_LT"  # artificial button for left stick on gamepads
BTNGLTSTK_RLS = "BTNGLTSTK_RLS"  # artificial button release for LTSTK on gamepads
BTNGLTSTK_RT = "BTNGLTSTK_RT"  # artificial button for left stick on gamepads
BTNGLTSTK_UP = "BTNGLTSTK_UP"  # artificial button for left stick on gamepads
BTNGLTSTK_UPLT = "BTNGLTSTK_UPLT"  # artificial button for left stick on gamepads
BTNGLTSTK_UPRT = "BTNGLTSTK_UPRT"  # artificial button for left stick on gamepads
BTNGRTSTK_DN = "BTNGRTSTK_DN"  # artificial button for left stick on gamepads
BTNGRTSTK_DNLT = "BTNGRTSTK_DNLT"  # artificial button for left stick on gamepads
BTNGRTSTK_DNRT = "BTNGRTSTK_DNRT"  # artificial button for left stick on gamepads
BTNGRTSTK_LT = "BTNGRTSTK_LT"  # artificial button for left stick on gamepads
BTNGRTSTK_RLS = "BTNGRTSTK_RLS"  # artificial button release for RTSTK on gamepads
BTNGRTSTK_RT = "BTNGRTSTK_RT"  # artificial button for left stick on gamepads
BTNGRTSTK_UP = "BTNGRTSTK_UP"  # artificial button for left stick on gamepads
BTNGRTSTK_UPLT = "BTNGRTSTK_UPLT"  # artificial button for left stick on gamepads
BTNGRTSTK_UPRT = "BTNGRTSTK_UPRT"  # artificial button for left stick on gamepads
BTNG_01 = "BTNG_01"  # BTNG001/X on gamepads
BTNG_02 = "BTNG_02"  # BTNG002/A on gamepads
BTNG_03 = "BTNG_03"  # BTNG003/B on gamepads
BTNG_04 = "BTNG_04"  # BTNG004/Y on gamepads
BTNG_05 = "BTNG_05"  # BTNG005/left shoulder on gamepads
BTNG_06 = "BTNG_06"  # BTNG006/right shoulder on gamepads
BTNG_07 = "BTNG_07"  # BTNG007/left trigger on gamepads
BTNG_08 = "BTNG_08"  # BTNG008/right trigger on gamepads
BTNG_09 = "BTNG_09"  # BTNG009/left face on gamepads
BTNG_10 = "BTNG_10"  # BTNG_010/right face on gamepads
BTNG_11LTSTK = "BTNG_11LTSTK"  # BTN011/left stick on gamepads
BTNG_12RTSTK = "BTNG_12RTSTK"  # BTN012/right stick on gamepads
BTNG_13 = "BTNG_13"  # BTN013/home/select on gamepads
BTNK_00 = "BTNK_00"  # BTN000 on a knob
BTNMODE_01 = "BTNMODE_01"  # switch through MODE1 move/wheel for mouse actions
BTNMODE_02 = "BTNMODE_02"  # switch through MODE2 normal/draglock for mouse actions
BTNMWH_DN = "BTNMWH_DN"  # BTNMWHLDN/MSE_DN on mice
BTNMWH_DNLT = "BTNMWH_DNLT"  # BTNMWHLDN/MSE_DNLT on mice
BTNMWH_DNRT = "BTNMWH_DNRT"  # BTNMWHLDN/MSE_DNRT on mice
BTNMWH_LT = "BTNMWH_LT"  # BTNMWHLLT/MSE_LT on mice
BTNMWH_RLS = "BTNMWH_RLS"  # BTNMWHLRLS/MSE_RLS on mice
BTNMWH_RT = "BTNMWH_RT"  # BTNMWHLRT/MSE_RT on mice
BTNMWH_UP = "BTNMWH_UP"  # BTNMWHLUP/MSE_UP on mice
BTNMWH_UPLT = "BTNMWH_UPLT"  # BTNMWHLUP/MSE_UPLT on mice
BTNMWH_UPRT = "BTNMWH_UPRT"  # BTNMWHLUP/MSE_UPRT on mice
BTNM_01LT = "BTNM_01LT"  # BTN01/LEFT on mice
BTNM_02MD = "BTNM_02MD"  # BTN02/MIDDLE on mice
BTNM_03RT = "BTNM_03RT"  # BTN03/RIGHT on mice
BTNM_04WHUP = "BTNM_04WHUP"  # BTNM04/MSEWHL_UP on mice
BTNM_05WHDN = "BTNM_05WHDN"  # BTNM05/MSEWHL_DN on mice
BTNM_06WHLT = "BTNM_06WHLT"  # BTNM06/MSEWHL_LT on mice
BTNM_07WHRT = "BTNM_07WHRT"  # BTNM07/MSEWHL_RT on mice
BTNM_08 = "BTNM_08"  # BTNM_08/NW most additional BTN on mice
BTNM_09 = "BTNM_09"  # BTNM_09 additional on mice
BTNM_10 = "BTNM_10"  # BTNM_10 additional on mice
BTNM_11 = "BTNM_11"  # BTNM_11 additional BTN on mice
BTNM_12 = "BTNM_12"  # BTNM_12/SE most additional BTN on mice
BTNM_MDN = "BTNM_MDN"  # BTNMDN/MSE_DN on mice
BTNM_MDNLT = "BTNM_MDNLT"  # BTNMDN/MSE_DNLT on mice
BTNM_MDNRT = "BTNM_MDNRT"  # BTNMDN/MSE_DNRT on mice
BTNM_MLT = "BTNM_MLT"  # BTNMLT/MSE_LT on mice
BTNM_MRLS = "BTNM_MRLS"  # MSE_MRLS on mice
BTNM_MRT = "BTNM_MRT"  # BTNMRT/MSE_RT on mice
BTNM_MUP = "BTNM_MUP"  # BTNMUP/MSE_UP on mice
BTNM_MUPLT = "BTNM_MUPLT"  # BTNMUP/MSE_UPLT on mice
BTNM_MUPRT = "BTNM_MUPRT"  # BTNMUP/MSE_UPRT on mice
BTNM_WHDN = "BTNM_WHDN"  # BTNMDN/MSE_DN on mice
BTNM_WHDNLT = "BTNM_WHDNLT"  # BTNMDN/MSE_DNLT on mice
BTNM_WHDNRT = "BTNM_WHDNRT"  # BTNMDN/MSE_DNRT on mice
BTNM_WHLT = "BTNM_WHLT"  # BTNMLT/MSE_LT on mice
BTNM_WHRT = "BTNM_WHRT"  # BTNMRT/MSE_RT on mice
BTNM_WHUP = "BTNM_WHUP"  # BTNMUP/MSE_UP on mice
BTNM_WHUPLT = "BTNM_WHUPLT"  # BTNMUP/MSE_UPLT on mice
BTNM_WHUPRT = "BTNM_WHUPRT"  # BTNMUP/MSE_UPRT on mice
BTNST_00 = "BTNST_00"  # BTN000 on a Saitek commander


BTNSHOLDABLELIST = [
]

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN11 FMAX _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMAXCF_SCTN003LAMBDADEF = "FMAXCF_SCTN003LAMBDADEF"  # define a lambda function <NAC><NAME><lambda str>
FMAXCF_SCTN003TYPEDEF = "FMAXCF_SCTN003TYPEDEF"  # define a fake type used in the translation dict <NAC><NAME><TYPE>
FMAXCF_SCTN201STRDEF = "FMAXCF_SCTN201STRDEF"  # define a STR in SCTN21 <NAC><NAME><str>
FMAXCF_SCTN201VALDEF = "FMAXCF_SCTN201VALDEF"  # define a VAL in SCTN21 <NAC><NAME><VAL>
FMAXCF_SCTN202PARMDEF = "FMAXCF_SCTN202PARMDEF"  # define a '-a[=]' in SCTN22 <NAC><PARM><VAL>
FMAXCF_SCTN202STRENTRYADD = "FMAXCF_SCTN202STRENTRYADD"  # define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>
FMAXCF_SCTN202VALENTRYADD = "FMAXCF_SCTN202VALENTRYADD"  # define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>
FMAXCF_SCTN203DICTDEF = "FMAXCF_SCTN203DICTDEF"  # define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN203DICTSTRADD = "FMAXCF_SCTN203DICTSTRADD"  # define a dict STR in SCTN23 <NAC><DICTNAME><STR>
FMAXCF_SCTN203DICTVALADD = "FMAXCF_SCTN203DICTVALADD"  # define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>
FMAXCF_SCTN204LISTDEF = "FMAXCF_SCTN204LISTDEF"  # define a list in SCTN24 <NAC><LISTNAME>
FMAXCF_SCTN204LISTSTRADD = "FMAXCF_SCTN204LISTSTRADD"  # define a list STR in SCTN24 <NAC><LISTNAME><STR>
FMAXCF_SCTN204LISTVALADD = "FMAXCF_SCTN204LISTVALADD"  # define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>
FMAXDO_SCTN401DEVICEDEF = "FMAXDO_SCTN401DEVICEDEF"  # define a device in PROF <NAC><MYNAME><DEV_NAME>
FMAXDO_SCTN401DICTKEYDEF = "FMAXDO_SCTN401DICTKEYDEF"  # define a profile dict key <NAC><KEY>
FMAXDO_SCTN401LAMBDADEF = "FMAXDO_SCTN401LAMBDADEF"  # define a profile lambda <NAC><NAME><LAMBDA>
FMAXDO_SCTN401STRDEF = "FMAXDO_SCTN401STRDEF"  # define a profile STR <NAC><NAME><VAL>
FMAXDO_SCTN401VALDEF = "FMAXDO_SCTN401VALDEF"  # define a profile value <NAC><NAME><VAL>
FMAXDO_SCTN402LDIEABSDEF = "FMAXDO_SCTN402LDIEABSDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN402LDIEBTNDEF = "FMAXDO_SCTN402LDIEBTNDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN402LDIEFUNCDEF = "FMAXDO_SCTN402LDIEFUNCDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN402LDIEKEYDEF = "FMAXDO_SCTN402LDIEKEYDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN402LDIERELDEF = "FMAXDO_SCTN402LDIERELDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN402LDIESPCLDEF = "FMAXDO_SCTN402LDIESPCLDEF"  # define IE psuedo entry for special events
FMAXDO_SCTN402LDIESYNDEF = "FMAXDO_SCTN402LDIESYNDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN403AXDEF = "FMAXDO_SCTN403AXDEF"  # define a profile action <NAC>
FMAXDO_SCTN403AXVALADD = "FMAXDO_SCTN403AXVALADD"  # add an item to an action <NAC><AX><VAL>
FMAXDO_SCTN404DEVICEENTRYSTRADD = "FMAXDO_SCTN404DEVICEENTRYSTRADD"  # define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>
FMAXDO_SCTN404DEVICEENTRYVALADD = "FMAXDO_SCTN404DEVICEENTRYVALADD"  # define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>
FMAXDO_SCTN405HOLDABLEADD1 = "FMAXDO_SCTN405HOLDABLEADD1"  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>
FMAXDO_SCTN405HOLDABLEADD2 = "FMAXDO_SCTN405HOLDABLEADD2"  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>
FMAXDO_SCTN405NOTHOLDABLEADD1 = "FMAXDO_SCTN405NOTHOLDABLEADD1"  # not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>
FMAXDO_SCTN405NOTHOLDABLEMODEDADD1 = "FMAXDO_SCTN405NOTHOLDABLEMODEDADD1"  # not holdable PROF items with a mode <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><MODENAME><NOTHOLDABLE><Ax>
FMAXDO_SCTN406XLATEADD = "FMAXDO_SCTN406XLATEADD"  # add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>
FMAXDO_SCTN407BTNSDEF = "FMAXDO_SCTN407BTNSDEF"  # define buttons all around <NAC><BTNNAME><HOLDABLE>
FMAXDO_SCTN408EVTYPEDEF = "FMAXDO_SCTN408EVTYPEDEF"  # define a device type list type<NAC>
FMAXDO_SCTN408EVTYPELST = "FMAXDO_SCTN408EVTYPELST"  # add a device list entry<NAC>
FMAXDO_SCTN409DIRTRANSDEVDEF = "FMAXDO_SCTN409DIRTRANSDEVDEF"  # add a dict to DO.py <NAV><DEVNAME>
FMAXDO_SCTN409DIRTRANSSTRADD = "FMAXDO_SCTN409DIRTRANSSTRADD"  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
FMAXDO_SCTN409DIRTRANSVALADD = "FMAXDO_SCTN409DIRTRANSVALADD"  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
FMAXDO_SCTN40AABSADD = "FMAXDO_SCTN40AABSADD"  # enable ABS entry for IDB
FMAXDO_SCTN40ABTNADD = "FMAXDO_SCTN40ABTNADD"  # enable BTN entry for IDB
FMAXDO_SCTN40AKEYADD = "FMAXDO_SCTN40AKEYADD"  # enable KEY entry for IDB
FMAXDO_SCTN40ARELADD = "FMAXDO_SCTN40ARELADD"  # enable REL entry for IDB
FMAXFM_SCTN101AXDEF = "FMAXFM_SCTN101AXDEF"  # define a new FM action <NAC>
FMAXFM_SCTN102VALDEF = "FMAXFM_SCTN102VALDEF"  # define a CM value_ <NAC><NAME><VAL>
FMAXFM_SCTN103DICTDEF = "FMAXFM_SCTN103DICTDEF"  # define a dict for FM <NAC>
FMAXFM_SCTN104LISTDEF = "FMAXFM_SCTN104LISTDEF"  # define a list in FM <NAC>
FMAXFO_SCTN301DICTDEF = "FMAXFO_SCTN301DICTDEF"  # define a dict in FO.py <NAC>
FMAX_NOP = "FMAX_NOP"  # skip this entry


FMAXFM_AXLST = [
	FMAXCF_SCTN003LAMBDADEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN003TYPEDEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN201STRDEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN201VALDEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN202PARMDEF,  # define a '-a[=]' in SCTN22 <NAC><PARM><VAL>
	FMAXCF_SCTN202STRENTRYADD,  # define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>
	FMAXCF_SCTN202VALENTRYADD,  # define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>
	FMAXCF_SCTN203DICTDEF,  # define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN203DICTSTRADD,  # define a dict STR in SCTN23 <NAC><DICTNAME><STR>
	FMAXCF_SCTN203DICTVALADD,  # define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN204LISTDEF,  # define a list in SCTN24 <NAC><LISTNAME>
	FMAXCF_SCTN204LISTSTRADD,  # define a list STR in SCTN24 <NAC><LISTNAME><STR>
	FMAXCF_SCTN204LISTVALADD,  # define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>
	FMAXDO_SCTN401DEVICEDEF,  # define a device in PROF <NAC><MYNAME><DEV_NAME>
	FMAXDO_SCTN401DICTKEYDEF,  # define a profile dict key <NAC><KEY>
	FMAXDO_SCTN401LAMBDADEF,  # define a profile lambda <NAC><NAME><LAMBDA>
	FMAXDO_SCTN401STRDEF,  # define a profile STR <NAC><NAME><VAL>
	FMAXDO_SCTN401VALDEF,  # define a profile value <NAC><NAME><VAL>
	FMAXDO_SCTN402LDIEABSDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN402LDIEBTNDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN402LDIEFUNCDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN402LDIEKEYDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN402LDIERELDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN402LDIESPCLDEF,  # define IE psuedo entry for special events
	FMAXDO_SCTN402LDIESYNDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN403AXDEF,  # define a profile action <NAC>
	FMAXDO_SCTN403AXVALADD,  # add an item to an action <NAC><AX><VAL>
	FMAXDO_SCTN404DEVICEENTRYSTRADD,  # define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>
	FMAXDO_SCTN404DEVICEENTRYVALADD,  # define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>
	FMAXDO_SCTN405HOLDABLEADD1,  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>
	FMAXDO_SCTN405HOLDABLEADD2,  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>
	FMAXDO_SCTN405NOTHOLDABLEADD1,  # not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>
	FMAXDO_SCTN405NOTHOLDABLEMODEDADD1,  # not holdable PROF items with a mode <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><MODENAME><NOTHOLDABLE><Ax>
	FMAXDO_SCTN406XLATEADD,  # add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>
	FMAXDO_SCTN407BTNSDEF,  # define buttons all around <NAC><BTNNAME><HOLDABLE>
	FMAXDO_SCTN408EVTYPEDEF,  # define a device type list type<NAC>
	FMAXDO_SCTN408EVTYPELST,  # add a device list entry<NAC>
	FMAXDO_SCTN409DIRTRANSDEVDEF,  # add a dict to DO.py <NAV><DEVNAME>
	FMAXDO_SCTN409DIRTRANSSTRADD,  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
	FMAXDO_SCTN409DIRTRANSVALADD,  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
	FMAXDO_SCTN40AABSADD,  # enable ABS entry for IDB
	FMAXDO_SCTN40ABTNADD,  # enable BTN entry for IDB
	FMAXDO_SCTN40AKEYADD,  # enable KEY entry for IDB
	FMAXDO_SCTN40ARELADD,  # enable REL entry for IDB
	FMAXFM_SCTN101AXDEF,  # define a new FM action <NAC>
	FMAXFM_SCTN102VALDEF,  # define a CM value_ <NAC><NAME><VAL>
	FMAXFM_SCTN103DICTDEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN104LISTDEF,  # define a list in FM <NAC>
	FMAXFO_SCTN301DICTDEF,  # define a dict in FO.py <NAC>
	FMAX_NOP,  # skip this entry
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN12 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN13 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMCF_SCTN003TYPECMNTDICT = {}  # SCTN09 types comments
FMCF_SCTN003TYPEDICT = {}  # SCTN03 types
FMCF_SCTN201DEFCMNTDICT = {}  # SCTN21 defines comments dict
FMCF_SCTN201DEFDICT = {}  # SCTN21 defines dict
FMCF_SCTN202OPTIONSCMNTDICT = {}  # SCTN22 options comments dict
FMCF_SCTN202OPTIONSDICT = {}  # SCTN22 options dict
FMCF_SCTN202PARMSCMNTDICT = {}  # SCTN22 options comments dict
FMCF_SCTN202PARMSDICT = {}  # SCTN22 options dict
FMCF_SCTN203DICTCMNTDICT = {}  # SCTN23 dict comments dict
FMCF_SCTN203DICTDICT = {}  # SCTN23 dict dict
FMCF_SCTN204LISTCMNTDICT = {}  # SCTN24 list comments dict
FMCF_SCTN204LISTDICT = {}  # SCTN24 list dict
FMDO_SCTN401DEVICEDEFCMNTDICT = {}  # SCTN21 device defines
FMDO_SCTN401DEVICEDEFDICT = {}  # SCTN21 device defines
FMDO_SCTN402LDIECMNTDICT = {}  # SCTN22 LDIE defined
FMDO_SCTN402LDIEDICT = {}  # SCTN22 LDIE defined
FMDO_SCTN403AXDEFCMNTDICT = {}  # SCTN23 output actions AX comments
FMDO_SCTN403AXDEFDICT = {}  # SCTN23 output actions AX
FMDO_SCTN404DEVICESCMNTDICT = {}  # SCTN24 device comments
FMDO_SCTN404DEVICESDICT = {}  # SCTN24 devices dict
FMDO_SCTN405BTNNDXDICT = {}  # SCTN45 device BTNTYPE dict
FMDO_SCTN405BTNTYPEDICT = {}  # SCTN45 device BTNTYPE dict
FMDO_SCTN405PROFDICT = {}  # SCTN45 device profile dict
FMDO_SCTN405RPTDICT = {}  # SCTN45 device RPT dict
FMDO_SCTN406XLATECMNTDICT = {}  # SCTN26 XLATE dict
FMDO_SCTN406XLATEDICT = {}  # SCTN26 XLATE dict
FMDO_SCTN407BTNSCMNTDICT = {}  # SCTN04 buttons
FMDO_SCTN407BTNSDICT = {}  # SCTN04 buttons
FMDO_SCTN408DEFCMNTDICT = {}  # define a device types list type
FMDO_SCTN408DEFDICT = {}  # define a device types list type
FMDO_SCTN408TYPESCMNTDICT = {}  # define a device types list type
FMDO_SCTN408TYPESDICT = {}  # define a device types list type
FMDO_SCTN409DIRTRANSCMNTDICT = {}  # holds dict for DO.py
FMDO_SCTN409DIRTRANSDICT = {}  # holds dict for DO.py
FMFM_SCTN101AXCMNTDICT = {}  # SCTN11 FMAX defined
FMFM_SCTN101AXDICT = {}  # SCTN11 FMAX defined
FMFM_SCTN102VALCMNTDICT = {}  # SCTN12 val
FMFM_SCTN102VALDICT = {}  # SCTN12 val
FMFM_SCTN103DICTCMNTDICT = {}  # SCTN13 dict defined
FMFM_SCTN103DICTDICT = {}  # SCTN13 dict defined
FMFM_SCTN104LISTCMNTDICT = {}  # SCTN21 device defines
FMFM_SCTN104LISTDICT = {}  # SCTN21 device defines


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN14 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMDO_SCTN402LDIERELLIST = []  # SCTN22 LDIE relative evdev actions defined
FMDO_SCTN402LDIESPCLLIST = []  # SCTN22 LDIE defined
FMDO_SCTN407BTNSHOLDABLELIST = []  # buttons holdable list
FMDO_SCTN40AHBIABSLIST = []  # SCTN50 list
FMDO_SCTN40AHBIBTNLIST = []  # SCTN51 list
FMDO_SCTN40AHBIKEYLIST = []  # SCTN52 list
FMDO_SCTN40AHBIRELLIST = []  # SCTN53 list


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


	global \
		FMCF_SCTN003TYPECMNTDICT, \
		FMCF_SCTN003TYPEDICT, \
		FMCF_SCTN201DEFCMNTDICT, \
		FMCF_SCTN201DEFDICT, \
		FMCF_SCTN202OPTIONSCMNTDICT, \
		FMCF_SCTN202OPTIONSDICT, \
		FMCF_SCTN202PARMSCMNTDICT, \
		FMCF_SCTN202PARMSDICT, \
		FMCF_SCTN203DICTCMNTDICT, \
		FMCF_SCTN203DICTDICT, \
		FMCF_SCTN204LISTCMNTDICT, \
		FMCF_SCTN204LISTDICT, \
		FMDO_SCTN401DEVICEDEFCMNTDICT, \
		FMDO_SCTN401DEVICEDEFDICT, \
		FMDO_SCTN402LDIECMNTDICT, \
		FMDO_SCTN402LDIEDICT, \
		FMDO_SCTN403AXDEFCMNTDICT, \
		FMDO_SCTN403AXDEFDICT, \
		FMDO_SCTN404DEVICESCMNTDICT, \
		FMDO_SCTN404DEVICESDICT, \
		FMDO_SCTN405BTNNDXDICT, \
		FMDO_SCTN405BTNTYPEDICT, \
		FMDO_SCTN405PROFDICT, \
		FMDO_SCTN405RPTDICT, \
		FMDO_SCTN406XLATECMNTDICT, \
		FMDO_SCTN406XLATEDICT, \
		FMDO_SCTN407BTNSCMNTDICT, \
		FMDO_SCTN407BTNSDICT, \
		FMDO_SCTN408DEFCMNTDICT, \
		FMDO_SCTN408DEFDICT, \
		FMDO_SCTN408TYPESCMNTDICT, \
		FMDO_SCTN408TYPESDICT, \
		FMDO_SCTN409DIRTRANSCMNTDICT, \
		FMDO_SCTN409DIRTRANSDICT, \
		FMFM_SCTN101AXCMNTDICT, \
		FMFM_SCTN101AXDICT, \
		FMFM_SCTN102VALCMNTDICT, \
		FMFM_SCTN102VALDICT, \
		FMFM_SCTN103DICTCMNTDICT, \
		FMFM_SCTN103DICTDICT, \
		FMFM_SCTN104LISTCMNTDICT, \
		FMFM_SCTN104LISTDICT, \
		FMDO_SCTN402LDIERELLIST, \
		FMDO_SCTN402LDIESPCLLIST, \
		FMDO_SCTN407BTNSHOLDABLELIST, \
		FMDO_SCTN40AHBIABSLIST, \
		FMDO_SCTN40AHBIBTNLIST, \
		FMDO_SCTN40AHBIKEYLIST, \
		FMDO_SCTN40AHBIRELLIST
