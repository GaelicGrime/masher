

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
# * def isPast(timeToChk_):
# * def MTS():
# * def MTSclr():
# * def MTSPlus(numToAdd_):
# * def mySleep(fToSleep_):
# * def mysql2LocalTime(SQLTIMEZ):
# * def myTimestamp(dtObj=DT.now()):
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
DOTOP_NAME = f"{CONFIGDIR}DOTOP.py"
EEOL = "\033[K"
_EMPTY_DICT_ = {}
_EMPTY_LIST_ = []
_EMPTY_STR_ = ""
EMPTYSTRLST = [None, "", DBLQT, DBLQT + DBLQT, "'", "''", "`", "None", "\r", "\n", "\r\n", "\n\r", ]
_EMPTY_TUPLE_ = ()
ESC = "\x1b"
FM_NAME = "newFM.py"
FMTOP_NAME = f"{CONFIGDIR}FMTOP.py"
FO_NAME = "newFO.py"
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
HASHER = "HASHER"  # HASHER key
HASH_blake2b = HL.blake2b()  # define blake2b value
HASH_blake2s = HL.blake2s()  # define blake2s value
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
HBIBTM_NAME = f"{CONFIGDIR}HBIBTM.py"
HBI_NAME = "newHBI.py"
HBITOP_NAME = f"{CONFIGDIR}HBITOP.py"
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
MARK1END = f"""# {"⥣1 " * (CMNTLEN // 3)}"""
MARK1ENDLN = f"""# {"⥣1 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK1MID = f"""# {"⥣1⥥ " * (CMNTLEN // 4)}"""
MARK1MIDLN = f"""# {"⥣1⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK1START = f"""# {"1⥥ " * (CMNTLEN // 3)}"""
MARK1STARTLN = f"""# {"1⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK2END = f"""# {"⥣2 " * (CMNTLEN // 3)}"""
MARK2ENDLN = f"""# {"⥣2 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK2MID = f"""# {"⥣2⥥ " * (CMNTLEN // 4)}"""
MARK2MIDLN = f"""# {"⥣2⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK2START = f"""# {"2⥥ " * (CMNTLEN // 3)}"""
MARK2STARTLN = f"""# {"2⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK3END = f"""# {"⥣3 " * (CMNTLEN // 3)}"""
MARK3ENDLN = f"""# {"⥣3 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK3MID = f"""# {"⥣3⥥ " * (CMNTLEN // 4)}"""
MARK3MIDLN = f"""# {"⥣3⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK3START = f"""# {"3⥥ " * (CMNTLEN // 3)}"""
MARK3STARTLN = f"""# {"3⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK4END = f"""# {"⥣4 " * (CMNTLEN // 3)}"""
MARK4ENDLN = f"""# {"⥣4 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK4MID = f"""# {"⥣4⥥ " * (CMNTLEN // 4)}"""
MARK4MIDLN = f"""# {"⥣4⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK4START = f"""# {"4⥥ " * (CMNTLEN // 3)}"""
MARK4STARTLN = f"""# {"4⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK5END = f"""# {"⥣5 " * (CMNTLEN // 3)}"""
MARK5ENDLN = f"""# {"⥣5 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK5MID = f"""# {"⥣5⥥ " * (CMNTLEN // 4)}"""
MARK5MIDLN = f"""# {"⥣5⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK5START = f"""# {"5⥥ " * (CMNTLEN // 3)}"""
MARK5STARTLN = f"""# {"5⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK6END = f"""# {"⥣6 " * (CMNTLEN // 3)}"""
MARK6ENDLN = f"""# {"⥣6 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK6MID = f"""# {"⥣6⥥ " * (CMNTLEN // 4)}"""
MARK6MIDLN = f"""# {"⥣6⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK6START = f"""# {"6⥥ " * (CMNTLEN // 3)}"""
MARK6STARTLN = f"""# {"6⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK7END = f"""# {"⥣7 " * (CMNTLEN // 3)}"""
MARK7ENDLN = f"""# {"⥣7 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK7MID = f"""# {"⥣7⥥ " * (CMNTLEN // 4)}"""
MARK7MIDLN = f"""# {"⥣7⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK7START = f"""# {"7⥥ " * (CMNTLEN // 3)}"""
MARK7STARTLN = f"""# {"7⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK8END = f"""# {"⥣8 " * (CMNTLEN // 3)}"""
MARK8ENDLN = f"""# {"⥣8 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK8MID = f"""# {"⥣8⥥ " * (CMNTLEN // 4)}"""
MARK8MIDLN = f"""# {"⥣8⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK8START = f"""# {"8⥥ " * (CMNTLEN // 3)}"""
MARK8STARTLN = f"""# {"8⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
MARK9END = f"""# {"⥣9 " * (CMNTLEN // 3)}"""
MARK9ENDLN = f"""# {"⥣9 " * (CMNTLEN // 3)}{NEWLINE}"""
MARK9MID = f"""# {"⥣9⥥ " * (CMNTLEN // 4)}"""
MARK9MIDLN = f"""# {"⥣9⥥ " * (CMNTLEN // 4)}{NEWLINE}"""
MARK9START = f"""# {"9⥥ " * (CMNTLEN // 3)}"""
MARK9STARTLN = f"""# {"9⥥ " * (CMNTLEN // 3)}{NEWLINE}"""
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


