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