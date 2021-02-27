#!/usr/bin/python

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# sections
#
# SCTN0x CF/FM  CF and FM stuff
# SCTN1x FM     file maker FM.py
# SCTN2x CF     common features CF.py
# SCTN3x FO     file operations FO.py
# SCTN4x DO     device operations DO.py
# SCTN5x HBI    hot beef injection output definition
# SCTN6x SP     SP.py sections (subprocess)
# SCTN7x DB*    DB*.py sections where SQLT=sqlite, MDB=MariaDB
#
# SCTN01 CF/FM  character constants loaded from rcr/00-common into CF and FM
# SCTN02 CF/FM  the remainder of the constants loaded from rcr/00-common into CF and FM
# SCTN03 CF/FM  _TYPES_ created in FM.py into CF.py and FM.py
# SCTN04 DO/FM  buttons list and holdables etc
#
# SCTN11 FM     file maker FMAX all in
# SCTN12 FM     file maker _STR_, _VAL_
# SCTN13 FM     file maker _DICT_
# SCTN14 FM     file maker _LIST_
# SCTN15 FM     file maker TBGLST
#
# SCTN20 CF     CF top
# SCTN21 CF     CF alone defines
# SCTN22 CF     options structures ('-a[=]', 'OPTNAME: VAL')
# SCTN23 CF     dict defines <DICTMODE>==['STRIN':KEY | KEY: VAL|'STR'] STRIN|KEYIN
# SCTN24 CF     list defines
#
# SCTN30 FO     file operations top
# SCTN31 FO     file operations dict
#
# SCTN41 DO     device defines
# SCTN47 DO     buttons lists DO FM
# SCTN42 DO     LD.IE
# SCTN43 DO     device actions
# SCTN44 DO     device entries
# SCTN45 DO     device profile
# SCTN46 DO     device to common translation table
# SCTN48 DO     event type dict and list
# SCTN49 DO     DO translate ABS/REL to sim buttons

#
# SCTN50 HBI    HBI.py hot beef injector builder ABS lines
# SCTN51 HBI    HBI.py hot beef injector builder BTN lines
# SCTN52 HBI    HBI.py hot beef injector builder KEY lines
# SCTN53 HBI    HBI.py hot beef injector builder REL lines
#
# SCTN60 SP     SP.py defines
# SCTN61 SP     SP.py dicts
# SCTN62 SP     SP.py lists
# SCTN63 SP     SP.py tuple dict function sets
#
# SCTN70 DB*    DB defines
# SCTN71 DB*    DB dict
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#




# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * modules defined in this file
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeCF():
# * def makeDO():
# * def makeFM():
# * def parseTBGLST():
# * def readFileToStr(FILENAME_):
# * def __main__():



#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN01 _CHR_ _CONST_
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BKQT = "`"  # BACK TICK
BKSLSH = "\\"  # BACKSLASH
CBRCE = "}"  # CLOSEBRACE
CBRKT = "]"  # CLOSEBRACKET
CMNTLEN = 150
CONFIGDIR = "/home/will/.config/python/"
CPAREN = ")"  # CLOSE PARENTHESIS
DBLQT = "\""  # DOUBLE QUOTE
FOLDLEN = 75
NEWLINE = "\n"  # NEWLINE
OBRCE = "{"  # OPENBRACE
OBRKT = "["  # OPENBRACKET
OPAREN = "("  # OPENPAREN
SGLQT = "'"  # simple ' character
TABSTR = "\t"  # TAB


#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN02 value_ constants
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


BIN32 = lambda X: f"{X:032b}"
CFBTM_NAME = f"{CONFIGDIR}CFBTM.py"
CF_NAME = "newCF.py"
CFTOP_NAME = f"{CONFIGDIR}CFTOP.py"
CLRALL = "\033[2J"
CLREOL = "\033[K"
CLRDOWN = "\033[J"
CMNTLINE = "# * " + "#*" * CMNTLEN
DBSQLT_NAME = "newDBSQLT.py"
DO_NAME = "newDO.py"
EEOL = "\033[K"
_EMPTY_DICT_ = {}
_EMPTY_LIST_ = []
_EMPTY_STR_ = ""
EMPTYSTRLST = [None, "", DBLQT, DBLQT + DBLQT, "'", "''", "`", "None", "\r", "\n", "\r\n", "\n\r", ]
_EMPTY_TUPLE_ = ()
ESC = "\x1b"
FM_NAME = "newFM.py"
FOLD1ENDHERE = "# fold here " + "⥣1" * FOLDLEN
FOLD1STARTHERE = "# fold here " + "⥥1" * FOLDLEN
FOLD2ENDHERE = "# fold here " + "⥣2" * FOLDLEN
FOLD2STARTHERE = "# fold here " + "⥥2" * FOLDLEN
FOLD3ENDHERE = "# fold here " + "⥣3" * FOLDLEN
FOLD3STARTHERE = "# fold here " + "⥣3" * FOLDLEN
FO_NAME = "newFO.py"
HBI_NAME = "newHBI.py"
HEX08 = lambda X_: f"{X_:02H}"   # {thisComment_}
HEX16 = lambda X_: f"{X_:04H}"   # {thisComment_}
HEX32 = lambda X_: f"{X_:08H}"   # {thisComment_}
HEX64 = lambda X_: f"{X_:016H}"   # {thisComment_}
IMPORTANTSTR = "# * " + "!-" * CMNTLEN  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = "# * " + "%_" * CMNTLEN  # INFO _STR_ line\
LINESUP = lambda NUM_:  f"\033[{NUM_}A"
MARK1END = "# " + "⥣1 " * CMNTLEN
MARK1MID = "# " + "1⥣⥥1 " * (CMNTLEN // 2)
MARK1START = "# " + "⥥1 " * CMNTLEN
MARK2END = "# " + "⥣2 " * CMNTLEN
MARK2MID = "# " + "2⥣⥥2 " * (CMNTLEN // 2)
MARK2START = "# " + "⥥2 " * CMNTLEN
MARK3END = "# " + "⥣3 " * CMNTLEN
MARK3MID = "# " + "3⥣⥥3 " * (CMNTLEN // 2)
MARK3START = "# " + "⥥3 " * CMNTLEN
MARK4END = "# " + "⥣4 " * CMNTLEN
MARK4MID = "# " + "4⥣⥥4 " * (CMNTLEN // 2)
MARK4START = "# " + "⥥4 " * CMNTLEN
MARK5END = "# " + "⥣5 " * CMNTLEN
MARK5MID = "# " + "5⥣⥥5 " * (CMNTLEN // 2)
MARK5START = "# " + "⥥5 " * CMNTLEN
MARK6END = "# " + "⥣6 " * CMNTLEN
MARK6MID = "# " + "6⥣⥥6 " * (CMNTLEN // 2)
MARK6START = "# " + "⥥6 " * CMNTLEN
MARK7END = "# " + "⥣7 " * CMNTLEN
MARK7MID = "# " + "7⥣⥥7 " * (CMNTLEN // 2)
MARK7START = "# " + "⥥7 " * CMNTLEN
MARK8END = "# " + "⥣8 " * CMNTLEN
MARK8MID = "# " + "8⥣⥥8 " * (CMNTLEN // 2)
MARK8START = "# " + "⥥8 " * CMNTLEN
MARK9END = "# " + "⥣9 " * CMNTLEN
MARK9MID = "# " + "9⥣⥥9 " * (CMNTLEN // 2)
MARK9START = "# " + "⥥9 " * CMNTLEN
MOVETO = lambda LN_, COL_: f"\033[{LN_};{COL_}H"
NTAB = lambda NUM_: TABSTR * NUM_  # returns a string with _NUM_ TAB
QTSET = ['"', "'", "`"]  # set of all quote characters
SCTN0102NAME = f"{CONFIGDIR}SCTN0102.py"
SCTNSNAME = f"{CONFIGDIR}SCTNS.py"
SP_NAME = "newSP.py"
TBGLST_NAME = "TBGLST.py"
TRIQT = DBLQT + DBLQT + DBLQT  # works most of the time triple quote


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
BTNM_08 = "BTNM_08"  # BTNM_08/NW most BTN on mice
BTNM_09 = "BTNM_09"  # BTNM_09 on mice
BTNM_10 = "BTNM_10"  # BTNM_10 on mice
BTNM_11 = "BTNM_11"  # BTNM_11 on mice
BTNM_12 = "BTNM_12"  # BTNM_12/SE most on mice
BTNM_MDN = "BTNM_MDN"  # BTNMDN/MSE_DN on mice
BTNM_MDNLT = "BTNM_MDNLT"  # BTNMDN/MSE_DNLT on mice
BTNM_MDNRT = "BTNM_MDNRT"  # BTNMDN/MSE_DNRT on mice
BTNM_MLT = "BTNM_MLT"  # BTNMLT/MSE_LT on mice
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


BTNSHOLDABLELIST = [
]

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN11 FMAX _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMAXCF_SCTN03LAMBDADEF = "FMAXCF_SCTN03LAMBDADEF"  # define a lambda function <NAC><NAME><lambda str>
FMAXCF_SCTN03TYPEDEF = "FMAXCF_SCTN03TYPEDEF"  # define a fake type used in the translation dict <NAC><NAME><TYPE>
FMAXCF_SCTN21STRDEF = "FMAXCF_SCTN21STRDEF"  # define a STR in SCTN21 <NAC><NAME><str>
FMAXCF_SCTN21VALDEF = "FMAXCF_SCTN21VALDEF"  # define a VAL in SCTN21 <NAC><NAME><VAL>
FMAXCF_SCTN22PARMDEF = "FMAXCF_SCTN22PARMDEF"  # define a '-a[=]' in SCTN22 <NAC><PARM><VAL>
FMAXCF_SCTN22STRENTRYADD = "FMAXCF_SCTN22STRENTRYADD"  # define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>
FMAXCF_SCTN22VALENTRYADD = "FMAXCF_SCTN22VALENTRYADD"  # define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>
FMAXCF_SCTN23DICTDEF = "FMAXCF_SCTN23DICTDEF"  # define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>
FMAXCF_SCTN23DICTSTRADD = "FMAXCF_SCTN23DICTSTRADD"  # define a dict STR in SCTN23 <NAC><DICTNAME><STR>
FMAXCF_SCTN23DICTVALADD = "FMAXCF_SCTN23DICTVALADD"  # define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>
FMAXCF_SCTN24LISTDEF = "FMAXCF_SCTN24LISTDEF"  # define a list in SCTN24 <NAC><LISTNAME>
FMAXCF_SCTN24LISTSTRADD = "FMAXCF_SCTN24LISTSTRADD"  # define a list STR in SCTN24 <NAC><LISTNAME><STR>
FMAXCF_SCTN24LISTVALADD = "FMAXCF_SCTN24LISTVALADD"  # define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>
FMAXDO_SCTN41DEVICEDEF = "FMAXDO_SCTN41DEVICEDEF"  # define a device in PROF <NAC><MYNAME><DEV_NAME>
FMAXDO_SCTN41DICTKEYDEF = "FMAXDO_SCTN41DICTKEYDEF"  # define a profile dict key <NAC><KEY>
FMAXDO_SCTN41LAMBDADEF = "FMAXDO_SCTN41LAMBDADEF"  # define a profile lambda <NAC><NAME><LAMBDA>
FMAXDO_SCTN41STRDEF = "FMAXDO_SCTN41STRDEF"  # define a profile STR <NAC><NAME><VAL>
FMAXDO_SCTN41VALDEF = "FMAXDO_SCTN41VALDEF"  # define a profile value <NAC><NAME><VAL>
FMAXDO_SCTN42LDIEABSDEF = "FMAXDO_SCTN42LDIEABSDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN42LDIEBTNDEF = "FMAXDO_SCTN42LDIEBTNDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN42LDIEKEYDEF = "FMAXDO_SCTN42LDIEKEYDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN42LDIERELDEF = "FMAXDO_SCTN42LDIERELDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN42LDIESPCLDEF = "FMAXDO_SCTN42LDIESPCLDEF"  # define IE psuedo entry for special events
FMAXDO_SCTN42LDIESYNDEF = "FMAXDO_SCTN42LDIESYNDEF"  # define an IE entry (3) <NAC><IESTR><VAL>
FMAXDO_SCTN43AXDEF = "FMAXDO_SCTN43AXDEF"  # define a profile action <NAC>
FMAXDO_SCTN43AXVALADD = "FMAXDO_SCTN43AXVALADD"  # add an item to an action <NAC><AX><VAL>
FMAXDO_SCTN44DEVICEENTRYSTRADD = "FMAXDO_SCTN44DEVICEENTRYSTRADD"  # define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>
FMAXDO_SCTN44DEVICEENTRYVALADD = "FMAXDO_SCTN44DEVICEENTRYVALADD"  # define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>
FMAXDO_SCTN45HOLDABLEADD1 = "FMAXDO_SCTN45HOLDABLEADD1"  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>
FMAXDO_SCTN45HOLDABLEADD2 = "FMAXDO_SCTN45HOLDABLEADD2"  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>
FMAXDO_SCTN45NOTHOLDABLEADD1 = "FMAXDO_SCTN45NOTHOLDABLEADD1"  # not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>
FMAXDO_SCTN46XLATEADD = "FMAXDO_SCTN46XLATEADD"  # add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>
FMAXDO_SCTN47BTNSDEF = "FMAXDO_SCTN47BTNSDEF"  # define buttons all around <NAC><BTNNAME><HOLDABLE>
FMAXDO_SCTN48EVTYPEDEF = "FMAXDO_SCTN48EVTYPEDEF"  # define a device type list type<NAC>
FMAXDO_SCTN48EVTYPELST = "FMAXDO_SCTN48EVTYPELST"  # add a device list entry<NAC>
FMAXDO_SCTN49DIRTRANSDEVDEF = "FMAXDO_SCTN49DIRTRANSDEVDEF"  # add a dict to DO.py <NAV><DEVNAME>
FMAXDO_SCTN49DIRTRANSSTRADD = "FMAXDO_SCTN49DIRTRANSSTRADD"  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
FMAXDO_SCTN49DIRTRANSVALADD = "FMAXDO_SCTN49DIRTRANSVALADD"  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
FMAXFM_NOP = "FMAXFM_NOP"  # skip this entry
FMAXFM_SCTN11AXDEF = "FMAXFM_SCTN11AXDEF"  # define a new FM action <NAC>
FMAXFM_SCTN12VALDEF = "FMAXFM_SCTN12VALDEF"  # define a CM value_ <NAC><NAME><VAL>
FMAXFM_SCTN13DICTDEF = "FMAXFM_SCTN13DICTDEF"  # define a dict for FM <NAC>
FMAXFM_SCTN14LISTDEF = "FMAXFM_SCTN14LISTDEF"  # define a list in FM <NAC>
FMAXFO_SCTN31DICTDEF = "FMAXFO_SCTN31DICTDEF"  # define a dict in FO.py <NAC>
FMAXHBI_SCTN50ABSADD = "FMAXHBI_SCTN50ABSADD"  # enable ABS entry for IDB
FMAXHBI_SCTN51BTNADD = "FMAXHBI_SCTN51BTNADD"  # enable BTN entry for IDB
FMAXHBI_SCTN52KEYADD = "FMAXHBI_SCTN52KEYADD"  # enable KEY entry for IDB
FMAXHBI_SCTN53RELADD = "FMAXHBI_SCTN53RELADD"  # enable REL entry for IDB


FMAXFM_AXLST = [
	FMAXCF_SCTN03LAMBDADEF,  # define a lambda function <NAC><NAME><lambda str>
	FMAXCF_SCTN03TYPEDEF,  # define a fake type used in the translation dict <NAC><NAME><TYPE>
	FMAXCF_SCTN21STRDEF,  # define a STR in SCTN21 <NAC><NAME><str>
	FMAXCF_SCTN21VALDEF,  # define a VAL in SCTN21 <NAC><NAME><VAL>
	FMAXCF_SCTN22PARMDEF,  # define a '-a[=]' in SCTN22 <NAC><PARM><VAL>
	FMAXCF_SCTN22STRENTRYADD,  # define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>
	FMAXCF_SCTN22VALENTRYADD,  # define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>
	FMAXCF_SCTN23DICTDEF,  # define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>
	FMAXCF_SCTN23DICTSTRADD,  # define a dict STR in SCTN23 <NAC><DICTNAME><STR>
	FMAXCF_SCTN23DICTVALADD,  # define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>
	FMAXCF_SCTN24LISTDEF,  # define a list in SCTN24 <NAC><LISTNAME>
	FMAXCF_SCTN24LISTSTRADD,  # define a list STR in SCTN24 <NAC><LISTNAME><STR>
	FMAXCF_SCTN24LISTVALADD,  # define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>
	FMAXDO_SCTN41DEVICEDEF,  # define a device in PROF <NAC><MYNAME><DEV_NAME>
	FMAXDO_SCTN41DICTKEYDEF,  # define a profile dict key <NAC><KEY>
	FMAXDO_SCTN41LAMBDADEF,  # define a profile lambda <NAC><NAME><LAMBDA>
	FMAXDO_SCTN41STRDEF,  # define a profile STR <NAC><NAME><VAL>
	FMAXDO_SCTN41VALDEF,  # define a profile value <NAC><NAME><VAL>
	FMAXDO_SCTN42LDIEABSDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN42LDIEBTNDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN42LDIEKEYDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN42LDIERELDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN42LDIESPCLDEF,  # define IE psuedo entry for special events
	FMAXDO_SCTN42LDIESYNDEF,  # define an IE entry (3) <NAC><IESTR><VAL>
	FMAXDO_SCTN43AXDEF,  # define a profile action <NAC>
	FMAXDO_SCTN43AXVALADD,  # add an item to an action <NAC><AX><VAL>
	FMAXDO_SCTN44DEVICEENTRYSTRADD,  # define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>
	FMAXDO_SCTN44DEVICEENTRYVALADD,  # define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>
	FMAXDO_SCTN45HOLDABLEADD1,  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>
	FMAXDO_SCTN45HOLDABLEADD2,  # define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>
	FMAXDO_SCTN45NOTHOLDABLEADD1,  # not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>
	FMAXDO_SCTN46XLATEADD,  # add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>
	FMAXDO_SCTN47BTNSDEF,  # define buttons all around <NAC><BTNNAME><HOLDABLE>
	FMAXDO_SCTN48EVTYPEDEF,  # define a device type list type<NAC>
	FMAXDO_SCTN48EVTYPELST,  # add a device list entry<NAC>
	FMAXDO_SCTN49DIRTRANSDEVDEF,  # add a dict to DO.py <NAV><DEVNAME>
	FMAXDO_SCTN49DIRTRANSSTRADD,  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
	FMAXDO_SCTN49DIRTRANSVALADD,  # add a dict to DO.py <NAV><DEVNAME><KEY><VAL>
	FMAXFM_NOP,  # skip this entry
	FMAXFM_SCTN11AXDEF,  # define a new FM action <NAC>
	FMAXFM_SCTN12VALDEF,  # define a CM value_ <NAC><NAME><VAL>
	FMAXFM_SCTN13DICTDEF,  # define a dict for FM <NAC>
	FMAXFM_SCTN14LISTDEF,  # define a list in FM <NAC>
	FMAXFO_SCTN31DICTDEF,  # define a dict in FO.py <NAC>
	FMAXHBI_SCTN50ABSADD,  # enable ABS entry for IDB
	FMAXHBI_SCTN51BTNADD,  # enable BTN entry for IDB
	FMAXHBI_SCTN52KEYADD,  # enable KEY entry for IDB
	FMAXHBI_SCTN53RELADD,  # enable REL entry for IDB
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN12 VAL _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN13 _DICT_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMCF_SCTN03TYPECMNTDICT = {}  # SCTN09 types comments
FMCF_SCTN03TYPEDICT = {}  # SCTN03 types
FMCF_SCTN21DEFCMNTDICT = {}  # SCTN21 defines comments dict
FMCF_SCTN21DEFDICT = {}  # SCTN21 defines dict
FMCF_SCTN22OPTIONSCMNTDICT = {}  # SCTN22 options comments dict
FMCF_SCTN22OPTIONSDICT = {}  # SCTN22 options dict
FMCF_SCTN22PARMSCMNTDICT = {}  # SCTN22 options comments dict
FMCF_SCTN22PARMSDICT = {}  # SCTN22 options dict
FMCF_SCTN23DICTCMNTDICT = {}  # SCTN23 dict comments dict
FMCF_SCTN23DICTDICT = {}  # SCTN23 dict dict
FMCF_SCTN24LISTCMNTDICT = {}  # SCTN24 list comments dict
FMCF_SCTN24LISTDICT = {}  # SCTN24 list dict
FMDO_SCTN41DEVICEDEFCMNTDICT = {}  # SCTN21 device defines
FMDO_SCTN41DEVICEDEFDICT = {}  # SCTN21 device defines
FMDO_SCTN42LDIECMNTDICT = {}  # SCTN22 LDIE defined
FMDO_SCTN42LDIEDICT = {}  # SCTN22 LDIE defined
FMDO_SCTN43AXDEFCMNTDICT = {}  # SCTN23 output actions AX comments
FMDO_SCTN43AXDEFDICT = {}  # SCTN23 output actions AX
FMDO_SCTN44DEVICESCMNTDICT = {}  # SCTN24 device comments
FMDO_SCTN44DEVICESDICT = {}  # SCTN24 devices dict
FMDO_SCTN45BTNTYPEDICT = {}  # SCTN25 device BTNTYPE dict
FMDO_SCTN45PROFDICT = {}  # SCTN25 device profile dict
FMDO_SCTN45RPTDICT = {}  # SCTN25 device RPT dict
FMDO_SCTN46XLATECMNTDICT = {}  # SCTN26 XLATE dict
FMDO_SCTN46XLATEDICT = {}  # SCTN26 XLATE dict
FMDO_SCTN47BTNSCMNTDICT = {}  # SCTN04 buttons
FMDO_SCTN47BTNSDICT = {}  # SCTN04 buttons
FMDO_SCTN48DEFCMNTDICT = {}  # define a device types list type
FMDO_SCTN48DEFDICT = {}  # define a device types list type
FMDO_SCTN48TYPESCMNTDICT = {}  # define a device types list type
FMDO_SCTN48TYPESDICT = {}  # define a device types list type
FMDO_SCTN49DIRTRANSCMNTDICT = {}  # holds dict for DO.py
FMDO_SCTN49DIRTRANSDICT = {}  # holds dict for DO.py
FMFM_SCTN11AXCMNTDICT = {}  # SCTN11 FMAX defined
FMFM_SCTN11AXDICT = {}  # SCTN11 FMAX defined
FMFM_SCTN12VALCMNTDICT = {}  # SCTN12 val
FMFM_SCTN12VALDICT = {}  # SCTN12 val
FMFM_SCTN13DICTCMNTDICT = {}  # SCTN13 dict defined
FMFM_SCTN13DICTDICT = {}  # SCTN13 dict defined
FMFM_SCTN14LISTCMNTDICT = {}  # SCTN21 device defines
FMFM_SCTN14LISTDICT = {}  # SCTN21 device defines


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN14 _LIST_ _DEF_
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FMDO_SCTN42LDIESPCLLIST = []  # SCTN22 LDIE defined
FMDO_SCTN47BTNSHOLDABLELIST = []  # buttons holdable list
FMHBI_SCTN50HBIABSLIST = []  # SCTN50 list
FMHBI_SCTN51HBIBTNLIST = []  # SCTN51 list
FMHBI_SCTN52HBIKEYLIST = []  # SCTN52 list
FMHBI_SCTN53HBIRELLIST = []  # SCTN53 list


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed portions of FM.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#  SCTN15 TBGLST NAME, ACTION, PARAMS, COMMENT
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!


TBGLST = [
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	("AXDSKTP1", FMAXDO_SCTN43AXDEF, "desktop #1",),
	("AXDSKTP101", FMAXDO_SCTN43AXVALADD, "AXDSKTP1", "KBDALTLT_PRS", "press ALT",),
	("AXDSKTP102", FMAXDO_SCTN43AXVALADD, "AXDSKTP1", "KBD1_PRS", "press 1",),
	("AXDSKTP103", FMAXDO_SCTN43AXVALADD, "AXDSKTP1", "KBD1_RLS", "release 1",),
	("AXDSKTP104", FMAXDO_SCTN43AXVALADD, "AXDSKTP1", "KBDALTLT_RLS", "release ALT",),
	("AXDSKTP105", FMAXDO_SCTN43AXVALADD, "AXDSKTP1", "SYNREPORT", "SYNREPORT",),
	("AXDSKTP2", FMAXDO_SCTN43AXDEF, "desktop #2",),
	("AXDSKTP201", FMAXDO_SCTN43AXVALADD, "AXDSKTP2", "KBDALTLT_PRS", "press ALT",),
	("AXDSKTP202", FMAXDO_SCTN43AXVALADD, "AXDSKTP2", "KBD2_PRS", "press 2",),
	("AXDSKTP203", FMAXDO_SCTN43AXVALADD, "AXDSKTP2", "KBD2_RLS", "release 2",),
	("AXDSKTP204", FMAXDO_SCTN43AXVALADD, "AXDSKTP2", "KBDALTLT_RLS", "release ALT",),
	("AXDSKTP205", FMAXDO_SCTN43AXVALADD, "AXDSKTP2", "SYNREPORT", "SYNREPORT",),
	("AXDSKTP3", FMAXDO_SCTN43AXDEF, "desktop #3",),
	("AXDSKTP301", FMAXDO_SCTN43AXVALADD, "AXDSKTP3", "KBDALTLT_PRS", "press ALT",),
	("AXDSKTP302", FMAXDO_SCTN43AXVALADD, "AXDSKTP3", "KBD3_PRS", "press 3",),
	("AXDSKTP303", FMAXDO_SCTN43AXVALADD, "AXDSKTP3", "KBD3_RLS", "release 3",),
	("AXDSKTP304", FMAXDO_SCTN43AXVALADD, "AXDSKTP3", "KBDALTLT_RLS", "release ALT",),
	("AXDSKTP305", FMAXDO_SCTN43AXVALADD, "AXDSKTP3", "SYNREPORT", "SYNREPORT",),
	("AXDSKTP4", FMAXDO_SCTN43AXDEF, "desktop #4",),
	("AXDSKTP401", FMAXDO_SCTN43AXVALADD, "AXDSKTP4", "KBDALTLT_PRS", "press ALT",),
	("AXDSKTP402", FMAXDO_SCTN43AXVALADD, "AXDSKTP4", "KBD4_PRS", "press 4",),
	("AXDSKTP403", FMAXDO_SCTN43AXVALADD, "AXDSKTP4", "KBD4_RLS", "release 4",),
	("AXDSKTP404", FMAXDO_SCTN43AXVALADD, "AXDSKTP4", "KBDALTLT_RLS", "release ALT",),
	("AXDSKTP405", FMAXDO_SCTN43AXVALADD, "AXDSKTP4", "SYNREPORT", "SYNREPORT",),
	("AXGIMPOVWRT", FMAXDO_SCTN43AXDEF, "GIMP overwrite imported file",),
	("AXGIMPOVWRT01", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBDALTLT_PRS", "press ALT",),
	("AXGIMPOVWRT02", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBDCTRLLT_PRS", "press LCTRL",),
	("AXGIMPOVWRT03", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBDSHIFTLT_PRS", "press LSHIFT",),
	("AXGIMPOVWRT04", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBD4_PRS", "press 4",),
	("AXGIMPOVWRT05", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBD4_RLS", "release 4",),
	("AXGIMPOVWRT06", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBDSHIFTLT_RLS", "release LSHIFT",),
	("AXGIMPOVWRT07", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBDCTRLLT_RLS", "release LCTRL",),
	("AXGIMPOVWRT08", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "KBDALTLT_RLS", "release ALT",),
	("AXGIMPOVWRT09", FMAXDO_SCTN43AXVALADD, "AXGIMPOVWRT", "SYNREPORT", "SYNREPORT",),
	("AXHRHWLDN", FMAXDO_SCTN43AXDEF, "high rez wheel DOWN",),
	("AXHRHWLDN00", FMAXDO_SCTN43AXVALADD, "AXHRHWLDN", "MSEWHL_DN", "move WHL down 1 unit",),
	("AXHRHWLDN01", FMAXDO_SCTN43AXVALADD, "AXHRHWLDN", "SYNREPORT", "SYNREPORT",),
	("AXHRHWLLT", FMAXDO_SCTN43AXDEF, "high rez wheel LEFT",),
	("AXHRHWLLT00", FMAXDO_SCTN43AXVALADD, "AXHRHWLLT", "MSEWHL_LT", "move WHL left 1 unit",),
	("AXHRHWLLT01", FMAXDO_SCTN43AXVALADD, "AXHRHWLLT", "SYNREPORT", "SYNREPORT",),
	("AXHRHWLRT", FMAXDO_SCTN43AXDEF, "high rez wheel RIGHT",),
	("AXHRHWLRT00", FMAXDO_SCTN43AXVALADD, "AXHRHWLRT", "MSEWHL_RT", "move WHL right 1 unit",),
	("AXHRHWLRT01", FMAXDO_SCTN43AXVALADD, "AXHRHWLRT", "SYNREPORT", "SYNREPORT",),
	("AXHRHWLUP", FMAXDO_SCTN43AXDEF, "high rez wheel UP",),
	("AXHRHWLUP00", FMAXDO_SCTN43AXVALADD, "AXHRHWLUP", "MSEWHL_UP", "move WHL up 1 unit",),
	("AXHRHWLUP01", FMAXDO_SCTN43AXVALADD, "AXHRHWLUP", "SYNREPORT", "SYNREPORT",),
	("AXMCCOPY", FMAXDO_SCTN43AXDEF, "MC copy F5, ENTER",),
	("AXMCCOPY01", FMAXDO_SCTN43AXVALADD, "AXMCCOPY", "KBDF5_PRS", "press F5",),
	("AXMCCOPY02", FMAXDO_SCTN43AXVALADD, "AXMCCOPY", "KBDF5_RLS", "release F5",),
	("AXMCCOPY03", FMAXDO_SCTN43AXVALADD, "AXMCCOPY", "SYNREPORT", "SYNREPORT",),
	("AXMCDEL", FMAXDO_SCTN43AXDEF, "MC del F8, ENTER",),
	("AXMCDEL01", FMAXDO_SCTN43AXVALADD, "AXMCDEL", "KBDF8_PRS", "press F8",),
	("AXMCDEL02", FMAXDO_SCTN43AXVALADD, "AXMCDEL", "KBDF8_RLS", "release F8",),
	("AXMCDEL03", FMAXDO_SCTN43AXVALADD, "AXMCDEL", "SYNREPORT", "SYNREPORT",),
	("AXMCMOVE", FMAXDO_SCTN43AXDEF, "MC move F6, ENTER",),
	("AXMCMOVE01", FMAXDO_SCTN43AXVALADD, "AXMCMOVE", "KBDF6_PRS", "press F6",),
	("AXMCMOVE02", FMAXDO_SCTN43AXVALADD, "AXMCMOVE", "KBDF6_RLS", "release F6",),
	("AXMCMOVE03", FMAXDO_SCTN43AXVALADD, "AXMCMOVE", "SYNREPORT", "SYNREPORT",),
	("AXMCSEL", FMAXDO_SCTN43AXDEF, "MC select INS",),
	("AXMCSEL01", FMAXDO_SCTN43AXVALADD, "AXMCSEL", "KBDINSERT_PRS", "press INSERT",),
	("AXMCSEL02", FMAXDO_SCTN43AXVALADD, "AXMCSEL", "KBDINSERT_RLS", "release INSERT",),
	("AXMCSEL03", FMAXDO_SCTN43AXVALADD, "AXMCSEL", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNBAK", FMAXDO_SCTN43AXDEF, "MSE BTN BACK",),
	("AXMSEBTNBAK01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNBAK", "MSEBTNBAK_PRSHLD", "press MSEBTNBAK",),
	("AXMSEBTNBAK02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNBAK", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNBAK03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNBAK", "MSEBTNBAK_RLS", "release MSEBTNBAK",),
	("AXMSEBTNBAK04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNBAK", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNFWD", FMAXDO_SCTN43AXDEF, "MSE BTN FWD",),
	("AXMSEBTNFWD01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNFWD", "MSEBTNFWD_PRSHLD", "press MSEBTNFWD",),
	("AXMSEBTNFWD02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNFWD", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNFWD03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNFWD", "MSEBTNFWD_RLS", "release MSEBTNFWD",),
	("AXMSEBTNFWD04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNFWD", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNLT", FMAXDO_SCTN43AXDEF, "MSE BTN LEFT",),
	("AXMSEBTNLT01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNLT", "MSEBTNLT_PRSHLD", "press MSEBTNLT",),
	("AXMSEBTNLT02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNLT03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNLT", "MSEBTNLT_RLS", "release MSEBTNLT",),
	("AXMSEBTNLT04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNMID", FMAXDO_SCTN43AXDEF, "MSE BTN MIDDLE",),
	("AXMSEBTNMID01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNMID", "MSEBTNMID_PRSHLD", "press MSEBTNMID",),
	("AXMSEBTNMID02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNMID", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNMID03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNMID", "MSEBTNMID_RLS", "release MSEBTNMID",),
	("AXMSEBTNMID04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNMID", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNRT", FMAXDO_SCTN43AXDEF, "MSE BTN RIGHT",),
	("AXMSEBTNRT01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNRT", "MSEBTNRT_PRSHLD", "press MSEBTNRT",),
	("AXMSEBTNRT02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNRT", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNRT03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNRT", "MSEBTNRT_RLS", "release MSEBTNRT",),
	("AXMSEBTNRT04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNRT", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNSIDE", FMAXDO_SCTN43AXDEF, "MSE BTN SIDE",),
	("AXMSEBTNSIDE01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNSIDE", "MSEBTNSIDE_PRSHLD", "press MSEBTNSIDE",),
	("AXMSEBTNSIDE02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNSIDE", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNSIDE03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNSIDE", "MSEBTNSIDE_RLS", "release MSEBTNSIDE",),
	("AXMSEBTNSIDE04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNSIDE", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNTASK", FMAXDO_SCTN43AXDEF, "MSE BTN TASK",),
	("AXMSEBTNTASK01", FMAXDO_SCTN43AXVALADD, "AXMSEBTNTASK", "MSEBTNTASK_PRSHLD", "press MSEBTNTASK",),
	("AXMSEBTNTASK02", FMAXDO_SCTN43AXVALADD, "AXMSEBTNTASK", "SYNREPORT", "SYNREPORT",),
	("AXMSEBTNTASK03", FMAXDO_SCTN43AXVALADD, "AXMSEBTNTASK", "MSEBTNTASK_RLS", "release MSEBTNTASK",),
	("AXMSEBTNTASK04", FMAXDO_SCTN43AXVALADD, "AXMSEBTNTASK", "SYNREPORT", "SYNREPORT",),
	("AXMSEDN", FMAXDO_SCTN43AXDEF, "MSE DOWN",),
	("AXMSEDN01", FMAXDO_SCTN43AXVALADD, "AXMSEDN", "MSE_DN", "MSE_DN by MOUSEDISTANCE",),
	("AXMSEDN02", FMAXDO_SCTN43AXVALADD, "AXMSEDN", "SYNREPORT", "SYNREPORT",),
	("AXMSEDNLT", FMAXDO_SCTN43AXDEF, "MSE DOWNLT",),
	("AXMSEDNLT01", FMAXDO_SCTN43AXVALADD, "AXMSEDNLT", "MSE_DN", "MSE_DN by MOUSEDISTANCE",),
	("AXMSEDNLT02", FMAXDO_SCTN43AXVALADD, "AXMSEDNLT", "MSE_LT", "MSE_LT by MOUSEDISTANCE",),
	("AXMSEDNLT03", FMAXDO_SCTN43AXVALADD, "AXMSEDNLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEDNRT", FMAXDO_SCTN43AXDEF, "MSE DOWNRT",),
	("AXMSEDNRT01", FMAXDO_SCTN43AXVALADD, "AXMSEDNRT", "MSE_DN", "MSE_DN by MOUSEDISTANCE",),
	("AXMSEDNRT02", FMAXDO_SCTN43AXVALADD, "AXMSEDNRT", "MSE_RT", "MSE_RT by MOUSEDISTANCE",),
	("AXMSEDNRT03", FMAXDO_SCTN43AXVALADD, "AXMSEDNRT", "SYNREPORT", "SYNREPORT",),
	("AXMSELT", FMAXDO_SCTN43AXDEF, "MSE LEFT",),
	("AXMSELT01", FMAXDO_SCTN43AXVALADD, "AXMSELT", "MSE_LT", "MSE_LT by MOUSEDISTANCE",),
	("AXMSELT02", FMAXDO_SCTN43AXVALADD, "AXMSELT", "SYNREPORT", "SYNREPORT",),
	("AXMSERT", FMAXDO_SCTN43AXDEF, "MSE RIGHT",),
	("AXMSERT01", FMAXDO_SCTN43AXVALADD, "AXMSERT", "MSE_RT", "MSE_RT by MOUSEDISTANCE",),
	("AXMSERT02", FMAXDO_SCTN43AXVALADD, "AXMSERT", "SYNREPORT", "SYNREPORT",),
	("AXMSEUP", FMAXDO_SCTN43AXDEF, "MSE UP",),
	("AXMSEUP01", FMAXDO_SCTN43AXVALADD, "AXMSEUP", "MSE_UP", "MSE_UP by MOUSEDISTANCE",),
	("AXMSEUP02", FMAXDO_SCTN43AXVALADD, "AXMSEUP", "SYNREPORT", "SYNREPORT",),
	("AXMSEUPLT", FMAXDO_SCTN43AXDEF, "MSE UPLT",),
	("AXMSEUPLT01", FMAXDO_SCTN43AXVALADD, "AXMSEUPLT", "MSE_LT", "MSE_LT by MOUSEDISTANCE",),
	("AXMSEUPLT01", FMAXDO_SCTN43AXVALADD, "AXMSEUPLT", "MSE_UP", "MSE_UP by MOUSEDISTANCE",),
	("AXMSEUPLT02", FMAXDO_SCTN43AXVALADD, "AXMSEUPLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEUPRT", FMAXDO_SCTN43AXDEF, "MSE UPRT",),
	("AXMSEUPRT01", FMAXDO_SCTN43AXVALADD, "AXMSEUPRT", "MSE_RT", "MSE_RT by MOUSEDISTANCE",),
	("AXMSEUPRT01", FMAXDO_SCTN43AXVALADD, "AXMSEUPRT", "MSE_UP", "MSE_UP by MOUSEDISTANCE",),
	("AXMSEUPRT02", FMAXDO_SCTN43AXVALADD, "AXMSEUPRT", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLDN", FMAXDO_SCTN43AXDEF, "wheel DOWN",),
	("AXMSEWHLDN01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDN", "MSEWHL_DN", "wheel DOWN",),
	("AXMSEWHLDN02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDN", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLDNLT", FMAXDO_SCTN43AXDEF, "wheel DNLT",),
	("AXMSEWHLDNLT01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDNLT", "MSEWHL_DN", "wheel DOWN",),
	("AXMSEWHLDNLT02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDNLT", "MSEWHL_LT", "wheel LEFT",),
	("AXMSEWHLDNLT03", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDNLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLDNRT", FMAXDO_SCTN43AXDEF, "wheel DNRT",),
	("AXMSEWHLDNRT01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDNRT", "MSEWHL_DN", "wheel DOWN",),
	("AXMSEWHLDNRT02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDNRT", "MSEWHL_RT", "wheel RIGHT",),
	("AXMSEWHLDNRT03", FMAXDO_SCTN43AXVALADD, "AXMSEWHLDNRT", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLLT", FMAXDO_SCTN43AXDEF, "wheel LEFT",),
	("AXMSEWHLLT01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLLT", "MSEWHL_LT", "wheel LEFT",),
	("AXMSEWHLLT02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLRT", FMAXDO_SCTN43AXDEF, "wheel RIGHT",),
	("AXMSEWHLRT01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLRT", "MSEWHL_RT", "wheel RIGHT",),
	("AXMSEWHLRT02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLRT", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLUP", FMAXDO_SCTN43AXDEF, "wheel UP",),
	("AXMSEWHLUP01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUP", "MSEWHL_UP", "wheel UP",),
	("AXMSEWHLUP02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUP", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLUPLT", FMAXDO_SCTN43AXDEF, "wheel UPLT",),
	("AXMSEWHLUPLT01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUPLT", "MSEWHL_UP", "wheel UP",),
	("AXMSEWHLUPLT02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUPLT", "MSEWHL_LT", "wheel LEFT",),
	("AXMSEWHLUPLT03", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUPLT", "SYNREPORT", "SYNREPORT",),
	("AXMSEWHLUPRT", FMAXDO_SCTN43AXDEF, "wheel UPRT",),
	("AXMSEWHLUPRT01", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUPRT", "MSEWHL_UP", "wheel UP",),
	("AXMSEWHLUPRT02", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUPRT", "MSEWHL_RT", "wheel RIGHT",),
	("AXMSEWHLUPRT03", FMAXDO_SCTN43AXVALADD, "AXMSEWHLUPRT", "SYNREPORT", "SYNREPORT",),
	("AXSAVE", FMAXDO_SCTN43AXDEF, "save CTRL-S",),
	("AXSAVE01", FMAXDO_SCTN43AXVALADD, "AXSAVE", "KBDCTRLLT_PRS", "press CTRL",),
	("AXSAVE02", FMAXDO_SCTN43AXVALADD, "AXSAVE", "KBDS_PRS", "press S",),
	("AXSAVE03", FMAXDO_SCTN43AXVALADD, "AXSAVE", "KBDS_RLS", "release S",),
	("AXSAVE04", FMAXDO_SCTN43AXVALADD, "AXSAVE", "KBDCTRLLT_RLS", "release CTRL",),
	("AXSAVE05", FMAXDO_SCTN43AXVALADD, "AXSAVE", "SYNREPORT", "SYNREPORT",),
	("AXXNVCOPYTO", FMAXDO_SCTN43AXDEF, "XnViewer COPYTO ALT-C",),
	("AXXNVCOPYTO01", FMAXDO_SCTN43AXVALADD, "AXXNVCOPYTO", "KBDALTLT_PRS", "press ALT",),
	("AXXNVCOPYTO02", FMAXDO_SCTN43AXVALADD, "AXXNVCOPYTO", "KBDS_PRS", "press S",),
	("AXXNVCOPYTO03", FMAXDO_SCTN43AXVALADD, "AXXNVCOPYTO", "KBDS_RLS", "release S",),
	("AXXNVCOPYTO04", FMAXDO_SCTN43AXVALADD, "AXXNVCOPYTO", "KBDALTLT_RLS", "release ALT",),
	("AXXNVCOPYTO05", FMAXDO_SCTN43AXVALADD, "AXXNVCOPYTO", "SYNREPORT", "SYNREPORT",),
	("AXXNVCROP", FMAXDO_SCTN43AXDEF, "XnViewer CROP SHIFT-X",),
	("AXXNVCROP01", FMAXDO_SCTN43AXVALADD, "AXXNVCROP", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AXXNVCROP02", FMAXDO_SCTN43AXVALADD, "AXXNVCROP", "KBDX_PRS", "press X",),
	("AXXNVCROP03", FMAXDO_SCTN43AXVALADD, "AXXNVCROP", "KBDX_RLS", "release X",),
	("AXXNVCROP04", FMAXDO_SCTN43AXVALADD, "AXXNVCROP", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AXXNVCROP05", FMAXDO_SCTN43AXVALADD, "AXXNVCROP", "SYNREPORT", "SYNREPORT",),
	("AXXNVFLIPH", FMAXDO_SCTN43AXDEF, "XnViewer FLIP horizontal ALT-F",),
	("AXXNVFLIPH01", FMAXDO_SCTN43AXVALADD, "AXXNVFLIPH", "KBDALTLT_PRS", "press ALT",),
	("AXXNVFLIPH02", FMAXDO_SCTN43AXVALADD, "AXXNVFLIPH", "KBDF_PRS", "press F",),
	("AXXNVFLIPH03", FMAXDO_SCTN43AXVALADD, "AXXNVFLIPH", "KBDF_RLS", "release F",),
	("AXXNVFLIPH04", FMAXDO_SCTN43AXVALADD, "AXXNVFLIPH", "KBDALTLT_RLS", "release ALT",),
	("AXXNVFLIPH05", FMAXDO_SCTN43AXVALADD, "AXXNVFLIPH", "SYNREPORT", "SYNREPORT",),
	("AXXNVMOVE", FMAXDO_SCTN43AXDEF, "XnViewer MOVE ALT-M",),
	("AXXNVMOVE01", FMAXDO_SCTN43AXVALADD, "AXXNVMOVE", "KBDALTLT_PRS", "press ALT",),
	("AXXNVMOVE02", FMAXDO_SCTN43AXVALADD, "AXXNVMOVE", "KBDM_PRS", "press M",),
	("AXXNVMOVE03", FMAXDO_SCTN43AXVALADD, "AXXNVMOVE", "KBDM_RLS", "release M",),
	("AXXNVMOVE04", FMAXDO_SCTN43AXVALADD, "AXXNVMOVE", "KBDALTLT_RLS", "release ALT",),
	("AXXNVMOVE05", FMAXDO_SCTN43AXVALADD, "AXXNVMOVE", "SYNREPORT", "SYNREPORT",),
	("AXXNVROTLT", FMAXDO_SCTN43AXDEF, "XnViewer ROT LEFT CTRL-SHIFT-L",),
	("AXXNVROTLT01", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AXXNVROTLT02", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "KBDCTRLLT_PRS", "press CTRL",),
	("AXXNVROTLT03", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "KBDL_PRS", "press L",),
	("AXXNVROTLT04", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "KBDL_RLS", "release L",),
	("AXXNVROTLT05", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "KBDCTRLLT_RLS", "release CTRL",),
	("AXXNVROTLT06", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AXXNVROTLT07", FMAXDO_SCTN43AXVALADD, "AXXNVROTLT", "SYNREPORT", "SYNREPORT",),
	("AXXNVROTRT", FMAXDO_SCTN43AXDEF, "XnViewer ROT RIGHT CTRL-SHIFT-R",),
	("AXXNVROTRT01", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AXXNVROTRT02", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "KBDCTRLLT_PRS", "press CTRL",),
	("AXXNVROTRT03", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "KBDR_PRS", "press R",),
	("AXXNVROTRT04", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "KBDR_RLS", "release R",),
	("AXXNVROTRT05", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "KBDCTRLLT_RLS", "release CTRL",),
	("AXXNVROTRT06", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AXXNVROTRT07", FMAXDO_SCTN43AXVALADD, "AXXNVROTRT", "SYNREPORT", "SYNREPORT",),
	("AXXNVSEL2TOP", FMAXDO_SCTN43AXDEF, "XnViewer SELECT to top SHIFT-HOME, SHIFT-RIGHT",),
	("AXXNVSEL2TOP01", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AXXNVSEL2TOP02", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "KBDHOME_PRS", "press HOME",),
	("AXXNVSEL2TOP03", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "KBDHOME_RLS", "release HOME",),
	("AXXNVSEL2TOP04", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "KBDRT_PRS", "press RIGHT",),
	("AXXNVSEL2TOP05", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "KBDRT_RLS", "release RIGHT",),
	("AXXNVSEL2TOP06", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AXXNVSEL2TOP07", FMAXDO_SCTN43AXVALADD, "AXXNVSEL2TOP", "SYNREPORT", "SYNREPORT",),
	("AXXNVZOOMFULL", FMAXDO_SCTN43AXDEF, "XnViewer zoom 1:1",),
	("AXXNVZOOMFULL01", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMFULL", "KBDSPLAT_PRS", "press *",),
	("AXXNVZOOMFULL02", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMFULL", "KBDSPLAT_RLS", "release *",),
	("AXXNVZOOMFULL03", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMFULL", "SYNREPORT", "SYNREPORT",),
	("AXXNVZOOMIN", FMAXDO_SCTN43AXDEF, "XnViewer zoom in/+",),
	("AXXNVZOOMIN01", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMIN", "KBDPLUS_PRS", "press +",),
	("AXXNVZOOMIN02", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMIN", "KBDPLUS_RLS", "release +",),
	("AXXNVZOOMIN03", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMIN", "SYNREPORT", "SYNREPORT",),
	("AXXNVZOOMOUT", FMAXDO_SCTN43AXDEF, "XnViewer zoom out/-",),
	("AXXNVZOOMOUT01", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMOUT", "KBDMINUS_PRS", "press -",),
	("AXXNVZOOMOUT02", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMOUT", "KBDMINUS_RLS", "release -",),
	("AXXNVZOOMOUT03", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMOUT", "SYNREPORT", "SYNREPORT",),
	("AXXNVZOOMRESET", FMAXDO_SCTN43AXDEF, "reset XnViewer zoom by back, forward, forward, back",),
	("AXXNVZOOMRESET01", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDLT_PRS", "press KBDLT",),
	("AXXNVZOOMRESET02", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDLT_RLS", "press KBDLT",),
	("AXXNVZOOMRESET03", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDRT_PRS", "press KBDLT",),
	("AXXNVZOOMRESET04", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDRT_RLS", "press KBDLT",),
	("AXXNVZOOMRESET05", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDRT_PRS", "press KBDLT",),
	("AXXNVZOOMRESET06", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDRT_RLS", "press KBDLT",),
	("AXXNVZOOMRESET07", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDLT_PRS", "press KBDLT",),
	("AXXNVZOOMRESET08", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "KBDLT_RLS", "press KBDLT",),
	("AXXNVZOOMRESET09", FMAXDO_SCTN43AXVALADD, "AXXNVZOOMRESET", "SYNREPORT", "SYNREPORT",),
	("AX_ALTC", FMAXDO_SCTN43AXDEF, "ALT-C",),
	("AX_ALTC01", FMAXDO_SCTN43AXVALADD, "AX_ALTC", "KBDALTLT_PRS", "press ALT",),
	("AX_ALTC02", FMAXDO_SCTN43AXVALADD, "AX_ALTC", "KBDC_PRS", "press C",),
	("AX_ALTC03", FMAXDO_SCTN43AXVALADD, "AX_ALTC", "KBDC_RLS", "release C",),
	("AX_ALTC04", FMAXDO_SCTN43AXVALADD, "AX_ALTC", "KBDALTLT_RLS", "release ALT",),
	("AX_ALTC05", FMAXDO_SCTN43AXVALADD, "AX_ALTC", "SYNREPORT", "SYNREPORT",),
	("AX_ALTD", FMAXDO_SCTN43AXDEF, "ALT-D",),
	("AX_ALTD01", FMAXDO_SCTN43AXVALADD, "AX_ALTD", "KBDALTLT_PRS", "press ALT",),
	("AX_ALTD02", FMAXDO_SCTN43AXVALADD, "AX_ALTD", "KBDD_PRS", "press D",),
	("AX_ALTD03", FMAXDO_SCTN43AXVALADD, "AX_ALTD", "KBDD_RLS", "release D",),
	("AX_ALTD04", FMAXDO_SCTN43AXVALADD, "AX_ALTD", "KBDALTLT_RLS", "release ALT",),
	("AX_ALTD05", FMAXDO_SCTN43AXVALADD, "AX_ALTD", "SYNREPORT", "SYNREPORT",),
	("AX_ALTTAB", FMAXDO_SCTN43AXDEF, "ALT-TAB",),
	("AX_ALTTAB01", FMAXDO_SCTN43AXVALADD, "AX_ALTTAB", "KBDALTLT_PRS", "press ALT",),
	("AX_ALTTAB02", FMAXDO_SCTN43AXVALADD, "AX_ALTTAB", "KBDTAB_PRS", "press TAB",),
	("AX_ALTTAB03", FMAXDO_SCTN43AXVALADD, "AX_ALTTAB", "KBDTAB_RLS", "release TAB",),
	("AX_ALTTAB04", FMAXDO_SCTN43AXVALADD, "AX_ALTTAB", "KBDALTLT_RLS", "release ALT",),
	("AX_ALTTAB05", FMAXDO_SCTN43AXVALADD, "AX_ALTTAB", "SYNREPORT", "SYNREPORT",),
	("AX_CRSRDN", FMAXDO_SCTN43AXDEF, "DOWN",),
	("AX_CRSRDN01", FMAXDO_SCTN43AXVALADD, "AX_CRSRDN", "KBDDN_PRS", "press DOWN",),
	("AX_CRSRDN02", FMAXDO_SCTN43AXVALADD, "AX_CRSRDN", "KBDDN_RLS", "release DOWN",),
	("AX_CRSRDN03", FMAXDO_SCTN43AXVALADD, "AX_CRSRDN", "SYNREPORT", "SYNREPORT",),
	("AX_CRSRDNLT", FMAXDO_SCTN43AXDEF, "DOWN",),
	("AX_CRSRDNLT01", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNLT", "KBDDN_PRS", "press DOWN",),
	("AX_CRSRDNLT02", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNLT", "KBDDN_RLS", "release DOWN",),
	("AX_CRSRDNLT03", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNLT", "KBDLT_PRS", "press LEFT",),
	("AX_CRSRDNLT04", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNLT", "KBDLT_RLS", "release LEFT",),
	("AX_CRSRDNLT05", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNLT", "SYNREPORT", "SYNREPORT",),
	("AX_CRSRDNRT", FMAXDO_SCTN43AXDEF, "DOWN",),
	("AX_CRSRDNRT01", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNRT", "KBDDN_PRS", "press DOWN",),
	("AX_CRSRDNRT02", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNRT", "KBDDN_RLS", "release DOWN",),
	("AX_CRSRDNRT03", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNRT", "KBDRT_PRS", "press RIGHT",),
	("AX_CRSRDNRT04", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNRT", "KBDRT_RLS", "release RIGHT",),
	("AX_CRSRDNRT05", FMAXDO_SCTN43AXVALADD, "AX_CRSRDNRT", "SYNREPORT", "SYNREPORT",),
	("AX_CRSRLT", FMAXDO_SCTN43AXDEF, "LEFT",),
	("AX_CRSRLT01", FMAXDO_SCTN43AXVALADD, "AX_CRSRLT", "KBDLT_PRS", "press LEFT",),
	("AX_CRSRLT02", FMAXDO_SCTN43AXVALADD, "AX_CRSRLT", "KBDLT_RLS", "press LEFT",),
	("AX_CRSRLT03", FMAXDO_SCTN43AXVALADD, "AX_CRSRLT", "SYNREPORT", "press LEFT",),
	("AX_CRSRRT", FMAXDO_SCTN43AXDEF, "RIGHT",),
	("AX_CRSRRT01", FMAXDO_SCTN43AXVALADD, "AX_CRSRRT", "KBDRT_PRS", "press RIGHT",),
	("AX_CRSRRT02", FMAXDO_SCTN43AXVALADD, "AX_CRSRRT", "KBDRT_RLS", "release RIGHT",),
	("AX_CRSRRT03", FMAXDO_SCTN43AXVALADD, "AX_CRSRRT", "SYNREPORT", "press RIGHT",),
	("AX_CRSRUP", FMAXDO_SCTN43AXDEF, "UP",),
	("AX_CRSRUP01", FMAXDO_SCTN43AXVALADD, "AX_CRSRUP", "KBDUP_PRS", "press UP",),
	("AX_CRSRUP02", FMAXDO_SCTN43AXVALADD, "AX_CRSRUP", "KBDUP_RLS", "press UP",),
	("AX_CRSRUP03", FMAXDO_SCTN43AXVALADD, "AX_CRSRUP", "SYNREPORT", "press UP",),
	("AX_CRSRUPLT", FMAXDO_SCTN43AXDEF, "UPLT",),
	("AX_CRSRUPLT01", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPLT", "KBDUP_PRS", "press UP",),
	("AX_CRSRUPLT02", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPLT", "KBDUP_RLS", "press UP",),
	("AX_CRSRUPLT03", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPLT", "KBDLT_PRS", "press LT",),
	("AX_CRSRUPLT04", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPLT", "KBDLT_RLS", "press LT",),
	("AX_CRSRUPLT05", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPLT", "SYNREPORT", "press UP",),
	("AX_CRSRUPRT", FMAXDO_SCTN43AXDEF, "UPRT",),
	("AX_CRSRUPRT01", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPRT", "KBDUP_PRS", "press UP",),
	("AX_CRSRUPRT02", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPRT", "KBDUP_RLS", "press UP",),
	("AX_CRSRUPRT03", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPRT", "KBDRT_PRS", "press RT",),
	("AX_CRSRUPRT04", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPRT", "KBDRT_RLS", "press RT",),
	("AX_CRSRUPRT05", FMAXDO_SCTN43AXVALADD, "AX_CRSRUPRT", "SYNREPORT", "press UP",),
	("AX_CTRLA", FMAXDO_SCTN43AXDEF, "CTRL-A",),
	("AX_CTRLA01", FMAXDO_SCTN43AXVALADD, "AX_CTRLA", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLA02", FMAXDO_SCTN43AXVALADD, "AX_CTRLA", "KBDA_PRS", "press A",),
	("AX_CTRLA03", FMAXDO_SCTN43AXVALADD, "AX_CTRLA", "KBDA_RLS", "release A",),
	("AX_CTRLA04", FMAXDO_SCTN43AXVALADD, "AX_CTRLA", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLA05", FMAXDO_SCTN43AXVALADD, "AX_CTRLA", "SYNREPORT", "SYNREPORT",),
	("AX_CTRLPGDN", FMAXDO_SCTN43AXDEF, "CTRLPGDN",),
	("AX_CTRLPGDN01", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGDN", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLPGDN02", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGDN", "KBDPGDN_PRS", "press PGDN",),
	("AX_CTRLPGDN03", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGDN", "KBDPGDN_RLS", "release PGDN",),
	("AX_CTRLPGDN04", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGDN", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLPGDN05", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGDN", "SYNREPORT", "SYNREPORT",),
	("AX_CTRLPGUP", FMAXDO_SCTN43AXDEF, "CTRLPGUP",),
	("AX_CTRLPGUP01", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGUP", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLPGUP02", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGUP", "KBDPGDN_PRS", "press PGDN",),
	("AX_CTRLPGUP03", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGUP", "KBDPGDN_RLS", "release PGDN",),
	("AX_CTRLPGUP04", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGUP", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLPGUP05", FMAXDO_SCTN43AXVALADD, "AX_CTRLPGUP", "SYNREPORT", "SYNREPORT",),
	("AX_CTRLQ", FMAXDO_SCTN43AXDEF, "CTRL-Q",),
	("AX_CTRLQ01", FMAXDO_SCTN43AXVALADD, "AX_CTRLQ", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLQ02", FMAXDO_SCTN43AXVALADD, "AX_CTRLQ", "KBDQ_PRS", "press Q",),
	("AX_CTRLQ03", FMAXDO_SCTN43AXVALADD, "AX_CTRLQ", "KBDQ_RLS", "release Q",),
	("AX_CTRLQ04", FMAXDO_SCTN43AXVALADD, "AX_CTRLQ", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLQ05", FMAXDO_SCTN43AXVALADD, "AX_CTRLQ", "SYNREPORT", "SYNREPORT",),
	("AX_CTRLS", FMAXDO_SCTN43AXDEF, "CTRL-S",),
	("AX_CTRLS01", FMAXDO_SCTN43AXVALADD, "AX_CTRLS", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLS02", FMAXDO_SCTN43AXVALADD, "AX_CTRLS", "KBDS_PRS", "press S",),
	("AX_CTRLS03", FMAXDO_SCTN43AXVALADD, "AX_CTRLS", "KBDS_RLS", "release S",),
	("AX_CTRLS04", FMAXDO_SCTN43AXVALADD, "AX_CTRLS", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLS05", FMAXDO_SCTN43AXVALADD, "AX_CTRLS", "SYNREPORT", "SYNREPORT",),
	("AX_CTRLTAB", FMAXDO_SCTN43AXDEF, "CTRL-TAB",),
	("AX_CTRLTAB01", FMAXDO_SCTN43AXVALADD, "AX_CTRLTAB", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLTAB02", FMAXDO_SCTN43AXVALADD, "AX_CTRLTAB", "KBDTAB_PRS", "press TAB",),
	("AX_CTRLTAB03", FMAXDO_SCTN43AXVALADD, "AX_CTRLTAB", "KBDTAB_RLS", "release TAB",),
	("AX_CTRLTAB04", FMAXDO_SCTN43AXVALADD, "AX_CTRLTAB", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLTAB05", FMAXDO_SCTN43AXVALADD, "AX_CTRLTAB", "SYNREPORT", "SYNREPORT",),
	("AX_CTRLW", FMAXDO_SCTN43AXDEF, "CTRL-W",),
	("AX_CTRLW01", FMAXDO_SCTN43AXVALADD, "AX_CTRLW", "KBDCTRLLT_PRS", "press CTRL",),
	("AX_CTRLW02", FMAXDO_SCTN43AXVALADD, "AX_CTRLW", "KBDW_PRS", "press W",),
	("AX_CTRLW03", FMAXDO_SCTN43AXVALADD, "AX_CTRLW", "KBDW_RLS", "release W",),
	("AX_CTRLW04", FMAXDO_SCTN43AXVALADD, "AX_CTRLW", "KBDCTRLLT_RLS", "release CTRL",),
	("AX_CTRLW05", FMAXDO_SCTN43AXVALADD, "AX_CTRLW", "SYNREPORT", "SYNREPORT",),
	("AX_DEL", FMAXDO_SCTN43AXDEF, "DEL",),
	("AX_DEL01", FMAXDO_SCTN43AXVALADD, "AX_DEL", "KBDDEL_PRS", "press DEL",),
	("AX_DEL02", FMAXDO_SCTN43AXVALADD, "AX_DEL", "KBDDEL_RLS", "release DEL",),
	("AX_DEL03", FMAXDO_SCTN43AXVALADD, "AX_DEL", "SYNREPORT", "SYNREPORT",),
	("AX_END", FMAXDO_SCTN43AXDEF, "END",),
	("AX_END01", FMAXDO_SCTN43AXVALADD, "AX_END", "KBDEND_PRS", "press END",),
	("AX_END02", FMAXDO_SCTN43AXVALADD, "AX_END", "KBDEND_RLS", "release END",),
	("AX_END03", FMAXDO_SCTN43AXVALADD, "AX_END", "SYNREPORT", "SYNREPORT",),
	("AX_ENTER", FMAXDO_SCTN43AXDEF, "ENTER",),
	("AX_ENTER01", FMAXDO_SCTN43AXVALADD, "AX_ENTER", "KBDENTER_PRS", "press ENTER",),
	("AX_ENTER02", FMAXDO_SCTN43AXVALADD, "AX_ENTER", "KBDENTER_RLS", "release ENTER",),
	("AX_ENTER03", FMAXDO_SCTN43AXVALADD, "AX_ENTER", "SYNREPORT", "SYNREPORT",),
	("AX_ESC", FMAXDO_SCTN43AXDEF, "ESC",),
	("AX_ESC01", FMAXDO_SCTN43AXVALADD, "AX_ESC", "KBDESC_PRS", "press ESC",),
	("AX_ESC02", FMAXDO_SCTN43AXVALADD, "AX_ESC", "KBDESC_RLS", "release ESC",),
	("AX_ESC03", FMAXDO_SCTN43AXVALADD, "AX_ESC", "SYNREPORT", "SYNREPORT",),
	("AX_F", FMAXDO_SCTN43AXDEF, "F",),
	("AX_F01", FMAXDO_SCTN43AXVALADD, "AX_F", "KBDF_PRS", "press F",),
	("AX_F02", FMAXDO_SCTN43AXVALADD, "AX_F", "KBDF_RLS", "release F",),
	("AX_F03", FMAXDO_SCTN43AXVALADD, "AX_F", "SYNREPORT", "SYNREPORT",),
	("AX_F10", FMAXDO_SCTN43AXDEF, "F10",),
	("AX_F1001", FMAXDO_SCTN43AXVALADD, "AX_F10", "KBDF10_PRS", "press F10",),
	("AX_F1002", FMAXDO_SCTN43AXVALADD, "AX_F10", "KBDF10_RLS", "release F10",),
	("AX_F1003", FMAXDO_SCTN43AXVALADD, "AX_F10", "SYNREPORT", "SYNREPORT",),
	("AX_F5", FMAXDO_SCTN43AXDEF, "F5",),
	("AX_F501", FMAXDO_SCTN43AXVALADD, "AX_F5", "KBDF5_PRS", "press F5",),
	("AX_F502", FMAXDO_SCTN43AXVALADD, "AX_F5", "KBDF5_RLS", "release F5",),
	("AX_F503", FMAXDO_SCTN43AXVALADD, "AX_F5", "SYNREPORT", "SYNREPORT",),
	("AX_F6", FMAXDO_SCTN43AXDEF, "F6",),
	("AX_F601", FMAXDO_SCTN43AXVALADD, "AX_F6", "KBDF6_PRS", "press F6",),
	("AX_F602", FMAXDO_SCTN43AXVALADD, "AX_F6", "KBDF6_RLS", "release F6",),
	("AX_F603", FMAXDO_SCTN43AXVALADD, "AX_F6", "SYNREPORT", "SYNREPORT",),
	("AX_HOME", FMAXDO_SCTN43AXDEF, "HOME",),
	("AX_HOME01", FMAXDO_SCTN43AXVALADD, "AX_HOME", "KBDHOME_PRS", "press HOME",),
	("AX_HOME02", FMAXDO_SCTN43AXVALADD, "AX_HOME", "KBDHOME_RLS", "release HOME",),
	("AX_HOME03", FMAXDO_SCTN43AXVALADD, "AX_HOME", "SYNREPORT", "SYNREPORT",),
	("AX_N", FMAXDO_SCTN43AXDEF, "N",),
	("AX_N01", FMAXDO_SCTN43AXVALADD, "AX_N", "KBDN_PRS", "press N",),
	("AX_N02", FMAXDO_SCTN43AXVALADD, "AX_N", "KBDN_RLS", "release N",),
	("AX_N03", FMAXDO_SCTN43AXVALADD, "AX_N", "SYNREPORT", "SYNREPORT",),
	("AX_PGDN", FMAXDO_SCTN43AXDEF, "PGDN",),
	("AX_PGDN01", FMAXDO_SCTN43AXVALADD, "AX_PGDN", "KBDPGDN_PRS", "press PGDN",),
	("AX_PGDN02", FMAXDO_SCTN43AXVALADD, "AX_PGDN", "KBDPGDN_RLS", "release PGDN",),
	("AX_PGDN03", FMAXDO_SCTN43AXVALADD, "AX_PGDN", "SYNREPORT", "SYNREPORT",),
	("AX_PGUP", FMAXDO_SCTN43AXDEF, "PGUP",),
	("AX_PGUP01", FMAXDO_SCTN43AXVALADD, "AX_PGUP", "KBDPGUP_PRS", "press PGUP",),
	("AX_PGUP02", FMAXDO_SCTN43AXVALADD, "AX_PGUP", "KBDPGUP_RLS", "release PGUP",),
	("AX_PGUP03", FMAXDO_SCTN43AXVALADD, "AX_PGUP", "SYNREPORT", "SYNREPORT",),
	("AX_Q", FMAXDO_SCTN43AXDEF, "Q",),
	("AX_Q01", FMAXDO_SCTN43AXVALADD, "AX_Q", "KBDQ_PRS", "press Q",),
	("AX_Q02", FMAXDO_SCTN43AXVALADD, "AX_Q", "KBDQ_RLS", "release Q",),
	("AX_Q03", FMAXDO_SCTN43AXVALADD, "AX_Q", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTDN", FMAXDO_SCTN43AXDEF, "SHIFT-DN",),
	("AX_SHIFTDN01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDN", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTDN02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDN", "KBDDN_PRS", "press DN",),
	("AX_SHIFTDN03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDN", "KBDDN_RLS", "release DN",),
	("AX_SHIFTDN04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDN", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTDN05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDN", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTDNLT", FMAXDO_SCTN43AXDEF, "SHIFT-DNLT",),
	("AX_SHIFTDNLT01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTDNLT02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "KBDDN_PRS", "press DN",),
	("AX_SHIFTDNLT03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "KBDDN_RLS", "release DN",),
	("AX_SHIFTDNLT06", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTDNLT07", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTDNRT", FMAXDO_SCTN43AXDEF, "SHIFT-DNRT",),
	("AX_SHIFTDNRT01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTDNRT02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "KBDDN_PRS", "press DN",),
	("AX_SHIFTDNRT03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "KBDDN_RLS", "release DN",),
	("AX_SHIFTDNRT04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "KBDRT_PRS", "press RT",),
	("AX_SHIFTDNRT05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "KBDRT_RLS", "release RT",),
	("AX_SHIFTDNRT06", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTDNRT07", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNRT", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTLT", FMAXDO_SCTN43AXDEF, "SHIFT-LT",),
	("AX_SHIFTLT01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTLT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTLT02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTLT", "KBDLT_PRS", "press LT",),
	("AX_SHIFTLT03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTLT", "KBDLT_RLS", "release LT",),
	("AX_SHIFTLT04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTLT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTLT05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTLT", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTLTLT04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "KBDLT_PRS", "press LT",),
	("AX_SHIFTLTLT04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "KBDLT_PRS", "press LT",),
	("AX_SHIFTLTLT05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTDNLT", "KBDLT_RLS", "release LT",),
	("AX_SHIFTLTLT05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "KBDLT_RLS", "release LT",),
	("AX_SHIFTRT", FMAXDO_SCTN43AXDEF, "SHIFT-RT",),
	("AX_SHIFTRT01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTRT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTRT02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTRT", "KBDRT_PRS", "press RT",),
	("AX_SHIFTRT03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTRT", "KBDRT_RLS", "release RT",),
	("AX_SHIFTRT04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTRT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTRT05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTRT", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTTAB", FMAXDO_SCTN43AXDEF, "ALT-SHIFT-TAB",),
	("AX_SHIFTTAB01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTTAB", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTTAB02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTTAB", "KBDTAB_PRS", "press TAB",),
	("AX_SHIFTTAB03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTTAB", "KBDTAB_RLS", "release TAB",),
	("AX_SHIFTTAB04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTTAB", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTTAB05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTTAB", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTUP", FMAXDO_SCTN43AXDEF, "SHIFT-UP",),
	("AX_SHIFTUP01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUP", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTUP02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUP", "KBDUP_PRS", "press UP",),
	("AX_SHIFTUP03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUP", "KBDUP_RLS", "release UP",),
	("AX_SHIFTUP04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUP", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTUP05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUP", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTUPLT", FMAXDO_SCTN43AXDEF, "SHIFT-UPLT",),
	("AX_SHIFTUPLT01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTUPLT02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "KBDUP_PRS", "press UP",),
	("AX_SHIFTUPLT03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "KBDUP_RLS", "release UP",),
	("AX_SHIFTUPLT06", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTUPLT07", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPLT", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTUPRT", FMAXDO_SCTN43AXDEF, "SHIFT-UPRT",),
	("AX_SHIFTUPRT01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "KBDSHIFTRT_PRS", "press SHIFT",),
	("AX_SHIFTUPRT02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "KBDUP_PRS", "press UP",),
	("AX_SHIFTUPRT03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "KBDUP_RLS", "release UP",),
	("AX_SHIFTUPRT04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "KBDRT_PRS", "press RT",),
	("AX_SHIFTUPRT05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "KBDRT_RLS", "release RT",),
	("AX_SHIFTUPRT06", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "KBDSHIFTRT_RLS", "release SHIFT",),
	("AX_SHIFTUPRT07", FMAXDO_SCTN43AXVALADD, "AX_SHIFTUPRT", "SYNREPORT", "SYNREPORT",),
	("AX_SHIFTX", FMAXDO_SCTN43AXDEF, "SHIFT-X",),
	("AX_SHIFTX01", FMAXDO_SCTN43AXVALADD, "AX_SHIFTX", "KBDSHIFTLT_PRS", "press SHIFT",),
	("AX_SHIFTX02", FMAXDO_SCTN43AXVALADD, "AX_SHIFTX", "KBDX_PRS", "press X",),
	("AX_SHIFTX03", FMAXDO_SCTN43AXVALADD, "AX_SHIFTX", "KBDX_RLS", "release X",),
	("AX_SHIFTX04", FMAXDO_SCTN43AXVALADD, "AX_SHIFTX", "KBDSHIFTLT_RLS", "release SHIFT",),
	("AX_SHIFTX05", FMAXDO_SCTN43AXVALADD, "AX_SHIFTX", "SYNREPORT", "SYNREPORT",),
	("AX_SPACE", FMAXDO_SCTN43AXDEF, "SPACE",),
	("AX_SPACE01", FMAXDO_SCTN43AXVALADD, "AX_SPACE", "KBDSPC_PRS", "press SPACE",),
	("AX_SPACE02", FMAXDO_SCTN43AXVALADD, "AX_SPACE", "KBDSPC_RLS", "release SPACE",),
	("AX_SPACE03", FMAXDO_SCTN43AXVALADD, "AX_SPACE", "SYNREPORT", "SYNREPORT",),
	("AX_TAB", FMAXDO_SCTN43AXDEF, "TAB",),
	("AX_TAB01", FMAXDO_SCTN43AXVALADD, "AX_TAB", "KBDTAB_PRS", "press TAB",),
	("AX_TAB02", FMAXDO_SCTN43AXVALADD, "AX_TAB", "KBDTAB_RLS", "release TAB",),
	("AX_TAB03", FMAXDO_SCTN43AXVALADD, "AX_TAB", "SYNREPORT", "SYNREPORT",),
	("AX_Y", FMAXDO_SCTN43AXDEF, "Y",),
	("AX_Y01", FMAXDO_SCTN43AXVALADD, "AX_Y", "KBDY_PRS", "press Y",),
	("AX_Y02", FMAXDO_SCTN43AXVALADD, "AX_Y", "KBDY_RLS", "release Y",),
	("AX_Y03", FMAXDO_SCTN43AXVALADD, "AX_Y", "SYNREPORT", "SYNREPORT",),
	("B_BTNGHAT_DN", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_DN", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_DNLT", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_DNLT", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_DNRT", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_DNRT", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_LT", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_LT", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_RLS", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_RLS", "BTNTYPE_SIMABS", "artifical button release for hat on gamepads",),
	("B_BTNGHAT_RT", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_RT", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_UP", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_UP", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_UPLT", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_UPLT", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGHAT_UPRT", FMAXDO_SCTN47BTNSDEF, "BTNGHAT_UPRT", "BTNTYPE_SIMABS", "artificial button for the hat on gamepads",),
	("B_BTNGLTSTK_DN", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_DN", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_DNLT", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_DNLT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_DNRT", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_DNRT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_LT", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_LT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_RLS", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_RLS", "BTNTYPE_SIMABS", "artificial button release for LTSTK on gamepads",),
	("B_BTNGLTSTK_RT", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_RT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_UP", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_UP", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_UPLT", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_UPLT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGLTSTK_UPRT", FMAXDO_SCTN47BTNSDEF, "BTNGLTSTK_UPRT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_DN", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_DN", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_DNLT", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_DNLT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_DNRT", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_DNRT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_LT", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_LT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_RLS", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_RLS", "BTNTYPE_SIMABS", "artificial button release for RTSTK on gamepads",),
	("B_BTNGRTSTK_RT", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_RT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_UP", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_UP", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_UPLT", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_UPLT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNGRTSTK_UPRT", FMAXDO_SCTN47BTNSDEF, "BTNGRTSTK_UPRT", "BTNTYPE_SIMABS", "artificial button for left stick on gamepads",),
	("B_BTNG_01", FMAXDO_SCTN47BTNSDEF, "BTNG_01", "BTNTYPE_NOTHOLDABLE", "BTNG001/X on gamepads",),
	("B_BTNG_02", FMAXDO_SCTN47BTNSDEF, "BTNG_02", "BTNTYPE_NOTHOLDABLE", "BTNG002/A on gamepads",),
	("B_BTNG_03", FMAXDO_SCTN47BTNSDEF, "BTNG_03", "BTNTYPE_NOTHOLDABLE", "BTNG003/B on gamepads",),
	("B_BTNG_04", FMAXDO_SCTN47BTNSDEF, "BTNG_04", "BTNTYPE_NOTHOLDABLE", "BTNG004/Y on gamepads",),
	("B_BTNG_05", FMAXDO_SCTN47BTNSDEF, "BTNG_05", "BTNTYPE_HOLDABLE", "BTNG005/left shoulder on gamepads",),
	("B_BTNG_06", FMAXDO_SCTN47BTNSDEF, "BTNG_06", "BTNTYPE_HOLDABLE", "BTNG006/right shoulder on gamepads",),
	("B_BTNG_07", FMAXDO_SCTN47BTNSDEF, "BTNG_07", "BTNTYPE_HOLDABLE", "BTNG007/left trigger on gamepads",),
	("B_BTNG_08", FMAXDO_SCTN47BTNSDEF, "BTNG_08", "BTNTYPE_HOLDABLE", "BTNG008/right trigger on gamepads",),
	("B_BTNG_09", FMAXDO_SCTN47BTNSDEF, "BTNG_09", "BTNTYPE_NOTHOLDABLE", "BTNG009/left face on gamepads",),
	("B_BTNG_10", FMAXDO_SCTN47BTNSDEF, "BTNG_10", "BTNTYPE_NOTHOLDABLE", "BTNG_010/right face on gamepads",),
	("B_BTNG_11LTSTK", FMAXDO_SCTN47BTNSDEF, "BTNG_11LTSTK", "BTNTYPE_NOTHOLDABLE", "BTN011/left stick on gamepads",),
	("B_BTNG_12RTSTK", FMAXDO_SCTN47BTNSDEF, "BTNG_12RTSTK", "BTNTYPE_NOTHOLDABLE", "BTN012/right stick on gamepads",),
	("B_BTNG_13", FMAXDO_SCTN47BTNSDEF, "BTNG_13", "BTNTYPE_NOTHOLDABLE", "BTN013/home/select on gamepads",),
	("B_BTNMWH_DN", FMAXDO_SCTN47BTNSDEF, "BTNMWH_DN", "BTNTYPE_SIMREL", "BTNMWHLDN/MSE_DN on mice",),
	("B_BTNMWH_DNLT", FMAXDO_SCTN47BTNSDEF, "BTNMWH_DNLT", "BTNTYPE_SIMREL", "BTNMWHLDN/MSE_DNLT on mice",),
	("B_BTNMWH_DNRT", FMAXDO_SCTN47BTNSDEF, "BTNMWH_DNRT", "BTNTYPE_SIMREL", "BTNMWHLDN/MSE_DNRT on mice",),
	("B_BTNMWH_LT", FMAXDO_SCTN47BTNSDEF, "BTNMWH_LT", "BTNTYPE_SIMREL", "BTNMWHLLT/MSE_LT on mice",),
	("B_BTNMWH_RLS", FMAXDO_SCTN47BTNSDEF, "BTNMWH_RLS", "BTNTYPE_SIMREL", "BTNMWHLRLS/MSE_RLS on mice",),
	("B_BTNMWH_RT", FMAXDO_SCTN47BTNSDEF, "BTNMWH_RT", "BTNTYPE_SIMREL", "BTNMWHLRT/MSE_RT on mice",),
	("B_BTNMWH_UP", FMAXDO_SCTN47BTNSDEF, "BTNMWH_UP", "BTNTYPE_SIMREL", "BTNMWHLUP/MSE_UP on mice",),
	("B_BTNMWH_UPLT", FMAXDO_SCTN47BTNSDEF, "BTNMWH_UPLT", "BTNTYPE_SIMREL", "BTNMWHLUP/MSE_UPLT on mice",),
	("B_BTNMWH_UPRT", FMAXDO_SCTN47BTNSDEF, "BTNMWH_UPRT", "BTNTYPE_SIMREL", "BTNMWHLUP/MSE_UPRT on mice",),
	("B_BTNM_01LT", FMAXDO_SCTN47BTNSDEF, "BTNM_01LT", "BTNTYPE_NOTHOLDABLE", "BTN01/LEFT on mice",),
	("B_BTNM_02MD", FMAXDO_SCTN47BTNSDEF, "BTNM_02MD", "BTNTYPE_NOTHOLDABLE", "BTN02/MIDDLE on mice",),
	("B_BTNM_03RT", FMAXDO_SCTN47BTNSDEF, "BTNM_03RT", "BTNTYPE_NOTHOLDABLE", "BTN03/RIGHT on mice",),
	("B_BTNM_04WHUP", FMAXDO_SCTN47BTNSDEF, "BTNM_04WHUP", "BTNTYPE_SIMREL", "BTNM04/MSEWHL_UP on mice",),
	("B_BTNM_05WHDN", FMAXDO_SCTN47BTNSDEF, "BTNM_05WHDN", "BTNTYPE_SIMREL", "BTNM05/MSEWHL_DN on mice",),
	("B_BTNM_06WHLT", FMAXDO_SCTN47BTNSDEF, "BTNM_06WHLT", "BTNTYPE_SIMREL", "BTNM06/MSEWHL_LT on mice",),
	("B_BTNM_07WHRT", FMAXDO_SCTN47BTNSDEF, "BTNM_07WHRT", "BTNTYPE_SIMREL", "BTNM07/MSEWHL_RT on mice",),
	("B_BTNM_08", FMAXDO_SCTN47BTNSDEF, "BTNM_08", "BTNTYPE_NOTHOLDABLE", "BTNM_08/NW most BTN on mice",),
	("B_BTNM_09", FMAXDO_SCTN47BTNSDEF, "BTNM_09", "BTNTYPE_NOTHOLDABLE", "BTNM_09 on mice",),
	("B_BTNM_10", FMAXDO_SCTN47BTNSDEF, "BTNM_10", "BTNTYPE_NOTHOLDABLE", "BTNM_10 on mice",),
	("B_BTNM_11", FMAXDO_SCTN47BTNSDEF, "BTNM_11", "BTNTYPE_NOTHOLDABLE", "BTNM_11 on mice",),
	("B_BTNM_12", FMAXDO_SCTN47BTNSDEF, "BTNM_12", "BTNTYPE_NOTHOLDABLE", "BTNM_12/SE most on mice",),
	("B_BTNM_MDN", FMAXDO_SCTN47BTNSDEF, "BTNM_MDN", "BTNTYPE_SIMREL", "BTNMDN/MSE_DN on mice",),
	("B_BTNM_MDNLT", FMAXDO_SCTN47BTNSDEF, "BTNM_MDNLT", "BTNTYPE_SIMREL", "BTNMDN/MSE_DNLT on mice",),
	("B_BTNM_MDNRT", FMAXDO_SCTN47BTNSDEF, "BTNM_MDNRT", "BTNTYPE_SIMREL", "BTNMDN/MSE_DNRT on mice",),
	("B_BTNM_MLT", FMAXDO_SCTN47BTNSDEF, "BTNM_MLT", "BTNTYPE_SIMREL", "BTNMLT/MSE_LT on mice",),
	("B_BTNM_MRT", FMAXDO_SCTN47BTNSDEF, "BTNM_MRT", "BTNTYPE_SIMREL", "BTNMRT/MSE_RT on mice",),
	("B_BTNM_MUP", FMAXDO_SCTN47BTNSDEF, "BTNM_MUP", "BTNTYPE_SIMREL", "BTNMUP/MSE_UP on mice",),
	("B_BTNM_MUPLT", FMAXDO_SCTN47BTNSDEF, "BTNM_MUPLT", "BTNTYPE_SIMREL", "BTNMUP/MSE_UPLT on mice",),
	("B_BTNM_MUPRT", FMAXDO_SCTN47BTNSDEF, "BTNM_MUPRT", "BTNTYPE_SIMREL", "BTNMUP/MSE_UPRT on mice",),
	("B_BTNM_WHDN", FMAXDO_SCTN47BTNSDEF, "BTNM_WHDN", "BTNTYPE_SIMREL", "BTNMDN/MSE_DN on mice",),
	("B_BTNM_WHDNLT", FMAXDO_SCTN47BTNSDEF, "BTNM_WHDNLT", "BTNTYPE_SIMREL", "BTNMDN/MSE_DNLT on mice",),
	("B_BTNM_WHDNRT", FMAXDO_SCTN47BTNSDEF, "BTNM_WHDNRT", "BTNTYPE_SIMREL", "BTNMDN/MSE_DNRT on mice",),
	("B_BTNM_WHLT", FMAXDO_SCTN47BTNSDEF, "BTNM_WHLT", "BTNTYPE_SIMREL", "BTNMLT/MSE_LT on mice",),
	("B_BTNM_WHRT", FMAXDO_SCTN47BTNSDEF, "BTNM_WHRT", "BTNTYPE_SIMREL", "BTNMRT/MSE_RT on mice",),
	("B_BTNM_WHUP", FMAXDO_SCTN47BTNSDEF, "BTNM_WHUP", "BTNTYPE_SIMREL", "BTNMUP/MSE_UP on mice",),
	("B_BTNM_WHUPLT", FMAXDO_SCTN47BTNSDEF, "BTNM_WHUPLT", "BTNTYPE_SIMREL", "BTNMUP/MSE_UPLT on mice",),
	("B_BTNM_WHUPRT", FMAXDO_SCTN47BTNSDEF, "BTNM_WHUPRT", "BTNTYPE_SIMREL", "BTNMUP/MSE_UPRT on mice",),
	("CFDICT_CODES2STRIP00", FMAXCF_SCTN24LISTDEF, "CODES2STRIP", "dict holding all of the things to strip from 'text' strings like color codes",),
	("CFDICT_CODES2STRIP01", FMAXCF_SCTN24LISTSTRADD, "CODES2STRIP", "{ESC}[0m", "entry for ESC-[0m",),
	("CFDICT_CODES2STRIP02", FMAXCF_SCTN24LISTSTRADD, "CODES2STRIP", "{ESC}[1m", "entry for ESC-[1m",),
	("CFDICT_CODES2STRIP03", FMAXCF_SCTN24LISTSTRADD, "CODES2STRIP", "{ESC}[32m", "entry for ESC-[32m",),
	("CFDICT_CODES2STRIP04", FMAXCF_SCTN24LISTSTRADD, "CODES2STRIP", "{ESC}[35m", "entry for ESC-[35m",),
	("CFDICT_CODES2STRIP05", FMAXCF_SCTN24LISTSTRADD, "CODES2STRIP", "{ESC}[36m", "entry for ESC-[36m",),
	("CFVAL_ARRAY", FMAXCF_SCTN03TYPEDEF, "_ARRAY_", "list", "list or array, adjust for language",),
	("CFVAL_AX", FMAXCF_SCTN03TYPEDEF, "_AX_", "_AX_", "action involving a common key combination like ALT-D CTRL-W",),
	("CFVAL_CHR", FMAXCF_SCTN03TYPEDEF, "_CHR_", "varchar", "character",),
	("CFVAL_CONST", FMAXCF_SCTN03TYPEDEF, "_CONST_", "_CONST_", "constant in all uses",),
	("CFVAL_DATETIME", FMAXCF_SCTN03TYPEDEF, "_DATETIME_", "datetime", "SQL datetime type",),
	("CFVAL_DEC", FMAXCF_SCTN03TYPEDEF, "_DEC_", "decimal", "BCD like decimal sql value_",),
	("CFVAL_DECIMAL", FMAXCF_SCTN03TYPEDEF, "_DECIMAL_", "decimal", "BCD like decimal sql value_",),
	("CFVAL_DEF", FMAXCF_SCTN03TYPEDEF, "_DEF_", "_DEF_", "define in all uses",),
	("CFVAL_DICT", FMAXCF_SCTN03TYPEDEF, "_DICT_", "dict", "dict dictionary",),
	("CFVAL_DICTMODE_KEYSTR", FMAXCF_SCTN21STRDEF, "DICTMODE_KEYSTR", "DICTMODE_KEYSTR", "define dictmode 'key':val",),
	("CFVAL_DICTMODE_KEYVAL", FMAXCF_SCTN21STRDEF, "DICTMODE_KEYVAL", "DICTMODE_KEYVAL", "define dictmode key:val",),
	("CFVAL_FLD", FMAXCF_SCTN03TYPEDEF, "_FLD_", "varchar", "field in all uses",),
	("CFVAL_FLOAT", FMAXCF_SCTN03TYPEDEF, "_FLOAT_", "float", "standard floating point numbers",),
	("CFVAL_HASHER", FMAXCF_SCTN21STRDEF, "HASHER", "HASHER", "HASHER key",),
	("CFVAL_HASH_blake2b", FMAXCF_SCTN21VALDEF, "HASH_blake2b", "HL.blake2b()", "define blake2b value",),
	("CFVAL_HASH_blake2s", FMAXCF_SCTN21VALDEF, "HASH_blake2s", "HL.blake2s()", "define blake2s value",),
	("CFVAL_HASH_md5", FMAXCF_SCTN21VALDEF, "HASH_md5", "HL.md5()", "define md5 value",),
	("CFVAL_HASH_sha1", FMAXCF_SCTN21VALDEF, "HASH_sha1", "HL.sha1()", "define sha1 value",),
	("CFVAL_HASH_sha224", FMAXCF_SCTN21VALDEF, "HASH_sha224", "HL.sha224()", "define sha224 value",),
	("CFVAL_HASH_sha256", FMAXCF_SCTN21VALDEF, "HASH_sha256", "HL.sha256()", "define sha256 value",),
	("CFVAL_HASH_sha384", FMAXCF_SCTN21VALDEF, "HASH_sha384", "HL.sha384()", "define sha384 value",),
	("CFVAL_HASH_sha3_224", FMAXCF_SCTN21VALDEF, "HASH_sha3_224", "HL.sha3_224()", "define sha3_224 value",),
	("CFVAL_HASH_sha3_256", FMAXCF_SCTN21VALDEF, "HASH_sha3_256", "HL.sha3_256()", "define sha3_256 value",),
	("CFVAL_HASH_sha3_384", FMAXCF_SCTN21VALDEF, "HASH_sha3_384", "HL.sha3_384()", "define sha3_384 value",),
	("CFVAL_HASH_sha3_512", FMAXCF_SCTN21VALDEF, "HASH_sha3_512", "HL.sha3_512()", "define sha3_512 value",),
	("CFVAL_HASH_sha512", FMAXCF_SCTN21VALDEF, "HASH_sha512", "HL.sha512()", "define sha512 value",),
	("CFVAL_INT", FMAXCF_SCTN03TYPEDEF, "_INT_", "int", "integer any use",),
	("CFVAL_KEY", FMAXCF_SCTN03TYPEDEF, "_KEY_", "key", "_DICT_ or DB key",),
	("CFVAL_KNOWNFILES", FMAXCF_SCTN21STRDEF, "KNOWNFILES", "KNOWNFILES", "KNOWNFILES key",),
	("CFVAL_LIST", FMAXCF_SCTN03TYPEDEF, "_LIST_", "list", "list, table, etc.",),
	("CFVAL_LST", FMAXCF_SCTN03TYPEDEF, "_LST_", "_LST_", "list in all uses",),
	("CFVAL_MEDIAFILES", FMAXCF_SCTN21STRDEF, "MEDIAFILES", "MEDIAFILES", "MEDIAFILES key",),
	("CFVAL_META", FMAXCF_SCTN03TYPEDEF, "_META_", "metadata", "metadata in all uses",),
	("CFVAL_NOTKNOWNFILES", FMAXCF_SCTN21STRDEF, "NOTKNOWNFILES", "KNOWNFILES", "NOTKNOWNFILES key",),
	("CFVAL_NOTMEDIAFILES", FMAXCF_SCTN21STRDEF, "NOTMEDIAFILES", "MEDIAFILES", "NOTMEDIAFILES key",),
	("CFVAL_NOTRECURSE", FMAXCF_SCTN21STRDEF, "NOTRECURSE", "RECURSE", "NOTRECURSE key",),
	("CFVAL_NOTTRIALRUN", FMAXCF_SCTN21STRDEF, "NOTTRIALRUN", "TRIALRUN", "TRIALRUN key",),
	("CFVAL_NOTUNKNOWNFILES", FMAXCF_SCTN21STRDEF, "NOTUNKNOWNFILES", "UNKNOWNFILES", "NOTUNKNOWNFILES key",),
	("CFVAL_NUM", FMAXCF_SCTN03TYPEDEF, "_NUM_", "NUMBER", "number in all uses",),
	("CFVAL_STR", FMAXCF_SCTN03TYPEDEF, "_STR_", "varchar", "DB _STR_ to VARCHAR defined",),
	("CFVAL_TUP", FMAXCF_SCTN03TYPEDEF, "_TUP_", "tuple", "define a tuple short method",),
	("CFVAL_TUPLE", FMAXCF_SCTN03TYPEDEF, "_TUPLE_", "tuple", "define a tuple long method",),
	("CFVAL_TYPE", FMAXCF_SCTN03TYPEDEF, "_TYPE_", "type", "type in all uses",),
	("CFVAL_TYPES", FMAXCF_SCTN03TYPEDEF, "_TYPES_", "types", "types in all uses",),
	("DEVT_ABSREL00", FMAXDO_SCTN48EVTYPEDEF, "ABSREL", "EV type list entry ABSS",),
	("DEVT_ABSREL01", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_ABSRZ", "code for right stick X entries",),
	("DEVT_ABSREL02", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_ABSX", "code for left stick X entries",),
	("DEVT_ABSREL03", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_ABSY", "code for left stick Y entries",),
	("DEVT_ABSREL04", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_ABSZ", "code for right stick Y entries",),
	("DEVT_ABSREL05", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_DN", "code for right stick Y entries",),
	("DEVT_ABSREL06", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_DNLT", "code for right stick Y entries",),
	("DEVT_ABSREL07", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_DNRT", "code for right stick Y entries",),
	("DEVT_ABSREL08", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_LT", "code for right stick Y entries",),
	("DEVT_ABSREL09", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_RT", "code for right stick Y entries",),
	("DEVT_ABSREL0A", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_UP", "code for right stick Y entries",),
	("DEVT_ABSREL0B", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_UPLT", "code for right stick Y entries",),
	("DEVT_ABSREL0C", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGHAT_UPRT", "code for right stick Y entries",),
	("DEVT_ABSREL0D", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_DN", "code for right stick Y entries",),
	("DEVT_ABSREL0E", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_DNLT", "code for right stick Y entries",),
	("DEVT_ABSREL0F", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_DNRT", "code for right stick Y entries",),
	("DEVT_ABSREL10", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_LT", "code for right stick Y entries",),
	("DEVT_ABSREL11", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_RT", "code for right stick Y entries",),
	("DEVT_ABSREL12", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_UP", "code for right stick Y entries",),
	("DEVT_ABSREL13", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_UPLT", "code for right stick Y entries",),
	("DEVT_ABSREL14", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGLTSTK_UPRT", "code for right stick Y entries",),
	("DEVT_ABSREL15", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_DN", "code for right stick Y entries",),
	("DEVT_ABSREL16", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_DNLT", "code for right stick Y entries",),
	("DEVT_ABSREL17", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_DNRT", "code for right stick Y entries",),
	("DEVT_ABSREL18", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_LT", "code for right stick Y entries",),
	("DEVT_ABSREL19", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_RT", "code for right stick Y entries",),
	("DEVT_ABSREL1A", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_UP", "code for right stick Y entries",),
	("DEVT_ABSREL1B", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_UPLT", "code for right stick Y entries",),
	("DEVT_ABSREL1C", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNGRTSTK_UPRT", "code for right stick Y entries",),
	("DEVT_ABSREL1D", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_DN", "BTNMWHLDN/MSE_DN on mice",),
	("DEVT_ABSREL1E", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_DNLT", "BTNMWHLDN/MSE_DNLT on mice",),
	("DEVT_ABSREL1F", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_DNRT", "BTNMWHLDN/MSE_DNRT on mice",),
	("DEVT_ABSREL20", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_LT", "BTNMWHLLT/MSE_LT on mice",),
	("DEVT_ABSREL21", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_RT", "BTNMWHLRT/MSE_RT on mice",),
	("DEVT_ABSREL22", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_UP", "BTNMWHLUP/MSE_UP on mice",),
	("DEVT_ABSREL23", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_UPLT", "BTNMWHLUP/MSE_UPLT on mice",),
	("DEVT_ABSREL24", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNMWH_UPRT", "BTNMWHLUP/MSE_UPRT on mice",),
	("DEVT_ABSREL25", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MDN", "BTNMDN/MSE_DN on mice",),
	("DEVT_ABSREL26", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MDNLT", "BTNMDN/MSE_DNLT on mice",),
	("DEVT_ABSREL27", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MDNRT", "BTNMDN/MSE_DNRT on mice",),
	("DEVT_ABSREL28", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MLT", "BTNMLT/MSE_LT on mice",),
	("DEVT_ABSREL29", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MRT", "BTNMRT/MSE_RT on mice",),
	("DEVT_ABSREL2A", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MUP", "BTNMUP/MSE_UP on mice",),
	("DEVT_ABSREL2B", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MUPLT", "BTNMUP/MSE_UPLT on mice",),
	("DEVT_ABSREL2C", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_BTNM_MUPRT", "BTNMUP/MSE_UPRT on mice",),
	("DEVT_ABSREL2D", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_HAT0X", "code for hat X entries",),
	("DEVT_ABSREL2E", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_HAT0Y", "code for hat Y entries",),
	("DEVT_ABSREL2F", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_RELHRHWHL", "DEVCD_RELHRHWHL entry",),
	("DEVT_ABSREL30", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_RELHRWHL", "DEVCD_RELHRWHL entry",),
	("DEVT_ABSREL31", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_RELHWHL", "DEVCD_RELHWHL entry",),
	("DEVT_ABSREL32", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_RELWHL", "DEVCD_RELWHL entry",),
	("DEVT_ABSREL33", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_RELX", "DEVCD_RELX entry",),
	("DEVT_ABSREL34", FMAXDO_SCTN48EVTYPELST, "ABSREL", "DEVCD_RELY", "DEVCD_RELY entry",),
	("DEVT_ABSS00", FMAXDO_SCTN48EVTYPEDEF, "ABSS", "EV type list entry ABSS",),
	("DEVT_ABSS01", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_ABSRZ", "code for right stick X entries",),
	("DEVT_ABSS02", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_ABSX", "code for left stick X entries",),
	("DEVT_ABSS03", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_ABSY", "code for left stick Y entries",),
	("DEVT_ABSS04", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_ABSZ", "code for right stick Y entries",),
	("DEVT_ABSS05", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_DN", "code for right stick Y entries",),
	("DEVT_ABSS06", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_DNLT", "code for right stick Y entries",),
	("DEVT_ABSS07", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_DNRT", "code for right stick Y entries",),
	("DEVT_ABSS08", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_LT", "code for right stick Y entries",),
	("DEVT_ABSS09", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_RT", "code for right stick Y entries",),
	("DEVT_ABSS0A", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_UP", "code for right stick Y entries",),
	("DEVT_ABSS0B", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_UPLT", "code for right stick Y entries",),
	("DEVT_ABSS0C", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGHAT_UPRT", "code for right stick Y entries",),
	("DEVT_ABSS0D", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_DN", "code for right stick Y entries",),
	("DEVT_ABSS0E", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_DNLT", "code for right stick Y entries",),
	("DEVT_ABSS0F", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_DNRT", "code for right stick Y entries",),
	("DEVT_ABSS10", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_LT", "code for right stick Y entries",),
	("DEVT_ABSS11", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_RT", "code for right stick Y entries",),
	("DEVT_ABSS12", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_UP", "code for right stick Y entries",),
	("DEVT_ABSS13", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_UPLT", "code for right stick Y entries",),
	("DEVT_ABSS14", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGLTSTK_UPRT", "code for right stick Y entries",),
	("DEVT_ABSS15", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_DN", "code for right stick Y entries",),
	("DEVT_ABSS16", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_DNLT", "code for right stick Y entries",),
	("DEVT_ABSS17", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_DNRT", "code for right stick Y entries",),
	("DEVT_ABSS18", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_LT", "code for right stick Y entries",),
	("DEVT_ABSS19", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_RT", "code for right stick Y entries",),
	("DEVT_ABSS1A", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_UP", "code for right stick Y entries",),
	("DEVT_ABSS1B", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_UPLT", "code for right stick Y entries",),
	("DEVT_ABSS1C", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_BTNGRTSTK_UPRT", "code for right stick Y entries",),
	("DEVT_ABSS1D", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_HAT0X", "code for hat X entries",),
	("DEVT_ABSS1E", FMAXDO_SCTN48EVTYPELST, "ABSS", "DEVCD_HAT0Y", "code for hat Y entries",),
	("DEVT_BTNS00", FMAXDO_SCTN48EVTYPEDEF, "BTNS", "EV type list BTNS entry",),
	("DEVT_BTNS01", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_BTNS02", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_DN", "DEVCD_BTNGHAT_DN entry in BTNS",),
	("DEVT_BTNS03", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_DNLT", "DEVCD_BTNGHAT_DNLT entry in BTNS",),
	("DEVT_BTNS04", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_DNRT", "DEVCD_BTNGHAT_DNRT entry in BTNS",),
	("DEVT_BTNS05", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_LT", "DEVCD_BTNGHAT_LT entry in BTNS",),
	("DEVT_BTNS06", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_RT", "DEVCD_BTNGHAT_RT entry in BTNS",),
	("DEVT_BTNS07", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_UP", "DEVCD_BTNGHAT_UP entry in BTNS",),
	("DEVT_BTNS08", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_UPLT", "DEVCD_BTNGHAT_UPLT entry in BTNS",),
	("DEVT_BTNS09", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGHAT_UPRT", "DEVCD_BTNGHAT_UPRT entry in BTNS",),
	("DEVT_BTNS0A", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_DN", "DEVCD_BTNGLTSTK_DN entry in BTNS",),
	("DEVT_BTNS0B", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_DNLT", "DEVCD_BTNGLTSTK_DNLT entry in BTNS",),
	("DEVT_BTNS0C", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_DNRT", "DEVCD_BTNGLTSTK_DNRT entry in BTNS",),
	("DEVT_BTNS0D", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_LT", "DEVCD_BTNGLTSTK_LT entry in BTNS",),
	("DEVT_BTNS0E", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_BTNS0F", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_RT", "DEVCD_BTNGLTSTK_RT entry in BTNS",),
	("DEVT_BTNS10", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_UP", "DEVCD_BTNGLTSTK_UP entry in BTNS",),
	("DEVT_BTNS11", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_UPLT", "DEVCD_BTNGLTSTK_UPLT entry in BTNS",),
	("DEVT_BTNS12", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGLTSTK_UPRT", "DEVCD_BTNGLTSTK_UPRT entry in BTNS",),
	("DEVT_BTNS13", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_DN", "DEVCD_BTNGRTSTK_DN entry in BTNS",),
	("DEVT_BTNS14", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_DNLT", "DEVCD_BTNGRTSTK_DNLT entry in BTNS",),
	("DEVT_BTNS15", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_DNRT", "DEVCD_BTNGRTSTK_DNRT entry in BTNS",),
	("DEVT_BTNS16", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_LT", "DEVCD_BTNGRTSTK_LT entry in BTNS",),
	("DEVT_BTNS17", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_BTNS18", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_RT", "DEVCD_BTNGRTSTK_RT entry in BTNS",),
	("DEVT_BTNS19", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_UP", "DEVCD_BTNGRTSTK_UP entry in BTNS",),
	("DEVT_BTNS1A", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_UPLT", "DEVCD_BTNGRTSTK_UPLT entry in BTNS",),
	("DEVT_BTNS1B", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNGRTSTK_UPRT", "DEVCD_BTNGRTSTK_UPRT entry in BTNS",),
	("DEVT_BTNS1C", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_01", "DEVCD_BTNG_01 entry in BTNS",),
	("DEVT_BTNS1D", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_02", "DEVCD_BTNG_02 entry in BTNS",),
	("DEVT_BTNS1E", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_03", "DEVCD_BTNG_03 entry in BTNS",),
	("DEVT_BTNS1F", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_04", "DEVCD_BTNG_04 entry in BTNS",),
	("DEVT_BTNS20", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_05", "DEVCD_BTNG_05 entry in BTNS",),
	("DEVT_BTNS21", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_06", "DEVCD_BTNG_06 entry in BTNS",),
	("DEVT_BTNS22", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_07", "DEVCD_BTNG_07 entry in BTNS",),
	("DEVT_BTNS23", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_08", "DEVCD_BTNG_08 entry in BTNS",),
	("DEVT_BTNS24", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_09", "DEVCD_BTNG_09 entry in BTNS",),
	("DEVT_BTNS25", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_10", "DEVCD_BTNG_10 entry in BTNS",),
	("DEVT_BTNS26", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_11LTSTK", "DEVCD_BTNG_11LTSTK entry in BTNS",),
	("DEVT_BTNS27", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_12RTSTK", "DEVCD_BTNG_12RTSTK entry in BTNS",),
	("DEVT_BTNS28", FMAXDO_SCTN48EVTYPELST, "BTNS", "DEVCD_BTNG_13", "DEVCD_BTNG_13 entry in BTNS",),
	("DEVT_HATS00", FMAXDO_SCTN48EVTYPEDEF, "HATS", "EV type list entry HAT",),
	("DEVT_HATS01", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_DN", "code for hat as BTN",),
	("DEVT_HATS02", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_DNLT", "code for hat as BTN",),
	("DEVT_HATS03", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_DNRT", "code for hat as BTN",),
	("DEVT_HATS04", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_LT", "code for hat as BTN",),
	("DEVT_HATS05", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_RLS", "code for hat as BTN",),
	("DEVT_HATS06", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_RT", "code for hat as BTN",),
	("DEVT_HATS07", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_UP", "code for hat as BTN",),
	("DEVT_HATS08", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_UPLT", "code for hat as BTN",),
	("DEVT_HATS09", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_BTNGHAT_UPRT", "code for hat as BTN",),
	("DEVT_HATS0A", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_HAT0X", "code for hat stick X entries",),
	("DEVT_HATS0B", FMAXDO_SCTN48EVTYPELST, "HATS", "DEVCD_HAT0Y", "code for hat stick Y entries",),
	("DEVT_LTSTK00", FMAXDO_SCTN48EVTYPEDEF, "LTSTK", "EV type list entry LTSTK",),
	("DEVT_LTSTK01", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_ABSX", "code for left stick X entries",),
	("DEVT_LTSTK02", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_ABSY", "code for left stick Y entries",),
	("DEVT_LTSTK03", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_DN", "DEVCD_BTNGLTSTK_DN entry in BTNS",),
	("DEVT_LTSTK04", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_DNLT", "DEVCD_BTNGLTSTK_DNLT entry in BTNS",),
	("DEVT_LTSTK05", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_DNRT", "DEVCD_BTNGLTSTK_DNRT entry in BTNS",),
	("DEVT_LTSTK06", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_LT", "DEVCD_BTNGLTSTK_LT entry in BTNS",),
	("DEVT_LTSTK07", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_LTSTK08", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_RT", "DEVCD_BTNGLTSTK_RT entry in BTNS",),
	("DEVT_LTSTK09", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_UP", "DEVCD_BTNGLTSTK_UP entry in BTNS",),
	("DEVT_LTSTK0A", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_UPLT", "DEVCD_BTNGLTSTK_UPLT entry in BTNS",),
	("DEVT_LTSTK0B", FMAXDO_SCTN48EVTYPELST, "LTSTK", "DEVCD_BTNGLTSTK_UPRT", "DEVCD_BTNGLTSTK_UPRT entry in BTNS",),
	("DEVT_RELS00", FMAXDO_SCTN48EVTYPEDEF, "RELS", "EV type for RELS supported",),
	("DEVT_RELS01", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_DN", "BTNMWHLDN/MSE_DN on mice",),
	("DEVT_RELS02", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_DNLT", "BTNMWHLDN/MSE_DNLT on mice",),
	("DEVT_RELS03", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_DNRT", "BTNMWHLDN/MSE_DNRT on mice",),
	("DEVT_RELS04", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_LT", "BTNMWHLLT/MSE_LT on mice",),
	("DEVT_RELS05", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_RT", "BTNMWHLRT/MSE_RT on mice",),
	("DEVT_RELS06", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_UP", "BTNMWHLUP/MSE_UP on mice",),
	("DEVT_RELS07", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_UPLT", "BTNMWHLUP/MSE_UPLT on mice",),
	("DEVT_RELS08", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNMWH_UPRT", "BTNMWHLUP/MSE_UPRT on mice",),
	("DEVT_RELS09", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MDN", "BTNMDN/MSE_DN on mice",),
	("DEVT_RELS0A", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MDNLT", "BTNMDN/MSE_DNLT on mice",),
	("DEVT_RELS0B", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MDNRT", "BTNMDN/MSE_DNRT on mice",),
	("DEVT_RELS0C", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MLT", "BTNMLT/MSE_LT on mice",),
	("DEVT_RELS0D", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MRT", "BTNMRT/MSE_RT on mice",),
	("DEVT_RELS0E", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MUP", "BTNMUP/MSE_UP on mice",),
	("DEVT_RELS0F", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MUPLT", "BTNMUP/MSE_UPLT on mice",),
	("DEVT_RELS10", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_BTNM_MUPRT", "BTNMUP/MSE_UPRT on mice",),
	("DEVT_RELS11", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_RELHRHWHL", "DEVCD_RELHRHWHL entry",),
	("DEVT_RELS12", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_RELHRWHL", "DEVCD_RELHRWHL entry",),
	("DEVT_RELS13", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_RELHWHL", "DEVCD_RELHWHL entry",),
	("DEVT_RELS14", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_RELWHL", "DEVCD_RELWHL entry",),
	("DEVT_RELS15", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_RELX", "DEVCD_RELX entry",),
	("DEVT_RELS16", FMAXDO_SCTN48EVTYPELST, "RELS", "DEVCD_RELY", "DEVCD_RELY entry",),
	("DEVT_RTSTK00", FMAXDO_SCTN48EVTYPEDEF, "RTSTK", "EV type list entry RTSTK",),
	("DEVT_RTSTK01", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_ABSRZ", "code for right stick X entries",),
	("DEVT_RTSTK02", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_ABSZ", "code for right stick Y entries",),
	("DEVT_RTSTK03", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_DN", "DEVCD_BTNGLTSTK_DN entry in BTNS",),
	("DEVT_RTSTK04", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_DNLT", "DEVCD_BTNGLTSTK_DNLT entry in BTNS",),
	("DEVT_RTSTK05", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_DNRT", "DEVCD_BTNGLTSTK_DNRT entry in BTNS",),
	("DEVT_RTSTK06", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_LT", "DEVCD_BTNGLTSTK_LT entry in BTNS",),
	("DEVT_RTSTK07", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_RTSTK08", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_RT", "DEVCD_BTNGLTSTK_RT entry in BTNS",),
	("DEVT_RTSTK09", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_UP", "DEVCD_BTNGLTSTK_UP entry in BTNS",),
	("DEVT_RTSTK0A", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_UPLT", "DEVCD_BTNGLTSTK_UPLT entry in BTNS",),
	("DEVT_RTSTK0B", FMAXDO_SCTN48EVTYPELST, "RTSTK", "DEVCD_BTNGRTSTK_UPRT", "DEVCD_BTNGLTSTK_UPRT entry in BTNS",),
	("DEVT_STICKS00", FMAXDO_SCTN48EVTYPEDEF, "STICKS", "EV type list entry STICKS",),
	("DEVT_STICKS01", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_ABSRZ", "code for right stick X entries",),
	("DEVT_STICKS02", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_ABSX", "code for left stick X entries",),
	("DEVT_STICKS03", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_ABSY", "code for left stick Y entries",),
	("DEVT_STICKS04", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_ABSZ", "code for right stick Y entries",),
	("DEVT_STICKS05", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_DN", "DEVCD_BTNGLTSTK_DN entry in BTNS",),
	("DEVT_STICKS06", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_DNLT", "DEVCD_BTNGLTSTK_DNLT entry in BTNS",),
	("DEVT_STICKS07", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_DNRT", "DEVCD_BTNGLTSTK_DNRT entry in BTNS",),
	("DEVT_STICKS08", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_LT", "DEVCD_BTNGLTSTK_LT entry in BTNS",),
	("DEVT_STICKS09", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_STICKS0A", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_RT", "DEVCD_BTNGLTSTK_RT entry in BTNS",),
	("DEVT_STICKS0B", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_UP", "DEVCD_BTNGLTSTK_UP entry in BTNS",),
	("DEVT_STICKS0C", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_UPLT", "DEVCD_BTNGLTSTK_UPLT entry in BTNS",),
	("DEVT_STICKS0D", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGLTSTK_UPRT", "DEVCD_BTNGLTSTK_UPRT entry in BTNS",),
	("DEVT_STICKS0E", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_DN", "DEVCD_BTNGLTSTK_DN entry in BTNS",),
	("DEVT_STICKS0F", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_DNLT", "DEVCD_BTNGLTSTK_DNLT entry in BTNS",),
	("DEVT_STICKS10", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_DNRT", "DEVCD_BTNGLTSTK_DNRT entry in BTNS",),
	("DEVT_STICKS11", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_LT", "DEVCD_BTNGLTSTK_LT entry in BTNS",),
	("DEVT_STICKS12", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_RLS", "DEVCD_BTNGHAT_RLS entry in BTNS",),
	("DEVT_STICKS13", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_RT", "DEVCD_BTNGLTSTK_RT entry in BTNS",),
	("DEVT_STICKS14", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_UP", "DEVCD_BTNGLTSTK_UP entry in BTNS",),
	("DEVT_STICKS15", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_UPLT", "DEVCD_BTNGLTSTK_UPLT entry in BTNS",),
	("DEVT_STICKS16", FMAXDO_SCTN48EVTYPELST, "STICKS", "DEVCD_BTNGRTSTK_UPRT", "DEVCD_BTNGLTSTK_UPRT entry in BTNS",),
	("DEVT_WHLS00", FMAXDO_SCTN48EVTYPEDEF, "WHLS", "EV type for WHLS supported",),
	("DEVT_WHLS01", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_RELHRHWHL", "DEVCD_RELHRHWHL entry",),
	("DEVT_WHLS02", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_RELHRWHL", "DEVCD_RELHRWHL entry",),
	("DEVT_WHLS03", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_RELHWHL", "DEVCD_RELHWHL entry",),
	("DEVT_WHLS04", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_RELWHL", "DEVCD_RELWHL entry",),
	("DEVT_WHLS05", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_DN", "DEVCD_RELWHL entry",),
	("DEVT_WHLS06", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_DNLT", "DEVCD_RELWHL entry",),
	("DEVT_WHLS07", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_DNRT", "DEVCD_RELWHL entry",),
	("DEVT_WHLS08", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_LT", "DEVCD_RELWHL entry",),
	("DEVT_WHLS09", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_RLS", "DEVCD_RELWHL entry",),
	("DEVT_WHLS0A", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_RT", "DEVCD_RELWHL entry",),
	("DEVT_WHLS0B", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_UP", "DEVCD_RELWHL entry",),
	("DEVT_WHLS0C", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_UPLT", "DEVCD_RELWHL entry",),
	("DEVT_WHLS0D", FMAXDO_SCTN48EVTYPELST, "WHLS", "DEVCD_BTNMWH_UPRT", "DEVCD_RELWHL entry",),
	("DOVAL_ABSDEADWIDTH", FMAXDO_SCTN41DICTKEYDEF, "ABSDEADWIDTH", "key for stick dead width",),
	("DOVAL_ABSMAX", FMAXDO_SCTN41DICTKEYDEF, "ABSMAX", "key for stick max",),
	("DOVAL_ABSMAXVAL", FMAXDO_SCTN41VALDEF, "ABSMAXVAL", "0XFFFFFFFFFFFFFFFF", "key for stick max val",),
	("DOVAL_ABSMIN", FMAXDO_SCTN41DICTKEYDEF, "ABSMIN", "key for stick min",),
	("DOVAL_ABSMINVAL", FMAXDO_SCTN41VALDEF, "ABSMINVAL", "-0XFFFFFFFFFFFFFFFF", "key for min stick val",),
	("DOVAL_ABSZERO", FMAXDO_SCTN41DICTKEYDEF, "ABSZERO", "stick center/resting position key",),
	("DOVAL_ABSZEROVAL", FMAXDO_SCTN41VALDEF, "ABSZEROVAL", "0X0000000000000000", "val used for stick 0 position",),
	("DOVAL_ABS_HAT0X", FMAXDO_SCTN41DICTKEYDEF, "ABS_HAT0X", "key for hat 0 X, the first, or only hat on the device",),
	("DOVAL_ABS_HAT0Y", FMAXDO_SCTN41DICTKEYDEF, "ABS_HAT0Y", "key for hat 0 Y, the first, or only hat on the device",),
	("DOVAL_ABS_RZ", FMAXDO_SCTN41DICTKEYDEF, "ABS_RZ", "key for stick 1 Y",),
	("DOVAL_ABS_X", FMAXDO_SCTN41DICTKEYDEF, "ABS_X", "key for stick 0 X",),
	("DOVAL_ABS_Y", FMAXDO_SCTN41DICTKEYDEF, "ABS_Y", "key for stick 0 Y",),
	("DOVAL_ABS_Z", FMAXDO_SCTN41DICTKEYDEF, "ABS_Z", "key for stick 1 X",),
	("DOVAL_BTNS00", FMAXDO_SCTN41VALDEF, "BTNS00", "0B00000001", "FLAG LD.EV_KEY holdable BTN0 GPM",),
	("DOVAL_BTNS05", FMAXDO_SCTN41VALDEF, "BTNS05", "0B00000010", "FLAG LD.EV_KEY holdable BTN5 gamepads",),
	("DOVAL_BTNS06", FMAXDO_SCTN41VALDEF, "BTNS06", "0B00000100", "FLAG LD.EV_KEY holdable BTN6 gamepads",),
	("DOVAL_BTNS07", FMAXDO_SCTN41VALDEF, "BTNS07", "0B00001000", "FLAG LD.EV_KEY holdable BTN7 gamepads",),
	("DOVAL_BTNS08", FMAXDO_SCTN41VALDEF, "BTNS08", "0B00010000", "FLAG LD.EV_KEY holdable BTN8 gamepads",),
	("DOVAL_BTNS22", FMAXDO_SCTN41VALDEF, "BTNS22", "0B00100000", "FLAG LD.EV_KEY holdable BTN22 saitek",),
	("DOVAL_BTNS23", FMAXDO_SCTN41VALDEF, "BTNS23", "0B01000000", "FLAG LD.EV_KEY holdable BTN23 saitek",),
	("DOVAL_BTNS24", FMAXDO_SCTN41VALDEF, "BTNS24", "0B10000000", "FLAG LD.EV_KEY holdable BTN24 saitek",),
	("DOVAL_BTNS_NOT", FMAXDO_SCTN41VALDEF, "BTNS_NOT", "0B00000000", "FLAG no BTN or _KEY_ held",),
	("DOVAL_BTNTYPE", FMAXDO_SCTN41DICTKEYDEF, "BTNTYPE", "action type key",),
	("DOVAL_BTNTYPE_HOLDABLE", FMAXDO_SCTN41STRDEF, "BTNTYPE_HOLDABLE", "BTNTYPE_HOLDABLE", "HOLDABLE button",),
	("DOVAL_BTNTYPE_LOCKING", FMAXDO_SCTN41DICTKEYDEF, "BTNTYPE_LOCKING", "action type key",),
	("DOVAL_BTNTYPE_NORMAL", FMAXDO_SCTN41DICTKEYDEF, "BTNTYPE_NORMAL", "action type NORMAL key",),
	("DOVAL_BTNTYPE_NOTHOLDABLE", FMAXDO_SCTN41STRDEF, "BTNTYPE_NOTHOLDABLE", "BTNTYPE_NOTHOLDABLE", "NOTHOLDABLE button",),
	("DOVAL_BTNTYPE_PUSHRELEASE", FMAXDO_SCTN41DICTKEYDEF, "BTNTYPE_PUSHRELEASE", "action type key",),
	("DOVAL_BTNTYPE_SIMABS", FMAXDO_SCTN41STRDEF, "BTNTYPE_SIMABS", "BTNTYPE_SIMABS", "simulated ABS button",),
	("DOVAL_BTNTYPE_SIMREL", FMAXDO_SCTN41STRDEF, "BTNTYPE_SIMREL", "BTNTYPE_SIMREL", "simulated REL button",),
	("DOVAL_BTNTYPE_TOGGLE", FMAXDO_SCTN41DICTKEYDEF, "BTNTYPE_TOGGLE", "action type key",),
	("DOVAL_BTNTYPE_WITHPAUSE", FMAXDO_SCTN41DICTKEYDEF, "BTNTYPE_WITHPAUSE", "action type key",),
	("DOVAL_DEFT", FMAXDO_SCTN41DICTKEYDEF, "DEFT", "device DEFT mouse",),
	("DOVAL_DEVCD_ABSRZ", FMAXDO_SCTN41VALDEF, "DEVCD_ABSRZ", "LD.EV_ABS.ABS_RZ", "shortcut to ABS_RZ",),
	("DOVAL_DEVCD_ABSX", FMAXDO_SCTN41VALDEF, "DEVCD_ABSX", "LD.EV_ABS.ABS_X", "shortcut to ABS_X",),
	("DOVAL_DEVCD_ABSY", FMAXDO_SCTN41VALDEF, "DEVCD_ABSY", "LD.EV_ABS.ABS_Y", "shortcut to ABS_HAT0Y",),
	("DOVAL_DEVCD_ABSZ", FMAXDO_SCTN41VALDEF, "DEVCD_ABSZ", "LD.EV_ABS.ABS_Z", "shortcut to ABS_Z",),
	("DOVAL_DEVCD_BTNGHAT_DN", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_DN", "BTNGHAT_DN", "shortcut to BTNGHAT_DN",),
	("DOVAL_DEVCD_BTNGHAT_DNLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_DNLT", "BTNGHAT_DNLT", "shortcut to BTNGHAT_DN",),
	("DOVAL_DEVCD_BTNGHAT_DNRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_DNRT", "BTNGHAT_DNRT", "shortcut to BTNGHAT_DN",),
	("DOVAL_DEVCD_BTNGHAT_LT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_LT", "BTNGHAT_LT", "shortcut to BTNGHAT_LT",),
	("DOVAL_DEVCD_BTNGHAT_RLS", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_RLS", "BTNGHAT_RLS", "shortcut to BTNGHAT_RLS",),
	("DOVAL_DEVCD_BTNGHAT_RT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_RT", "BTNGHAT_RT", "shortcut to BTNGHAT_RT",),
	("DOVAL_DEVCD_BTNGHAT_UP", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_UP", "BTNGHAT_UP", "shortcut to BTNGHAT_UP",),
	("DOVAL_DEVCD_BTNGHAT_UPLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_UPLT", "BTNGHAT_UPLT", "shortcut to BTNGHAT_UP",),
	("DOVAL_DEVCD_BTNGHAT_UPRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGHAT_UPRT", "BTNGHAT_UPRT", "shortcut to BTNGHAT_UP",),
	("DOVAL_DEVCD_BTNGLTSTK_DN", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_DN", "BTNGLTSTK_DN", "shortcut to BTNGLTSTK_DN",),
	("DOVAL_DEVCD_BTNGLTSTK_DNLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_DNLT", "BTNGLTSTK_DNLT", "shortcut to BTNGLTSTK_DN",),
	("DOVAL_DEVCD_BTNGLTSTK_DNRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_DNRT", "BTNGLTSTK_DNRT", "shortcut to BTNGLTSTK_DN",),
	("DOVAL_DEVCD_BTNGLTSTK_LT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_LT", "BTNGLTSTK_LT", "shortcut to BTNGLTSTK_LT",),
	("DOVAL_DEVCD_BTNGLTSTK_RLS", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_RLS", "BTNGLTSTK_RLS", "shortcut to BTNGLTSTK_RT",),
	("DOVAL_DEVCD_BTNGLTSTK_RT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_RT", "BTNGLTSTK_RT", "shortcut to BTNGLTSTK_RT",),
	("DOVAL_DEVCD_BTNGLTSTK_UP", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_UP", "BTNGLTSTK_UP", "shortcut to BTNGLTSTK_UP",),
	("DOVAL_DEVCD_BTNGLTSTK_UPLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_UPLT", "BTNGLTSTK_UPLT", "shortcut to BTNGLTSTK_UPLT",),
	("DOVAL_DEVCD_BTNGLTSTK_UPRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGLTSTK_UPRT", "BTNGLTSTK_UPRT", "shortcut to BTNGLTSTK_UPRT",),
	("DOVAL_DEVCD_BTNGRTSTK_DN", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_DN", "BTNGRTSTK_DN", "shortcut to BTNGRTSTK_DN",),
	("DOVAL_DEVCD_BTNGRTSTK_DNLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_DNLT", "BTNGRTSTK_DNLT", "shortcut to BTNGRTSTK_DNLT",),
	("DOVAL_DEVCD_BTNGRTSTK_DNRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_DNRT", "BTNGRTSTK_DNRT", "shortcut to BTNGRTSTK_DNRT",),
	("DOVAL_DEVCD_BTNGRTSTK_LT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_LT", "BTNGRTSTK_LT", "shortcut to BTNGRTSTK_LT",),
	("DOVAL_DEVCD_BTNGRTSTK_RLS", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_RLS", "BTNGRTSTK_RLS", "shortcut to BTNGRTSTK_RT",),
	("DOVAL_DEVCD_BTNGRTSTK_RT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_RT", "BTNGRTSTK_RT", "shortcut to BTNGRTSTK_RT",),
	("DOVAL_DEVCD_BTNGRTSTK_UP", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_UP", "BTNGRTSTK_UP", "shortcut to BTNGRTSTK_UP",),
	("DOVAL_DEVCD_BTNGRTSTK_UPLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_UPLT", "BTNGRTSTK_UPLT", "shortcut to BTNGRTSTK_UPLT",),
	("DOVAL_DEVCD_BTNGRTSTK_UPRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNGRTSTK_UPRT", "BTNGRTSTK_UPRT", "shortcut to BTNGRTSTK_UPRT",),
	("DOVAL_DEVCD_BTNG_01", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_01", "BTNG_01", "shortcut to BTNG_01",),
	("DOVAL_DEVCD_BTNG_02", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_02", "BTNG_02", "shortcut to BTNG_02",),
	("DOVAL_DEVCD_BTNG_03", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_03", "BTNG_03", "shortcut to BTNG_03",),
	("DOVAL_DEVCD_BTNG_04", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_04", "BTNG_04", "shortcut to BTNG_04",),
	("DOVAL_DEVCD_BTNG_05", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_05", "BTNG_05", "shortcut to BTNG_05",),
	("DOVAL_DEVCD_BTNG_06", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_06", "BTNG_06", "shortcut to BTNG_06",),
	("DOVAL_DEVCD_BTNG_07", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_07", "BTNG_07", "shortcut to BTNG_07",),
	("DOVAL_DEVCD_BTNG_08", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_08", "BTNG_08", "shortcut to BTNG_08",),
	("DOVAL_DEVCD_BTNG_09", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_09", "BTNG_09", "shortcut to BTNG_09",),
	("DOVAL_DEVCD_BTNG_10", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_10", "BTNG_10", "shortcut to BTNG_10",),
	("DOVAL_DEVCD_BTNG_11LTSTK", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_11LTSTK", "BTNG_11LTSTK", "shortcut to BTNG_11LTSTK",),
	("DOVAL_DEVCD_BTNG_12RTSTK", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_12RTSTK", "BTNG_12RTSTK", "shortcut to BTNG_12RTSTK",),
	("DOVAL_DEVCD_BTNG_13", FMAXDO_SCTN41VALDEF, "DEVCD_BTNG_13", "BTNG_13", "shortcut to BTNG_13",),
	("DOVAL_DEVCD_BTNMWH_DN", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_DN", "BTNMWH_DN", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNMWH_DNLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_DNLT", "BTNMWH_DNLT", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNMWH_DNRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_DNRT", "BTNMWH_DNRT", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNMWH_LT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_LT", "BTNMWH_LT", "shortcut to BTNM_06WHLT",),
	("DOVAL_DEVCD_BTNMWH_RLS", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_RLS", "BTNMWH_RLS", "shortcut to BTNM_07WHRT",),
	("DOVAL_DEVCD_BTNMWH_RT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_RT", "BTNMWH_RT", "shortcut to BTNM_07WHRT",),
	("DOVAL_DEVCD_BTNMWH_UP", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_UP", "BTNMWH_UP", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_BTNMWH_UPLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_UPLT", "BTNMWH_UPLT", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_BTNMWH_UPRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNMWH_UPRT", "BTNMWH_UPRT", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_BTNM_01LT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_01LT", "BTNM_01LT", "shortcut to BTNM_01LT",),
	("DOVAL_DEVCD_BTNM_02MD", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_02MD", "BTNM_02MD", "shortcut to BTNM_02MD",),
	("DOVAL_DEVCD_BTNM_03RT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_03RT", "BTNM_03RT", "shortcut to BTNM_03RT",),
	("DOVAL_DEVCD_BTNM_04WHUP", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_04WHUP", "BTNM_04WHUP", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_BTNM_05WHDN", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_05WHDN", "BTNM_05WHDN", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNM_06WHLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_06WHLT", "BTNM_06WHLT", "shortcut to BTNM_06WHLT",),
	("DOVAL_DEVCD_BTNM_07WHRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_07WHRT", "BTNM_07WHRT", "shortcut to BTNM_07WHRT",),
	("DOVAL_DEVCD_BTNM_08", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_08", "BTNM_08", "shortcut to BTNM_08",),
	("DOVAL_DEVCD_BTNM_09", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_09", "BTNM_09", "shortcut to BTNM_09",),
	("DOVAL_DEVCD_BTNM_10", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_10", "BTNM_10", "shortcut to BTNM_10",),
	("DOVAL_DEVCD_BTNM_11", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_11", "BTNM_11", "shortcut to BTNM_11",),
	("DOVAL_DEVCD_BTNM_12", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_12", "BTNM_12", "shortcut to BTNM_12",),
	("DOVAL_DEVCD_BTNM_MDN", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MDN", "BTNM_MDN", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNM_MDNLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MDNLT", "BTNM_MDNLT", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNM_MDNRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MDNRT", "BTNM_MDNRT", "shortcut to BTNM_05WHDN",),
	("DOVAL_DEVCD_BTNM_MLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MLT", "BTNM_MLT", "shortcut to BTNM_06WHLT",),
	("DOVAL_DEVCD_BTNM_MRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MRT", "BTNM_MRT", "shortcut to BTNM_07WHRT",),
	("DOVAL_DEVCD_BTNM_MUP", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MUP", "BTNM_MUP", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_BTNM_MUPLT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MUPLT", "BTNM_MUPLT", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_BTNM_MUPRT", FMAXDO_SCTN41VALDEF, "DEVCD_BTNM_MUPRT", "BTNM_MUPRT", "shortcut to BTNM_04WHUP",),
	("DOVAL_DEVCD_HAT0X", FMAXDO_SCTN41VALDEF, "DEVCD_HAT0X", "LD.EV_ABS.ABS_HAT0X", "shortcut to ABS_HAT0X",),
	("DOVAL_DEVCD_HAT0Y", FMAXDO_SCTN41VALDEF, "DEVCD_HAT0Y", "LD.EV_ABS.ABS_HAT0Y", "shortcut to ABS_HAT0Y",),
	("DOVAL_DEVCD_RELHRHWHL", FMAXDO_SCTN41VALDEF, "DEVCD_RELHRHWHL", "LD.EV_REL.REL_HWHEEL_HI_RES", "shortcut to REL_HWHEEL_HI_RES",),
	("DOVAL_DEVCD_RELHRWHL", FMAXDO_SCTN41VALDEF, "DEVCD_RELHRWHL", "LD.EV_REL.REL_WHEEL_HI_RES", "shortcut to REL_WHEEL_HI_RES",),
	("DOVAL_DEVCD_RELHWHL", FMAXDO_SCTN41VALDEF, "DEVCD_RELHWHL", "LD.EV_REL.REL_HWHEEL", "shortcut to REL_HWHEEL",),
	("DOVAL_DEVCD_RELWHL", FMAXDO_SCTN41VALDEF, "DEVCD_RELWHL", "LD.EV_REL.REL_WHEEL", "shortcut to REL_WHEEL",),
	("DOVAL_DEVCD_RELX", FMAXDO_SCTN41VALDEF, "DEVCD_RELX", "LD.EV_REL.REL_X", "shortcut to REL_X",),
	("DOVAL_DEVCD_RELY", FMAXDO_SCTN41VALDEF, "DEVCD_RELY", "LD.EV_REL.REL_Y", "shortcut to REL_Y",),
	("DOVAL_DEVICESTATUS_CONNECTED", FMAXDO_SCTN41DICTKEYDEF, "DEVICESTATUS_CONNECTED", "status connected",),
	("DOVAL_DEVICESTATUS_DISCONNECTED", FMAXDO_SCTN41DICTKEYDEF, "DEVICESTATUS_DISCONNECTED", "status disconnected",),
	("DOVAL_DEVICESTATUS_ERROR", FMAXDO_SCTN41DICTKEYDEF, "DEVICESTATUS_ERROR", "status error condition",),
	("DOVAL_DEVICETYPE", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE", "JOYSTICK MOUSE KEYBOARD SAITEK GAMEPAD GPM KNOB",),
	("DOVAL_DEVICETYPE", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE", "JOYSTICK MOUSE KEYBOARD SAITEK GAMEPAD GPM KNOB",),
	("DOVAL_DEVICETYPE_GAMEPAD", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE_GAMEPAD", "define a device type GAMEPAD",),
	("DOVAL_DEVICETYPE_GPM", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE_GPM", "define a device type GPM",),
	("DOVAL_DEVICETYPE_JOYSTICK", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE_JOYSTICK", "define a device type JOYSTICK",),
	("DOVAL_DEVICETYPE_KNOB", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE_KNOB", "device type KNOB",),
	("DOVAL_DEVICETYPE_MOUSE", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE_MOUSE", "define a device type MOUSE",),
	("DOVAL_DEVICETYPE_SAITEK", FMAXDO_SCTN41DICTKEYDEF, "DEVICETYPE_SAITEK", "device type SAITEK defined",),
	("DOVAL_DEV_ABSHAT_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_ABSHAT_STATUS", "status of ABS items on the device",),
	("DOVAL_DEV_ABSLTSTK_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_ABSLTSTK_STATUS", "status of ABS items on the device",),
	("DOVAL_DEV_ABSRTSTK_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_ABSRTSTK_STATUS", "status of ABS items on the device",),
	("DOVAL_DEV_BTN_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_BTN_STATUS", "device holdable buttons status",),
	("DOVAL_DEV_DEVICETYPE", FMAXDO_SCTN41DICTKEYDEF, "DEV_DEVICETYPE", "device type FLAG True to process thids device",),
	("DOVAL_DEV_ENABLED", FMAXDO_SCTN41DICTKEYDEF, "DEV_ENABLED", "device enabled FLAG True to process thids device",),
	("DOVAL_DEV_ERR_DELTA", FMAXDO_SCTN41DICTKEYDEF, "DEV_ERR_DELTA", "number of ticks (1/100) between error checks",),
	("DOVAL_DEV_ERR_NEXTTIME", FMAXDO_SCTN41DICTKEYDEF, "DEV_ERR_NEXTTIME", "next error time for this device if erroring",),
	("DOVAL_DEV_FD", FMAXDO_SCTN41DICTKEYDEF, "DEV_FD", "FD (file descriptor) of the device",),
	("DOVAL_DEV_GRAB", FMAXDO_SCTN41DICTKEYDEF, "DEV_GRAB", "GRAB shal the device be grabbed exclusively or not",),
	("DOVAL_DEV_MYNAME", FMAXDO_SCTN41DICTKEYDEF, "DEV_MYNAME", "device normal name_",),
	("DOVAL_DEV_NAME", FMAXDO_SCTN41DICTKEYDEF, "DEV_NAME", "NAME of device returned by uvdev/evdev/etc",),
	("DOVAL_DEV_QUEUE", FMAXDO_SCTN41DICTKEYDEF, "DEV_QUEUE", "QUEUE holding EVENT as they come in to the device handler",),
	("DOVAL_DEV_RELMSE_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_RELMSE_STATUS", "ABS status flags key",),
	("DOVAL_DEV_RELMWH_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_RELMW_STATUS", "ABS status flags key",),
	("DOVAL_DEV_RPT_NEXTTIME", FMAXDO_SCTN41DICTKEYDEF, "DEV_RPT_NEXTTIME", "next TIME device will repeat",),
	("DOVAL_DEV_RPT_NEXTTIMEDELTA", FMAXDO_SCTN41DICTKEYDEF, "DEV_RPT_NEXTTIMEDELTA", "now many TICK between repeats",),
	("DOVAL_DEV_SPENT", FMAXDO_SCTN41DICTKEYDEF, "DEV_SPENT", "queue is spent",),
	("DOVAL_DEV_STATUS", FMAXDO_SCTN41DICTKEYDEF, "DEV_STATUS", "device status",),
	("DOVAL_DIRDNLT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRDNLT_AND", "X_: DIRDNLT_VAL & X_", "FLAG DIR DNLT and lambda",),
	("DOVAL_DIRDNLT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRDNLT_MSK_AND", "X_: DIRDNLT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRDNLT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRDNLT_MSK_OR", "X_: DIRDNLT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRDNLT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRDNLT_MSK_VAL", "0B0011", "MASK DIR DOWN LEFT",),
	("DOVAL_DIRDNLT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRDNLT_OR", "X_: DIRDNLT_VAL | X_", "FLAG DIR DNLT or lambda",),
	("DOVAL_DIRDNLT_VAL", FMAXDO_SCTN41VALDEF, "DIRDNLT_VAL", "0B1100", "FLAG DIR DOWN LEFT",),
	("DOVAL_DIRDNRTUP_VAL", FMAXDO_SCTN41VALDEF, "DIRDNRTUP_VAL", "0B0111", "FLAG DIRDNRTUP",),
	("DOVAL_DIRDNRT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRDNRT_AND", "X_: DIRDNRT_VAL & X_", "FLAG DIR DNRT and lambda",),
	("DOVAL_DIRDNRT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRDNRT_MSK_AND", "X_: DIRDNRT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRDNRT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRDNRT_MSK_OR", "X_: DIRDNRT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRDNRT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRDNRT_MSK_VAL", "0B1001", "MASK DIR DOWN RIGHT",),
	("DOVAL_DIRDNRT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRDNRT_OR", "X_: DIRDNRT_VAL | X_", "FLAG DIR DNRT or lambda",),
	("DOVAL_DIRDNRT_VAL", FMAXDO_SCTN41VALDEF, "DIRDNRT_VAL", "0B0110", "FLAG DIR DOWN RIGHT",),
	("DOVAL_DIRDNUP_VAL", FMAXDO_SCTN41VALDEF, "DIRDNUP_VAL", "0B0101", "FLAG DIRDNUP ",),
	("DOVAL_DIRDN_AND", FMAXDO_SCTN41LAMBDADEF, "DIRDN_AND", "X_: DIRDN_VAL & X_", "FLAG DIR DN and lambda",),
	("DOVAL_DIRDN_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRDN_MSK_AND", "X_: DIRDN_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRDN_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRDN_MSK_OR", "X_: DIRDN_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRDN_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRDN_MSK_VAL", "0B1011", "MASK DIR DOWN",),
	("DOVAL_DIRDN_OR", FMAXDO_SCTN41LAMBDADEF, "DIRDN_OR", "X_: DIRDN_VAL | X_", "FLAG DIR DN or lambda",),
	("DOVAL_DIRDN_VAL", FMAXDO_SCTN41VALDEF, "DIRDN_VAL", "0B0100", "FLAG DIR DN val",),
	("DOVAL_DIRLTDNRTUP_VAL", FMAXDO_SCTN41VALDEF, "DIRLTDNRTUP_VAL", "0B1111", "LTDNRTUP direction VAL",),
	("DOVAL_DIRLTDNRT_VAL", FMAXDO_SCTN41VALDEF, "DIRLTDNRT_VAL", "0B1110", "FLAG DIRLTDNRT",),
	("DOVAL_DIRLTDNUP_VAL", FMAXDO_SCTN41VALDEF, "DIRLTDNUP_VAL", "0B1101", "FLAG DIRLTDNUP",),
	("DOVAL_DIRLTRTUP_VAL", FMAXDO_SCTN41VALDEF, "DIRLTRTUP_VAL", "0B1011", "FLAG DIRLTRT",),
	("DOVAL_DIRLTRT_VAL", FMAXDO_SCTN41VALDEF, "DIRLTRT_VAL", "0B1010", "FLAG DIRLTRT",),
	("DOVAL_DIRLT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRLT_AND", "X_: DIRLT_VAL & X_", "FLAG DIR LT and lambda",),
	("DOVAL_DIRLT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRLT_MSK_AND", "X_: DIRLT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRLT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRLT_MSK_OR", "X_: DIRLT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRLT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRLT_MSK_VAL", "0B0111", "MASK DIR LEFT",),
	("DOVAL_DIRLT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRLT_OR", "X_: DIRLT_VAL | X_", "FLAG DIR LT or lambda",),
	("DOVAL_DIRLT_VAL", FMAXDO_SCTN41VALDEF, "DIRLT_VAL", "0B1000", "FLAG DIR LEFT",),
	("DOVAL_DIRNOT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRNOT_AND", "X_: DIRNOT_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRNOT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRNOT_MSK_AND", "X_: DIRNOT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRNOT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRNOT_MSK_OR", "X_: DIRNOT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRNOT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRNOT_MSK_VAL", "0B1111", "MASK no DIR active",),
	("DOVAL_DIRNOT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRNOT_OR", "X_: DIRNOT_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRNOT_VAL", FMAXDO_SCTN41VALDEF, "DIRNOT_VAL", "0B0000", "FLAG no DIR active",),
	("DOVAL_DIRRT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRRT_AND", "X_: DIRRT_VAL & X_", "FLAG DIR RT and lambda",),
	("DOVAL_DIRRT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRRT_MSK_AND", "X_: DIRRT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRRT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRRT_MSK_OR", "X_: DIRRT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRRT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRRT_MSK_VAL", "0B1101", "MASK DIR RIGHT",),
	("DOVAL_DIRRT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRRT_OR", "X_: DIRRT_VAL | X_", "FLAG DIR RT or lambda",),
	("DOVAL_DIRRT_VAL", FMAXDO_SCTN41VALDEF, "DIRRT_VAL", "0B0010", "FLAG DIR RIGHT",),
	("DOVAL_DIRUPLT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRUPLT_AND", "X_: DIRUPLT_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRUPLT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRUPLT_MSK_AND", "X_: DIRUPLT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRUPLT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRUPLT_MSK_OR", "X_: DIRUPLT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRUPLT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRUPLT_MSK_VAL", "0B0110", "MASK DIR UP LEFT",),
	("DOVAL_DIRUPLT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRUPLT_OR", "X_: DIRUPLT_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRUPLT_VAL", FMAXDO_SCTN41VALDEF, "DIRUPLT_VAL", "0B1001", "FLAG DIR UP LEFT",),
	("DOVAL_DIRUPRT", FMAXDO_SCTN41VALDEF, "DIRUPRT", "0B0011", "FLAG DIR UP RIGHT",),
	("DOVAL_DIRUPRT_AND", FMAXDO_SCTN41LAMBDADEF, "DIRUPRT_AND", "X_: DIRUPRT_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRUPRT_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRUPRT_MSK_AND", "X_: DIRUPRT_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRUPRT_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRUPRT_MSK_OR", "X_: DIRUPRT_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRUPRT_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRUPRT_MSK_VAL", "0B1100", "MASK DIR UP RIGHT",),
	("DOVAL_DIRUPRT_OR", FMAXDO_SCTN41LAMBDADEF, "DIRUPRT_OR", "X_: DIRUPRT_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRUPRT_VAL", FMAXDO_SCTN41VALDEF, "DIRUPRT_VAL", "0B0011", "UPRT direction VAL",),
	("DOVAL_DIRUP_AND", FMAXDO_SCTN41LAMBDADEF, "DIRUP_AND", "X_: DIRUP_VAL & X_", "FLAG DIR UP and lambda",),
	("DOVAL_DIRUP_MSK_AND", FMAXDO_SCTN41LAMBDADEF, "DIRUP_MSK_AND", "X_: DIRUP_MSK_VAL & X_", "FLAG DIR DOWN and lambda",),
	("DOVAL_DIRUP_MSK_OR", FMAXDO_SCTN41LAMBDADEF, "DIRUP_MSK_OR", "X_: DIRUP_MSK_VAL | X_", "FLAG DIR DOWN or lambda",),
	("DOVAL_DIRUP_MSK_VAL", FMAXDO_SCTN41VALDEF, "DIRUP_MSK_VAL", "0B1110", "MASK DIR UP",),
	("DOVAL_DIRUP_OR", FMAXDO_SCTN41LAMBDADEF, "DIRUP_OR", "X_: DIRUP_VAL | X_", "FLAG DIR UP or lambda",),
	("DOVAL_DIRUP_VAL", FMAXDO_SCTN41VALDEF, "DIRUP_VAL", "0B0001", "FLAG DIR UP",),
	("DOVAL_DIRX_AND", FMAXDO_SCTN41LAMBDADEF, "DIRX_AND", "X_: DIRX_VAL & X_", "FLAG DIR LTRT and lambda",),
	("DOVAL_DIRX_OR", FMAXDO_SCTN41LAMBDADEF, "DIRX_OR", "X_: DIRX_VAL | X_", "FLAG DIR LTRT or lambda",),
	("DOVAL_DIRX_VAL", FMAXDO_SCTN41VALDEF, "DIRX_VAL", "0B1010", "LTRT directions",),
	("DOVAL_DIRY_AND", FMAXDO_SCTN41LAMBDADEF, "DIRY_AND", "X_: DIRY_VAL & X_", "FLAG DIR UPDN and lambda",),
	("DOVAL_DIRY_OR", FMAXDO_SCTN41LAMBDADEF, "DIRY_OR", "X_: DIRY_VAL | X_", "FLAG DIR UPDN or lambda",),
	("DOVAL_DIRY_VAL", FMAXDO_SCTN41VALDEF, "DIRY_VAL", "0B0101", "UP/DN directions",),
	("DOVAL_DORPT_CRSR", FMAXDO_SCTN41VALDEF, "DORPT_CRSR", "50", "cursor repeat",),
	("DOVAL_DORPT_MSE", FMAXDO_SCTN41VALDEF, "DORPT_MSE", "5", "mouse repeat",),
	("DOVAL_DORPT_NOT", FMAXDO_SCTN41VALDEF, "DORPT_NOT", "0", "no repeat",),
	("DOVAL_DORPT_PAUSE", FMAXDO_SCTN41VALDEF, "DORPT_PAUSE", "50", "pause before repeating",),
	("DOVAL_DORPT_WHL", FMAXDO_SCTN41VALDEF, "DORPT_WHL", "10", "mouse  wheelrepeat",),
	("DOVAL_ERRORNOT", FMAXDO_SCTN41VALDEF, "ERRORNOT", "0X00000000", "FLAG NOTHING is ERROR",),
	("DOVAL_ERRORTDELTA", FMAXDO_SCTN41VALDEF, "ERRORTDELTA", "300", "FLAG NOTHING is ERROR",),
	("DOVAL_HATMAX", FMAXDO_SCTN41VALDEF, "HATMAX", "1", "HAT MAX",),
	("DOVAL_HATMID", FMAXDO_SCTN41VALDEF, "HATMID", "0", "HAT MID/REST",),
	("DOVAL_HATMIN", FMAXDO_SCTN41VALDEF, "HATMIN", "-1", "HAT MIN",),
	("DOVAL_JOYSTICKDEAD", FMAXDO_SCTN41VALDEF, "JOYSTICKDEAD", "100", "DEAD zone on a lo rez ABS device",),
	("DOVAL_JOYSTICKMAX", FMAXDO_SCTN41VALDEF, "JOYSTICKMAX", "255", "MAX on lo rez ABS device",),
	("DOVAL_JOYSTICKMID", FMAXDO_SCTN41VALDEF, "JOYSTICKMID", "128", "MID on lo rez ABS device",),
	("DOVAL_JOYSTICKMIN", FMAXDO_SCTN41VALDEF, "JOYSTICKMIN", "0", "MIN on lo rez ABS device",),
	("DOVAL_KEYHLD", FMAXDO_SCTN41VALDEF, "KEYHLD", "0X02", "KEY held",),
	("DOVAL_KEYPRS", FMAXDO_SCTN41VALDEF, "KEYPRS", "0X01", "KEY pressed",),
	("DOVAL_KEYPRSHLD", FMAXDO_SCTN41VALDEF, "KEYPRSHLD", "0X03", "KEY pressed held",),
	("DOVAL_KEYRLS", FMAXDO_SCTN41VALDEF, "KEYRLS", "0X00", "KEY released",),
	("DOVAL_LOGITECH", FMAXDO_SCTN41DICTKEYDEF, "LOGITECH", "device Logitech trackman marble",),
	("DOVAL_MIMD", FMAXDO_SCTN41DICTKEYDEF, "MIMD", "device for MIMD gamepads",),
	("DOVAL_MOUSEDISTANCE", FMAXDO_SCTN41VALDEF, "MOUSEDISTANCE", "3", "how far to move the mouse per event",),
	("DOVAL_OBJMODE_CLASS", FMAXDO_SCTN41DICTKEYDEF, "OBJMODE_CLASS", "dict key for class internal []{}",),
	("DOVAL_OBJMODE_STANDALONE", FMAXDO_SCTN41DICTKEYDEF, "OBJMODE_STANDALONE", "dict key for standalone []{}",),
	("DOVAL_OBJMODE_STANDALONECLASS", FMAXDO_SCTN41DICTKEYDEF, "OBJMODE_STANDALONECLASS", "dict key for a class []{}",),
	("DOVAL_OBJMODE_TAB1", FMAXDO_SCTN41DICTKEYDEF, "OBJMODE_TAB1", "dict key for a []{} with a tab before name_, 2 before entries",),
	("DOVAL_OBJMODE_TAB2", FMAXDO_SCTN41DICTKEYDEF, "OBJMODE_TAB2", "2 tabs before name_, 3 before entries",),
	("DOVAL_SAITEK", FMAXDO_SCTN41DICTKEYDEF, "SAITEK", "device Saitek controller",),
	("DOVAL_SPCL_PAUSE", FMAXDO_SCTN41DICTKEYDEF, "SPCL_PAUSE", "special action pause",),
	("DOVAL_SPCL_PAUSE30F", FMAXDO_SCTN42LDIESPCLDEF, "SPCL_PAUSE", "30", "pause 3/10 seconds",),
	("DOVAL_SPCL_PAUSE3S", FMAXDO_SCTN42LDIESPCLDEF, "SPCL_PAUSE", "300", "pause 3 seconds",),
	("DOVAL_SPCL_PAUSE50F", FMAXDO_SCTN42LDIESPCLDEF, "SPCL_PAUSE", "50", "pause 1/2 seconds",),
	("DOVAL_WHEELDISTANCE", FMAXDO_SCTN41VALDEF, "WHEELDISTANCE", "1", "how many clicks of the wheel per event",),
	("D_DEFT", FMAXDO_SCTN41DEVICEDEF, "DEFT", "define the DEFT trackball",),
	("D_DEFT_ABSHAT_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_ABSHAT_STATUS", "DIRNOT_VAL", "no ABS to status check",),
	("D_DEFT_ABSLTSTK_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_ABSLTSTK_STATUS", "DIRNOT_VAL", "no ABS to status check",),
	("D_DEFT_ABSRTSTK_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_ABSRTSTK_STATUS", "DIRNOT_VAL", "no ABS to status check",),
	("D_DEFT_BTNSTATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_BTN_STATUS", "BTNS_NOT", "no buttons held",),
	("D_DEFT_DEVICETYPE", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_DEVICETYPE", "DEVICETYPE_MOUSE", "DEFT device type flag",),
	("D_DEFT_ENABLED", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_ENABLED", "False", "DEFT enabled flag",),
	("D_DEFT_ERR_DELTA", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_ERR_DELTA", "300 * 60 * 100", "5 minutes between error checks",),
	("D_DEFT_ERR_NEXTTIME", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_ERR_NEXTTIME", "0", "DEFT next time to check error status",),
	("D_DEFT_FD", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_FD", "None", "file descriptor for DEFT",),
	("D_DEFT_GRAB", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_GRAB", "True", "grab the device",),
	("D_DEFT_NAME", FMAXDO_SCTN44DEVICEENTRYSTRADD, "DEFT", "DEV_NAME", "ELECOM ELECOM TrackBall Mouse", "DEFT name",),
	("D_DEFT_QUEUE", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_QUEUE", "[]", "DEFT queue",),
	("D_DEFT_RELMSE_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_RELMSE_STATUS", "DIRNOT_VAL", "DEFT REL status",),
	("D_DEFT_RELMW_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_RELMW_STATUS", "DIRNOT_VAL", "DEFT REL status",),
	("D_DEFT_RPT_NEXTTIME", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_RPT_NEXTTIME", "0", "DEFT next time to repeat",),
	("D_DEFT_RPT_NEXTTIMEDELTA", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_RPT_NEXTTIMEDELTA", "DORPT_NOT", "DEFT time between repeats",),
	("D_DEFT_SPENT", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_SPENT", "False", "DEFT queue has been sent/spent",),
	("D_DEFT_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "DEFT", "DEV_STATUS", "DEVICESTATUS_DISCONNECTED", "DEFT status",),
	("D_DEFT___BTNM01LT", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_LEFT", "BTNM_01LT", "DEFT:LT=BTNM_01LT",),
	("D_DEFT___BTNM02MD", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_MIDDLE", "BTNM_02MD", "DEFT:LT=BTNM_02MD",),
	("D_DEFT___BTNM03RT", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_RIGHT", "BTNM_03RT", "DEFT:LT=BTNM_03RT",),
	("D_DEFT___BTNM08", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_EXTRA", "BTNM_08", "DEFT:LT=BTNM_08",),
	("D_DEFT___BTNM09", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_SIDE", "BTNM_09", "DEFT:LT=BTNM_09",),
	("D_DEFT___BTNM10", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_FORWARD", "BTNM_10", "DEFT:LT=BTNM_10",),
	("D_DEFT___BTNM11", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_BACK", "BTNM_11", "DEFT:LT=BTNM_11",),
	("D_DEFT___BTNM12", FMAXDO_SCTN46XLATEADD, "DEFT", "LD.EV_KEY.BTN_TASK", "BTNM_12", "DEFT:RT=BTNM_12",),
	("D_MIMD", FMAXDO_SCTN41DEVICEDEF, "MIMD", "define MIMD gamepad",),
	("D_MIMD_ABSHAT_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_ABSHAT_STATUS", "DIRNOT_VAL", "no ABS to status check",),
	("D_MIMD_ABSLTSTK_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_ABSLTSTK_STATUS", "DIRNOT_VAL", "no ABS to status check",),
	("D_MIMD_ABSRTSTK_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_ABSRTSTK_STATUS", "DIRNOT_VAL", "no ABS to status check",),
	("D_MIMD_BTN_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_BTN_STATUS", "BTNS_NOT", "no buttons held",),
	("D_MIMD_DEVICETYPE", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_DEVICETYPE", "DEVICETYPE_GAMEPAD", "MIMD device type flag",),
	("D_MIMD_ENABLED", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_ENABLED", "True", "MIMD enabled flag",),
	("D_MIMD_ERR_DELTA", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_ERR_DELTA", "30000", "300 seconds delta for error checking",),
	("D_MIMD_ERR_NEXTTIME", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_ERR_NEXTTIME", "0", "MIMD next time to check error status",),
	("D_MIMD_FD", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_FD", "None", "MIMD file descriptor",),
	("D_MIMD_GRAB", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_GRAB", "True", "grab the MIMD",),
	("D_MIMD_NAME", FMAXDO_SCTN44DEVICEENTRYSTRADD, "MIMD", "DEV_NAME", "ShanWan     GAME:PAD S PRO-BLUETOOTH-V6.20", "MIMD name",),
	("D_MIMD_QUEUE", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_QUEUE", "[]", "MIMD queue",),
	("D_MIMD_RELMSE_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_RELMSE_STATUS", "DIRNOT_VAL", "MIMD REL status",),
	("D_MIMD_RPT_NEXTTIME", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_RPT_NEXTTIME", "0", "MIMD next time to repeat",),
	("D_MIMD_RPT_NEXTTIMEDELTA", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_RPT_NEXTTIMEDELTA", "DORPT_NOT", "MIMD time between repeats",),
	("D_MIMD_SPENT", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_SPENT", "False", "MIMD queue has been sent/spent",),
	("D_MIMD_STATUS", FMAXDO_SCTN44DEVICEENTRYVALADD, "MIMD", "DEV_STATUS", "DEVICESTATUS_DISCONNECTED", "MIMD status",),
	("D_MIMD__BTNGHAT_DN", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_DN", "AX_CRSRDN", "artificial button hat down DOWN",),
	("D_MIMD__BTNGHAT_DNLT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_DNLT", "AX_CRSRDNLT", "artificial button hat down DOWN",),
	("D_MIMD__BTNGHAT_DNRT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_DNRT", "AX_CRSRDNRT", "artificial button hat down DOWN",),
	("D_MIMD__BTNGHAT_LT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_LT", "AX_CRSRLT", "artificial button hat left LEFT",),
	("D_MIMD__BTNGHAT_RT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_RT", "AX_CRSRRT", "artificial button hat right RIGHT",),
	("D_MIMD__BTNGHAT_UP", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_UP", "AX_CRSRUP", "artificial button hat up UP",),
	("D_MIMD__BTNGHAT_UPLT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_UPLT", "AX_CRSRUPLT", "artificial button hat up UP",),
	("D_MIMD__BTNGHAT_UPRT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNGHAT_UPRT", "AX_CRSRUPRT", "artificial button hat up UP",),
	("D_MIMD__BTNGLTSTK_DN", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_DN", "AXMSEDN", "artificial button left stick down MSE_DN",),
	("D_MIMD__BTNGLTSTK_DNLT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_DNLT", "AXMSEDNLT", "artificial button left stick down MSE_DN",),
	("D_MIMD__BTNGLTSTK_DNRT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_DNRT", "AXMSEDNRT", "artificial button left stick down MSE_DN",),
	("D_MIMD__BTNGLTSTK_LT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_LT", "AXMSELT", "artificial button left stick left MSE_LT",),
	("D_MIMD__BTNGLTSTK_RT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_RT", "AXMSERT", "artificial button left stick right MSE_RT",),
	("D_MIMD__BTNGLTSTK_UP", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_UP", "AXMSEUP", "left stick up MSE_UP",),
	("D_MIMD__BTNGLTSTK_UPLT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_UPLT", "AXMSEUPLT", "left stick up MSE_UP",),
	("D_MIMD__BTNGLTSTK_UPRT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_MSE", "BTNGLTSTK_UPRT", "AXMSEUPRT", "left stick up MSE_UP",),
	("D_MIMD__BTNGRTSTK_DN", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_DN", "AXMSEWHLDN", "right stick down MSEWHL_DN",),
	("D_MIMD__BTNGRTSTK_DNLT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_DNLT", "AXMSEWHLDNLT", "right stick down MSEWHL_DN",),
	("D_MIMD__BTNGRTSTK_DNRT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_DNRT", "AXMSEWHLDNRT", "right stick down MSEWHL_DN",),
	("D_MIMD__BTNGRTSTK_LT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_LT", "AXMSEWHLLT", "right stick left MSEWHL_LT",),
	("D_MIMD__BTNGRTSTK_RT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_RT", "AXMSEWHLRT", "right stick right MSEWHL_RT",),
	("D_MIMD__BTNGRTSTK_UP", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_UP", "AXMSEWHLUP", "right stick up MSEWHL_UP",),
	("D_MIMD__BTNGRTSTK_UPLT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_UPLT", "AXMSEWHLUPLT", "right stick up MSEWHL_UP",),
	("D_MIMD__BTNGRTSTK_UPRT", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_WHL", "BTNGRTSTK_UPRT", "AXMSEWHLUPRT", "right stick up MSEWHL_UP",),
	("D_MIMD__BTNG_01", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_01", "AXXNVFLIPH", "XnViewer flip horizontal",),
	("D_MIMD__BTNG_02", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_02", "AX_ESC", "ESC key",),
	("D_MIMD__BTNG_03", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_03", "AXMSEBTNMID", "press middle mouse button",),
	("D_MIMD__BTNG_04", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_04", "AX_CTRLS", "save/CTRL-S",),
	("D_MIMD__BTNG_0501", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_05", "BTNG_01", "AX_CTRLA", "select all CTRL-A",),
	("D_MIMD__BTNG_0503", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_05", "BTNG_03", "AXXNVCROP", "XnViewer CROP",),
	("D_MIMD__BTNG_050601", FMAXDO_SCTN45HOLDABLEADD2, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_05", "BTNG_06", "BTNG_01", "AX_CTRLQ", "quit CTRL-Q",),
	("D_MIMD__BTNG_0513", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_05", "BTNG_13", "AXXNVSEL2TOP", "select to top SHIFT-HOME SHIFT-RT",),
	("D_MIMD__BTNG_05HATDN", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_DN", "AX_SHIFTDN", "SHIFT-DN",),
	("D_MIMD__BTNG_05HATDNLT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_DNLT", "AX_SHIFTDNLT", "SHIFT-DNLT",),
	("D_MIMD__BTNG_05HATDNRT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_DNRT", "AX_SHIFTDNRT", "SHIFT-DNRT",),
	("D_MIMD__BTNG_05HATLT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_LT", "AX_SHIFTLT", "SHIFT-LT",),
	("D_MIMD__BTNG_05HATRT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_RT", "AX_SHIFTRT", "SHIFT-RT",),
	("D_MIMD__BTNG_05HATUP", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_UP", "AX_SHIFTUP", "SHIFT-UP",),
	("D_MIMD__BTNG_05HATUPLT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_UPLT", "AX_SHIFTUPLT", "SHIFT-UPLT",),
	("D_MIMD__BTNG_05HATUPRT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_CRSR", "BTNG_05", "BTNGHAT_UPRT", "AX_SHIFTUPRT", "SHIFT-UPRT",),
	("D_MIMD__BTNG_0601", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNG_01", "AX_Q", "QUIT Q in many programs",),
	("D_MIMD__BTNG_0602", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNG_02", "AX_CTRLQ", "QUIT CTRL-Q in many programs",),
	("D_MIMD__BTNG_0603", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNG_03", "AX_ALTD", "ALT-D dismiss in some programs",),
	("D_MIMD__BTNG_0604", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNG_04", "AXGIMPOVWRT", "gimp overwrite ALT-CTRL-SHIFT-O",),
	("D_MIMD__BTNG_06HATDN", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNGHAT_DN", "AX_PGDN", "PGDN",),
	("D_MIMD__BTNG_06HATLT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNGHAT_LT", "AX_HOME", "HOME",),
	("D_MIMD__BTNG_06HATRT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNGHAT_RT", "AX_END", "END",),
	("D_MIMD__BTNG_06HATUP", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_06", "BTNGHAT_UP", "AX_PGUP", "PGUP",),
	("D_MIMD__BTNG_0701", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNG_01", "AXDSKTP1", "desktop 1 ALT-1",),
	("D_MIMD__BTNG_0702", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNG_02", "AXDSKTP2", "desktop 2 ALT-2",),
	("D_MIMD__BTNG_0703", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNG_03", "AXDSKTP3", "desktop 3 ALT-3",),
	("D_MIMD__BTNG_0704", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNG_04", "AXDSKTP4", "desktop 4 ALT-4",),
	("D_MIMD__BTNG_0713", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNG_13", "AX_DEL", "DEL on BTNG_07-BTNG_13",),
	("D_MIMD__BTNG_07HATDN", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNGHAT_DN", "AXXNVZOOMIN", "XnViewer zoom to out/-",),
	("D_MIMD__BTNG_07HATLT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNGHAT_LT", "AXXNVZOOMRESET", "XnViewer zoom to default",),
	("D_MIMD__BTNG_07HATRT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNGHAT_RT", "AXXNVZOOMFULL", "XnViewer zoom to 1:1",),
	("D_MIMD__BTNG_07HATUP", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_07", "BTNGHAT_UP", "AXXNVZOOMOUT", "XnViewer zoom to out/-",),
	("D_MIMD__BTNG_0813", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_08", "BTNG_13", "AX_DEL", "DEL on BTNG_08-BTNG_13",),
	("D_MIMD__BTNG_08HATDN", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_08", "BTNGHAT_DN", "AX_CTRLPGDN", "PGDN",),
	("D_MIMD__BTNG_08HATLT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_08", "BTNGHAT_LT", "AX_ALTTAB", "ALTTAB",),
	("D_MIMD__BTNG_08HATRT", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_08", "BTNGHAT_RT", "AX_CTRLTAB", "CTRLTAB",),
	("D_MIMD__BTNG_08HATUP", FMAXDO_SCTN45HOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_08", "BTNGHAT_UP", "AX_CTRLPGUP", "PGUP",),
	("D_MIMD__BTNG_09", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_09", "AX_ENTER", "ENTER on BTNG_09",),
	("D_MIMD__BTNG_10", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_10", "AXXNVMOVE", "XnViewer move",),
	("D_MIMD__BTNG_11LTSTK", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_11LTSTK", "AXMSEBTNLT", "left mouse button on same stick click",),
	("D_MIMD__BTNG_12RTSTK", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_12RTSTK", "AXMSEBTNRT", "right mouse button on same stick click",),
	("D_MIMD__BTNG_13", FMAXDO_SCTN45NOTHOLDABLEADD1, "MIMD", "BTNTYPE_NORMAL", "DORPT_NOT", "BTNG_13", "AX_ENTER", "ENTER on HOME/BTNG_13",),
	("D_MIMD___BTNG_01", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_SOUTH", "BTNG_01", "MIMD:01=BTN_SOUTH",),
	("D_MIMD___BTNG_02", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_EAST", "BTNG_02", "MIMD:02=BTN_EAST",),
	("D_MIMD___BTNG_03", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_C", "BTNG_03", "MIMD:03=BTN_C",),
	("D_MIMD___BTNG_04", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_NORTH", "BTNG_04", "MIMD:04=BTN_NORTH",),
	("D_MIMD___BTNG_05", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_WEST", "BTNG_05", "MIMD:05=BTN_WEST",),
	("D_MIMD___BTNG_06", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_Z", "BTNG_06", "MIMD:06=BTN_Z",),
	("D_MIMD___BTNG_07", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_TL", "BTNG_07", "MIMD:07=BTN_TL",),
	("D_MIMD___BTNG_08", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_TR", "BTNG_08", "MIMD:08=BTN_TR",),
	("D_MIMD___BTNG_09", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_TL2", "BTNG_09", "MIMD:09=BTN_TL2",),
	("D_MIMD___BTNG_10", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_TR2", "BTNG_10", "MIMD:10=BTN_TR2",),
	("D_MIMD___BTNG_11LTSTK", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_SELECT", "BTNG_11LTSTK", "MIMD:11=BTN_SELECT",),
	("D_MIMD___BTNG_12RTSTK", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_START", "BTNG_12RTSTK", "MIMD:12=BTN_START",),
	("D_MIMD___BTNG_13", FMAXDO_SCTN46XLATEADD, "MIMD", "LD.EV_KEY.BTN_MODE", "BTNG_13", "MIMD:13=BTN_MODE",),
	("D__HATS", FMAXDO_SCTN49DIRTRANSDEVDEF, "HATS", "table to convert between directions and buttons",),
	("D__HATS00", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRNOT_VAL", "BTNGHAT_RLS", "release hat sim buttons",),
	("D__HATS01", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRUP_VAL", "BTNGHAT_UP", "table to convert between directions and buttons",),
	("D__HATS02", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRRT_VAL", "BTNGHAT_RT", "table to convert between directions and buttons",),
	("D__HATS03", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRUPRT_VAL", "BTNGHAT_UPRT", "table to convert between directions and buttons",),
	("D__HATS04", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRDN_VAL", "BTNGHAT_DN", "table to convert between directions and buttons",),
	("D__HATS05", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRDNUP_VAL", "BTNGHAT_RLS", "table to convert between directions and buttons",),
	("D__HATS06", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRDNRT_VAL", "BTNGHAT_DNRT", "table to convert between directions and buttons",),
	("D__HATS07", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRDNRTUP_VAL", "BTNGHAT_RLS", "table to convert between directions and buttons",),
	("D__HATS08", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRLT_VAL", "BTNGHAT_LT", "table to convert between directions and buttons",),
	("D__HATS09", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRUPLT_VAL", "BTNGHAT_UPLT", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__HATS0A", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRLTRT_VAL", "BTNGHAT_RLS", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__HATS0B", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRLTRTUP_VAL", "BTNGHAT_RLS", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__HATS0C", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRDNLT_VAL", "BTNGHAT_DNLT", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__HATS0D", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRLTDNUP_VAL", "BTNGHAT_RLS", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__HATS0E", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRLTDNRT_VAL", "BTNGHAT_RLS", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__HATS0F", FMAXDO_SCTN49DIRTRANSVALADD, "HATS", "DIRLTDNRTUP_VAL", "BTNGHAT_RLS", "convert DIRUPLT_VAL to BTNGHAT_UPLT",),
	("D__LTSTK", FMAXDO_SCTN49DIRTRANSDEVDEF, "LTSTK", "table to convert between directions and buttons",),
	("D__LTSTK00", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRNOT_VAL", "BTNGLTSTK_RLS", "release hat sim buttons",),
	("D__LTSTK01", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRUP_VAL", "BTNGLTSTK_UP", "table to convert between directions and buttons",),
	("D__LTSTK02", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRRT_VAL", "BTNGLTSTK_RT", "table to convert between directions and buttons",),
	("D__LTSTK03", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRUPRT_VAL", "BTNGLTSTK_UPRT", "table to convert between directions and buttons",),
	("D__LTSTK04", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRDN_VAL", "BTNGLTSTK_DN", "table to convert between directions and buttons",),
	("D__LTSTK05", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRDNUP_VAL", "BTNGLTSTK_RLS", "table to convert between directions and buttons",),
	("D__LTSTK06", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRDNRT_VAL", "BTNGLTSTK_DNRT", "table to convert between directions and buttons",),
	("D__LTSTK07", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRDNRTUP_VAL", "BTNGLTSTK_RLS", "table to convert between directions and buttons",),
	("D__LTSTK08", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRLT_VAL", "BTNGLTSTK_LT", "table to convert between directions and buttons",),
	("D__LTSTK09", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRUPLT_VAL", "BTNGLTSTK_UPLT", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__LTSTK0A", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRLTRT_VAL", "BTNGLTSTK_RLS", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__LTSTK0B", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRLTRTUP_VAL", "BTNGLTSTK_RLS", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__LTSTK0C", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRDNLT_VAL", "BTNGLTSTK_DNLT", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__LTSTK0D", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRLTDNUP_VAL", "BTNGLTSTK_RLS", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__LTSTK0E", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRLTDNRT_VAL", "BTNGLTSTK_RLS", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__LTSTK0F", FMAXDO_SCTN49DIRTRANSVALADD, "LTSTK", "DIRLTDNRTUP_VAL", "BTNGLTSTK_RLS", "convert DIRUPLT_VAL to BTNGLTSTK_UPLT",),
	("D__RTSTK", FMAXDO_SCTN49DIRTRANSDEVDEF, "RTSTK", "table to convert between directions and buttons",),
	("D__RTSTK00", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRNOT_VAL", "BTNGRTSTK_RLS", "release hat sim buttons",),
	("D__RTSTK01", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRUP_VAL", "BTNGRTSTK_UP", "table to convert between directions and buttons",),
	("D__RTSTK02", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRRT_VAL", "BTNGRTSTK_RT", "table to convert between directions and buttons",),
	("D__RTSTK03", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRUPRT_VAL", "BTNGRTSTK_UPRT", "table to convert between directions and buttons",),
	("D__RTSTK04", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRDN_VAL", "BTNGRTSTK_DN", "table to convert between directions and buttons",),
	("D__RTSTK05", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRDNUP_VAL", "BTNGRTSTK_RLS", "table to convert between directions and buttons",),
	("D__RTSTK06", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRDNRT_VAL", "BTNGRTSTK_DNRT", "table to convert between directions and buttons",),
	("D__RTSTK07", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRDNRTUP_VAL", "BTNGRTSTK_RLS", "table to convert between directions and buttons",),
	("D__RTSTK08", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRLT_VAL", "BTNGRTSTK_LT", "table to convert between directions and buttons",),
	("D__RTSTK09", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRUPLT_VAL", "BTNGRTSTK_UPLT", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("D__RTSTK0A", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRLTRT_VAL", "BTNGRTSTK_RLS", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("D__RTSTK0B", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRLTRTUP_VAL", "BTNGRTSTK_RLS", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("D__RTSTK0C", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRDNLT_VAL", "BTNGRTSTK_DNLT", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("D__RTSTK0D", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRLTDNUP_VAL", "BTNGRTSTK_RLS", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("D__RTSTK0E", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRLTDNRT_VAL", "BTNGRTSTK_RLS", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("D__RTSTK0F", FMAXDO_SCTN49DIRTRANSVALADD, "RTSTK", "DIRLTDNRTUP_VAL", "BTNGRTSTK_RLS", "convert DIRUPLT_VAL to BTNGRTSTK_UPLT",),
	("FMAXCF_SCTN03LAMBDADEF", FMAXFM_SCTN11AXDEF, "define a lambda function <NAC><NAME><lambda str>",),
	("FMAXCF_SCTN03TYPEDEF", FMAXFM_SCTN11AXDEF, "define a fake type used in the translation dict <NAC><NAME><TYPE>",),
	("FMAXCF_SCTN21STRDEF", FMAXFM_SCTN11AXDEF, "define a STR in SCTN21 <NAC><NAME><str>",),
	("FMAXCF_SCTN21VALDEF", FMAXFM_SCTN11AXDEF, "define a VAL in SCTN21 <NAC><NAME><VAL>",),
	("FMAXCF_SCTN22PARMDEF", FMAXFM_SCTN11AXDEF, "define a '-a[=]' in SCTN22 <NAC><PARM><VAL>",),
	("FMAXCF_SCTN22STRENTRYADD", FMAXFM_SCTN11AXDEF, "define a OPTNAME: 'str' in SCTN22 <NAC><KEY><STR>",),
	("FMAXCF_SCTN22VALENTRYADD", FMAXFM_SCTN11AXDEF, "define a OPTNAME: VAL in SCTN22 <NAC><KEY><VAL>",),
	("FMAXCF_SCTN23DICTDEF", FMAXFM_SCTN11AXDEF, "define a dict in SCTN23 <NAC><DICTNAME><DICTMODE>",),
	("FMAXCF_SCTN23DICTSTRADD", FMAXFM_SCTN11AXDEF, "define a dict STR in SCTN23 <NAC><DICTNAME><STR>",),
	("FMAXCF_SCTN23DICTVALADD", FMAXFM_SCTN11AXDEF, "define a dict VAL in SCTN23 <NAC><DICTNAME><VAL>",),
	("FMAXCF_SCTN24LISTDEF", FMAXFM_SCTN11AXDEF, "define a list in SCTN24 <NAC><LISTNAME>",),
	("FMAXCF_SCTN24LISTSTRADD", FMAXFM_SCTN11AXDEF, "define a list STR in SCTN24 <NAC><LISTNAME><STR>",),
	("FMAXCF_SCTN24LISTVALADD", FMAXFM_SCTN11AXDEF, "define a VAL in a list in SCTN24 <NAC><LISTNAME><VAL>",),
	("FMAXDO_SCTN41DEVICEDEF", FMAXFM_SCTN11AXDEF, "define a device in PROF <NAC><MYNAME><DEV_NAME>",),
	("FMAXDO_SCTN41DICTKEYDEF", FMAXFM_SCTN11AXDEF, "define a profile dict key <NAC><KEY>",),
	("FMAXDO_SCTN41LAMBDADEF", FMAXFM_SCTN11AXDEF, "define a profile lambda <NAC><NAME><LAMBDA>",),
	("FMAXDO_SCTN41STRDEF", FMAXFM_SCTN11AXDEF, "define a profile STR <NAC><NAME><VAL>",),
	("FMAXDO_SCTN41VALDEF", FMAXFM_SCTN11AXDEF, "define a profile value <NAC><NAME><VAL>",),
	("FMAXDO_SCTN42LDIEABSDEF", FMAXFM_SCTN11AXDEF, "define an IE entry (3) <NAC><IESTR><VAL>",),
	("FMAXDO_SCTN42LDIEBTNDEF", FMAXFM_SCTN11AXDEF, "define an IE entry (3) <NAC><IESTR><VAL>",),
	("FMAXDO_SCTN42LDIEKEYDEF", FMAXFM_SCTN11AXDEF, "define an IE entry (3) <NAC><IESTR><VAL>",),
	("FMAXDO_SCTN42LDIERELDEF", FMAXFM_SCTN11AXDEF, "define an IE entry (3) <NAC><IESTR><VAL>",),
	("FMAXDO_SCTN42LDIESPCLDEF", FMAXFM_SCTN11AXDEF, "define IE psuedo entry for special events",),
	("FMAXDO_SCTN42LDIESYNDEF", FMAXFM_SCTN11AXDEF, "define an IE entry (3) <NAC><IESTR><VAL>",),
	("FMAXDO_SCTN43AXDEF", FMAXFM_SCTN11AXDEF, "define a profile action <NAC>",),
	("FMAXDO_SCTN43AXVALADD", FMAXFM_SCTN11AXDEF, "add an item to an action <NAC><AX><VAL>",),
	("FMAXDO_SCTN44DEVICEENTRYSTRADD", FMAXFM_SCTN11AXDEF, "define an entry in a device <NAC><MYNAME><ENTRYKEY><STR>",),
	("FMAXDO_SCTN44DEVICEENTRYVALADD", FMAXFM_SCTN11AXDEF, "define an entry in a device <NAC><MYNAME><ENTRYKEY><VAL>",),
	("FMAXDO_SCTN45HOLDABLEADD1", FMAXFM_SCTN11AXDEF, "define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE><NOTHOLDABLE><Ax>",),
	("FMAXDO_SCTN45HOLDABLEADD2", FMAXFM_SCTN11AXDEF, "define holdable items in profile <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><HOLDABLE1><HOLDABLE2><NOTHOLDABLE><Ax>",),
	("FMAXDO_SCTN45NOTHOLDABLEADD1", FMAXFM_SCTN11AXDEF, "not holdable PROF items <NAC><DEV_MYNAME><BTNTYPE><REPEATRATE><NOTHOLDABLE><Ax>",),
	("FMAXDO_SCTN46XLATEADD", FMAXFM_SCTN11AXDEF, "add an item to an XLATE entry <NAC><DEV_MYNAME><DEVBTN><COMMONBTN>",),
	("FMAXDO_SCTN47BTNSDEF", FMAXFM_SCTN11AXDEF, "define buttons all around <NAC><BTNNAME><HOLDABLE>",),
	("FMAXDO_SCTN48EVTYPEDEF", FMAXFM_SCTN11AXDEF, "define a device type list type<NAC>",),
	("FMAXDO_SCTN48EVTYPELST", FMAXFM_SCTN11AXDEF, "add a device list entry<NAC>",),
	("FMAXDO_SCTN49DIRTRANSDEVDEF", FMAXFM_SCTN11AXDEF, "add a dict to DO.py <NAV><DEVNAME>",),
	("FMAXDO_SCTN49DIRTRANSSTRADD", FMAXFM_SCTN11AXDEF, "add a dict to DO.py <NAV><DEVNAME><KEY><VAL>",),
	("FMAXDO_SCTN49DIRTRANSVALADD", FMAXFM_SCTN11AXDEF, "add a dict to DO.py <NAV><DEVNAME><KEY><VAL>",),
	("FMAXFM_NOP", FMAXFM_SCTN11AXDEF, "skip this entry",),
	("FMAXFM_SCTN11AXDEF", FMAXFM_SCTN11AXDEF, "define a new FM action <NAC>",),
	("FMAXFM_SCTN12VALDEF", FMAXFM_SCTN11AXDEF, "define a CM value_ <NAC><NAME><VAL>",),
	("FMAXFM_SCTN13DICTDEF", FMAXFM_SCTN11AXDEF, "define a dict for FM <NAC>",),
	("FMAXFM_SCTN14LISTDEF", FMAXFM_SCTN11AXDEF, "define a list in FM <NAC>",),
	("FMAXFO_SCTN31DICTDEF", FMAXFM_SCTN11AXDEF, "define a dict in FO.py <NAC>",),
	("FMAXHBI_SCTN50ABSADD", FMAXFM_SCTN11AXDEF, "enable ABS entry for IDB",),
	("FMAXHBI_SCTN51BTNADD", FMAXFM_SCTN11AXDEF, "enable BTN entry for IDB",),
	("FMAXHBI_SCTN52KEYADD", FMAXFM_SCTN11AXDEF, "enable KEY entry for IDB",),
	("FMAXHBI_SCTN53RELADD", FMAXFM_SCTN11AXDEF, "enable REL entry for IDB",),
	("FMCF_SCTN03TYPECMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN09 types comments",),
	("FMCF_SCTN03TYPEDICT", FMAXFM_SCTN13DICTDEF, "SCTN03 types",),
	("FMCF_SCTN21DEFCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN21 defines comments dict",),
	("FMCF_SCTN21DEFDICT", FMAXFM_SCTN13DICTDEF, "SCTN21 defines dict",),
	("FMCF_SCTN22OPTIONSCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN22 options comments dict",),
	("FMCF_SCTN22OPTIONSDICT", FMAXFM_SCTN13DICTDEF, "SCTN22 options dict",),
	("FMCF_SCTN22PARMSCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN22 options comments dict",),
	("FMCF_SCTN22PARMSDICT", FMAXFM_SCTN13DICTDEF, "SCTN22 options dict",),
	("FMCF_SCTN23DICTCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN23 dict comments dict",),
	("FMCF_SCTN23DICTDICT", FMAXFM_SCTN13DICTDEF, "SCTN23 dict dict",),
	("FMCF_SCTN24LISTCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN24 list comments dict",),
	("FMCF_SCTN24LISTDICT", FMAXFM_SCTN13DICTDEF, "SCTN24 list dict",),
	("FMDO_SCTN41DEVICEDEFCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN21 device defines",),
	("FMDO_SCTN41DEVICEDEFDICT", FMAXFM_SCTN13DICTDEF, "SCTN21 device defines",),
	("FMDO_SCTN42LDIECMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN22 LDIE defined",),
	("FMDO_SCTN42LDIEDICT", FMAXFM_SCTN13DICTDEF, "SCTN22 LDIE defined",),
	("FMDO_SCTN42LDIESPCLLIST", FMAXFM_SCTN14LISTDEF, "SCTN22 LDIE defined",),
	("FMDO_SCTN43AXDEFCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN23 output actions AX comments",),
	("FMDO_SCTN43AXDEFDICT", FMAXFM_SCTN13DICTDEF, "SCTN23 output actions AX",),
	("FMDO_SCTN44DEVICESCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN24 device comments",),
	("FMDO_SCTN44DEVICESDICT", FMAXFM_SCTN13DICTDEF, "SCTN24 devices dict",),
	("FMDO_SCTN45BTNTYPEDICT", FMAXFM_SCTN13DICTDEF, "SCTN25 device BTNTYPE dict",),
	("FMDO_SCTN45PROFDICT", FMAXFM_SCTN13DICTDEF, "SCTN25 device profile dict",),
	("FMDO_SCTN45RPTDICT", FMAXFM_SCTN13DICTDEF, "SCTN25 device RPT dict",),
	("FMDO_SCTN46XLATECMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN26 XLATE dict",),
	("FMDO_SCTN46XLATEDICT", FMAXFM_SCTN13DICTDEF, "SCTN26 XLATE dict",),
	("FMDO_SCTN47BTNSCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN04 buttons",),
	("FMDO_SCTN47BTNSDICT", FMAXFM_SCTN13DICTDEF, "SCTN04 buttons",),
	("FMDO_SCTN47BTNSHOLDABLELIST", FMAXFM_SCTN14LISTDEF, "buttons holdable list",),
	("FMDO_SCTN48DEFCMNTDICT", FMAXFM_SCTN13DICTDEF, "define a device types list type",),
	("FMDO_SCTN48DEFDICT", FMAXFM_SCTN13DICTDEF, "define a device types list type",),
	("FMDO_SCTN48TYPESCMNTDICT", FMAXFM_SCTN13DICTDEF, "define a device types list type",),
	("FMDO_SCTN48TYPESDICT", FMAXFM_SCTN13DICTDEF, "define a device types list type",),
	("FMDO_SCTN49DIRTRANSCMNTDICT", FMAXFM_SCTN13DICTDEF, "holds dict for DO.py",),
	("FMDO_SCTN49DIRTRANSDICT", FMAXFM_SCTN13DICTDEF, "holds dict for DO.py",),
	("FMFM_SCTN11AXCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN03 types",),
	("FMFM_SCTN11AXCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN11 FMAX defined",),
	("FMFM_SCTN11AXDICT", FMAXFM_SCTN13DICTDEF, "SCTN11 FMAX defined",),
	("FMFM_SCTN12VALCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN12 val",),
	("FMFM_SCTN12VALDICT", FMAXFM_SCTN13DICTDEF, "SCTN12 val",),
	("FMFM_SCTN13DICTCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN13 dict defined",),
	("FMFM_SCTN13DICTDICT", FMAXFM_SCTN13DICTDEF, "SCTN13 dict defined",),
	("FMFM_SCTN14LISTCMNTDICT", FMAXFM_SCTN13DICTDEF, "SCTN21 device defines",),
	("FMFM_SCTN14LISTDICT", FMAXFM_SCTN13DICTDEF, "SCTN21 device defines",),
	("FMHBI_SCTN50HBIABSLIST", FMAXFM_SCTN14LISTDEF, "SCTN50 list",),
	("FMHBI_SCTN51HBIBTNLIST", FMAXFM_SCTN14LISTDEF, "SCTN51 list",),
	("FMHBI_SCTN52HBIKEYLIST", FMAXFM_SCTN14LISTDEF, "SCTN52 list",),
	("FMHBI_SCTN53HBIRELLIST", FMAXFM_SCTN14LISTDEF, "SCTN53 list",),
	("GBTNC_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_C", "KEYHLD", "comment",),
	("GBTNC_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_C", "KEYPRS", "comment",),
	("GBTNC_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_C", "KEYRLS", "comment",),
	("GBTNEAST_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EAST", "KEYHLD", "comment",),
	("GBTNEAST_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EAST", "KEYPRS", "comment",),
	("GBTNEAST_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EAST", "KEYRLS", "comment",),
	("GBTNMODE_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MODE", "KEYHLD", "comment",),
	("GBTNMODE_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MODE", "KEYPRS", "comment",),
	("GBTNMODE_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MODE", "KEYRLS", "comment",),
	("GBTNNORTH_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_NORTH", "KEYHLD", "comment",),
	("GBTNNORTH_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_NORTH", "KEYPRS", "comment",),
	("GBTNNORTH_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_NORTH", "KEYRLS", "comment",),
	("GBTNSELECT_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SELECT", "KEYHLD", "comment",),
	("GBTNSELECT_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SELECT", "KEYPRS", "comment",),
	("GBTNSELECT_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SELECT", "KEYRLS", "comment",),
	("GBTNSOUTH_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SOUTH", "KEYHLD", "comment",),
	("GBTNSOUTH_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SOUTH", "KEYPRS", "comment",),
	("GBTNSOUTH_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SOUTH", "KEYRLS", "comment",),
	("GBTNSTART_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_START", "KEYHLD", "comment",),
	("GBTNSTART_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_START", "KEYPRS", "comment",),
	("GBTNSTART_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_START", "KEYRLS", "comment",),
	("GBTNTL2_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TL2", "KEYHLD", "comment",),
	("GBTNTL2_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TL2", "KEYPRS", "comment",),
	("GBTNTL2_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TL2", "KEYRLS", "comment",),
	("GBTNTL_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TL", "KEYHLD", "comment",),
	("GBTNTL_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TL", "KEYPRS", "comment",),
	("GBTNTL_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TL", "KEYRLS", "comment",),
	("GBTNTR2_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TR2", "KEYHLD", "comment",),
	("GBTNTR2_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TR2", "KEYPRS", "comment",),
	("GBTNTR2_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TR2", "KEYRLS", "comment",),
	("GBTNTR_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TR", "KEYHLD", "comment",),
	("GBTNTR_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TR", "KEYPRS", "comment",),
	("GBTNTR_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TR", "KEYRLS", "comment",),
	("GBTNWEST_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_WEST", "KEYHLD", "comment",),
	("GBTNWEST_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_WEST", "KEYPRS", "comment",),
	("GBTNWEST_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_WEST", "KEYRLS", "comment",),
	("GBTNZ_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_Z", "KEYHLD", "comment",),
	("GBTNZ_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_Z", "KEYPRS", "comment",),
	("GBTNZ_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_Z", "KEYRLS", "comment",),
	("HASHDICT_00", FMAXCF_SCTN23DICTDEF, "HASHDICT", "define HASHDICT",),
	("HASHDICT_01", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "blake2b", "HASH_blake2b", "HASHDICT blake2b entry",),
	("HASHDICT_02", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "blake2s", "HASH_blake2s", "HASHDICT blake2s entry",),
	("HASHDICT_03", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha1", "HASH_sha1", "HASHDICT sha1 entry",),
	("HASHDICT_04", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha224", "HASH_sha224", "HASHDICT sha224 entry",),
	("HASHDICT_05", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha256", "HASH_sha256", "HASHDICT sha256 entry",),
	("HASHDICT_06", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha3224", "HASH_sha3224", "HASHDICT sha3224 entry",),
	("HASHDICT_07", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha3256", "HASH_sha3256", "HASHDICT sha3256 entry",),
	("HASHDICT_08", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha3384", "HASH_sha3384", "HASHDICT sha3384 entry",),
	("HASHDICT_09", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha3512", "HASH_sha3512", "HASHDICT sha3512 entry",),
	("HASHDICT_0A", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha384", "HASH_sha384", "HASHDICT sha384 entry",),
	("HASHDICT_0B", FMAXCF_SCTN23DICTVALADD, "HASHDICT", "sha512", "HASH_sha512", "HASHDICT sha512 entry",),
	("HBIBTN_M01LT", FMAXHBI_SCTN51BTNADD, "BTN_LEFT", "ability to send MSEBTNLT",),
	("HBIBTN_M02MID", FMAXHBI_SCTN51BTNADD, "BTN_MIDDLE", "ability to send MSEBTNMID",),
	("HBIBTN_M03RT ", FMAXHBI_SCTN51BTNADD, "BTN_RIGHT", "ability to send MSEBTNRT",),
	("HBIBTN_M08", FMAXHBI_SCTN51BTNADD, "BTN_EXTRA", "ability to send MSEBTNXTRA",),
	("HBIBTN_M09", FMAXHBI_SCTN51BTNADD, "BTN_SIDE", "ability to send MSEBTNSIDE",),
	("HBIBTN_M0A", FMAXHBI_SCTN51BTNADD, "BTN_FORWARD", "ability to send MSEBTNFWD",),
	("HBIBTN_M0B", FMAXHBI_SCTN51BTNADD, "BTN_BACK", "ability to send MSEBTNBAK",),
	("HBIBTN_M0C", FMAXHBI_SCTN51BTNADD, "BTN_TASK", "ability to send MSEBTNTASK",),
	("HBIKEY_0", FMAXHBI_SCTN52KEYADD, "KEY_0", "ability to send KEY_0",),
	("HBIKEY_1", FMAXHBI_SCTN52KEYADD, "KEY_1", "make KEY_1 available",),
	("HBIKEY_102ND", FMAXHBI_SCTN52KEYADD, "KEY_102ND", "make KEY_102ND available",),
	("HBIKEY_2", FMAXHBI_SCTN52KEYADD, "KEY_2", "make KEY_2 available",),
	("HBIKEY_3", FMAXHBI_SCTN52KEYADD, "KEY_3", "make KEY_3 available",),
	("HBIKEY_4", FMAXHBI_SCTN52KEYADD, "KEY_4", "make KEY_4 available",),
	("HBIKEY_5", FMAXHBI_SCTN52KEYADD, "KEY_5", "make KEY_5 available",),
	("HBIKEY_6", FMAXHBI_SCTN52KEYADD, "KEY_6", "make KEY_6 available",),
	("HBIKEY_7", FMAXHBI_SCTN52KEYADD, "KEY_7", "make KEY_7 available",),
	("HBIKEY_8", FMAXHBI_SCTN52KEYADD, "KEY_8", "make KEY_8 available",),
	("HBIKEY_9", FMAXHBI_SCTN52KEYADD, "KEY_9", "make KEY_9 available",),
	("HBIKEY_A", FMAXHBI_SCTN52KEYADD, "KEY_A", "make KEY_A available",),
	("HBIKEY_AGAIN", FMAXHBI_SCTN52KEYADD, "KEY_AGAIN", "make KEY_AGAIN available",),
	("HBIKEY_APOSTROPHE", FMAXHBI_SCTN52KEYADD, "KEY_APOSTROPHE", "make KEY_APOSTROPHE available",),
	("HBIKEY_B", FMAXHBI_SCTN52KEYADD, "KEY_B", "make KEY_B available",),
	("HBIKEY_BACK", FMAXHBI_SCTN52KEYADD, "KEY_BACK", "make KEY_BACK available",),
	("HBIKEY_BACKSLASH", FMAXHBI_SCTN52KEYADD, "KEY_BACKSLASH", "make KEY_BACKSLASH available",),
	("HBIKEY_BACKSPACE", FMAXHBI_SCTN52KEYADD, "KEY_BACKSPACE", "make KEY_BACKSPACE available",),
	("HBIKEY_C", FMAXHBI_SCTN52KEYADD, "KEY_C", "make KEY_C available",),
	("HBIKEY_CALC", FMAXHBI_SCTN52KEYADD, "KEY_CALC", "make KEY_CALC available",),
	("HBIKEY_CAPSLOCK", FMAXHBI_SCTN52KEYADD, "KEY_CAPSLOCK", "make KEY_CAPSLOCK available",),
	("HBIKEY_COFFEE", FMAXHBI_SCTN52KEYADD, "KEY_COFFEE", "make KEY_COFFEE available",),
	("HBIKEY_COMMA", FMAXHBI_SCTN52KEYADD, "KEY_COMMA", "make KEY_COMMA available",),
	("HBIKEY_COMPOSE", FMAXHBI_SCTN52KEYADD, "KEY_COMPOSE", "make KEY_COMPOSE available",),
	("HBIKEY_COPY", FMAXHBI_SCTN52KEYADD, "KEY_COPY", "make KEY_COPY available",),
	("HBIKEY_CUT", FMAXHBI_SCTN52KEYADD, "KEY_CUT", "make KEY_CUT available",),
	("HBIKEY_D", FMAXHBI_SCTN52KEYADD, "KEY_D", "make KEY_D available",),
	("HBIKEY_DELETE", FMAXHBI_SCTN52KEYADD, "KEY_DELETE", "make KEY_DELETE available",),
	("HBIKEY_DOT", FMAXHBI_SCTN52KEYADD, "KEY_DOT", "make KEY_DOT available",),
	("HBIKEY_DOWN", FMAXHBI_SCTN52KEYADD, "KEY_DOWN", "make KEY_DOWN available",),
	("HBIKEY_E", FMAXHBI_SCTN52KEYADD, "KEY_E", "make KEY_E available",),
	("HBIKEY_EDIT", FMAXHBI_SCTN52KEYADD, "KEY_EDIT", "make KEY_EDIT available",),
	("HBIKEY_EJECTCD", FMAXHBI_SCTN52KEYADD, "KEY_EJECTCD", "make KEY_EJECTCD available",),
	("HBIKEY_END", FMAXHBI_SCTN52KEYADD, "KEY_END", "make KEY_END available",),
	("HBIKEY_ENTER", FMAXHBI_SCTN52KEYADD, "KEY_ENTER", "make KEY_ENTER available",),
	("HBIKEY_EQUAL", FMAXHBI_SCTN52KEYADD, "KEY_EQUAL", "make KEY_EQUAL available",),
	("HBIKEY_ESC", FMAXHBI_SCTN52KEYADD, "KEY_ESC", "make KEY_ESC available",),
	("HBIKEY_F", FMAXHBI_SCTN52KEYADD, "KEY_F", "make KEY_F available",),
	("HBIKEY_F1", FMAXHBI_SCTN52KEYADD, "KEY_F1", "make KEY_F1 available",),
	("HBIKEY_F10", FMAXHBI_SCTN52KEYADD, "KEY_F10", "make KEY_F10 available",),
	("HBIKEY_F11", FMAXHBI_SCTN52KEYADD, "KEY_F11", "make KEY_F11 available",),
	("HBIKEY_F12", FMAXHBI_SCTN52KEYADD, "KEY_F12", "make KEY_F12 available",),
	("HBIKEY_F13", FMAXHBI_SCTN52KEYADD, "KEY_F13", "make KEY_F13 available",),
	("HBIKEY_F14", FMAXHBI_SCTN52KEYADD, "KEY_F14", "make KEY_F14 available",),
	("HBIKEY_F15", FMAXHBI_SCTN52KEYADD, "KEY_F15", "make KEY_F15 available",),
	("HBIKEY_F16", FMAXHBI_SCTN52KEYADD, "KEY_F16", "make KEY_F16 available",),
	("HBIKEY_F17", FMAXHBI_SCTN52KEYADD, "KEY_F17", "make KEY_F17 available",),
	("HBIKEY_F18", FMAXHBI_SCTN52KEYADD, "KEY_F18", "make KEY_F18 available",),
	("HBIKEY_F19", FMAXHBI_SCTN52KEYADD, "KEY_F19", "make KEY_F19 available",),
	("HBIKEY_F2", FMAXHBI_SCTN52KEYADD, "KEY_F2", "make KEY_F2 available",),
	("HBIKEY_F20", FMAXHBI_SCTN52KEYADD, "KEY_F20", "make KEY_F20 available",),
	("HBIKEY_F21", FMAXHBI_SCTN52KEYADD, "KEY_F21", "make KEY_F21 available",),
	("HBIKEY_F22", FMAXHBI_SCTN52KEYADD, "KEY_F22", "make KEY_F22 available",),
	("HBIKEY_F23", FMAXHBI_SCTN52KEYADD, "KEY_F23", "make KEY_F23 available",),
	("HBIKEY_F24", FMAXHBI_SCTN52KEYADD, "KEY_F24", "make KEY_F24 available",),
	("HBIKEY_F3", FMAXHBI_SCTN52KEYADD, "KEY_F3", "make KEY_F3 available",),
	("HBIKEY_F4", FMAXHBI_SCTN52KEYADD, "KEY_F4", "make KEY_F4 available",),
	("HBIKEY_F5", FMAXHBI_SCTN52KEYADD, "KEY_F5", "make KEY_F5 available",),
	("HBIKEY_F6", FMAXHBI_SCTN52KEYADD, "KEY_F6", "make KEY_F6 available",),
	("HBIKEY_F7", FMAXHBI_SCTN52KEYADD, "KEY_F7", "make KEY_F7 available",),
	("HBIKEY_F8", FMAXHBI_SCTN52KEYADD, "KEY_F8", "make KEY_F8 available",),
	("HBIKEY_F9", FMAXHBI_SCTN52KEYADD, "KEY_F9", "make KEY_F9 available",),
	("HBIKEY_FIND", FMAXHBI_SCTN52KEYADD, "KEY_FIND", "make KEY_FIND available",),
	("HBIKEY_FORWARD", FMAXHBI_SCTN52KEYADD, "KEY_FORWARD", "make KEY_FORWARD available",),
	("HBIKEY_FRONT", FMAXHBI_SCTN52KEYADD, "KEY_FRONT", "make KEY_FRONT available",),
	("HBIKEY_G", FMAXHBI_SCTN52KEYADD, "KEY_G", "make KEY_G available",),
	("HBIKEY_GRAVE", FMAXHBI_SCTN52KEYADD, "KEY_GRAVE", "make KEY_GRAVE available",),
	("HBIKEY_H", FMAXHBI_SCTN52KEYADD, "KEY_H", "make KEY_H available",),
	("HBIKEY_HANGEUL", FMAXHBI_SCTN52KEYADD, "KEY_HANGEUL", "make KEY_HANGEUL available",),
	("HBIKEY_HANJA", FMAXHBI_SCTN52KEYADD, "KEY_HANJA", "make KEY_HANJA available",),
	("HBIKEY_HELP", FMAXHBI_SCTN52KEYADD, "KEY_HELP", "make KEY_HELP available",),
	("HBIKEY_HENKAN", FMAXHBI_SCTN52KEYADD, "KEY_HENKAN", "make KEY_HENKAN available",),
	("HBIKEY_HIRAGANA", FMAXHBI_SCTN52KEYADD, "KEY_HIRAGANA", "make KEY_HIRAGANA available",),
	("HBIKEY_HOME", FMAXHBI_SCTN52KEYADD, "KEY_HOME", "make KEY_HOME available",),
	("HBIKEY_I", FMAXHBI_SCTN52KEYADD, "KEY_I", "make KEY_I available",),
	("HBIKEY_INSERT", FMAXHBI_SCTN52KEYADD, "KEY_INSERT", "make KEY_INSERT available",),
	("HBIKEY_J", FMAXHBI_SCTN52KEYADD, "KEY_J", "make KEY_J available",),
	("HBIKEY_K", FMAXHBI_SCTN52KEYADD, "KEY_K", "make KEY_K available",),
	("HBIKEY_KATAKANA", FMAXHBI_SCTN52KEYADD, "KEY_KATAKANA", "make KEY_KATAKANA available",),
	("HBIKEY_KATAKANAHIRAGANA", FMAXHBI_SCTN52KEYADD, "KEY_KATAKANAHIRAGANA", "make KEY_KATAKANAHIRAGANA available",),
	("HBIKEY_KP0", FMAXHBI_SCTN52KEYADD, "KEY_KP0", "make KEY_KP0 available",),
	("HBIKEY_KP1", FMAXHBI_SCTN52KEYADD, "KEY_KP1", "make KEY_KP1 available",),
	("HBIKEY_KP2", FMAXHBI_SCTN52KEYADD, "KEY_KP2", "make KEY_KP2 available",),
	("HBIKEY_KP3", FMAXHBI_SCTN52KEYADD, "KEY_KP3", "make KEY_KP3 available",),
	("HBIKEY_KP4", FMAXHBI_SCTN52KEYADD, "KEY_KP4", "make KEY_KP4 available",),
	("HBIKEY_KP5", FMAXHBI_SCTN52KEYADD, "KEY_KP5", "make KEY_KP5 available",),
	("HBIKEY_KP6", FMAXHBI_SCTN52KEYADD, "KEY_KP6", "make KEY_KP6 available",),
	("HBIKEY_KP7", FMAXHBI_SCTN52KEYADD, "KEY_KP7", "make KEY_KP7 available",),
	("HBIKEY_KP8", FMAXHBI_SCTN52KEYADD, "KEY_KP8", "make KEY_KP8 available",),
	("HBIKEY_KP9", FMAXHBI_SCTN52KEYADD, "KEY_KP9", "make KEY_KP9 available",),
	("HBIKEY_KPASTERISK", FMAXHBI_SCTN52KEYADD, "KEY_KPASTERISK", "make KEY_KPASTERISK available",),
	("HBIKEY_KPCOMMA", FMAXHBI_SCTN52KEYADD, "KEY_KPCOMMA", "make KEY_KPCOMMA available",),
	("HBIKEY_KPDOT", FMAXHBI_SCTN52KEYADD, "KEY_KPDOT", "make KEY_KPDOT available",),
	("HBIKEY_KPENTER", FMAXHBI_SCTN52KEYADD, "KEY_KPENTER", "make KEY_KPENTER available",),
	("HBIKEY_KPEQUAL", FMAXHBI_SCTN52KEYADD, "KEY_KPEQUAL", "make KEY_KPEQUAL available",),
	("HBIKEY_KPJPCOMMA", FMAXHBI_SCTN52KEYADD, "KEY_KPJPCOMMA", "make KEY_KPJPCOMMA available",),
	("HBIKEY_KPLEFTPAREN", FMAXHBI_SCTN52KEYADD, "KEY_KPLEFTPAREN", "make KEY_KPLEFTPAREN available",),
	("HBIKEY_KPMINUS", FMAXHBI_SCTN52KEYADD, "KEY_KPMINUS", "make KEY_KPMINUS available",),
	("HBIKEY_KPPLUS", FMAXHBI_SCTN52KEYADD, "KEY_KPPLUS", "make KEY_KPPLUS available",),
	("HBIKEY_KPRIGHTPAREN", FMAXHBI_SCTN52KEYADD, "KEY_KPRIGHTPAREN", "make KEY_KPRIGHTPAREN available",),
	("HBIKEY_KPSLASH", FMAXHBI_SCTN52KEYADD, "KEY_KPSLASH", "make KEY_KPSLASH available",),
	("HBIKEY_L", FMAXHBI_SCTN52KEYADD, "KEY_L", "make KEY_L available",),
	("HBIKEY_LEFT", FMAXHBI_SCTN52KEYADD, "KEY_LEFT", "make KEY_LEFT available",),
	("HBIKEY_LEFTALT", FMAXHBI_SCTN52KEYADD, "KEY_LEFTALT", "make KEY_LEFTALT available",),
	("HBIKEY_LEFTBRACE", FMAXHBI_SCTN52KEYADD, "KEY_LEFTBRACE", "make KEY_LEFTBRACE available",),
	("HBIKEY_LEFTCTRL", FMAXHBI_SCTN52KEYADD, "KEY_LEFTCTRL", "make KEY_LEFTCTRL available",),
	("HBIKEY_LEFTMETA", FMAXHBI_SCTN52KEYADD, "KEY_LEFTMETA", "make KEY_LEFTMETA available",),
	("HBIKEY_LEFTSHIFT", FMAXHBI_SCTN52KEYADD, "KEY_LEFTSHIFT", "make KEY_LEFTSHIFT available",),
	("HBIKEY_M", FMAXHBI_SCTN52KEYADD, "KEY_M", "make KEY_M available",),
	("HBIKEY_MINUS", FMAXHBI_SCTN52KEYADD, "KEY_MINUS", "make KEY_MINUS available",),
	("HBIKEY_MUHENKAN", FMAXHBI_SCTN52KEYADD, "KEY_MUHENKAN", "make KEY_MUHENKAN available",),
	("HBIKEY_MUTE", FMAXHBI_SCTN52KEYADD, "KEY_MUTE", "make KEY_MUTE available",),
	("HBIKEY_N", FMAXHBI_SCTN52KEYADD, "KEY_N", "make KEY_N available",),
	("HBIKEY_NEXTSONG", FMAXHBI_SCTN52KEYADD, "KEY_NEXTSONG", "make KEY_NEXTSONG available",),
	("HBIKEY_NUMLOCK", FMAXHBI_SCTN52KEYADD, "KEY_NUMLOCK", "make KEY_NUMLOCK available",),
	("HBIKEY_O", FMAXHBI_SCTN52KEYADD, "KEY_O", "make KEY_O available",),
	("HBIKEY_OPEN", FMAXHBI_SCTN52KEYADD, "KEY_OPEN", "make KEY_OPEN available",),
	("HBIKEY_P", FMAXHBI_SCTN52KEYADD, "KEY_P", "make KEY_P available",),
	("HBIKEY_PAGEDOWN", FMAXHBI_SCTN52KEYADD, "KEY_PAGEDOWN", "make KEY_PAGEDOWN available",),
	("HBIKEY_PAGEUP", FMAXHBI_SCTN52KEYADD, "KEY_PAGEUP", "make KEY_PAGEUP available",),
	("HBIKEY_PASTE", FMAXHBI_SCTN52KEYADD, "KEY_PASTE", "make KEY_PASTE available",),
	("HBIKEY_PAUSE", FMAXHBI_SCTN52KEYADD, "KEY_PAUSE", "make KEY_PAUSE available",),
	("HBIKEY_PLAYPAUSE", FMAXHBI_SCTN52KEYADD, "KEY_PLAYPAUSE", "make KEY_PLAYPAUSE available",),
	("HBIKEY_POWER", FMAXHBI_SCTN52KEYADD, "KEY_POWER", "make KEY_POWER available",),
	("HBIKEY_PREVIOUSSONG", FMAXHBI_SCTN52KEYADD, "KEY_PREVIOUSSONG", "make KEY_PREVIOUSSONG available",),
	("HBIKEY_PROPS", FMAXHBI_SCTN52KEYADD, "KEY_PROPS", "make KEY_PROPS available",),
	("HBIKEY_Q", FMAXHBI_SCTN52KEYADD, "KEY_Q", "make KEY_Q available",),
	("HBIKEY_R", FMAXHBI_SCTN52KEYADD, "KEY_R", "make KEY_R available",),
	("HBIKEY_REFRESH", FMAXHBI_SCTN52KEYADD, "KEY_REFRESH", "make KEY_REFRESH available",),
	("HBIKEY_RIGHT", FMAXHBI_SCTN52KEYADD, "KEY_RIGHT", "make KEY_RIGHT available",),
	("HBIKEY_RIGHTALT", FMAXHBI_SCTN52KEYADD, "KEY_RIGHTALT", "make KEY_RIGHTALT available",),
	("HBIKEY_RIGHTBRACE", FMAXHBI_SCTN52KEYADD, "KEY_RIGHTBRACE", "make KEY_RIGHTBRACE available",),
	("HBIKEY_RIGHTCTRL", FMAXHBI_SCTN52KEYADD, "KEY_RIGHTCTRL", "make KEY_RIGHTCTRL available",),
	("HBIKEY_RIGHTMETA", FMAXHBI_SCTN52KEYADD, "KEY_RIGHTMETA", "make KEY_RIGHTMETA available",),
	("HBIKEY_RIGHTSHIFT", FMAXHBI_SCTN52KEYADD, "KEY_RIGHTSHIFT", "make KEY_RIGHTSHIFT available",),
	("HBIKEY_RO", FMAXHBI_SCTN52KEYADD, "KEY_RO", "make KEY_RO available",),
	("HBIKEY_S", FMAXHBI_SCTN52KEYADD, "KEY_S", "make KEY_S available",),
	("HBIKEY_SCROLLDOWN", FMAXHBI_SCTN52KEYADD, "KEY_SCROLLDOWN", "make KEY_SCROLLDOWN available",),
	("HBIKEY_SCROLLLOCK", FMAXHBI_SCTN52KEYADD, "KEY_SCROLLLOCK", "make KEY_SCROLLLOCK available",),
	("HBIKEY_SCROLLUP", FMAXHBI_SCTN52KEYADD, "KEY_SCROLLUP", "make KEY_SCROLLUP available",),
	("HBIKEY_SEMICOLON", FMAXHBI_SCTN52KEYADD, "KEY_SEMICOLON", "make KEY_SEMICOLON available",),
	("HBIKEY_SLASH", FMAXHBI_SCTN52KEYADD, "KEY_SLASH", "make KEY_SLASH available",),
	("HBIKEY_SLEEP", FMAXHBI_SCTN52KEYADD, "KEY_SLEEP", "make KEY_SLEEP available",),
	("HBIKEY_SPACE", FMAXHBI_SCTN52KEYADD, "KEY_SPACE", "make KEY_SPACE available",),
	("HBIKEY_STOP", FMAXHBI_SCTN52KEYADD, "KEY_STOP", "make KEY_STOP available",),
	("HBIKEY_STOPCD", FMAXHBI_SCTN52KEYADD, "KEY_STOPCD", "make KEY_STOPCD available",),
	("HBIKEY_SYSRQ", FMAXHBI_SCTN52KEYADD, "KEY_SYSRQ", "make KEY_SYSRQ available",),
	("HBIKEY_T", FMAXHBI_SCTN52KEYADD, "KEY_T", "make KEY_T available",),
	("HBIKEY_TAB", FMAXHBI_SCTN52KEYADD, "KEY_TAB", "make KEY_TAB available",),
	("HBIKEY_U", FMAXHBI_SCTN52KEYADD, "KEY_U", "make KEY_U available",),
	("HBIKEY_UNDO", FMAXHBI_SCTN52KEYADD, "KEY_UNDO", "make KEY_UNDO available",),
	("HBIKEY_UNKNOWN", FMAXHBI_SCTN52KEYADD, "KEY_UNKNOWN", "make KEY_UNKNOWN available",),
	("HBIKEY_UP", FMAXHBI_SCTN52KEYADD, "KEY_UP", "make KEY_UP available",),
	("HBIKEY_V", FMAXHBI_SCTN52KEYADD, "KEY_V", "make KEY_V available",),
	("HBIKEY_VOLUMEDOWN", FMAXHBI_SCTN52KEYADD, "KEY_VOLUMEDOWN", "make KEY_VOLUMEDOWN available",),
	("HBIKEY_VOLUMEUP", FMAXHBI_SCTN52KEYADD, "KEY_VOLUMEUP", "make KEY_VOLUMEUP available",),
	("HBIKEY_W", FMAXHBI_SCTN52KEYADD, "KEY_W", "make KEY_W available",),
	("HBIKEY_WWW", FMAXHBI_SCTN52KEYADD, "KEY_WWW", "make KEY_WWW available",),
	("HBIKEY_X", FMAXHBI_SCTN52KEYADD, "KEY_X", "make KEY_X available",),
	("HBIKEY_Y", FMAXHBI_SCTN52KEYADD, "KEY_Y", "make KEY_Y available",),
	("HBIKEY_YEN", FMAXHBI_SCTN52KEYADD, "KEY_YEN", "make KEY_YEN available",),
	("HBIKEY_Z", FMAXHBI_SCTN52KEYADD, "KEY_Z", "make KEY_Z available",),
	("HBIKEY_ZENKAKUHANKAKU", FMAXHBI_SCTN52KEYADD, "KEY_ZENKAKUHANKAKU", "make KEY_ZENKAKUHANKAKU available",),
	("HBIREL_HWHEEL", FMAXHBI_SCTN53RELADD, "REL_HWHEEL", "make REL_HWHEEL available",),
	("HBIREL_HWHEEL_HI_RES", FMAXHBI_SCTN53RELADD, "REL_HWHEEL_HI_RES", "make REL_HWHEEL_HI_RES available",),
	("HBIREL_WHEEL", FMAXHBI_SCTN53RELADD, "REL_WHEEL", "make REL_WHEEL available",),
	("HBIREL_WHEEL_HI_RES", FMAXHBI_SCTN53RELADD, "REL_WHEEL_HI_RES", "make REL_WHEEL_HI_RES available",),
	("HBIREL_X", FMAXHBI_SCTN53RELADD, "REL_X", "make REL_X available",),
	("HBIREL_Y", FMAXHBI_SCTN53RELADD, "REL_Y", "make REL_Y available",),
	("KBD0_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_0", "KEYHLD", "0_held",),
	("KBD0_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_0", "KEYPRS", "0_pressed",),
	("KBD0_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_0", "KEYRLS", "0_released",),
	("KBD102_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_102ND", "KEYHLD", "102_held",),
	("KBD102_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_102ND", "KEYPRS", "102_pressed",),
	("KBD102_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_102ND", "KEYRLS", "102_released",),
	("KBD1_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_1", "KEYHLD", "1_held",),
	("KBD1_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_1", "KEYPRS", "1_pressed",),
	("KBD1_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_1", "KEYRLS", "1_released",),
	("KBD2_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_2", "KEYHLD", "2_held",),
	("KBD2_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_2", "KEYPRS", "2_pressed",),
	("KBD2_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_2", "KEYRLS", "2_released",),
	("KBD3_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_3", "KEYHLD", "3_held",),
	("KBD3_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_3", "KEYPRS", "3_pressed",),
	("KBD3_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_3", "KEYRLS", "3_released",),
	("KBD4_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_4", "KEYHLD", "4_held",),
	("KBD4_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_4", "KEYPRS", "4_pressed",),
	("KBD4_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_4", "KEYRLS", "4_released",),
	("KBD5_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_5", "KEYHLD", "5_held",),
	("KBD5_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_5", "KEYPRS", "5_pressed",),
	("KBD5_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_5", "KEYRLS", "5_released",),
	("KBD6_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_6", "KEYHLD", "6_held",),
	("KBD6_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_6", "KEYPRS", "6_pressed",),
	("KBD6_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_6", "KEYRLS", "6_released",),
	("KBD7_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_7", "KEYHLD", "7_held",),
	("KBD7_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_7", "KEYPRS", "7_pressed",),
	("KBD7_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_7", "KEYRLS", "7_released",),
	("KBD8_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_8", "KEYHLD", "8_held",),
	("KBD8_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_8", "KEYPRS", "8_pressed",),
	("KBD8_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_8", "KEYRLS", "8_released",),
	("KBD9_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_9", "KEYHLD", "9_held",),
	("KBD9_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_9", "KEYPRS", "9_pressed",),
	("KBD9_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_9", "KEYRLS", "9_released",),
	("KBDAGAIN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_AGAIN", "KEYHLD", "AGAIN_held",),
	("KBDAGAIN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_AGAIN", "KEYPRS", "AGAIN_pressed",),
	("KBDAGAIN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_AGAIN", "KEYRLS", "AGAIN_released",),
	("KBDALTLT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTALT", "KEYHLD", "ALT_held",),
	("KBDALTLT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTALT", "KEYPRS", "ALT_pressed",),
	("KBDALTLT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTALT", "KEYRLS", "ALT_released",),
	("KBDALTRT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTALT", "KEYHLD", "RALT_held",),
	("KBDALTRT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTALT", "KEYPRS", "RALT_pressed",),
	("KBDALTRT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTALT", "KEYRLS", "RALT_released",),
	("KBDAPOSTROPHE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_APOSTROPHE", "KEYHLD", "APOSTROPHE_held",),
	("KBDAPOSTROPHE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_APOSTROPHE", "KEYPRS", "APOSTROPHE_pressed",),
	("KBDAPOSTROPHE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_APOSTROPHE", "KEYRLS", "APOSTROPHE_released",),
	("KBDA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_A", "KEYHLD", "A_held",),
	("KBDA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_A", "KEYPRS", "A_pressed",),
	("KBDA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_A", "KEYRLS", "A_released",),
	("KBDBKSLASH_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACKSLASH", "KEYHLD", "BACKSLASH_held",),
	("KBDBKSLASH_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACKSLASH", "KEYPRS", "BACKSLASH_pressed",),
	("KBDBKSLASH_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACKSLASH", "KEYRLS", "BACKSLASH_released",),
	("KBDBKSPC_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACKSPACE", "KEYHLD", "BACKSPACE_held",),
	("KBDBKSPC_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACKSPACE", "KEYPRS", "BACKSPACE_pressed",),
	("KBDBKSPC_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACKSPACE", "KEYRLS", "BACKSPACE_released",),
	("KBDBK_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACK", "KEYHLD", "BK_held",),
	("KBDBK_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACK", "KEYPRS", "BK_pressed",),
	("KBDBK_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_BACK", "KEYRLS", "BK_released",),
	("KBDBRACELT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTBRACE", "KEYHLD", "LBRACE_held",),
	("KBDBRACELT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTBRACE", "KEYPRS", "LBRACE_pressed",),
	("KBDBRACELT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTBRACE", "KEYRLS", "LBRACE_released",),
	("KBDBRACERT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTBRACE", "KEYHLD", "RBRACE_held",),
	("KBDBRACERT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTBRACE", "KEYPRS", "RBRACE_pressed",),
	("KBDBRACERT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTBRACE", "KEYRLS", "RBRACE_released",),
	("KBDB_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_B", "KEYHLD", "B_held_held",),
	("KBDB_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_B", "KEYPRS", "B_pressed",),
	("KBDB_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_B", "KEYRLS", "B_released",),
	("KBDCALC_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CALC", "KEYHLD", "CALC_held",),
	("KBDCALC_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CALC", "KEYPRS", "CALC_pressed",),
	("KBDCALC_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CALC", "KEYRLS", "CALC_released",),
	("KBDCAPSLK_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CAPSLOCK", "KEYHLD", "CAPS_held",),
	("KBDCAPSLK_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CAPSLOCK", "KEYPRS", "CAPS_pressed",),
	("KBDCAPSLK_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CAPSLOCK", "KEYRLS", "CAPS_released",),
	("KBDCOFFEE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COFFEE", "KEYHLD", "COFFEE_held",),
	("KBDCOFFEE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COFFEE", "KEYPRS", "COFFEE_pressed",),
	("KBDCOFFEE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COFFEE", "KEYRLS", "COFFEE_released",),
	("KBDCOMMA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COMMA", "KEYHLD", "COMMA_held",),
	("KBDCOMMA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COMMA", "KEYPRS", "COMMA_pressed",),
	("KBDCOMMA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COMMA", "KEYRLS", "COMMA_released",),
	("KBDCOMPOSE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COMPOSE", "KEYHLD", "COMPOSE_held",),
	("KBDCOMPOSE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COMPOSE", "KEYPRS", "COMPOSE_pressed",),
	("KBDCOMPOSE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COMPOSE", "KEYRLS", "COMPOSE_released",),
	("KBDCOPY_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COPY", "KEYHLD", "COPY_held",),
	("KBDCOPY_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COPY", "KEYPRS", "COPY_pressed",),
	("KBDCOPY_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_COPY", "KEYRLS", "COPY_released",),
	("KBDCTRLLT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTCTRL", "KEYHLD", "LCTRL_held",),
	("KBDCTRLLT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTCTRL", "KEYPRS", "LCTRL_pressed",),
	("KBDCTRLLT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTCTRL", "KEYRLS", "LCTRL_released",),
	("KBDCTRLRT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTCTRL", "KEYHLD", "RCTRL_held",),
	("KBDCTRLRT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTCTRL", "KEYPRS", "RCTRL_pressed",),
	("KBDCTRLRT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTCTRL", "KEYRLS", "RCTRL_released",),
	("KBDCUT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CUT", "KEYHLD", "CUT_held",),
	("KBDCUT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CUT", "KEYPRS", "CUT_pressed",),
	("KBDCUT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_CUT", "KEYRLS", "CUT_released",),
	("KBDC_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_C", "KEYHLD", "C_held",),
	("KBDC_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_C", "KEYPRS", "C_pressed",),
	("KBDC_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_C", "KEYRLS", "C_released",),
	("KBDDEL_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DELETE", "KEYHLD", "DEL_held",),
	("KBDDEL_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DELETE", "KEYPRS", "DEL_pressed",),
	("KBDDEL_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DELETE", "KEYRLS", "DEL_released",),
	("KBDDN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DOWN", "KEYHLD", "DOWN_held",),
	("KBDDN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DOWN", "KEYPRS", "DOWN_pressed",),
	("KBDDN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DOWN", "KEYRLS", "DOWN_released",),
	("KBDDOT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DOT", "KEYHLD", "DOT_held",),
	("KBDDOT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DOT", "KEYPRS", "DOT_pressed",),
	("KBDDOT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_DOT", "KEYRLS", "DOT_released",),
	("KBDD_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_D", "KEYHLD", "D_held",),
	("KBDD_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_D", "KEYPRS", "D_pressed",),
	("KBDD_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_D", "KEYRLS", "D_released",),
	("KBDEDIT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EDIT", "KEYHLD", "EDIT_held",),
	("KBDEDIT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EDIT", "KEYPRS", "EDIT_pressed",),
	("KBDEDIT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EDIT", "KEYRLS", "EDIT_released",),
	("KBDEJECTCD_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EJECTCD", "KEYHLD", "EJECTCD_held",),
	("KBDEJECTCD_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EJECTCD", "KEYPRS", "EJECTCD_pressed",),
	("KBDEJECTCD_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EJECTCD", "KEYRLS", "EJECTCD_released",),
	("KBDEND_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_END", "KEYHLD", "END_held",),
	("KBDEND_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_END", "KEYPRS", "END_pressed",),
	("KBDEND_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_END", "KEYRLS", "END_released",),
	("KBDENTER_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ENTER", "KEYHLD", "ENTER_held",),
	("KBDENTER_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ENTER", "KEYPRS", "ENTER_pressed",),
	("KBDENTER_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ENTER", "KEYRLS", "ENTER_released",),
	("KBDEQ_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EQUAL", "KEYHLD", "EQUAL_held",),
	("KBDEQ_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EQUAL", "KEYPRS", "EQUAL_pressed",),
	("KBDEQ_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_EQUAL", "KEYRLS", "EQUAL_released",),
	("KBDESC_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ESC", "KEYHLD", "ESC_held",),
	("KBDESC_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ESC", "KEYPRS", "ESC_pressed",),
	("KBDESC_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ESC", "KEYRLS", "ESC_released",),
	("KBDE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_E", "KEYHLD", "E_held",),
	("KBDE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_E", "KEYPRS", "E_pressed",),
	("KBDE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_E", "KEYRLS", "E_released",),
	("KBDF10_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F10", "KEYHLD", "F10_held",),
	("KBDF10_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F10", "KEYPRS", "F10_pressed",),
	("KBDF10_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F10", "KEYRLS", "F10_released",),
	("KBDF11_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F11", "KEYHLD", "F11_held",),
	("KBDF11_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F11", "KEYPRS", "F11_pressed",),
	("KBDF11_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F11", "KEYRLS", "F11_released",),
	("KBDF12_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F12", "KEYHLD", "F12_held",),
	("KBDF12_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F12", "KEYPRS", "F12_pressed",),
	("KBDF12_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F12", "KEYRLS", "F12_released",),
	("KBDF13_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F13", "KEYHLD", "F13_held",),
	("KBDF13_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F13", "KEYPRS", "F13_pressed",),
	("KBDF13_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F13", "KEYRLS", "F13_released",),
	("KBDF14_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F14", "KEYHLD", "F14_held",),
	("KBDF14_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F14", "KEYPRS", "F14_pressed",),
	("KBDF14_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F14", "KEYRLS", "F14_released",),
	("KBDF15_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F15", "KEYHLD", "F15_held",),
	("KBDF15_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F15", "KEYPRS", "F15_pressed",),
	("KBDF15_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F15", "KEYRLS", "F15_released",),
	("KBDF16_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F16", "KEYHLD", "F16_held",),
	("KBDF16_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F16", "KEYPRS", "F16_pressed",),
	("KBDF16_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F16", "KEYRLS", "F16_released",),
	("KBDF17_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F17", "KEYHLD", "F17_held",),
	("KBDF17_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F17", "KEYPRS", "F17_pressed",),
	("KBDF17_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F17", "KEYRLS", "F17_released",),
	("KBDF18_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F18", "KEYHLD", "F18_held",),
	("KBDF18_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F18", "KEYPRS", "F18_pressed",),
	("KBDF18_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F18", "KEYRLS", "F18_released",),
	("KBDF19_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F19", "KEYHLD", "F19_held",),
	("KBDF19_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F19", "KEYPRS", "F19_pressed",),
	("KBDF19_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F19", "KEYRLS", "F19_released",),
	("KBDF1_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F1", "KEYHLD", "F1_held",),
	("KBDF1_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F1", "KEYPRS", "F1_pressed",),
	("KBDF1_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F1", "KEYRLS", "F1_released",),
	("KBDF20_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F20", "KEYHLD", "F20_held",),
	("KBDF20_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F20", "KEYPRS", "F20_pressed",),
	("KBDF20_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F20", "KEYRLS", "F20_released",),
	("KBDF21_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F21", "KEYHLD", "F21_held",),
	("KBDF21_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F21", "KEYPRS", "F21_pressed",),
	("KBDF21_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F21", "KEYRLS", "F21_released",),
	("KBDF22_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F22", "KEYHLD", "F22_held",),
	("KBDF22_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F22", "KEYPRS", "F22_pressed",),
	("KBDF22_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F22", "KEYRLS", "F22_released",),
	("KBDF23_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F23", "KEYHLD", "F23_held",),
	("KBDF23_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F23", "KEYPRS", "F23_pressed",),
	("KBDF23_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F23", "KEYRLS", "F23_released",),
	("KBDF24_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F24", "KEYHLD", "F24_held",),
	("KBDF24_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F24", "KEYPRS", "F24_pressed",),
	("KBDF24_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F24", "KEYRLS", "F24_released",),
	("KBDF2_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F2", "KEYHLD", "F2_held",),
	("KBDF2_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F2", "KEYPRS", "F2_pressed",),
	("KBDF2_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F2", "KEYRLS", "F2_released",),
	("KBDF3_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F3", "KEYHLD", "F3_held",),
	("KBDF3_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F3", "KEYPRS", "F3_pressed",),
	("KBDF3_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F3", "KEYRLS", "F3_released",),
	("KBDF4_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F4", "KEYHLD", "F4_held",),
	("KBDF4_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F4", "KEYPRS", "F4_pressed",),
	("KBDF4_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F4", "KEYRLS", "F4_released",),
	("KBDF5_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F5", "KEYHLD", "F5_held",),
	("KBDF5_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F5", "KEYPRS", "F5_pressed",),
	("KBDF5_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F5", "KEYRLS", "F5_released",),
	("KBDF6_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F6", "KEYHLD", "F6_held",),
	("KBDF6_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F6", "KEYPRS", "F6_pressed",),
	("KBDF6_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F6", "KEYRLS", "F6_released",),
	("KBDF7_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F7", "KEYHLD", "F7_held",),
	("KBDF7_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F7", "KEYPRS", "F7_pressed",),
	("KBDF7_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F7", "KEYRLS", "F7_released",),
	("KBDF8_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F8", "KEYHLD", "F8_held",),
	("KBDF8_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F8", "KEYPRS", "F8_pressed",),
	("KBDF8_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F8", "KEYRLS", "F8_released",),
	("KBDF9_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F9", "KEYHLD", "F9_held",),
	("KBDF9_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F9", "KEYPRS", "F9_pressed",),
	("KBDF9_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F9", "KEYRLS", "F9_released",),
	("KBDFIND_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FIND", "KEYHLD", "FIND_held",),
	("KBDFIND_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FIND", "KEYPRS", "FIND_pressed",),
	("KBDFIND_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FIND", "KEYRLS", "FIND_released",),
	("KBDFORWARD_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FORWARD", "KEYHLD", "FORWARD_held",),
	("KBDFORWARD_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FORWARD", "KEYPRS", "FORWARD_pressed",),
	("KBDFORWARD_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FORWARD", "KEYRLS", "FORWARD_released",),
	("KBDFRONT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FRONT", "KEYHLD", "FRONT_held",),
	("KBDFRONT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FRONT", "KEYPRS", "FRONT_pressed",),
	("KBDFRONT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_FRONT", "KEYRLS", "FRONT_released",),
	("KBDF_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F", "KEYHLD", "F_held",),
	("KBDF_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F", "KEYPRS", "F_pressed",),
	("KBDF_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_F", "KEYRLS", "F_released",),
	("KBDGRAVE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_GRAVE", "KEYHLD", "GRAVÉ_held",),
	("KBDGRAVE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_GRAVE", "KEYPRS", "GRAVÉ_pressed",),
	("KBDGRAVE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_GRAVE", "KEYRLS", "GRAVÉ_released",),
	("KBDG_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_G", "KEYHLD", "G_held",),
	("KBDG_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_G", "KEYPRS", "G_pressed",),
	("KBDG_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_G", "KEYRLS", "G_released",),
	("KBDHANGUEL_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HANGEUL", "KEYHLD", "HANGUEL_held",),
	("KBDHANGUEL_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HANGEUL", "KEYPRS", "HANGUEL_pressed",),
	("KBDHANGUEL_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HANGEUL", "KEYRLS", "HANGUEL_released",),
	("KBDHANJA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HANJA", "KEYHLD", "HANJA_held",),
	("KBDHANJA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HANJA", "KEYPRS", "HANJA_pressed",),
	("KBDHANJA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HANJA", "KEYRLS", "HANJA_released",),
	("KBDHELP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HELP", "KEYHLD", "HELP_held",),
	("KBDHELP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HELP", "KEYPRS", "HELP_pressed",),
	("KBDHELP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HELP", "KEYRLS", "HELP_released",),
	("KBDHENKAN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HENKAN", "KEYHLD", "HENKAN_held",),
	("KBDHENKAN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HENKAN", "KEYPRS", "HENKAN_pressed",),
	("KBDHENKAN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HENKAN", "KEYRLS", "HENKAN_released",),
	("KBDHIRAGANA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HIRAGANA", "KEYHLD", "HIRAGANA_held",),
	("KBDHIRAGANA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HIRAGANA", "KEYPRS", "HIRAGANA_pressed",),
	("KBDHIRAGANA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HIRAGANA", "KEYRLS", "HIRAGANA_released",),
	("KBDHOME_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HOME", "KEYHLD", "HOME_held",),
	("KBDHOME_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HOME", "KEYPRS", "HOME_pressed",),
	("KBDHOME_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_HOME", "KEYRLS", "HOME_released",),
	("KBDH_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_H", "KEYHLD", "H_held",),
	("KBDH_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_H", "KEYPRS", "H_pressed",),
	("KBDH_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_H", "KEYRLS", "H_released",),
	("KBDINSERT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_INSERT", "KEYHLD", "INSERT_held",),
	("KBDINSERT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_INSERT", "KEYPRS", "INSERT_pressed",),
	("KBDINSERT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_INSERT", "KEYRLS", "INSERT_released",),
	("KBDI_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_I", "KEYHLD", "I_held",),
	("KBDI_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_I", "KEYPRS", "I_pressed",),
	("KBDI_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_I", "KEYRLS", "I_released",),
	("KBDJ_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_J", "KEYHLD", "J_held",),
	("KBDJ_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_J", "KEYPRS", "J_pressed",),
	("KBDJ_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_J", "KEYRLS", "J_released",),
	("KBDKATAKANAHIRAGANA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KATAKANAHIRAGANA", "KEYHLD", "KATAKANAHIRAGANA_held",),
	("KBDKATAKANAHIRAGANA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KATAKANAHIRAGANA", "KEYPRS", "KATAKANAHIRAGANA_pressed",),
	("KBDKATAKANAHIRAGANA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KATAKANAHIRAGANA", "KEYRLS", "KATAKANAHIRAGANA_released",),
	("KBDKATAKANA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KATAKANA", "KEYHLD", "KATAKANA_held",),
	("KBDKATAKANA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KATAKANA", "KEYPRS", "KATAKANA_pressed",),
	("KBDKATAKANA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KATAKANA", "KEYRLS", "KATAKANA_released",),
	("KBDKP0_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP0", "KEYHLD", "KP0_held",),
	("KBDKP0_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP0", "KEYPRS", "KP0_pressed",),
	("KBDKP0_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP0", "KEYRLS", "KP0_released",),
	("KBDKP1_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP1", "KEYHLD", "KP1_held",),
	("KBDKP1_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP1", "KEYPRS", "KP1_pressed",),
	("KBDKP1_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP1", "KEYRLS", "KP1_released",),
	("KBDKP2_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP2", "KEYHLD", "KP2_held",),
	("KBDKP2_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP2", "KEYPRS", "KP2_pressed",),
	("KBDKP2_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP2", "KEYRLS", "KP2_released",),
	("KBDKP3_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP3", "KEYHLD", "KP3_held",),
	("KBDKP3_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP3", "KEYPRS", "KP3_pressed",),
	("KBDKP3_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP3", "KEYRLS", "KP3_released",),
	("KBDKP4_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP4", "KEYHLD", "KP4_held",),
	("KBDKP4_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP4", "KEYPRS", "KP4_pressed",),
	("KBDKP4_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP4", "KEYRLS", "KP4_released",),
	("KBDKP5_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP5", "KEYHLD", "KP5_held",),
	("KBDKP5_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP5", "KEYPRS", "KP5_pressed",),
	("KBDKP5_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP5", "KEYRLS", "KP5_released",),
	("KBDKP6_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP6", "KEYHLD", "KP6_held",),
	("KBDKP6_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP6", "KEYPRS", "KP6_pressed",),
	("KBDKP6_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP6", "KEYRLS", "KP6_released",),
	("KBDKP7_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP7", "KEYHLD", "KP7_held",),
	("KBDKP7_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP7", "KEYPRS", "KP7_pressed",),
	("KBDKP7_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP7", "KEYRLS", "KP7_released",),
	("KBDKP8_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP8", "KEYHLD", "KP8_held",),
	("KBDKP8_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP8", "KEYPRS", "KP8_pressed",),
	("KBDKP8_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP8", "KEYRLS", "KP8_released",),
	("KBDKP9_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP9", "KEYHLD", "KP9_held",),
	("KBDKP9_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP9", "KEYPRS", "KP9_pressed",),
	("KBDKP9_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KP9", "KEYRLS", "KP9_released",),
	("KBDKPCOMMA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPCOMMA", "KEYHLD", "KPCOMMA_held",),
	("KBDKPCOMMA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPCOMMA", "KEYPRS", "KPCOMMA_pressed",),
	("KBDKPCOMMA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPCOMMA", "KEYRLS", "KPCOMMA_released",),
	("KBDKPDOT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPDOT", "KEYHLD", "KPDOT_held",),
	("KBDKPDOT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPDOT", "KEYPRS", "KPDOT_pressed",),
	("KBDKPDOT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPDOT", "KEYRLS", "KPDOT_released",),
	("KBDKPENTER_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPENTER", "KEYHLD", "KPENTER_held",),
	("KBDKPENTER_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPENTER", "KEYPRS", "KPENTER_pressed",),
	("KBDKPENTER_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPENTER", "KEYRLS", "KPENTER_released",),
	("KBDKPJPCOMMA_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPJPCOMMA", "KEYHLD", "KPJPCOMMA_held",),
	("KBDKPJPCOMMA_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPJPCOMMA", "KEYPRS", "KPJPCOMMA_pressed",),
	("KBDKPJPCOMMA_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPJPCOMMA", "KEYRLS", "KPJPCOMMA_released",),
	("KBDKPRPAREN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPRIGHTPAREN", "KEYHLD", "KPRPAREN_held",),
	("KBDKPRPAREN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPRIGHTPAREN", "KEYPRS", "KPRPAREN_pressed",),
	("KBDKPRPAREN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPRIGHTPAREN", "KEYRLS", "KPRPAREN_released",),
	("KBDKPSLASH_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPSLASH", "KEYHLD", "KPSLASH_held",),
	("KBDKPSLASH_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPSLASH", "KEYPRS", "KPSLASH_pressed",),
	("KBDKPSLASH_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPSLASH", "KEYRLS", "KPSLASH_released",),
	("KBDK_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_K", "KEYHLD", "K_held",),
	("KBDK_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_K", "KEYPRS", "K_pressed",),
	("KBDK_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_K", "KEYRLS", "K_released",),
	("KBDLT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFT", "KEYHLD", "LEFT_held",),
	("KBDLT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFT", "KEYPRS", "LEFT_pressed",),
	("KBDLT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFT", "KEYRLS", "LEFT_released",),
	("KBDL_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_L", "KEYHLD", "L_held",),
	("KBDL_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_L", "KEYPRS", "L_pressed",),
	("KBDL_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_L", "KEYRLS", "L_released",),
	("KBDMETALT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTMETA", "KEYHLD", "LMETA_held",),
	("KBDMETALT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTMETA", "KEYPRS", "LMETA_pressed",),
	("KBDMETALT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTMETA", "KEYRLS", "LMETA_released",),
	("KBDMETART_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTMETA", "KEYHLD", "RMETA_held",),
	("KBDMETART_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTMETA", "KEYPRS", "RMETA_pressed",),
	("KBDMETART_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTMETA", "KEYRLS", "RMETA_released",),
	("KBDMINUSKP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPMINUS", "KEYHLD", "KPMINUS_held",),
	("KBDMINUSKP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPMINUS", "KEYPRS", "KPMINUS_pressed",),
	("KBDMINUSKP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPMINUS", "KEYRLS", "KPMINUS_released",),
	("KBDMINUS_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MINUS", "KEYHLD", "MINUS_held",),
	("KBDMINUS_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MINUS", "KEYPRS", "MINUS_pressed",),
	("KBDMINUS_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MINUS", "KEYRLS", "MINUS_released",),
	("KBDMUHENKAN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MUHENKAN", "KEYHLD", "MUHENKAN_held",),
	("KBDMUHENKAN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MUHENKAN", "KEYPRS", "MUHENKAN_pressed",),
	("KBDMUHENKAN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MUHENKAN", "KEYRLS", "MUHENKAN_released",),
	("KBDMUTE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MUTE", "KEYHLD", "MUTE_held",),
	("KBDMUTE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MUTE", "KEYPRS", "MUTE_pressed",),
	("KBDMUTE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_MUTE", "KEYRLS", "MUTE_released",),
	("KBDM_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_M", "KEYHLD", "M_held",),
	("KBDM_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_M", "KEYPRS", "M_pressed",),
	("KBDM_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_M", "KEYRLS", "M_released",),
	("KBDNEXTSONG_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_NEXTSONG", "KEYHLD", "NEXTSONG_held",),
	("KBDNEXTSONG_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_NEXTSONG", "KEYPRS", "NEXTSONG_pressed",),
	("KBDNEXTSONG_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_NEXTSONG", "KEYRLS", "NEXTSONG_released",),
	("KBDNUMLK_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_NUMLOCK", "KEYHLD", "NUMLOCK_held",),
	("KBDNUMLK_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_NUMLOCK", "KEYPRS", "NUMLOCK_pressed",),
	("KBDNUMLK_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_NUMLOCK", "KEYRLS", "NUMLOCK_released",),
	("KBDN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_N", "KEYHLD", "DOWN_held",),
	("KBDN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_N", "KEYPRS", "DOWN_pressed",),
	("KBDN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_N", "KEYRLS", "DOWN_released",),
	("KBDOPEN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_OPEN", "KEYHLD", "OPEN_held",),
	("KBDOPEN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_OPEN", "KEYPRS", "OPEN_pressed",),
	("KBDOPEN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_OPEN", "KEYRLS", "OPEN_released",),
	("KBDO_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_O", "KEYHLD", "O_held",),
	("KBDO_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_O", "KEYPRS", "O_pressed",),
	("KBDO_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_O", "KEYRLS", "O_released",),
	("KBDPARENLT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPLEFTPAREN", "KEYHLD", "KPLPAREN_held",),
	("KBDPARENLT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPLEFTPAREN", "KEYPRS", "KPLPAREN_pressed",),
	("KBDPARENLT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPLEFTPAREN", "KEYRLS", "KPLPAREN_released",),
	("KBDPASTE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PASTE", "KEYHLD", "PASTE_held",),
	("KBDPASTE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PASTE", "KEYPRS", "PASTE_pressed",),
	("KBDPASTE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PASTE", "KEYRLS", "PASTE_released",),
	("KBDPAUSE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAUSE", "KEYHLD", "PAUSE_held",),
	("KBDPAUSE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAUSE", "KEYPRS", "PAUSE_pressed",),
	("KBDPAUSE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAUSE", "KEYRLS", "PAUSE_released",),
	("KBDPGDN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAGEDOWN", "KEYHLD", "PGDN_held",),
	("KBDPGDN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAGEDOWN", "KEYPRS", "PGDN_pressed",),
	("KBDPGDN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAGEDOWN", "KEYRLS", "PGDN_released",),
	("KBDPGUP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAGEUP", "KEYHLD", "PGUP_held",),
	("KBDPGUP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAGEUP", "KEYPRS", "PGUP_pressed",),
	("KBDPGUP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PAGEUP", "KEYRLS", "PGUP_released",),
	("KBDPLAYPAUSE_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PLAYPAUSE", "KEYHLD", "PLAY_held",),
	("KBDPLAYPAUSE_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PLAYPAUSE", "KEYPRS", "PLAY_pressed",),
	("KBDPLAYPAUSE_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PLAYPAUSE", "KEYRLS", "PLAY_released",),
	("KBDPLUS_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPPLUS", "KEYHLD", "KPPLUS_held",),
	("KBDPLUS_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPPLUS", "KEYPRS", "KPPLUS_pressed",),
	("KBDPLUS_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPPLUS", "KEYRLS", "KPPLUS_released",),
	("KBDPOWER_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_POWER", "KEYHLD", "POWER_held",),
	("KBDPOWER_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_POWER", "KEYPRS", "POWER_pressed",),
	("KBDPOWER_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_POWER", "KEYRLS", "POWER_released",),
	("KBDPREVIOUSSONG_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PREVIOUSSONG", "KEYHLD", "PREVSONG_held",),
	("KBDPREVIOUSSONG_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PREVIOUSSONG", "KEYPRS", "PREVSONG_pressed",),
	("KBDPREVIOUSSONG_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PREVIOUSSONG", "KEYRLS", "PREVSONG_released",),
	("KBDPROPS_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PROPS", "KEYHLD", "PROPS_held",),
	("KBDPROPS_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PROPS", "KEYPRS", "PROPS_pressed",),
	("KBDPROPS_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_PROPS", "KEYRLS", "PROPS_released",),
	("KBDP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_P", "KEYPRS", "P_pressed",),
	("KBDP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_P", "KEYRLS", "P_released",),
	("KBDP_RLSHLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_P", "KEYHLD", "P_held",),
	("KBDQ_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Q", "KEYHLD", "Q_held",),
	("KBDQ_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Q", "KEYPRS", "Q_pressed",),
	("KBDQ_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Q", "KEYRLS", "Q_released",),
	("KBDREFRESH_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_REFRESH", "KEYHLD", "REFRESH_held",),
	("KBDREFRESH_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_REFRESH", "KEYPRS", "REFRESH_pressed",),
	("KBDREFRESH_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_REFRESH", "KEYRLS", "REFRESH_released",),
	("KBDRO_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RO", "KEYHLD", "RO_held",),
	("KBDRO_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RO", "KEYPRS", "RO_pressed",),
	("KBDRO_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RO", "KEYRLS", "RO_released",),
	("KBDRT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHT", "KEYHLD", "RIGHT_held",),
	("KBDRT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHT", "KEYPRS", "RIGHT_pressed",),
	("KBDRT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHT", "KEYRLS", "RIGHT_released",),
	("KBDR_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_R", "KEYHLD", "R_HELD",),
	("KBDR_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_R", "KEYPRS", "R_pressed",),
	("KBDR_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_R", "KEYRLS", "R_released",),
	("KBDSCROLLDN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLDOWN", "KEYHLD", "SCROLLDOWN_held",),
	("KBDSCROLLDN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLDOWN", "KEYPRS", "SCROLLDOWN_pressed",),
	("KBDSCROLLDN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLDOWN", "KEYRLS", "SCROLLDOWN_released",),
	("KBDSCROLLLK_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLLOCK", "KEYHLD", "SCROLLLOCK_held",),
	("KBDSCROLLLK_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLLOCK", "KEYPRS", "SCROLLLOCK_pressed",),
	("KBDSCROLLLK_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLLOCK", "KEYRLS", "SCROLLLOCK_released",),
	("KBDSCROLLUP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLUP", "KEYHLD", "SCROLLUP_held",),
	("KBDSCROLLUP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLUP", "KEYPRS", "SCROLLUP_pressed",),
	("KBDSCROLLUP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SCROLLUP", "KEYRLS", "SCROLLUP_released",),
	("KBDSEMICOLON_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SEMICOLON", "KEYHLD", "SEMICOLON_held",),
	("KBDSEMICOLON_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SEMICOLON", "KEYPRS", "SEMICOLON_pressed",),
	("KBDSEMICOLON_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SEMICOLON", "KEYRLS", "SEMICOLON_released",),
	("KBDSHIFTLT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTSHIFT", "KEYHLD", "LSHIFT_held",),
	("KBDSHIFTLT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTSHIFT", "KEYPRS", "LSHIFT_pressed",),
	("KBDSHIFTLT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_LEFTSHIFT", "KEYRLS", "LSHIFT_released",),
	("KBDSHIFTRT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTSHIFT", "KEYHLD", "RSHIFT_held",),
	("KBDSHIFTRT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTSHIFT", "KEYPRS", "RSHIFT_pressed",),
	("KBDSHIFTRT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_RIGHTSHIFT", "KEYRLS", "RSHIFT_released",),
	("KBDSLASH_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SLASH", "KEYHLD", "SLASH_held",),
	("KBDSLASH_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SLASH", "KEYPRS", "SLASH_pressed",),
	("KBDSLASH_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SLASH", "KEYRLS", "SLASH_released",),
	("KBDSLEEP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SLEEP", "KEYHLD", "SLEEP_held",),
	("KBDSLEEP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SLEEP", "KEYPRS", "SLEEP_pressed",),
	("KBDSLEEP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SLEEP", "KEYRLS", "SLEEP_released",),
	("KBDSPC_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SPACE", "KEYHLD", "SPACE_held",),
	("KBDSPC_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SPACE", "KEYPRS", "SPACE_pressed",),
	("KBDSPC_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SPACE", "KEYRLS", "SPACE_released",),
	("KBDSPLAT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPASTERISK", "KEYHLD", "KPSPLAT_held",),
	("KBDSPLAT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPASTERISK", "KEYPRS", "KPSPLAT_pressed",),
	("KBDSPLAT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_KPASTERISK", "KEYRLS", "KPSPLAT_released",),
	("KBDSTOPCD_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_STOPCD", "KEYHLD", "STOPCD_held",),
	("KBDSTOPCD_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_STOPCD", "KEYPRS", "STOPCD_pressed",),
	("KBDSTOPCD_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_STOPCD", "KEYRLS", "STOPCD_released",),
	("KBDSTOP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_STOP", "KEYHLD", "STOP_held",),
	("KBDSTOP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_STOP", "KEYPRS", "STOP_pressed",),
	("KBDSTOP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_STOP", "KEYRLS", "STOP_released",),
	("KBDSYSRQ_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SYSRQ", "KEYHLD", "SYSREQ_held",),
	("KBDSYSRQ_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SYSRQ", "KEYPRS", "SYSREQ_pressed",),
	("KBDSYSRQ_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_SYSRQ", "KEYRLS", "SYSREQ_released",),
	("KBDS_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_S", "KEYHLD", "S_held",),
	("KBDS_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_S", "KEYPRS", "S_pressed",),
	("KBDS_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_S", "KEYRLS", "S_released",),
	("KBDTAB_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_TAB", "KEYHLD", "TAB_held",),
	("KBDTAB_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_TAB", "KEYPRS", "TAB_pressed",),
	("KBDTAB_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_TAB", "KEYRLS", "TAB_released",),
	("KBDT_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_T", "KEYHLD", "T_held",),
	("KBDT_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_T", "KEYPRS", "T_pressed",),
	("KBDT_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_T", "KEYRLS", "T_released",),
	("KBDUNDO_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UNDO", "KEYHLD", "UNDO_held",),
	("KBDUNDO_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UNDO", "KEYPRS", "UNDO_pressed",),
	("KBDUNDO_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UNDO", "KEYRLS", "UNDO_released",),
	("KBDUNKNOWN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UNKNOWN", "KEYHLD", "UNKNOW_held",),
	("KBDUNKNOWN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UNKNOWN", "KEYPRS", "UNKNOW_pressed",),
	("KBDUNKNOWN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UNKNOWN", "KEYRLS", "UNKNOW_released",),
	("KBDUP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UP", "KEYHLD", "UP_held",),
	("KBDUP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UP", "KEYPRS", "UP_pressed",),
	("KBDUP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_UP", "KEYRLS", "UP_released",),
	("KBDU_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_U", "KEYHLD", "U_held",),
	("KBDU_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_U", "KEYPRS", "U_pressed",),
	("KBDU_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_U", "KEYRLS", "U_released",),
	("KBDVOLDN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_VOLUMEDOWN", "KEYHLD", "VOLDN_held",),
	("KBDVOLDN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_VOLUMEDOWN", "KEYPRS", "VOLDN_pressed",),
	("KBDVOLDN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_VOLUMEDOWN", "KEYRLS", "VOLDN_released",),
	("KBDVOLUP_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_VOLUMEUP", "KEYHLD", "VOLUP_held",),
	("KBDVOLUP_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_VOLUMEUP", "KEYPRS", "VOLUP_pressed",),
	("KBDVOLUP_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_VOLUMEUP", "KEYRLS", "VOLUP_released",),
	("KBDV_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_V", "KEYHLD", "V_held",),
	("KBDV_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_V", "KEYPRS", "V_pressed",),
	("KBDV_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_V", "KEYRLS", "V_released",),
	("KBDWWW_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_WWW", "KEYHLD", "WWW_held",),
	("KBDWWW_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_WWW", "KEYPRS", "WWW_pressed",),
	("KBDWWW_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_WWW", "KEYRLS", "WWW_released",),
	("KBDW_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_W", "KEYHLD", "W_held",),
	("KBDW_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_W", "KEYPRS", "W_pressed",),
	("KBDW_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_W", "KEYRLS", "W_released",),
	("KBDX_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_X", "KEYHLD", "X_held",),
	("KBDX_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_X", "KEYPRS", "X_pressed",),
	("KBDX_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_X", "KEYRLS", "X_released",),
	("KBDYEN_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_YEN", "KEYHLD", "YEN_held",),
	("KBDYEN_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_YEN", "KEYPRS", "YEN_pressed",),
	("KBDYEN_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_YEN", "KEYRLS", "YEN_released",),
	("KBDY_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Y", "KEYHLD", "Y_held",),
	("KBDY_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Y", "KEYPRS", "Y_pressed",),
	("KBDY_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Y", "KEYRLS", "Y_released",),
	("KBDZENKAKUHANKAKU_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ZENKAKUHANKAKU", "KEYHLD", "ZENKAKUHANKAKU_held",),
	("KBDZENKAKUHANKAKU_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ZENKAKUHANKAKU", "KEYPRS", "ZENKAKUHANKAKU_pressed",),
	("KBDZENKAKUHANKAKU_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_ZENKAKUHANKAKU", "KEYRLS", "ZENKAKUHANKAKU_released",),
	("KBDZ_HLD", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Z", "KEYHLD", "Z_held",),
	("KBDZ_PRS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Z", "KEYPRS", "Z_pressed",),
	("KBDZ_RLS", FMAXDO_SCTN42LDIEKEYDEF, "KEY_Z", "KEYRLS", "Z_released",),
	("MSEBTNBAK_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_BACK", "KEYPRS", "MSEBTNBAK_held",),
	("MSEBTNBAK_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_BACK", "KEYPRSHLD", "MSEBTNBAK_pressedHeld",),
	("MSEBTNBAK_PSR", FMAXDO_SCTN42LDIEBTNDEF, "BTN_BACK", "KEYPRS", "MSEBTNBAK_pressed",),
	("MSEBTNBAK_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_BACK", "KEYRLS", "MSEBTNBAK_released",),
	("MSEBTNFWD_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_FORWARD", "KEYHLD", "MSEBTNFWD_held",),
	("MSEBTNFWD_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_FORWARD", "KEYPRS", "MSEBTNFWD_pressed",),
	("MSEBTNFWD_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_FORWARD", "KEYPRSHLD", "MSEBTNFWD_pressedHeld",),
	("MSEBTNFWD_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_FORWARD", "KEYRLS", "MSEBTNFWD_released",),
	("MSEBTNLT_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_LEFT", "KEYHLD", "MSE left BTN held",),
	("MSEBTNLT_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_LEFT", "KEYPRS", "MSEBTNLEFT_pressed",),
	("MSEBTNLT_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_LEFT", "KEYPRSHLD", "MSEBTNLEFT_pressedHeld",),
	("MSEBTNLT_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_LEFT", "KEYRLS", "MSEBTNLEFT_released",),
	("MSEBTNMID_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MIDDLE", "KEYHLD", "MSEBTNMID_held",),
	("MSEBTNMID_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MIDDLE", "KEYPRS", "MSEBTNMID_pressed",),
	("MSEBTNMID_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MIDDLE", "KEYPRSHLD", "MSEBTNMID_pressedHeld",),
	("MSEBTNMID_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_MIDDLE", "KEYRLS", "MSEBTNMID_released",),
	("MSEBTNRT_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_RIGHT", "KEYHLD", "MSEBTNRIGHT_held",),
	("MSEBTNRT_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_RIGHT", "KEYPRS", "MSEBTNRIGHT_pressed",),
	("MSEBTNRT_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_RIGHT", "KEYPRSHLD", "MSEBTNRIGHT_pressedHeld",),
	("MSEBTNRT_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_RIGHT", "KEYRLS", "MSEBTNRIGHT_released",),
	("MSEBTNSIDE_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SIDE", "KEYHLD", "MSEBTNSIDE_held",),
	("MSEBTNSIDE_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SIDE", "KEYPRS", "MSEBTNSIDE_pressedHeld",),
	("MSEBTNSIDE_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SIDE", "KEYPRSHLD", "MSEBTNSIDE_pressed",),
	("MSEBTNSIDE_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_SIDE", "KEYRLS", "MSEBTNSIDE_released",),
	("MSEBTNTASK_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TASK", "KEYHLD", "MSEBTNTASK_held",),
	("MSEBTNTASK_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TASK", "KEYPRS", "MSEBTNTASK_pressedHeld",),
	("MSEBTNTASK_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TASK", "KEYPRSHLD", "MSEBTNTASK_pressed",),
	("MSEBTNTASK_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_TASK", "KEYRLS", "MSEBTNTASK_released",),
	("MSEBTNXTRA_HLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EXTRA", "KEYHLD", "MSEBTNEXTRA_held",),
	("MSEBTNXTRA_PRS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EXTRA", "KEYPRS", "MSEBTNEXTRA_pressed",),
	("MSEBTNXTRA_PRSHLD", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EXTRA", "KEYPRSHLD", "MSEBTNEXTRA_pressedHeld",),
	("MSEBTNXTRA_RLS", FMAXDO_SCTN42LDIEBTNDEF, "BTN_EXTRA", "KEYRLS", "MSEBTNEXTRA_released",),
	("MSEHRWHL_DN", FMAXDO_SCTN42LDIERELDEF, "REL_WHEEL_HI_RES", "-WHEELDISTANCE", "move HR MSE WHL down WHEELDISTANCE ticks",),
	("MSEHRWHL_LT", FMAXDO_SCTN42LDIERELDEF, "REL_HWHEEL_HI_RES", "-WHEELDISTANCE", "move HR MSE WHL left WHEELDISTANCE ticks",),
	("MSEHRWHL_RT", FMAXDO_SCTN42LDIERELDEF, "REL_HWHEEL_HI_RES", "WHEELDISTANCE", "move HR MSE WHL right WHEELDISTANCE ticks",),
	("MSEHRWHL_UP", FMAXDO_SCTN42LDIERELDEF, "REL_WHEEL_HI_RES", "WHEELDISTANCE", "move HR MSE WHL up WHEELDISTANCE ticks",),
	("MSEWHL_DN", FMAXDO_SCTN42LDIERELDEF, "REL_WHEEL", "-WHEELDISTANCE", "move MSE WHL down WHEELDISTANCE",),
	("MSEWHL_LT", FMAXDO_SCTN42LDIERELDEF, "REL_HWHEEL", "-WHEELDISTANCE", "move MSE WHL left WHEELDISTANCE",),
	("MSEWHL_RT", FMAXDO_SCTN42LDIERELDEF, "REL_HWHEEL", "WHEELDISTANCE", "move MSE WHL right WHEELDISTANCE",),
	("MSEWHL_UP", FMAXDO_SCTN42LDIERELDEF, "REL_WHEEL", "WHEELDISTANCE", "move MSE WHL up WHEELDISTANCE",),
	("MSE_DN", FMAXDO_SCTN42LDIERELDEF, "REL_Y", "MOUSEDISTANCE", "how far to move the mouse per event",),
	("MSE_LT", FMAXDO_SCTN42LDIERELDEF, "REL_X", "-MOUSEDISTANCE", "move MSE left -MOUSEDISTANCE",),
	("MSE_RT", FMAXDO_SCTN42LDIERELDEF, "REL_X", "MOUSEDISTANCE", "move mouse right MOUSEDISTANCE",),
	("MSE_UP", FMAXDO_SCTN42LDIERELDEF, "REL_Y", "-MOUSEDISTANCE", "move mouse up MOUSEDISTANCE",),
	("SYNREPORT", FMAXDO_SCTN42LDIESYNDEF, "SYN_REPORT", "0", "send a sync report 0",),
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1
]
TBGLST.sort()


# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# END OF TBGLST
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!
# !_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!_!


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAComment(comment_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += CMNTLINE + NEWLINE
	strToRtn_ += f"# * {comment_}" + NEWLINE
	strToRtn_ += CMNTLINE + NEWLINE
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# readFileToStr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def readFileToStr(FILENAME_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	with open(FILENAME_, "tr") as FDIN:
		strToRtn_ += FDIN.read()
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# copied sections
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


DO_TOP = f"""{NEWLINE}{NEWLINE}{makeAComment("SCTN40 start of CF.py")}#
from libevdev import InputEvent as IE
import fcntl
import libevdev as LD
import os
{NEWLINE}
import CF
{NEWLINE}{NEWLINE}{makeAComment("included modules")}#
# * def fixBtn(DEVTCode_):
# * def fixEvent(thisDevice_, eventToFix_):
# * def isMatch(eventCD1_, eventCD2_):
# * def openOutputDevice(lookingForDeviceName_):
# * def SPCL_(spclEvent_, spclVal_):
{NEWLINE}{NEWLINE}"""


FM_TOP = f"""#!/usr/bin/python{NEWLINE}{NEWLINE}{readFileToStr(SCTNSNAME)}{NEWLINE}{NEWLINE}
{makeAComment("modules defined in this file")}#
# * def doErrorItem(message_, itemToError_):
# * def explodeItem(itemToExplode_):
# * def makeAComment(comment_):
# * def makeCF():
# * def makeDO():
# * def makeFM():
# * def parseTBGLST():
# * def readFileToStr(FILENAME_):
# * def __main__():{NEWLINE}{NEWLINE}
"""


HBI_TOP = f"""#{NEWLINE}#{NEWLINE}{makeAComment("SCTN50 start of HBI")}from time import sleep{NEWLINE}#
import libevdev as LD{NEWLINE}{NEWLINE}
def IDB():
{NTAB(1)}devHBI = LD.Device()
{NTAB(1)}devHBI.name = "HBI hot beef injector"
"""


HBI_BTM = f"""{NTAB(1)}hbiDevice = devHBI.create_uinput_device()
	print(f"New device at {OBRCE}hbiDevice.devnode{CBRCE} ({OBRCE}hbiDevice.syspath{CBRCE})")
	sleep(1)
	return hbiDevice{NEWLINE}{NEWLINE}#{NEWLINE}#{NEWLINE}{makeAComment("end of HBI.py")}{NEWLINE}
"""


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# make C.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeCF():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += readFileToStr(CFTOP_NAME)
	strToRtn_ += readFileToStr(SCTN0102NAME)
	strToRtn_ += f"{NEWLINE}{NEWLINE}"

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN21 CF defines")
	for name_, value_ in FMCF_SCTN21DEFDICT.items():
		strToRtn_ += f"{name_} = {value_}  # {FMCF_SCTN21DEFCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += f"{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"""{makeAComment("SCTN22 options structures")}PARMSDICT = {OBRCE}{NEWLINE}"""
	for name_, value_ in FMCF_SCTN22PARMSDICT.items():
		strToRtn_ += f"{value_}"
	strToRtn_ += f"{CBRCE}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"OPTIONSDICT = {OBRCE}{NEWLINE}"
	for name_, value_ in FMCF_SCTN22OPTIONSDICT.items():
		strToRtn_ += f"{value_}"
	strToRtn_ += f"""{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"""
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	strToRtn_ += f"{readFileToStr(CFBTM_NAME)}"
	return strToRtn_

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeDO
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeDO():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += DO_TOP

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN41 device defines")
	for name_, value_ in FMDO_SCTN41DEVICEDEFDICT.items():
		strToRtn_ += f"{value_}  # {FMDO_SCTN41DEVICEDEFCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += f"""{NEWLINE}{NEWLINE}{makeAComment("SCTN47 buttons lists")}BTNSHOLDABLELIST = {OBRKT}{NEWLINE}"""
	for item_ in BTNSHOLDABLELIST:
		strToRtn_ += f"{NTAB(1)}{item_},{NEWLINE}"
	strToRtn_ += f"{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN42 LDIE entries")
	for name_, value_ in FMDO_SCTN42LDIEDICT.items():
		strToRtn_ += f"{name_} = {value_}  # {FMDO_SCTN42LDIECMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += f"{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"SPCLAXLIST = {OBRKT}{NEWLINE}"
	for thisItem_ in FMDO_SCTN42LDIESPCLLIST:
		strToRtn_ += f"{NTAB(1)}{thisItem_},  # {FMDO_SCTN42LDIECMNTDICT[thisItem_]}{NEWLINE}"
	strToRtn_ += f"{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN43 actions to output entries")
	strToRtn_ += f"ACTIONS = {OBRCE}{NEWLINE}"
	for name_, value_ in FMDO_SCTN43AXDEFDICT.items():
		strToRtn_ += f"{NTAB(1)}{name_}: {OBRKT}  # {FMDO_SCTN43AXDEFCMNTDICT[name_]}{NEWLINE}{value_}{NTAB(1)}{CBRKT},{NEWLINE}{NEWLINE}"
	strToRtn_ += f"{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN48 device code list and dict")
	for name_, item_ in FMDO_SCTN48DEFDICT.items():
		strToRtn_ += f"{item_}  # {FMDO_SCTN48DEFCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += f"{NEWLINE}{NEWLINE}"
	strToRtn1_ = ""
	strToRtn2_ = ""
	strToRtn1_ += f"DEVTLIST = {OBRKT}{NEWLINE}"
	strToRtn2_ += f"DEVTDICT = {OBRCE}{NEWLINE}"
	for name_, values_ in FMDO_SCTN48TYPESDICT.items():
		strToRtn1_ += f"{NTAB(1)}{name_},  # {FMDO_SCTN48TYPESCMNTDICT[name_]}{NEWLINE}"
		strToRtn2_ += f"{NTAB(1)}{name_}: {OBRKT}  # {FMDO_SCTN48TYPESCMNTDICT[name_]}{NEWLINE}"
		for thisValue_ in values_:
			strToRtn2_ += f"{NTAB(2)}{thisValue_}{NEWLINE}"
		strToRtn2_ += f"{NTAB(1)}{CBRKT},{NEWLINE}"
	strToRtn1_ += f"{CBRKT}{NEWLINE}{NEWLINE}{NEWLINE}"
	strToRtn2_ += f"{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"
	strToRtn_ += strToRtn1_
	strToRtn_ += strToRtn2_
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN44 filled and empty device entries")
	strToRtn1_ = ""
	strToRtn_ += f"DEVICES = {OBRCE}  # define SCTN44 DEVICES{NEWLINE}"
	for name_, value_ in FMDO_SCTN44DEVICESDICT.items():
		strToRtn1_ += f"{NTAB(1)}{name_}: {OBRCE}  # {FMDO_SCTN41DEVICEDEFCMNTDICT[name_]}{NEWLINE}"
		for name1_, value1_ in value_.items():
			strToRtn1_ += f"{NTAB(2)}{name1_}: {value1_}, {NEWLINE}"
		strToRtn1_ += f"{NTAB(1)}{CBRCE},{NEWLINE}"
	strToRtn1_ += f"{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"
	strToRtn_ += strToRtn1_
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"""{makeAComment("SCTN45 device profile and REPEATDICT")}PROFILE = {OBRCE}  # device profile defined{NEWLINE}"""
	strToRtn1_ = f"""REPEATDICT = {OBRCE}{NEWLINE}"""
	strToRtn2_ = f"""BTNTYPEDICT = {OBRCE}{NEWLINE}"""
	for thisDEV_MYNAME_, thisVal1_ in FMDO_SCTN45PROFDICT.items():
		# ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1
		strToRtn_ += f"{NTAB(1)}{thisDEV_MYNAME_}: {OBRCE}{NEWLINE}"
		strToRtn1_ += f"{NTAB(1)}{thisDEV_MYNAME_}: {OBRCE}{NEWLINE}"
		strToRtn2_ += f"{NTAB(1)}{thisDEV_MYNAME_}: {OBRCE}{NEWLINE}"
		for thisBTNName1_, thisVal2_ in thisVal1_.items():
			# ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2
			if thisBTNName1_ not in BTNSHOLDABLELIST:
				# ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3
				strToRtn_ += f"{NTAB(2)}{thisBTNName1_}: {thisVal2_}{NEWLINE}"
				strToRtn1_ += f"""{NTAB(2)}{thisBTNName1_}: {FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisBTNName1_]}{NEWLINE}"""
				strToRtn2_ += f"""{NTAB(2)}{thisBTNName1_}: {FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisBTNName1_]}{NEWLINE}"""
				# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
			elif thisBTNName1_ in BTNSHOLDABLELIST:
				# ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3
				strToRtn_ += f"{NTAB(2)}{thisBTNName1_}: {OBRCE}  # holdable button {thisBTNName1_}{NEWLINE}"
				strToRtn1_ += f"{NTAB(2)}{thisBTNName1_}: {OBRCE}  # holdable button {thisBTNName1_}{NEWLINE}"
				strToRtn2_ += f"{NTAB(2)}{thisBTNName1_}: {OBRCE}  # holdable button {thisBTNName1_}{NEWLINE}"
				for thisBTNName2_, thisVal3 in thisVal2_.items():
					# ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4
					if thisBTNName2_ not in BTNSHOLDABLELIST:
						# ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5
						strToRtn_ += f"{NTAB(3)}{thisBTNName2_}: {thisVal3}{NEWLINE}"
						strToRtn1_ += f"{NTAB(3)}{thisBTNName2_}: {FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisBTNName1_][thisBTNName2_]}{NEWLINE}"
						strToRtn2_ += f"{NTAB(3)}{thisBTNName2_}: {FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisBTNName1_][thisBTNName2_]}{NEWLINE}"
						# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5
					elif thisBTNName2_ in BTNSHOLDABLELIST:
						# ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5 ⥥5
						strToRtn_ += f"{NTAB(3)}{thisBTNName2_}: {OBRCE}  # holdable buttons {thisBTNName1_}:{thisBTNName2_}{NEWLINE}"
						strToRtn1_ += f"{NTAB(3)}{thisBTNName2_}: {OBRCE}  # holdable buttons {thisBTNName1_}:{thisBTNName2_}{NEWLINE}"
						strToRtn2_ += f"{NTAB(3)}{thisBTNName2_}: {OBRCE}  # holdable buttons {thisBTNName1_}:{thisBTNName2_}{NEWLINE}"
						for thisBTNName3_, thisAX_ in thisVal3.items():
							# ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6 ⥥6
							strToRtn_ += f"{NTAB(4)}{thisBTNName3_}: {thisAX_}{NEWLINE}"
							strToRtn1_ += f"{NTAB(4)}{thisBTNName3_}: {FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisBTNName1_][thisBTNName2_][thisBTNName3_]}{NEWLINE}"
							strToRtn2_ += f"{NTAB(4)}{thisBTNName3_}: {FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisBTNName1_][thisBTNName2_][thisBTNName3_]}{NEWLINE}"
							# ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6 ⥣6
						strToRtn_ += f"{NTAB(3)}{CBRCE},{NEWLINE}"
						strToRtn1_ += f"{NTAB(3)}{CBRCE},{NEWLINE}"
						strToRtn2_ += f"{NTAB(3)}{CBRCE},{NEWLINE}"
						# ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5 ⥣5
					# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
				strToRtn_ += f"{NTAB(2)}{CBRCE},{NEWLINE}"
				strToRtn1_ += f"{NTAB(2)}{CBRCE},{NEWLINE}"
				strToRtn2_ += f"{NTAB(2)}{CBRCE},{NEWLINE}"
				# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3
			# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
		strToRtn_ += f"{NTAB(1)}{CBRCE},{NEWLINE}"
		strToRtn1_ += f"{NTAB(1)}{CBRCE},{NEWLINE}"
		strToRtn2_ += f"{NTAB(1)}{CBRCE},{NEWLINE}"
	strToRtn_ += f"{CBRCE}{NEWLINE}{NEWLINE}{strToRtn1_}{CBRCE}{NEWLINE}{NEWLINE}{strToRtn2_}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"""{makeAComment("SCTN46 device XLATE table")}XLATETABLE = {OBRCE}{NEWLINE}"""
	for thisDEV_MYNAME_, entries_ in FMDO_SCTN46XLATEDICT.items():
		strToRtn_ += f"{NTAB(1)}{thisDEV_MYNAME_}: {OBRCE}{NEWLINE}{entries_}{NTAB(1)}{CBRCE},{NEWLINE}"
	strToRtn_ += f"{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"""{makeAComment("SCTN49 DIR to BTN SIM translation")}DIR2BTN = {OBRCE}{NEWLINE}"""
	for thisDEVT_, theseItems_ in FMDO_SCTN49DIRTRANSDICT.items():
		strToRtn_ += f"""{NTAB(1)}{thisDEVT_}: {OBRCE}  # {FMDO_SCTN49DIRTRANSCMNTDICT[thisDEVT_]}{NEWLINE}{theseItems_}{NTAB(1)}{CBRCE},{NEWLINE}"""
	strToRtn_ += f"{CBRCE}{NEWLINE}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	strToRtn_ += f"""#{NEWLINE}#{NEWLINE}{makeAComment("end of managed section of DO.py")}#{NEWLINE}#{NEWLINE}{NEWLINE}{NEWLINE}"""

	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeFM
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeFM():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += FM_TOP
	strToRtn_+= readFileToStr(SCTN0102NAME)

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN03 TYPEs and lambda")
	for name_, value_ in FMCF_SCTN03TYPEDICT.items():
		strToRtn_ += f"{name_} = {value_}  # {FMCF_SCTN03TYPECMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += NEWLINE + NEWLINE
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN04 BTNS")
	strToRtn1_ = ""
	for name_, value_ in FMDO_SCTN47BTNSDICT.items():
		strToRtn_ += f"{name_} = {DBLQT}{name_}{DBLQT}  # {FMDO_SCTN47BTNSCMNTDICT[name_]}{NEWLINE}"
		if value_ == "True":
			strToRtn1_ += f"{NTAB(1)}{name_},{NEWLINE}"
	strToRtn_ += f"{NEWLINE}{NEWLINE}BTNSHOLDABLELIST = {OBRKT}{NEWLINE}{strToRtn1_}{CBRKT}{NEWLINE}{NEWLINE}"
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN11 FMAX _DEF_")
	strToRtn01_ = ""
	for name_, value_ in FMFM_SCTN11AXDICT.items():
		strToRtn_ += f"{name_} = {value_}  # {FMFM_SCTN11AXCMNTDICT[name_]}{NEWLINE}"
		strToRtn01_ += f"{NTAB(1)}{name_},  # {FMFM_SCTN11AXCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += NEWLINE + NEWLINE
	strToRtn_ += f"FMAXFM_AXLST = {OBRKT}{NEWLINE}{strToRtn01_}{CBRKT}{NEWLINE}"
	strToRtn_ += NEWLINE + NEWLINE
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN12 VAL _DEF_")
	strToRtn01_ = ""
	for name_, value_ in FMFM_SCTN12VALDICT.items():
		strToRtn_ += f"{name_} = {OBRCE}{CBRCE}  # {FMFM_SCTN12VALCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += NEWLINE + NEWLINE
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN13 _DICT_ _DEF_")
	strToRtn01_ = ""
	for name_, value_ in FMFM_SCTN13DICTDICT.items():
		strToRtn_ += f"{name_} = {OBRCE}{CBRCE}  # {FMFM_SCTN13DICTCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += NEWLINE + NEWLINE
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += makeAComment("SCTN14 _LIST_ _DEF_")
	for name_, value_ in FMFM_SCTN14LISTDICT.items():
		strToRtn_ += f"{name_} = {value_}  # {FMFM_SCTN14LISTCMNTDICT[name_]}{NEWLINE}"
	strToRtn_ += NEWLINE + NEWLINE
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	strToRtn_ += f"""#{NEWLINE}#{NEWLINE}{makeAComment("end of managed portions of FM.py")}#{NEWLINE}#{NEWLINE}{NEWLINE}{NEWLINE}"""

	# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
	strToRtn_ += f"{NTAB(1)}global {BKSLSH}{NEWLINE}"
	for key_ in FMFM_SCTN13DICTDICT:
		strToRtn_ += f"{NTAB(2)}{key_}, {BKSLSH}{NEWLINE}"
	for key_ in FMFM_SCTN14LISTDICT:
		strToRtn_ += f"{NTAB(2)}{key_}, {BKSLSH}{NEWLINE}"
	strToRtn_ = strToRtn_[:-4] + NEWLINE
	# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeHBI
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeHBI():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"{HBI_TOP}"
	for item_ in FMHBI_SCTN50HBIABSLIST:
		strToRtn_ += f"{NTAB(1)}devHBI.enable{OPAREN}LD.EV_ABS.{item_}{NEWLINE}"
	for item_ in FMHBI_SCTN51HBIBTNLIST:
		strToRtn_ += f"{NTAB(1)}devHBI.enable{OPAREN}LD.EV_KEY.{item_}{NEWLINE}"
	for item_ in FMHBI_SCTN52HBIKEYLIST:
		strToRtn_ += f"{NTAB(1)}devHBI.enable{OPAREN}LD.EV_KEY.{item_}{NEWLINE}"
	for item_ in FMHBI_SCTN53HBIRELLIST:
		strToRtn_ += f"{NTAB(1)}devHBI.enable{OPAREN}LD.EV_REL.{item_}{NEWLINE}"
	strToRtn_ += f"{HBI_BTM}"
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doErrorItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doErrorItem(message_, itemToError_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	print(f"""
{message_}
is a tuple {isinstance(itemToError_, tuple)}
item as parsed
{repr(itemToError_)}
""")
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# explodeItem
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def explodeItem(itemToExplode_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	strToRtn_ = ""
	strToRtn_ += f"{NTAB(1)}{OPAREN}{DBLQT}{itemToExplode_[0]}{DBLQT}, {itemToExplode_[1]}, "
	for TI1_ in range(2, len(itemToExplode_)):
		strToRtn_ += f"{DBLQT}{itemToExplode_[TI1_]}{DBLQT}, "
	strToRtn_ = strToRtn_[:-1] + f"{CPAREN},{NEWLINE}"
	return strToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# parseTBGLST
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def parseTBGLST(FDTBGLST):
	global \
		FMCF_SCTN03TYPECMNTDICT, \
		FMCF_SCTN03TYPEDICT, \
		FMCF_SCTN21DEFCMNTDICT, \
		FMCF_SCTN21DEFDICT, \
		FMCF_SCTN22OPTIONSCMNTDICT, \
		FMCF_SCTN22OPTIONSDICT, \
		FMCF_SCTN22PARMSCMNTDICT, \
		FMCF_SCTN22PARMSDICT, \
		FMCF_SCTN23DICTCMNTDICT, \
		FMCF_SCTN23DICTDICT, \
		FMCF_SCTN24LISTCMNTDICT, \
		FMCF_SCTN24LISTDICT, \
		FMDO_SCTN41DEVICEDEFCMNTDICT, \
		FMDO_SCTN41DEVICEDEFDICT, \
		FMDO_SCTN42LDIECMNTDICT, \
		FMDO_SCTN42LDIEDICT, \
		FMDO_SCTN43AXDEFCMNTDICT, \
		FMDO_SCTN43AXDEFDICT, \
		FMDO_SCTN44DEVICESCMNTDICT, \
		FMDO_SCTN44DEVICESDICT, \
		FMDO_SCTN45BTNTYPEDICT, \
		FMDO_SCTN45PROFDICT, \
		FMDO_SCTN45RPTDICT, \
		FMDO_SCTN46XLATECMNTDICT, \
		FMDO_SCTN46XLATEDICT, \
		FMDO_SCTN47BTNSCMNTDICT, \
		FMDO_SCTN47BTNSDICT, \
		FMDO_SCTN48DEFCMNTDICT, \
		FMDO_SCTN48DEFDICT, \
		FMDO_SCTN48TYPESCMNTDICT, \
		FMDO_SCTN48TYPESDICT, \
		FMDO_SCTN49DIRTRANSCMNTDICT, \
		FMDO_SCTN49DIRTRANSDICT, \
		FMFM_SCTN11AXCMNTDICT, \
		FMFM_SCTN11AXDICT, \
		FMFM_SCTN12VALCMNTDICT, \
		FMFM_SCTN12VALDICT, \
		FMFM_SCTN13DICTCMNTDICT, \
		FMFM_SCTN13DICTDICT, \
		FMFM_SCTN14LISTCMNTDICT, \
		FMFM_SCTN14LISTDICT, \
		FMDO_SCTN42LDIESPCLLIST, \
		FMDO_SCTN47BTNSHOLDABLELIST, \
		FMHBI_SCTN50HBIABSLIST, \
		FMHBI_SCTN51HBIBTNLIST, \
		FMHBI_SCTN52HBIKEYLIST, \
		FMHBI_SCTN53HBIRELLIST
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	for thisItem_ in TBGLST:
		FDTBGLST.write(f"{explodeItem(thisItem_)}")
		thisItemLen_ = len(thisItem_)
		if thisItemLen_ < 3:
			doErrorItem("fewer than 3 elements", thisItem_)
			continue
		if not isinstance(thisItem_, tuple):
			doErrorItem("not a tuple", thisItem_)
			continue
		thisName_ = thisItem_[0]
		thisAX_ = thisItem_[1]
		thisComment_ = thisItem_[-1]
		if thisAX_ not in FMAXFM_AXLST:
			doErrorItem("not a supported action in FM", thisItem_)
			continue
		if thisAX_ is None:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN03LAMBDADEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisLambdaName_ = thisItem_[2]
			thisLambdaVal_ = thisItem_[3]
			FMCF_SCTN03TYPEDICT[thisLambdaName_] = f"lambda {thisLambdaVal_}"
			FMCF_SCTN03TYPECMNTDICT[thisLambdaName_] = "{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN03TYPEDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisTypeName_ = thisItem_[2]
			thisType_ = thisItem_[3]
			FMCF_SCTN03TYPEDICT[thisTypeName_] = f"{DBLQT}{thisType_}{DBLQT}"
			FMCF_SCTN03TYPECMNTDICT[thisTypeName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN21STRDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN21DEFDICT[thisValName_] = f"{DBLQT}{thisVal_}{DBLQT}"
			FMCF_SCTN21DEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN21VALDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN21DEFDICT[thisValName_] = f"{thisVal_}"
			FMCF_SCTN21DEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN22PARMDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisParam_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN22PARMSDICT[thisName_] = f"{NTAB(1)}{DBLQT}{thisParam_}{DBLQT}: {thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN22STRENTRYADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN22OPTIONSDICT[thisName_] = f"{NTAB(1)}{thisKey_}: {DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN22VALENTRYADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN22OPTIONSDICT[thisName_] = f"{NTAB(1)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN24LISTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			FMCF_SCTN24LISTDICT[thisListName_] = ""
			FMCF_SCTN24LISTCMNTDICT[thisListName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN24LISTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN24LISTDICT[thisListName_] += f"{NTAB(1)}f{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN24LISTSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN24LISTDICT[thisListName_] += f"{NTAB(1)}{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXCF_SCTN24LISTVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisListName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMCF_SCTN24LISTDICT[thisListName_] += f"{NTAB(1)}{thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN41DEVICEDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDEV_MYNAME_ = thisItem_[2]
			FMDO_SCTN41DEVICEDEFDICT[thisDEV_MYNAME_] = f"{thisDEV_MYNAME_} = {DBLQT}{thisDEV_MYNAME_}{DBLQT}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisDEV_MYNAME_] = f"{thisComment_}"
			FMDO_SCTN44DEVICESCMNTDICT[thisDEV_MYNAME_] = f"{thisComment_}"
			#if thisDEV_MYNAME_ not in FMDO_SCTN44DEVICESDICT:
			#	FMDO_SCTN44DEVICESDICT[thisDEV_MYNAME_] = {}
			#FMDO_SCTN44DEVICESDICT[thisDEV_MYNAME_]["DEV_MYNAME"] = thisDEV_MYNAME_
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN41DICTKEYDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisKey_ = thisItem_[2]
			FMDO_SCTN41DEVICEDEFDICT[thisKey_] = f"{thisKey_} = {DBLQT}{thisKey_}{DBLQT}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisKey_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN41LAMBDADEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMDO_SCTN41DEVICEDEFDICT[thisValName_] = f"{thisValName_} = lambda {thisVal_}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN41STRDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMDO_SCTN41DEVICEDEFDICT[thisValName_] = f"{thisValName_} = {DBLQT}{thisVal_}{DBLQT}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN41VALDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMDO_SCTN41DEVICEDEFDICT[thisValName_] = f"{thisValName_} = {thisVal_}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN42LDIEABSDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisIEStr_ = thisItem_[2]
			thisIEVAL_ = thisItem_[3]
			FMDO_SCTN42LDIEDICT[thisName_] = f"IE(LD.EV_ABS.{thisIEStr_}, {thisIEVAL_})"
			FMDO_SCTN42LDIECMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN42LDIEBTNDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisIEStr_ = thisItem_[2]
			thisIEVAL_ = thisItem_[3]
			FMDO_SCTN42LDIEDICT[thisName_] = f"IE(LD.EV_KEY.{thisIEStr_}, {thisIEVAL_})"
			FMDO_SCTN42LDIECMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN42LDIEKEYDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisIEStr_ = thisItem_[2]
			thisIEVAL_ = thisItem_[3]
			FMDO_SCTN42LDIEDICT[thisName_] = f"IE(LD.EV_KEY.{thisIEStr_}, {thisIEVAL_})"
			FMDO_SCTN42LDIECMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN42LDIERELDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisIEStr_ = thisItem_[2]
			thisIEVAL_ = thisItem_[3]
			FMDO_SCTN42LDIEDICT[thisName_] = f"IE(LD.EV_REL.{thisIEStr_}, {thisIEVAL_})"
			FMDO_SCTN42LDIECMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN42LDIESPCLDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisIEStr_ = thisItem_[2]
			thisIEVAL_ = thisItem_[3]
			FMDO_SCTN42LDIEDICT[thisName_] = f"{OPAREN}{thisIEStr_}, {thisIEVAL_}{CPAREN}"
			FMDO_SCTN42LDIECMNTDICT[thisName_] = f"{thisComment_}"
			FMDO_SCTN42LDIESPCLLIST.append(thisName_)
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN42LDIESYNDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisIEStr_ = thisItem_[2]
			thisIEVAL_ = thisItem_[3]
			FMDO_SCTN42LDIEDICT[thisName_] = f"IE(LD.EV_SYN.{thisIEStr_}, {thisIEVAL_})"
			FMDO_SCTN42LDIECMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN43AXDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMDO_SCTN41DEVICEDEFDICT[thisName_] = f"{thisName_} = {DBLQT}{thisName_}{DBLQT}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisName_] = f"{thisComment_}"
			FMDO_SCTN43AXDEFDICT[thisName_] = ""
			FMDO_SCTN43AXDEFCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN43AXVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisAXName_ = thisItem_[2]
			thisAXVal_ = thisItem_[3]
			if thisAXName_ not in FMDO_SCTN43AXDEFDICT:
				FMDO_SCTN43AXDEFDICT[thisAXName_] = ""
			FMDO_SCTN43AXDEFDICT[thisAXName_] += f"{NTAB(2)}{thisAXVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN44DEVICEENTRYSTRADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDEV_MYNAME_ = thisItem_[2]
			thisDEV_key_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDEV_MYNAME_ not in FMDO_SCTN44DEVICESDICT:
				FMDO_SCTN44DEVICESDICT[thisDEV_MYNAME_] = {}
			FMDO_SCTN44DEVICESDICT[thisDEV_MYNAME_][thisDEV_key_] = f"{DBLQT}{thisVal_}{DBLQT},  # {thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN44DEVICEENTRYVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			# print(f"thisItem {thisItem_}")
			thisDEV_MYNAME_ = thisItem_[2]
			thisDEV_key_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDEV_MYNAME_ not in FMDO_SCTN44DEVICESDICT:
				FMDO_SCTN44DEVICESDICT[thisDEV_MYNAME_] = {}
			FMDO_SCTN44DEVICESDICT[thisDEV_MYNAME_][thisDEV_key_] = f"{thisVal_},  # {thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN45HOLDABLEADD1:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 9:
				doErrorItem("not 9 items", thisItem_)
				continue
			thisDEV_MYNAME_ = thisItem_[2]
			thisBtnType_ = thisItem_[3]
			thisRepeat_ = thisItem_[4]
			thisHOLDABLE_ = thisItem_[5]
			thisNOTHOLDABLE_ = thisItem_[6]
			thisAX_ = thisItem_[7]

			if thisDEV_MYNAME_ not in FMDO_SCTN45PROFDICT:
				FMDO_SCTN45PROFDICT[thisDEV_MYNAME_] = {}
			if thisHOLDABLE_ not in FMDO_SCTN45PROFDICT[thisDEV_MYNAME_]:
				FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisHOLDABLE_] = {}
			FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisHOLDABLE_][thisNOTHOLDABLE_] = f"{thisAX_},  # {thisComment_}"

			if thisDEV_MYNAME_ not in FMDO_SCTN45RPTDICT:
				FMDO_SCTN45RPTDICT[thisDEV_MYNAME_] = {}
			if thisHOLDABLE_ not in FMDO_SCTN45RPTDICT[thisDEV_MYNAME_]:
				FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisHOLDABLE_] = {}
			FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisHOLDABLE_][thisNOTHOLDABLE_] = f"{thisRepeat_},  # {thisComment_}"

			if thisDEV_MYNAME_ not in FMDO_SCTN45BTNTYPEDICT:
				FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_] = {}
			if thisHOLDABLE_ not in FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_]:
				FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisHOLDABLE_] = {}
			FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisHOLDABLE_][thisNOTHOLDABLE_] = f"{thisBtnType_},  # {thisComment_}"

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN45HOLDABLEADD2:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 10:
				doErrorItem("not 10 items", thisItem_)
				continue
			thisDEV_MYNAME_ = thisItem_[2]
			thisBtnType_ = thisItem_[3]
			thisRepeat_ = thisItem_[4]
			thisHOLDABLE1_ = thisItem_[5]
			thisHOLDABLE2_ = thisItem_[6]
			thisNOTHOLDABLE_ = thisItem_[7]
			thisAX_ = thisItem_[8]

			if thisDEV_MYNAME_ not in FMDO_SCTN45PROFDICT:
				FMDO_SCTN45PROFDICT[thisDEV_MYNAME_] = {}
			if thisHOLDABLE1_ not in FMDO_SCTN45PROFDICT[thisDEV_MYNAME_]:
				FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisHOLDABLE1_] = {}
			if thisHOLDABLE2_ not in FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisHOLDABLE1_]:
				FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisHOLDABLE1_][thisHOLDABLE2_] = {}
			FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisHOLDABLE1_][thisHOLDABLE2_][thisNOTHOLDABLE_] = f"{thisAX_},  # {thisComment_}"

			if thisDEV_MYNAME_ not in FMDO_SCTN45RPTDICT:
				FMDO_SCTN45RPTDICT[thisDEV_MYNAME_] = {}
			if thisHOLDABLE1_ not in FMDO_SCTN45RPTDICT[thisDEV_MYNAME_]:
				FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisHOLDABLE1_] = {}
			if thisHOLDABLE2_ not in FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisHOLDABLE1_]:
				FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisHOLDABLE1_][thisHOLDABLE2_] = {}
			FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisHOLDABLE1_][thisHOLDABLE2_][thisNOTHOLDABLE_] = f"{thisRepeat_},  # {thisComment_}"

			if thisDEV_MYNAME_ not in FMDO_SCTN45BTNTYPEDICT:
				FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_] = {}
			if thisHOLDABLE1_ not in FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_]:
				FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisHOLDABLE1_] = {}
			if thisHOLDABLE2_ not in FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisHOLDABLE1_]:
				FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisHOLDABLE1_][thisHOLDABLE2_] = {}
			FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisHOLDABLE1_][thisHOLDABLE2_][thisNOTHOLDABLE_] = f"{thisBtnType_},  # {thisComment_}"

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN45NOTHOLDABLEADD1:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 8:
				doErrorItem("not 8 items", thisItem_)
				continue
			thisDEV_MYNAME_ = thisItem_[2]
			thisBtnType_ = thisItem_[3]
			thisRepeat_ = thisItem_[4]
			thisNOTHOLDABLE_ = thisItem_[5]
			thisAX_ = thisItem_[6]

			if thisDEV_MYNAME_ not in FMDO_SCTN45PROFDICT:
				FMDO_SCTN45PROFDICT[thisDEV_MYNAME_] = {}
			FMDO_SCTN45PROFDICT[thisDEV_MYNAME_][thisNOTHOLDABLE_] = f"{thisAX_},  # {thisComment_}"

			if thisDEV_MYNAME_ not in FMDO_SCTN45RPTDICT:
				FMDO_SCTN45RPTDICT[thisDEV_MYNAME_] = {}
			FMDO_SCTN45RPTDICT[thisDEV_MYNAME_][thisNOTHOLDABLE_] = f"{thisRepeat_},  # {thisComment_}"

			if thisDEV_MYNAME_ not in FMDO_SCTN45BTNTYPEDICT:
				FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_] = {}
			FMDO_SCTN45BTNTYPEDICT[thisDEV_MYNAME_][thisNOTHOLDABLE_] = f"{thisBtnType_},  # {thisComment_}"

			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN46XLATEADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDEV_MYNAME_ = thisItem_[2]
			thisDEV_BTN = thisItem_[3]
			thisDEV_COMMON = thisItem_[4]
			if thisDEV_MYNAME_ not in FMDO_SCTN46XLATEDICT:
				FMDO_SCTN46XLATEDICT[thisDEV_MYNAME_] = ""
			FMDO_SCTN46XLATEDICT[thisDEV_MYNAME_] += f"{NTAB(2)}{thisDEV_BTN}: {thisDEV_COMMON},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN47BTNSDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisBTNName_ = thisItem_[2]
			thisHOLDABLE_ = thisItem_[3]
			FMDO_SCTN41DEVICEDEFDICT[thisBTNName_] = f"{thisBTNName_} = {DBLQT}{thisBTNName_}{DBLQT}"
			FMDO_SCTN41DEVICEDEFCMNTDICT[thisBTNName_] = f"{thisComment_}"
			FMDO_SCTN47BTNSDICT[thisBTNName_] = f"{thisHOLDABLE_}"
			if thisHOLDABLE_ == "BTNTYPE_HOLDABLE":
				BTNSHOLDABLELIST.append(f"{thisBTNName_}")
			FMDO_SCTN47BTNSCMNTDICT[thisBTNName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN48EVTYPEDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDEVT_ = thisItem_[2]
			FMDO_SCTN48DEFDICT[thisName_] = f"{thisDEVT_} = {DBLQT}{thisDEVT_}{DBLQT}"
			FMDO_SCTN48DEFCMNTDICT[thisName_] = f"{thisComment_}"
			if thisDEVT_ not in FMDO_SCTN48TYPESDICT:
				FMDO_SCTN48TYPESDICT[thisDEVT_] = []
			FMDO_SCTN48TYPESCMNTDICT[thisDEVT_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN48EVTYPELST:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisDEVT_ = thisItem_[2]
			thisDEVTCD_ = thisItem_[3]
			if thisDEVT_ not in FMDO_SCTN48TYPESDICT:
				FMDO_SCTN48TYPESDICT[thisDEVT_] = []
			FMDO_SCTN48TYPESDICT[thisDEVT_].append(f"{thisDEVTCD_},  # {thisComment_}")
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN49DIRTRANSDEVDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisDEVT_ = thisItem_[2]
			if thisDEVT_ not in FMDO_SCTN49DIRTRANSDICT:
				FMDO_SCTN49DIRTRANSDICT[thisDEVT_] = ""
			FMDO_SCTN49DIRTRANSCMNTDICT[thisDEVT_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXDO_SCTN49DIRTRANSVALADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 6:
				doErrorItem("not 6 items", thisItem_)
				continue
			thisDEVT_ = thisItem_[2]
			thisKey_ = thisItem_[3]
			thisVal_ = thisItem_[4]
			if thisDEVT_ not in FMDO_SCTN49DIRTRANSDICT:
				FMDO_SCTN49DIRTRANSDICT[thisDEVT_] = ""
			FMDO_SCTN49DIRTRANSDICT[thisDEVT_] += f"{NTAB(2)}{thisKey_}: {thisVal_},  # {thisComment_}{NEWLINE}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXFM_SCTN11AXDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN11AXDICT[thisName_] = f"{DBLQT}{thisName_}{DBLQT}"
			FMFM_SCTN11AXCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXFM_SCTN12VALDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 5:
				doErrorItem("not 5 items", thisItem_)
				continue
			thisValName_ = thisItem_[2]
			thisVal_ = thisItem_[3]
			FMFM_SCTN12VALDICT[thisValName_] = thisVal_
			FMFM_SCTN12VALCMNTDICT[thisValName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXFM_SCTN13DICTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN13DICTDICT[thisName_] = f"{OBRCE}{CBRCE}"
			FMFM_SCTN13DICTCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXFM_SCTN14LISTDEF:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 3:
				doErrorItem("not 3 items", thisItem_)
				continue
			FMFM_SCTN14LISTDICT[thisName_] = f"{OBRKT}{CBRKT}"
			FMFM_SCTN14LISTCMNTDICT[thisName_] = f"{thisComment_}"
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXHBI_SCTN50ABSADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisHBIVal_ = thisItem_[2]
			FMHBI_SCTN50HBIABSLIST.append(f"{thisHBIVal_}{CPAREN}  # {thisComment_}")
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXHBI_SCTN51BTNADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisHBIVal_ = thisItem_[2]
			FMHBI_SCTN51HBIBTNLIST.append(f"{thisHBIVal_}{CPAREN}  # {thisComment_}")
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXHBI_SCTN52KEYADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisHBIVal_ = thisItem_[2]
			FMHBI_SCTN52HBIKEYLIST.append(f"{thisHBIVal_}{CPAREN}  # {thisComment_}")
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisAX_ == FMAXHBI_SCTN53RELADD:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisItemLen_ != 4:
				doErrorItem("not 4 items", thisItem_)
				continue
			thisHBIVal_ = thisItem_[2]
			FMHBI_SCTN53HBIRELLIST.append(f"{thisHBIVal_}{CPAREN}  # {thisComment_}")
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# __main__
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def __main__():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	with open(TBGLST_NAME, "tw") as FDOut:
		FDOut.write(f"TBGLST = {OBRKT}{NEWLINE}{NTAB(1)}{FOLD1STARTHERE}{NEWLINE}")
		parseTBGLST(FDOut)
		FDOut.write(f"{NTAB(1)}{FOLD1ENDHERE}{NEWLINE}{CBRKT}{NEWLINE}")

	with open(CF_NAME, "tw") as FDOut:
		strToWrt_ = makeCF()
		FDOut.writelines(strToWrt_)

	with open(DO_NAME, "tw") as FDOut:
		strToWrt_ = makeDO()
		FDOut.writelines(strToWrt_)

	with open(FM_NAME, "tw") as FDOut:
		strToWrt_ = makeFM()
		FDOut.writelines(strToWrt_)

	with open(HBI_NAME, "tw") as FDOut:
		strToWrt_ = makeHBI()
		FDOut.writelines(strToWrt_)
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


if __name__ == "__main__":
	__main__()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of FM.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#