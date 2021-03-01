

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of managed sections and file CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from datetime import datetime as DT
from datetime import timedelta as TD
from dateutil import parser as PD
from dateutil import tz as TZ
from dateutil.relativedelta import relativedelta as RD
from sys import argv
from sys import exit
from time import mktime as MT
from time import monotonic as TMT
from time import time_ns as TNS
import datedelta as DD
import datetime
import hashlib as HL
import inspect
import pickle as PD


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules defined in CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# * def dateIntvlM(dateToUse, months):
# * def dateToStr(dateIn):
# * def displayStats(LN_, COL_, statsStr_):
# * def doAHash(HASH_, stringToHash):
# * def doError(strToOutToErr_):
# * def getDebugInfo():
# * def gmdate(dtObj=DT.now()):
# * def ISO2TS(ISOStrIn):
# * def mysql2LocalTime(SQLTIMEZ):
# * def now():
# * def nowStr(dtObj=DT.now()):
# * def nowStrSql(dtObj=DT.now()):
# * def nowTimeStr(dtObj=DT.now()):
# * def nowZ():
# * def nowZStr(dtObj=DT.utcnow()):
# * def nowZStrSql(dtObj=DT.utcnow()):
# * def outputOptionsDict():
# * def pickleIt(fileName_, dataToPickle_):
# * def print_(*args_):
# * def readFileToStr(FILENAME_):
# * def relDateDiff(startTS, endTS):
# * def relDateDiffStripped(startTS, endTS):
# * def removeDictQuotes(dictToUnquote_):
# * def removeStrQuotes(strToStrip_):
# * def setOptions(argv_):
# * def stripCodesAndVersion(strToStrip_):
# * def stripCodes(strToStrip_):
# * def timeHoler(timeStr):
# * def today():
# * def todayStr(dtObj=DT.today()):
# * def tomorrow(dtObj=today()):
# * def tomorrowStr(dtObj=tomorrow()):
# * def toStr(TDIn):
# * def TS2ISO(TSIn):
# * def unPickleIt(fileName_):
# * def USGS2LocalTime(usgsTimeZ):
# * def USGS2MysqlTime(USGSDate):
# * def yesterday(dtObj=DT.today()):
# * def yesterdayStr(dtObj=yesterday(DT.today())):


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
CLRDOWN = "\033[J"
CLREOL = "\033[K"
CMNTLINE = "# * " + "#*" * CMNTLEN
DBSQLT_NAME = "newDBSQLT.py"
DICTMODE_KEYSTR = "DICTMODE_KEYSTR"  # define dictmode 'key':val
DICTMODE_KEYVAL = "DICTMODE_KEYVAL"  # define dictmode key:val
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
HASH_blake2b = HL.blake2b()  # define blake2b value
HASH_blake2s = HL.blake2s()  # define blake2s value
HASHER = "HASHER"  # HASHER key
HASH_md5 = HL.md5()  # define md5 value
HASH_sha1 = HL.sha1()  # define sha1 value
HASH_sha224 = HL.sha224()  # define sha224 value
HASH_sha256 = HL.sha256()  # define sha256 value
HASH_sha3_224 = HL.sha3_224()  # define sha3_224 value
HASH_sha3_256 = HL.sha3_256()  # define sha3_256 value
HASH_sha3_384 = HL.sha3_384()  # define sha3_384 value
HASH_sha3_512 = HL.sha3_512()  # define sha3_512 value
HASH_sha384 = HL.sha384()  # define sha384 value
HASH_sha512 = HL.sha512()  # define sha512 value
HBI_NAME = "newHBI.py"
HEX08 = lambda X_: f"{X_:02H}"   # {thisComment_}
HEX16 = lambda X_: f"{X_:04H}"   # {thisComment_}
HEX32 = lambda X_: f"{X_:08H}"   # {thisComment_}
HEX64 = lambda X_: f"{X_:016H}"   # {thisComment_}
IMPORTANTSTR = "# * " + "!-" * CMNTLEN  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = "# * " + "%_" * CMNTLEN  # INFO _STR_ line\
KNOWNFILES = "KNOWNFILES"  # KNOWNFILES key
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
MEDIAFILES = "MEDIAFILES"  # MEDIAFILES key
MOVETO = lambda LN_, COL_: f"\033[{LN_};{COL_}H"
NOTKNOWNFILES = "KNOWNFILES"  # NOTKNOWNFILES key
NOTMEDIAFILES = "MEDIAFILES"  # NOTMEDIAFILES key
NOTRECURSE = "RECURSE"  # NOTRECURSE key
NOTTRIALRUN = "TRIALRUN"  # TRIALRUN key
NOTUNKNOWNFILES = "UNKNOWNFILES"  # NOTUNKNOWNFILES key
NTAB = lambda NUM_: TABSTR * NUM_  # returns a string with _NUM_ TAB
QTSET = ['"', "'", "`"]  # set of all quote characters
SCTN0102NAME = f"{CONFIGDIR}SCTN0102.py"
SCTNSNAME = f"{CONFIGDIR}SCTNS.py"
SP_NAME = "newSP.py"
TBGLST_NAME = "TBGLST.py"
TRIQT = DBLQT + DBLQT + DBLQT  # works most of the time triple quote




# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN21 CF defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN22 options structures
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
PARMSDICT = {
}

OPTIONSDICT = {
}


#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of managed sections of CF.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#


