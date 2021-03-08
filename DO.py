

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN40 start of CF.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
from libevdev import InputEvent as IE
import fcntl
import libevdev as LD
import os


import CF


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * included modules
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
# * def fixBtn(DEVTCode_):
# * def fixEvent(thisDevice_, eventToFix_):
# * def incNdx(AXLst_, currentNDX_):
# * def isMatch(eventCD1_, eventCD2_):
# * def openOutputDevice(lookingForDeviceName_):
# * def SPCL_(spclEvent_, spclVal_):


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN41 device defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
AXDSKTP1 = "AXDSKTP1"  # desktop #1
AXDSKTP2 = "AXDSKTP2"  # desktop #2
AXDSKTP3 = "AXDSKTP3"  # desktop #3
AXDSKTP4 = "AXDSKTP4"  # desktop #4
AXGIMPOVWRT = "AXGIMPOVWRT"  # GIMP overwrite imported file
AXHRHWLDN = "AXHRHWLDN"  # high rez wheel DOWN
AXHRHWLLT = "AXHRHWLLT"  # high rez wheel LEFT
AXHRHWLRT = "AXHRHWLRT"  # high rez wheel RIGHT
AXHRHWLUP = "AXHRHWLUP"  # high rez wheel UP
AXMCCOPY = "AXMCCOPY"  # MC copy F5, ENTER
AXMCDEL = "AXMCDEL"  # MC del F8, ENTER
AXMCMOVE = "AXMCMOVE"  # MC move F6, ENTER
AXMCSEL = "AXMCSEL"  # MC select INS
AXMSEBTNBAK = "AXMSEBTNBAK"  # MSE BTN BACK
AXMSEBTNFWD = "AXMSEBTNFWD"  # MSE BTN FWD
AXMSEBTNLT = "AXMSEBTNLT"  # MSE BTN LEFT
AXMSEBTNLT_L00 = "AXMSEBTNLT_L00"  # MSE BTN LEFT
AXMSEBTNLT_L01 = "AXMSEBTNLT_L01"  # MSE BTN LEFT_1 pressed
AXMSEBTNLT_L02 = "AXMSEBTNLT_L02"  # MSE BTN LEFT_2 released
AXMSEBTNLT_T01 = "AXMSEBTNLT_T01"  # MSE BTN LEFT_1 pressed
AXMSEBTNLT_T02 = "AXMSEBTNLT_T02"  # MSE BTN LEFT_2 released
AXMSEBTNMID = "AXMSEBTNMID"  # MSE BTN MIDDLE
AXMSEBTNRT = "AXMSEBTNRT"  # MSE BTN RIGHT
AXMSEBTNRT_T01 = "AXMSEBTNRT_T01"  # MSE BTN LEFT_1 pressed
AXMSEBTNRT_T02 = "AXMSEBTNRT_T02"  # MSE BTN LEFT_2 released
AXMSEBTNSIDE = "AXMSEBTNSIDE"  # MSE BTN SIDE
AXMSEBTNTASK = "AXMSEBTNTASK"  # MSE BTN TASK
AXMSEDN = "AXMSEDN"  # MSE DOWN
AXMSEDNA = "AXMSEDNA"  # MSE DOWN
AXMSEDNLT = "AXMSEDNLT"  # MSE DOWNLT
AXMSEDNRT = "AXMSEDNRT"  # MSE DOWNRT
AXMSELT = "AXMSELT"  # MSE LEFT
AXMSELTA = "AXMSELTA"  # MSE LEFT
AXMSERT = "AXMSERT"  # MSE RIGHT
AXMSERTA = "AXMSERTA"  # MSE RIGHT
AXMSEUP = "AXMSEUP"  # MSE UP
AXMSEUPA = "AXMSEUPA"  # MSE UP
AXMSEUPLT = "AXMSEUPLT"  # MSE UPLT
AXMSEUPRT = "AXMSEUPRT"  # MSE UPRT
AXMSEWHLDN = "AXMSEWHLDN"  # wheel DOWN
AXMSEWHLDNLT = "AXMSEWHLDNLT"  # wheel DNLT
AXMSEWHLDNRT = "AXMSEWHLDNRT"  # wheel DNRT
AXMSEWHLLT = "AXMSEWHLLT"  # wheel LEFT
AXMSEWHLRT = "AXMSEWHLRT"  # wheel RIGHT
AXMSEWHLUP = "AXMSEWHLUP"  # wheel UP
AXMSEWHLUPLT = "AXMSEWHLUPLT"  # wheel UPLT
AXMSEWHLUPRT = "AXMSEWHLUPRT"  # wheel UPRT
AXSAVE = "AXSAVE"  # save CTRL-S
AXXNVCOPYTO = "AXXNVCOPYTO"  # XnViewer COPYTO ALT-C
AXXNVCROP = "AXXNVCROP"  # XnViewer CROP SHIFT-X
AXXNVFLIPH = "AXXNVFLIPH"  # XnViewer FLIP horizontal ALT-F
AXXNVMOVE = "AXXNVMOVE"  # XnViewer MOVE ALT-M
AXXNVROTLT = "AXXNVROTLT"  # XnViewer ROT LEFT CTRL-SHIFT-L
AXXNVROTRT = "AXXNVROTRT"  # XnViewer ROT RIGHT CTRL-SHIFT-R
AXXNVSEL2TOP = "AXXNVSEL2TOP"  # XnViewer SELECT to top SHIFT-HOME, SHIFT-RIGHT
AXXNVZOOMFULL = "AXXNVZOOMFULL"  # XnViewer zoom 1:1
AXXNVZOOMIN = "AXXNVZOOMIN"  # XnViewer zoom in/+
AXXNVZOOMOUT = "AXXNVZOOMOUT"  # XnViewer zoom out/-
AXXNVZOOMRESET = "AXXNVZOOMRESET"  # reset XnViewer zoom by back, forward, forward, back
AX_ALTC = "AX_ALTC"  # ALT-C
AX_ALTD = "AX_ALTD"  # ALT-D
AX_ALTTAB = "AX_ALTTAB"  # ALT-TAB
AX_ALT_T01 = "AX_ALT_T01"  # ALT-C
AX_ALT_T02 = "AX_ALT_T02"  # ALT-C
AX_CRSRDN = "AX_CRSRDN"  # DOWN
AX_CRSRDNLT = "AX_CRSRDNLT"  # DOWN
AX_CRSRDNRT = "AX_CRSRDNRT"  # DOWN
AX_CRSRLT = "AX_CRSRLT"  # LEFT
AX_CRSRRT = "AX_CRSRRT"  # RIGHT
AX_CRSRUP = "AX_CRSRUP"  # UP
AX_CRSRUPLT = "AX_CRSRUPLT"  # UPLT
AX_CRSRUPRT = "AX_CRSRUPRT"  # UPRT
AX_CTRLA = "AX_CTRLA"  # CTRL-A
AX_CTRLPGDN = "AX_CTRLPGDN"  # CTRLPGDN
AX_CTRLPGUP = "AX_CTRLPGUP"  # CTRLPGUP
AX_CTRLQ = "AX_CTRLQ"  # CTRL-Q
AX_CTRLS = "AX_CTRLS"  # CTRL-S
AX_CTRLTAB = "AX_CTRLTAB"  # CTRL-TAB
AX_CTRLW = "AX_CTRLW"  # CTRL-W
AX_CTRL_T01 = "AX_CTRL_T01"  # CTRL toggle actions
AX_CTRL_T02 = "AX_CTRL_T02"  # CTRL toggle actions
AX_DEL = "AX_DEL"  # DEL
AX_END = "AX_END"  # END
AX_ENTER = "AX_ENTER"  # ENTER
AX_ESC = "AX_ESC"  # ESC
AX_F = "AX_F"  # F
AX_F10 = "AX_F10"  # F10
AX_F5 = "AX_F5"  # F5
AX_F6 = "AX_F6"  # F6
AX_HOME = "AX_HOME"  # HOME
AX_INS = "AX_INS"  # MC select INS
AX_N = "AX_N"  # N
AX_PGDN = "AX_PGDN"  # PGDN
AX_PGUP = "AX_PGUP"  # PGUP
AX_Q = "AX_Q"  # Q
AX_SHIFTDN = "AX_SHIFTDN"  # SHIFT-DN
AX_SHIFTDNLT = "AX_SHIFTDNLT"  # SHIFT-DNLT
AX_SHIFTDNRT = "AX_SHIFTDNRT"  # SHIFT-DNRT
AX_SHIFTLT = "AX_SHIFTLT"  # SHIFT-LT
AX_SHIFTRT = "AX_SHIFTRT"  # SHIFT-RT
AX_SHIFTTAB = "AX_SHIFTTAB"  # ALT-SHIFT-TAB
AX_SHIFTUP = "AX_SHIFTUP"  # SHIFT-UP
AX_SHIFTUPLT = "AX_SHIFTUPLT"  # SHIFT-UPLT
AX_SHIFTUPRT = "AX_SHIFTUPRT"  # SHIFT-UPRT
AX_SHIFTX = "AX_SHIFTX"  # SHIFT-X
AX_SHIFT_T01 = "AX_SHIFT_T01"  # SHIFT toggle actions
AX_SHIFT_T02 = "AX_SHIFT_T02"  # SHIFT toggle actions
AX_SPACE = "AX_SPACE"  # SPACE
AX_TAB = "AX_TAB"  # TAB
AX_Y = "AX_Y"  # Y
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
BTNM_MDNA = "BTNM_MDNA"  # BTNMDN/MSE_DN on mice
BTNM_MDNLT = "BTNM_MDNLT"  # BTNMDN/MSE_DNLT on mice
BTNM_MDNRT = "BTNM_MDNRT"  # BTNMDN/MSE_DNRT on mice
BTNM_MLT = "BTNM_MLT"  # BTNMLT/MSE_LT on mice
BTNM_MLTA = "BTNM_MLTA"  # BTNMLT/MSE_LT on mice
BTNM_MRT = "BTNM_MRT"  # BTNMRT/MSE_RT on mice
BTNM_MRTA = "BTNM_MRTA"  # BTNMRT/MSE_RT on mice
BTNM_MUP = "BTNM_MUP"  # BTNMUP/MSE_UP on mice
BTNM_MUPA = "BTNM_MUPA"  # BTNMUP/MSE_UP on mice
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
BTNS_MODE1 = "BTNS_MODE1"  # switch through MODE1 move/wheel for mouse actions
BTNS_MODE2 = "BTNS_MODE2"  # switch through MODE2 normal/draglock for mouse actions
ABSDEADWIDTH = "ABSDEADWIDTH"  # key for stick dead width
ABSMAX = "ABSMAX"  # key for stick max
ABSMAXVAL = 0XFFFFFFFFFFFFFFFF  # key for stick max val
ABSMIN = "ABSMIN"  # key for stick min
ABSMINVAL = -0XFFFFFFFFFFFFFFFF  # key for min stick val
ABSZERO = "ABSZERO"  # stick center/resting position key
ABSZEROVAL = 0X0000000000000000  # val used for stick 0 position
ABS_HAT0X = "ABS_HAT0X"  # key for hat 0 X, the first, or only hat on the device
ABS_HAT0Y = "ABS_HAT0Y"  # key for hat 0 Y, the first, or only hat on the device
ABS_RZ = "ABS_RZ"  # key for stick 1 Y
ABS_X = "ABS_X"  # key for stick 0 X
ABS_Y = "ABS_Y"  # key for stick 0 Y
ABS_Z = "ABS_Z"  # key for stick 1 X
BTNAXTYPE_LOCKING = "BTNAXTYPE_LOCKING"  # action type NORMAL key
BTNAXTYPE_MODED = "BTNAXTYPE_MODED"  # action type NORMAL key
BTNAXTYPE_NORMAL = "BTNAXTYPE_NORMAL"  # action type NORMAL key
BTNAXTYPE_SPCL = "BTNAXTYPE_SPCL"  # action type key
BTNAXTYPE_TOGGLE = "BTNAXTYPE_TOGGLE"  # action type key
BTNS00 = 0B00000001  # FLAG LD.EV_KEY holdable BTN0 GPM
BTNS05 = 0B00000010  # FLAG LD.EV_KEY holdable BTN5 gamepads
BTNS06 = 0B00000100  # FLAG LD.EV_KEY holdable BTN6 gamepads
BTNS07 = 0B00001000  # FLAG LD.EV_KEY holdable BTN7 gamepads
BTNS08 = 0B00010000  # FLAG LD.EV_KEY holdable BTN8 gamepads
BTNS22 = 0B00100000  # FLAG LD.EV_KEY holdable BTN22 saitek
BTNS23 = 0B01000000  # FLAG LD.EV_KEY holdable BTN23 saitek
BTNS24 = 0B10000000  # FLAG LD.EV_KEY holdable BTN24 saitek
BTNS_NOT = 0B00000000  # FLAG no BTN or _KEY_ held
BTNTYPE = "BTNTYPE"  # action type key
BTNTYPE_HOLDABLE = "BTNTYPE_HOLDABLE"  # HOLDABLE button
BTNTYPE_NOTHOLDABLE = "BTNTYPE_NOTHOLDABLE"  # NOTHOLDABLE button
BTNTYPE_SIMABS = "BTNTYPE_SIMABS"  # simulated ABS button
BTNTYPE_SIMKEY = "BTNTYPE_SIMKEY"  # simulated REL button
BTNTYPE_SIMREL = "BTNTYPE_SIMREL"  # simulated REL button
DEFT = "DEFT"  # define the DEFT trackball
DEVCD_ABSRZ = LD.EV_ABS.ABS_RZ  # shortcut to ABS_RZ
DEVCD_ABSX = LD.EV_ABS.ABS_X  # shortcut to ABS_X
DEVCD_ABSY = LD.EV_ABS.ABS_Y  # shortcut to ABS_HAT0Y
DEVCD_ABSZ = LD.EV_ABS.ABS_Z  # shortcut to ABS_Z
DEVCD_BTNGHAT_DN = BTNGHAT_DN  # shortcut to BTNGHAT_DN
DEVCD_BTNGHAT_DNLT = BTNGHAT_DNLT  # shortcut to BTNGHAT_DN
DEVCD_BTNGHAT_DNRT = BTNGHAT_DNRT  # shortcut to BTNGHAT_DN
DEVCD_BTNGHAT_LT = BTNGHAT_LT  # shortcut to BTNGHAT_LT
DEVCD_BTNGHAT_RLS = BTNGHAT_RLS  # shortcut to BTNGHAT_RLS
DEVCD_BTNGHAT_RT = BTNGHAT_RT  # shortcut to BTNGHAT_RT
DEVCD_BTNGHAT_UP = BTNGHAT_UP  # shortcut to BTNGHAT_UP
DEVCD_BTNGHAT_UPLT = BTNGHAT_UPLT  # shortcut to BTNGHAT_UP
DEVCD_BTNGHAT_UPRT = BTNGHAT_UPRT  # shortcut to BTNGHAT_UP
DEVCD_BTNGLTSTK_DN = BTNGLTSTK_DN  # shortcut to BTNGLTSTK_DN
DEVCD_BTNGLTSTK_DNLT = BTNGLTSTK_DNLT  # shortcut to BTNGLTSTK_DN
DEVCD_BTNGLTSTK_DNRT = BTNGLTSTK_DNRT  # shortcut to BTNGLTSTK_DN
DEVCD_BTNGLTSTK_LT = BTNGLTSTK_LT  # shortcut to BTNGLTSTK_LT
DEVCD_BTNGLTSTK_RLS = BTNGLTSTK_RLS  # shortcut to BTNGLTSTK_RT
DEVCD_BTNGLTSTK_RT = BTNGLTSTK_RT  # shortcut to BTNGLTSTK_RT
DEVCD_BTNGLTSTK_UP = BTNGLTSTK_UP  # shortcut to BTNGLTSTK_UP
DEVCD_BTNGLTSTK_UPLT = BTNGLTSTK_UPLT  # shortcut to BTNGLTSTK_UPLT
DEVCD_BTNGLTSTK_UPRT = BTNGLTSTK_UPRT  # shortcut to BTNGLTSTK_UPRT
DEVCD_BTNGRTSTK_DN = BTNGRTSTK_DN  # shortcut to BTNGRTSTK_DN
DEVCD_BTNGRTSTK_DNLT = BTNGRTSTK_DNLT  # shortcut to BTNGRTSTK_DNLT
DEVCD_BTNGRTSTK_DNRT = BTNGRTSTK_DNRT  # shortcut to BTNGRTSTK_DNRT
DEVCD_BTNGRTSTK_LT = BTNGRTSTK_LT  # shortcut to BTNGRTSTK_LT
DEVCD_BTNGRTSTK_RLS = BTNGRTSTK_RLS  # shortcut to BTNGRTSTK_RT
DEVCD_BTNGRTSTK_RT = BTNGRTSTK_RT  # shortcut to BTNGRTSTK_RT
DEVCD_BTNGRTSTK_UP = BTNGRTSTK_UP  # shortcut to BTNGRTSTK_UP
DEVCD_BTNGRTSTK_UPLT = BTNGRTSTK_UPLT  # shortcut to BTNGRTSTK_UPLT
DEVCD_BTNGRTSTK_UPRT = BTNGRTSTK_UPRT  # shortcut to BTNGRTSTK_UPRT
DEVCD_BTNG_01 = BTNG_01  # shortcut to BTNG_01
DEVCD_BTNG_02 = BTNG_02  # shortcut to BTNG_02
DEVCD_BTNG_03 = BTNG_03  # shortcut to BTNG_03
DEVCD_BTNG_04 = BTNG_04  # shortcut to BTNG_04
DEVCD_BTNG_05 = BTNG_05  # shortcut to BTNG_05
DEVCD_BTNG_06 = BTNG_06  # shortcut to BTNG_06
DEVCD_BTNG_07 = BTNG_07  # shortcut to BTNG_07
DEVCD_BTNG_08 = BTNG_08  # shortcut to BTNG_08
DEVCD_BTNG_09 = BTNG_09  # shortcut to BTNG_09
DEVCD_BTNG_10 = BTNG_10  # shortcut to BTNG_10
DEVCD_BTNG_11LTSTK = BTNG_11LTSTK  # shortcut to BTNG_11LTSTK
DEVCD_BTNG_12RTSTK = BTNG_12RTSTK  # shortcut to BTNG_12RTSTK
DEVCD_BTNG_13 = BTNG_13  # shortcut to BTNG_13
DEVCD_BTNMWH_DN = BTNMWH_DN  # shortcut to BTNM_05WHDN
DEVCD_BTNMWH_DNLT = BTNMWH_DNLT  # shortcut to BTNM_05WHDN
DEVCD_BTNMWH_DNRT = BTNMWH_DNRT  # shortcut to BTNM_05WHDN
DEVCD_BTNMWH_LT = BTNMWH_LT  # shortcut to BTNM_06WHLT
DEVCD_BTNMWH_RLS = BTNMWH_RLS  # shortcut to BTNM_07WHRT
DEVCD_BTNMWH_RT = BTNMWH_RT  # shortcut to BTNM_07WHRT
DEVCD_BTNMWH_UP = BTNMWH_UP  # shortcut to BTNM_04WHUP
DEVCD_BTNMWH_UPLT = BTNMWH_UPLT  # shortcut to BTNM_04WHUP
DEVCD_BTNMWH_UPRT = BTNMWH_UPRT  # shortcut to BTNM_04WHUP
DEVCD_BTNM_01LT = BTNM_01LT  # shortcut to BTNM_01LT
DEVCD_BTNM_02MD = BTNM_02MD  # shortcut to BTNM_02MD
DEVCD_BTNM_03RT = BTNM_03RT  # shortcut to BTNM_03RT
DEVCD_BTNM_04WHUP = BTNM_04WHUP  # shortcut to BTNM_04WHUP
DEVCD_BTNM_05WHDN = BTNM_05WHDN  # shortcut to BTNM_05WHDN
DEVCD_BTNM_06WHLT = BTNM_06WHLT  # shortcut to BTNM_06WHLT
DEVCD_BTNM_07WHRT = BTNM_07WHRT  # shortcut to BTNM_07WHRT
DEVCD_BTNM_08 = BTNM_08  # shortcut to BTNM_08
DEVCD_BTNM_09 = BTNM_09  # shortcut to BTNM_09
DEVCD_BTNM_10 = BTNM_10  # shortcut to BTNM_10
DEVCD_BTNM_11 = BTNM_11  # shortcut to BTNM_11
DEVCD_BTNM_12 = BTNM_12  # shortcut to BTNM_12
DEVCD_BTNM_MDN = BTNM_MDN  # shortcut to BTNM_05WHDN
DEVCD_BTNM_MDNA = BTNM_MDNA  # shortcut to BTNM_05WHDN
DEVCD_BTNM_MDNLT = BTNM_MDNLT  # shortcut to BTNM_05WHDN
DEVCD_BTNM_MDNRT = BTNM_MDNRT  # shortcut to BTNM_05WHDN
DEVCD_BTNM_MLT = BTNM_MLT  # shortcut to BTNM_06WHLT
DEVCD_BTNM_MLTA = BTNM_MLTA  # shortcut to BTNM_06WHLT
DEVCD_BTNM_MRT = BTNM_MRT  # shortcut to BTNM_07WHRT
DEVCD_BTNM_MRTA = BTNM_MRTA  # shortcut to BTNM_07WHRT
DEVCD_BTNM_MUP = BTNM_MUP  # shortcut to BTNM_04WHUP
DEVCD_BTNM_MUPA = BTNM_MUPA  # shortcut to BTNM_04WHUP
DEVCD_BTNM_MUPLT = BTNM_MUPLT  # shortcut to BTNM_04WHUP
DEVCD_BTNM_MUPRT = BTNM_MUPRT  # shortcut to BTNM_04WHUP
DEVCD_BTNS_MODE1 = BTNS_MODE1  # shortcut to special mode 1 button
DEVCD_BTNS_MODE2 = BTNS_MODE2  # shortcut to special mode 1 button
DEVCD_HAT0X = LD.EV_ABS.ABS_HAT0X  # shortcut to ABS_HAT0X
DEVCD_HAT0Y = LD.EV_ABS.ABS_HAT0Y  # shortcut to ABS_HAT0Y
DEVCD_RELHRHWHL = LD.EV_REL.REL_HWHEEL_HI_RES  # shortcut to REL_HWHEEL_HI_RES
DEVCD_RELHRWHL = LD.EV_REL.REL_WHEEL_HI_RES  # shortcut to REL_WHEEL_HI_RES
DEVCD_RELHWHL = LD.EV_REL.REL_HWHEEL  # shortcut to REL_HWHEEL
DEVCD_RELWHL = LD.EV_REL.REL_WHEEL  # shortcut to REL_WHEEL
DEVCD_RELX = LD.EV_REL.REL_X  # shortcut to REL_X
DEVCD_RELY = LD.EV_REL.REL_Y  # shortcut to REL_Y
DEVICESTATUS_CONNECTED = "DEVICESTATUS_CONNECTED"  # status connected
DEVICESTATUS_DISCONNECTED = "DEVICESTATUS_DISCONNECTED"  # status disconnected
DEVICESTATUS_ERROR = "DEVICESTATUS_ERROR"  # status error condition
DEVICETYPE = "DEVICETYPE"  # JOYSTICK MOUSE KEYBOARD SAITEK GAMEPAD GPM KNOB
DEVICETYPE_GAMEPAD = "DEVICETYPE_GAMEPAD"  # define a device type GAMEPAD
DEVICETYPE_GPM = "DEVICETYPE_GPM"  # define a device type GPM
DEVICETYPE_JOYSTICK = "DEVICETYPE_JOYSTICK"  # define a device type JOYSTICK
DEVICETYPE_KNOB = "DEVICETYPE_KNOB"  # device type KNOB
DEVICETYPE_MOUSE = "DEVICETYPE_MOUSE"  # define a device type MOUSE
DEVICETYPE_SAITEK = "DEVICETYPE_SAITEK"  # device type SAITEK defined
DEV_ABSHAT_STATUS = "DEV_ABSHAT_STATUS"  # status of ABS items on the device
DEV_ABSLTSTK_STATUS = "DEV_ABSLTSTK_STATUS"  # status of ABS items on the device
DEV_ABSRTSTK_STATUS = "DEV_ABSRTSTK_STATUS"  # status of ABS items on the device
DEV_BTN_STATUS = "DEV_BTN_STATUS"  # device holdable buttons status
DEV_DEVICETYPE = "DEV_DEVICETYPE"  # device type FLAG True to process thids device
DEV_ENABLED = "DEV_ENABLED"  # device enabled FLAG True to process thids device
DEV_ERR_DELTA = "DEV_ERR_DELTA"  # number of ticks (1/100) between error checks
DEV_ERR_NEXTTIME = "DEV_ERR_NEXTTIME"  # next error time for this device if erroring
DEV_FD = "DEV_FD"  # FD (file descriptor) of the device
DEV_GRAB = "DEV_GRAB"  # GRAB shal the device be grabbed exclusively or not
DEV_MYNAME = "DEV_MYNAME"  # device normal name_
DEV_NAME = "DEV_NAME"  # NAME of device returned by uvdev/evdev/etc
DEV_HASPAUSED = "DEV_HASPAUSED"  # PAUSED
DEV_QUEUE = "DEV_QUEUE"  # QUEUE holding EVENT as they come in to the device handler
DEV_RELMSE_STATUS = "DEV_RELMSE_STATUS"  # ABS status flags key
DEV_RELMW_STATUS = "DEV_RELMW_STATUS"  # ABS status flags key
DEV_RPT_NEXTTIME = "DEV_RPT_NEXTTIME"  # next TIME device will repeat
DEV_RPT_NEXTTIMEDELTA = "DEV_RPT_NEXTTIMEDELTA"  # now many TICK between repeats
DEV_SPENT = "DEV_SPENT"  # queue is spent
DEV_STATUS = "DEV_STATUS"  # device status
DIRDNLT_AND = lambda X_: DIRDNLT_VAL & X_  # FLAG DIR DNLT and lambda
DIRDNLT_MSK_AND = lambda X_: DIRDNLT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRDNLT_MSK_OR = lambda X_: DIRDNLT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRDNLT_MSK_VAL = 0B0011  # MASK DIR DOWN LEFT
DIRDNLT_OR = lambda X_: DIRDNLT_VAL | X_  # FLAG DIR DNLT or lambda
DIRDNLT_VAL = 0B1100  # FLAG DIR DOWN LEFT
DIRDNRTUP_VAL = 0B0111  # FLAG DIRDNRTUP
DIRDNRT_AND = lambda X_: DIRDNRT_VAL & X_  # FLAG DIR DNRT and lambda
DIRDNRT_MSK_AND = lambda X_: DIRDNRT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRDNRT_MSK_OR = lambda X_: DIRDNRT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRDNRT_MSK_VAL = 0B1001  # MASK DIR DOWN RIGHT
DIRDNRT_OR = lambda X_: DIRDNRT_VAL | X_  # FLAG DIR DNRT or lambda
DIRDNRT_VAL = 0B0110  # FLAG DIR DOWN RIGHT
DIRDNUP_VAL = 0B0101  # FLAG DIRDNUP
DIRDN_AND = lambda X_: DIRDN_VAL & X_  # FLAG DIR DN and lambda
DIRDN_MSK_AND = lambda X_: DIRDN_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRDN_MSK_OR = lambda X_: DIRDN_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRDN_MSK_VAL = 0B1011  # MASK DIR DOWN
DIRDN_OR = lambda X_: DIRDN_VAL | X_  # FLAG DIR DN or lambda
DIRDN_VAL = 0B0100  # FLAG DIR DN val
DIRLTDNRTUP_VAL = 0B1111  # LTDNRTUP direction VAL
DIRLTDNRT_VAL = 0B1110  # FLAG DIRLTDNRT
DIRLTDNUP_VAL = 0B1101  # FLAG DIRLTDNUP
DIRLTRTUP_VAL = 0B1011  # FLAG DIRLTRT
DIRLTRT_VAL = 0B1010  # FLAG DIRLTRT
DIRLT_AND = lambda X_: DIRLT_VAL & X_  # FLAG DIR LT and lambda
DIRLT_MSK_AND = lambda X_: DIRLT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRLT_MSK_OR = lambda X_: DIRLT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRLT_MSK_VAL = 0B0111  # MASK DIR LEFT
DIRLT_OR = lambda X_: DIRLT_VAL | X_  # FLAG DIR LT or lambda
DIRLT_VAL = 0B1000  # FLAG DIR LEFT
DIRNOT_AND = lambda X_: DIRNOT_VAL & X_  # FLAG DIR DOWN and lambda
DIRNOT_MSK_AND = lambda X_: DIRNOT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRNOT_MSK_OR = lambda X_: DIRNOT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRNOT_MSK_VAL = 0B1111  # MASK no DIR active
DIRNOT_OR = lambda X_: DIRNOT_VAL | X_  # FLAG DIR DOWN or lambda
DIRNOT_VAL = 0B0000  # FLAG no DIR active
DIRRT_AND = lambda X_: DIRRT_VAL & X_  # FLAG DIR RT and lambda
DIRRT_MSK_AND = lambda X_: DIRRT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRRT_MSK_OR = lambda X_: DIRRT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRRT_MSK_VAL = 0B1101  # MASK DIR RIGHT
DIRRT_OR = lambda X_: DIRRT_VAL | X_  # FLAG DIR RT or lambda
DIRRT_VAL = 0B0010  # FLAG DIR RIGHT
DIRUPLT_AND = lambda X_: DIRUPLT_VAL & X_  # FLAG DIR DOWN and lambda
DIRUPLT_MSK_AND = lambda X_: DIRUPLT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRUPLT_MSK_OR = lambda X_: DIRUPLT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRUPLT_MSK_VAL = 0B0110  # MASK DIR UP LEFT
DIRUPLT_OR = lambda X_: DIRUPLT_VAL | X_  # FLAG DIR DOWN or lambda
DIRUPLT_VAL = 0B1001  # FLAG DIR UP LEFT
DIRUPRT = 0B0011  # FLAG DIR UP RIGHT
DIRUPRT_AND = lambda X_: DIRUPRT_VAL & X_  # FLAG DIR DOWN and lambda
DIRUPRT_MSK_AND = lambda X_: DIRUPRT_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRUPRT_MSK_OR = lambda X_: DIRUPRT_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRUPRT_MSK_VAL = 0B1100  # MASK DIR UP RIGHT
DIRUPRT_OR = lambda X_: DIRUPRT_VAL | X_  # FLAG DIR DOWN or lambda
DIRUPRT_VAL = 0B0011  # UPRT direction VAL
DIRUP_AND = lambda X_: DIRUP_VAL & X_  # FLAG DIR UP and lambda
DIRUP_MSK_AND = lambda X_: DIRUP_MSK_VAL & X_  # FLAG DIR DOWN and lambda
DIRUP_MSK_OR = lambda X_: DIRUP_MSK_VAL | X_  # FLAG DIR DOWN or lambda
DIRUP_MSK_VAL = 0B1110  # MASK DIR UP
DIRUP_OR = lambda X_: DIRUP_VAL | X_  # FLAG DIR UP or lambda
DIRUP_VAL = 0B0001  # FLAG DIR UP
DIRX_AND = lambda X_: DIRX_VAL & X_  # FLAG DIR LTRT and lambda
DIRX_OR = lambda X_: DIRX_VAL | X_  # FLAG DIR LTRT or lambda
DIRX_VAL = 0B1010  # LTRT directions
DIRY_AND = lambda X_: DIRY_VAL & X_  # FLAG DIR UPDN and lambda
DIRY_OR = lambda X_: DIRY_VAL | X_  # FLAG DIR UPDN or lambda
DIRY_VAL = 0B0101  # UP/DN directions
DORPT_CRSR = 200  # cursor repeat
DORPT_MSE = 10  # mouse repeat
DORPT_NOT = 0  # no repeat
DORPT_PAUSE = 250  # pause before repeating
DORPT_WHL = 100  # mouse  wheelrepeat
ERRORNOT = 0X00000000  # FLAG NOTHING is ERROR
ERRORTDELTA = 30000  # FLAG NOTHING is ERROR
HATMAX = 1  # HAT MAX
HATMID = 0  # HAT MID/REST
HATMIN = -1  # HAT MIN
JOYSTICKDEAD = 120  # DEAD zone on a lo rez ABS device
JOYSTICKMAX = 255  # MAX on lo rez ABS device
JOYSTICKMID = 128  # MID on lo rez ABS device
JOYSTICKMIN = 0  # MIN on lo rez ABS device
KEYHLD = 0X02  # KEY held
KEYPRS = 0X01  # KEY pressed
KEYPRSHLD = 0X03  # KEY pressed held
KEYRLS = 0X00  # KEY released
LOGITECH = "LOGITECH"  # device Logitech trackman marble
MIMD = "MIMD"  # define MIMD gamepad
MOUSEDISTANCE = 2  # how far to move the mouse per event
MOUSEDISTANCEARB = 2  # how far to move the mouse per event
OBJMODE_CLASS = "OBJMODE_CLASS"  # dict key for class internal []{}
OBJMODE_STANDALONE = "OBJMODE_STANDALONE"  # dict key for standalone []{}
OBJMODE_STANDALONECLASS = "OBJMODE_STANDALONECLASS"  # dict key for a class []{}
OBJMODE_TAB1 = "OBJMODE_TAB1"  # dict key for a []{} with a tab before name_, 2 before entries
OBJMODE_TAB2 = "OBJMODE_TAB2"  # 2 tabs before name_, 3 before entries
SAITEK = "SAITEK"  # device Saitek controller
SPCL_PAUSE = "SPCL_PAUSE"  # special action pause
WHEELDISTANCE = 1  # how many clicks of the wheel per event


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN47 buttons lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
BTNSHOLDABLELIST = [
	BTNG_05,
	BTNG_06,
	BTNG_07,
	BTNG_08,
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN42 LDIE entries
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DOVAL_SPCL_PAUSE30F = (SPCL_PAUSE, 30)  # pause 3/10 seconds
DOVAL_SPCL_PAUSE3S = (SPCL_PAUSE, 300)  # pause 3 seconds
DOVAL_SPCL_PAUSE50F = (SPCL_PAUSE, 50)  # pause 1/2 seconds
GBTNC_HLD = IE(LD.EV_KEY.BTN_C, KEYHLD)  # comment
GBTNC_PRS = IE(LD.EV_KEY.BTN_C, KEYPRS)  # comment
GBTNC_RLS = IE(LD.EV_KEY.BTN_C, KEYRLS)  # comment
GBTNEAST_HLD = IE(LD.EV_KEY.BTN_EAST, KEYHLD)  # comment
GBTNEAST_PRS = IE(LD.EV_KEY.BTN_EAST, KEYPRS)  # comment
GBTNEAST_RLS = IE(LD.EV_KEY.BTN_EAST, KEYRLS)  # comment
GBTNMODE_HLD = IE(LD.EV_KEY.BTN_MODE, KEYHLD)  # comment
GBTNMODE_PRS = IE(LD.EV_KEY.BTN_MODE, KEYPRS)  # comment
GBTNMODE_RLS = IE(LD.EV_KEY.BTN_MODE, KEYRLS)  # comment
GBTNNORTH_HLD = IE(LD.EV_KEY.BTN_NORTH, KEYHLD)  # comment
GBTNNORTH_PRS = IE(LD.EV_KEY.BTN_NORTH, KEYPRS)  # comment
GBTNNORTH_RLS = IE(LD.EV_KEY.BTN_NORTH, KEYRLS)  # comment
GBTNSELECT_HLD = IE(LD.EV_KEY.BTN_SELECT, KEYHLD)  # comment
GBTNSELECT_PRS = IE(LD.EV_KEY.BTN_SELECT, KEYPRS)  # comment
GBTNSELECT_RLS = IE(LD.EV_KEY.BTN_SELECT, KEYRLS)  # comment
GBTNSOUTH_HLD = IE(LD.EV_KEY.BTN_SOUTH, KEYHLD)  # comment
GBTNSOUTH_PRS = IE(LD.EV_KEY.BTN_SOUTH, KEYPRS)  # comment
GBTNSOUTH_RLS = IE(LD.EV_KEY.BTN_SOUTH, KEYRLS)  # comment
GBTNSTART_HLD = IE(LD.EV_KEY.BTN_START, KEYHLD)  # comment
GBTNSTART_PRS = IE(LD.EV_KEY.BTN_START, KEYPRS)  # comment
GBTNSTART_RLS = IE(LD.EV_KEY.BTN_START, KEYRLS)  # comment
GBTNTL2_HLD = IE(LD.EV_KEY.BTN_TL2, KEYHLD)  # comment
GBTNTL2_PRS = IE(LD.EV_KEY.BTN_TL2, KEYPRS)  # comment
GBTNTL2_RLS = IE(LD.EV_KEY.BTN_TL2, KEYRLS)  # comment
GBTNTL_HLD = IE(LD.EV_KEY.BTN_TL, KEYHLD)  # comment
GBTNTL_PRS = IE(LD.EV_KEY.BTN_TL, KEYPRS)  # comment
GBTNTL_RLS = IE(LD.EV_KEY.BTN_TL, KEYRLS)  # comment
GBTNTR2_HLD = IE(LD.EV_KEY.BTN_TR2, KEYHLD)  # comment
GBTNTR2_PRS = IE(LD.EV_KEY.BTN_TR2, KEYPRS)  # comment
GBTNTR2_RLS = IE(LD.EV_KEY.BTN_TR2, KEYRLS)  # comment
GBTNTR_HLD = IE(LD.EV_KEY.BTN_TR, KEYHLD)  # comment
GBTNTR_PRS = IE(LD.EV_KEY.BTN_TR, KEYPRS)  # comment
GBTNTR_RLS = IE(LD.EV_KEY.BTN_TR, KEYRLS)  # comment
GBTNWEST_HLD = IE(LD.EV_KEY.BTN_WEST, KEYHLD)  # comment
GBTNWEST_PRS = IE(LD.EV_KEY.BTN_WEST, KEYPRS)  # comment
GBTNWEST_RLS = IE(LD.EV_KEY.BTN_WEST, KEYRLS)  # comment
GBTNZ_HLD = IE(LD.EV_KEY.BTN_Z, KEYHLD)  # comment
GBTNZ_PRS = IE(LD.EV_KEY.BTN_Z, KEYPRS)  # comment
GBTNZ_RLS = IE(LD.EV_KEY.BTN_Z, KEYRLS)  # comment
KBD0_HLD = IE(LD.EV_KEY.KEY_0, KEYHLD)  # 0_held
KBD0_PRS = IE(LD.EV_KEY.KEY_0, KEYPRS)  # 0_pressed
KBD0_RLS = IE(LD.EV_KEY.KEY_0, KEYRLS)  # 0_released
KBD102_HLD = IE(LD.EV_KEY.KEY_102ND, KEYHLD)  # 102_held
KBD102_PRS = IE(LD.EV_KEY.KEY_102ND, KEYPRS)  # 102_pressed
KBD102_RLS = IE(LD.EV_KEY.KEY_102ND, KEYRLS)  # 102_released
KBD1_HLD = IE(LD.EV_KEY.KEY_1, KEYHLD)  # 1_held
KBD1_PRS = IE(LD.EV_KEY.KEY_1, KEYPRS)  # 1_pressed
KBD1_RLS = IE(LD.EV_KEY.KEY_1, KEYRLS)  # 1_released
KBD2_HLD = IE(LD.EV_KEY.KEY_2, KEYHLD)  # 2_held
KBD2_PRS = IE(LD.EV_KEY.KEY_2, KEYPRS)  # 2_pressed
KBD2_RLS = IE(LD.EV_KEY.KEY_2, KEYRLS)  # 2_released
KBD3_HLD = IE(LD.EV_KEY.KEY_3, KEYHLD)  # 3_held
KBD3_PRS = IE(LD.EV_KEY.KEY_3, KEYPRS)  # 3_pressed
KBD3_RLS = IE(LD.EV_KEY.KEY_3, KEYRLS)  # 3_released
KBD4_HLD = IE(LD.EV_KEY.KEY_4, KEYHLD)  # 4_held
KBD4_PRS = IE(LD.EV_KEY.KEY_4, KEYPRS)  # 4_pressed
KBD4_RLS = IE(LD.EV_KEY.KEY_4, KEYRLS)  # 4_released
KBD5_HLD = IE(LD.EV_KEY.KEY_5, KEYHLD)  # 5_held
KBD5_PRS = IE(LD.EV_KEY.KEY_5, KEYPRS)  # 5_pressed
KBD5_RLS = IE(LD.EV_KEY.KEY_5, KEYRLS)  # 5_released
KBD6_HLD = IE(LD.EV_KEY.KEY_6, KEYHLD)  # 6_held
KBD6_PRS = IE(LD.EV_KEY.KEY_6, KEYPRS)  # 6_pressed
KBD6_RLS = IE(LD.EV_KEY.KEY_6, KEYRLS)  # 6_released
KBD7_HLD = IE(LD.EV_KEY.KEY_7, KEYHLD)  # 7_held
KBD7_PRS = IE(LD.EV_KEY.KEY_7, KEYPRS)  # 7_pressed
KBD7_RLS = IE(LD.EV_KEY.KEY_7, KEYRLS)  # 7_released
KBD8_HLD = IE(LD.EV_KEY.KEY_8, KEYHLD)  # 8_held
KBD8_PRS = IE(LD.EV_KEY.KEY_8, KEYPRS)  # 8_pressed
KBD8_RLS = IE(LD.EV_KEY.KEY_8, KEYRLS)  # 8_released
KBD9_HLD = IE(LD.EV_KEY.KEY_9, KEYHLD)  # 9_held
KBD9_PRS = IE(LD.EV_KEY.KEY_9, KEYPRS)  # 9_pressed
KBD9_RLS = IE(LD.EV_KEY.KEY_9, KEYRLS)  # 9_released
KBDAGAIN_HLD = IE(LD.EV_KEY.KEY_AGAIN, KEYHLD)  # AGAIN_held
KBDAGAIN_PRS = IE(LD.EV_KEY.KEY_AGAIN, KEYPRS)  # AGAIN_pressed
KBDAGAIN_RLS = IE(LD.EV_KEY.KEY_AGAIN, KEYRLS)  # AGAIN_released
KBDALTLT_HLD = IE(LD.EV_KEY.KEY_LEFTALT, KEYHLD)  # ALT_held
KBDALTLT_PRS = IE(LD.EV_KEY.KEY_LEFTALT, KEYPRS)  # ALT_pressed
KBDALTLT_RLS = IE(LD.EV_KEY.KEY_LEFTALT, KEYRLS)  # ALT_released
KBDALTRT_HLD = IE(LD.EV_KEY.KEY_RIGHTALT, KEYHLD)  # RALT_held
KBDALTRT_PRS = IE(LD.EV_KEY.KEY_RIGHTALT, KEYPRS)  # RALT_pressed
KBDALTRT_RLS = IE(LD.EV_KEY.KEY_RIGHTALT, KEYRLS)  # RALT_released
KBDAPOSTROPHE_HLD = IE(LD.EV_KEY.KEY_APOSTROPHE, KEYHLD)  # APOSTROPHE_held
KBDAPOSTROPHE_PRS = IE(LD.EV_KEY.KEY_APOSTROPHE, KEYPRS)  # APOSTROPHE_pressed
KBDAPOSTROPHE_RLS = IE(LD.EV_KEY.KEY_APOSTROPHE, KEYRLS)  # APOSTROPHE_released
KBDA_HLD = IE(LD.EV_KEY.KEY_A, KEYHLD)  # A_held
KBDA_PRS = IE(LD.EV_KEY.KEY_A, KEYPRS)  # A_pressed
KBDA_RLS = IE(LD.EV_KEY.KEY_A, KEYRLS)  # A_released
KBDBKSLASH_HLD = IE(LD.EV_KEY.KEY_BACKSLASH, KEYHLD)  # BACKSLASH_held
KBDBKSLASH_PRS = IE(LD.EV_KEY.KEY_BACKSLASH, KEYPRS)  # BACKSLASH_pressed
KBDBKSLASH_RLS = IE(LD.EV_KEY.KEY_BACKSLASH, KEYRLS)  # BACKSLASH_released
KBDBKSPC_HLD = IE(LD.EV_KEY.KEY_BACKSPACE, KEYHLD)  # BACKSPACE_held
KBDBKSPC_PRS = IE(LD.EV_KEY.KEY_BACKSPACE, KEYPRS)  # BACKSPACE_pressed
KBDBKSPC_RLS = IE(LD.EV_KEY.KEY_BACKSPACE, KEYRLS)  # BACKSPACE_released
KBDBK_HLD = IE(LD.EV_KEY.KEY_BACK, KEYHLD)  # BK_held
KBDBK_PRS = IE(LD.EV_KEY.KEY_BACK, KEYPRS)  # BK_pressed
KBDBK_RLS = IE(LD.EV_KEY.KEY_BACK, KEYRLS)  # BK_released
KBDBRACELT_HLD = IE(LD.EV_KEY.KEY_LEFTBRACE, KEYHLD)  # LBRACE_held
KBDBRACELT_PRS = IE(LD.EV_KEY.KEY_LEFTBRACE, KEYPRS)  # LBRACE_pressed
KBDBRACELT_RLS = IE(LD.EV_KEY.KEY_LEFTBRACE, KEYRLS)  # LBRACE_released
KBDBRACERT_HLD = IE(LD.EV_KEY.KEY_RIGHTBRACE, KEYHLD)  # RBRACE_held
KBDBRACERT_PRS = IE(LD.EV_KEY.KEY_RIGHTBRACE, KEYPRS)  # RBRACE_pressed
KBDBRACERT_RLS = IE(LD.EV_KEY.KEY_RIGHTBRACE, KEYRLS)  # RBRACE_released
KBDB_HLD = IE(LD.EV_KEY.KEY_B, KEYHLD)  # B_held_held
KBDB_PRS = IE(LD.EV_KEY.KEY_B, KEYPRS)  # B_pressed
KBDB_RLS = IE(LD.EV_KEY.KEY_B, KEYRLS)  # B_released
KBDCALC_HLD = IE(LD.EV_KEY.KEY_CALC, KEYHLD)  # CALC_held
KBDCALC_PRS = IE(LD.EV_KEY.KEY_CALC, KEYPRS)  # CALC_pressed
KBDCALC_RLS = IE(LD.EV_KEY.KEY_CALC, KEYRLS)  # CALC_released
KBDCAPSLK_HLD = IE(LD.EV_KEY.KEY_CAPSLOCK, KEYHLD)  # CAPS_held
KBDCAPSLK_PRS = IE(LD.EV_KEY.KEY_CAPSLOCK, KEYPRS)  # CAPS_pressed
KBDCAPSLK_RLS = IE(LD.EV_KEY.KEY_CAPSLOCK, KEYRLS)  # CAPS_released
KBDCOFFEE_HLD = IE(LD.EV_KEY.KEY_COFFEE, KEYHLD)  # COFFEE_held
KBDCOFFEE_PRS = IE(LD.EV_KEY.KEY_COFFEE, KEYPRS)  # COFFEE_pressed
KBDCOFFEE_RLS = IE(LD.EV_KEY.KEY_COFFEE, KEYRLS)  # COFFEE_released
KBDCOMMA_HLD = IE(LD.EV_KEY.KEY_COMMA, KEYHLD)  # COMMA_held
KBDCOMMA_PRS = IE(LD.EV_KEY.KEY_COMMA, KEYPRS)  # COMMA_pressed
KBDCOMMA_RLS = IE(LD.EV_KEY.KEY_COMMA, KEYRLS)  # COMMA_released
KBDCOMPOSE_HLD = IE(LD.EV_KEY.KEY_COMPOSE, KEYHLD)  # COMPOSE_held
KBDCOMPOSE_PRS = IE(LD.EV_KEY.KEY_COMPOSE, KEYPRS)  # COMPOSE_pressed
KBDCOMPOSE_RLS = IE(LD.EV_KEY.KEY_COMPOSE, KEYRLS)  # COMPOSE_released
KBDCOPY_HLD = IE(LD.EV_KEY.KEY_COPY, KEYHLD)  # COPY_held
KBDCOPY_PRS = IE(LD.EV_KEY.KEY_COPY, KEYPRS)  # COPY_pressed
KBDCOPY_RLS = IE(LD.EV_KEY.KEY_COPY, KEYRLS)  # COPY_released
KBDCTRLLT_HLD = IE(LD.EV_KEY.KEY_LEFTCTRL, KEYHLD)  # LCTRL_held
KBDCTRLLT_PRS = IE(LD.EV_KEY.KEY_LEFTCTRL, KEYPRS)  # LCTRL_pressed
KBDCTRLLT_RLS = IE(LD.EV_KEY.KEY_LEFTCTRL, KEYRLS)  # LCTRL_released
KBDCTRLRT_HLD = IE(LD.EV_KEY.KEY_RIGHTCTRL, KEYHLD)  # RCTRL_held
KBDCTRLRT_PRS = IE(LD.EV_KEY.KEY_RIGHTCTRL, KEYPRS)  # RCTRL_pressed
KBDCTRLRT_RLS = IE(LD.EV_KEY.KEY_RIGHTCTRL, KEYRLS)  # RCTRL_released
KBDCUT_HLD = IE(LD.EV_KEY.KEY_CUT, KEYHLD)  # CUT_held
KBDCUT_PRS = IE(LD.EV_KEY.KEY_CUT, KEYPRS)  # CUT_pressed
KBDCUT_RLS = IE(LD.EV_KEY.KEY_CUT, KEYRLS)  # CUT_released
KBDC_HLD = IE(LD.EV_KEY.KEY_C, KEYHLD)  # C_held
KBDC_PRS = IE(LD.EV_KEY.KEY_C, KEYPRS)  # C_pressed
KBDC_RLS = IE(LD.EV_KEY.KEY_C, KEYRLS)  # C_released
KBDDEL_HLD = IE(LD.EV_KEY.KEY_DELETE, KEYHLD)  # DEL_held
KBDDEL_PRS = IE(LD.EV_KEY.KEY_DELETE, KEYPRS)  # DEL_pressed
KBDDEL_RLS = IE(LD.EV_KEY.KEY_DELETE, KEYRLS)  # DEL_released
KBDDN_HLD = IE(LD.EV_KEY.KEY_DOWN, KEYHLD)  # DOWN_held
KBDDN_PRS = IE(LD.EV_KEY.KEY_DOWN, KEYPRS)  # DOWN_pressed
KBDDN_RLS = IE(LD.EV_KEY.KEY_DOWN, KEYRLS)  # DOWN_released
KBDDOT_HLD = IE(LD.EV_KEY.KEY_DOT, KEYHLD)  # DOT_held
KBDDOT_PRS = IE(LD.EV_KEY.KEY_DOT, KEYPRS)  # DOT_pressed
KBDDOT_RLS = IE(LD.EV_KEY.KEY_DOT, KEYRLS)  # DOT_released
KBDD_HLD = IE(LD.EV_KEY.KEY_D, KEYHLD)  # D_held
KBDD_PRS = IE(LD.EV_KEY.KEY_D, KEYPRS)  # D_pressed
KBDD_RLS = IE(LD.EV_KEY.KEY_D, KEYRLS)  # D_released
KBDEDIT_HLD = IE(LD.EV_KEY.KEY_EDIT, KEYHLD)  # EDIT_held
KBDEDIT_PRS = IE(LD.EV_KEY.KEY_EDIT, KEYPRS)  # EDIT_pressed
KBDEDIT_RLS = IE(LD.EV_KEY.KEY_EDIT, KEYRLS)  # EDIT_released
KBDEJECTCD_HLD = IE(LD.EV_KEY.KEY_EJECTCD, KEYHLD)  # EJECTCD_held
KBDEJECTCD_PRS = IE(LD.EV_KEY.KEY_EJECTCD, KEYPRS)  # EJECTCD_pressed
KBDEJECTCD_RLS = IE(LD.EV_KEY.KEY_EJECTCD, KEYRLS)  # EJECTCD_released
KBDEND_HLD = IE(LD.EV_KEY.KEY_END, KEYHLD)  # END_held
KBDEND_PRS = IE(LD.EV_KEY.KEY_END, KEYPRS)  # END_pressed
KBDEND_RLS = IE(LD.EV_KEY.KEY_END, KEYRLS)  # END_released
KBDENTER_HLD = IE(LD.EV_KEY.KEY_ENTER, KEYHLD)  # ENTER_held
KBDENTER_PRS = IE(LD.EV_KEY.KEY_ENTER, KEYPRS)  # ENTER_pressed
KBDENTER_RLS = IE(LD.EV_KEY.KEY_ENTER, KEYRLS)  # ENTER_released
KBDEQ_HLD = IE(LD.EV_KEY.KEY_EQUAL, KEYHLD)  # EQUAL_held
KBDEQ_PRS = IE(LD.EV_KEY.KEY_EQUAL, KEYPRS)  # EQUAL_pressed
KBDEQ_RLS = IE(LD.EV_KEY.KEY_EQUAL, KEYRLS)  # EQUAL_released
KBDESC_HLD = IE(LD.EV_KEY.KEY_ESC, KEYHLD)  # ESC_held
KBDESC_PRS = IE(LD.EV_KEY.KEY_ESC, KEYPRS)  # ESC_pressed
KBDESC_RLS = IE(LD.EV_KEY.KEY_ESC, KEYRLS)  # ESC_released
KBDE_HLD = IE(LD.EV_KEY.KEY_E, KEYHLD)  # E_held
KBDE_PRS = IE(LD.EV_KEY.KEY_E, KEYPRS)  # E_pressed
KBDE_RLS = IE(LD.EV_KEY.KEY_E, KEYRLS)  # E_released
KBDF10_HLD = IE(LD.EV_KEY.KEY_F10, KEYHLD)  # F10_held
KBDF10_PRS = IE(LD.EV_KEY.KEY_F10, KEYPRS)  # F10_pressed
KBDF10_RLS = IE(LD.EV_KEY.KEY_F10, KEYRLS)  # F10_released
KBDF11_HLD = IE(LD.EV_KEY.KEY_F11, KEYHLD)  # F11_held
KBDF11_PRS = IE(LD.EV_KEY.KEY_F11, KEYPRS)  # F11_pressed
KBDF11_RLS = IE(LD.EV_KEY.KEY_F11, KEYRLS)  # F11_released
KBDF12_HLD = IE(LD.EV_KEY.KEY_F12, KEYHLD)  # F12_held
KBDF12_PRS = IE(LD.EV_KEY.KEY_F12, KEYPRS)  # F12_pressed
KBDF12_RLS = IE(LD.EV_KEY.KEY_F12, KEYRLS)  # F12_released
KBDF13_HLD = IE(LD.EV_KEY.KEY_F13, KEYHLD)  # F13_held
KBDF13_PRS = IE(LD.EV_KEY.KEY_F13, KEYPRS)  # F13_pressed
KBDF13_RLS = IE(LD.EV_KEY.KEY_F13, KEYRLS)  # F13_released
KBDF14_HLD = IE(LD.EV_KEY.KEY_F14, KEYHLD)  # F14_held
KBDF14_PRS = IE(LD.EV_KEY.KEY_F14, KEYPRS)  # F14_pressed
KBDF14_RLS = IE(LD.EV_KEY.KEY_F14, KEYRLS)  # F14_released
KBDF15_HLD = IE(LD.EV_KEY.KEY_F15, KEYHLD)  # F15_held
KBDF15_PRS = IE(LD.EV_KEY.KEY_F15, KEYPRS)  # F15_pressed
KBDF15_RLS = IE(LD.EV_KEY.KEY_F15, KEYRLS)  # F15_released
KBDF16_HLD = IE(LD.EV_KEY.KEY_F16, KEYHLD)  # F16_held
KBDF16_PRS = IE(LD.EV_KEY.KEY_F16, KEYPRS)  # F16_pressed
KBDF16_RLS = IE(LD.EV_KEY.KEY_F16, KEYRLS)  # F16_released
KBDF17_HLD = IE(LD.EV_KEY.KEY_F17, KEYHLD)  # F17_held
KBDF17_PRS = IE(LD.EV_KEY.KEY_F17, KEYPRS)  # F17_pressed
KBDF17_RLS = IE(LD.EV_KEY.KEY_F17, KEYRLS)  # F17_released
KBDF18_HLD = IE(LD.EV_KEY.KEY_F18, KEYHLD)  # F18_held
KBDF18_PRS = IE(LD.EV_KEY.KEY_F18, KEYPRS)  # F18_pressed
KBDF18_RLS = IE(LD.EV_KEY.KEY_F18, KEYRLS)  # F18_released
KBDF19_HLD = IE(LD.EV_KEY.KEY_F19, KEYHLD)  # F19_held
KBDF19_PRS = IE(LD.EV_KEY.KEY_F19, KEYPRS)  # F19_pressed
KBDF19_RLS = IE(LD.EV_KEY.KEY_F19, KEYRLS)  # F19_released
KBDF1_HLD = IE(LD.EV_KEY.KEY_F1, KEYHLD)  # F1_held
KBDF1_PRS = IE(LD.EV_KEY.KEY_F1, KEYPRS)  # F1_pressed
KBDF1_RLS = IE(LD.EV_KEY.KEY_F1, KEYRLS)  # F1_released
KBDF20_HLD = IE(LD.EV_KEY.KEY_F20, KEYHLD)  # F20_held
KBDF20_PRS = IE(LD.EV_KEY.KEY_F20, KEYPRS)  # F20_pressed
KBDF20_RLS = IE(LD.EV_KEY.KEY_F20, KEYRLS)  # F20_released
KBDF21_HLD = IE(LD.EV_KEY.KEY_F21, KEYHLD)  # F21_held
KBDF21_PRS = IE(LD.EV_KEY.KEY_F21, KEYPRS)  # F21_pressed
KBDF21_RLS = IE(LD.EV_KEY.KEY_F21, KEYRLS)  # F21_released
KBDF22_HLD = IE(LD.EV_KEY.KEY_F22, KEYHLD)  # F22_held
KBDF22_PRS = IE(LD.EV_KEY.KEY_F22, KEYPRS)  # F22_pressed
KBDF22_RLS = IE(LD.EV_KEY.KEY_F22, KEYRLS)  # F22_released
KBDF23_HLD = IE(LD.EV_KEY.KEY_F23, KEYHLD)  # F23_held
KBDF23_PRS = IE(LD.EV_KEY.KEY_F23, KEYPRS)  # F23_pressed
KBDF23_RLS = IE(LD.EV_KEY.KEY_F23, KEYRLS)  # F23_released
KBDF24_HLD = IE(LD.EV_KEY.KEY_F24, KEYHLD)  # F24_held
KBDF24_PRS = IE(LD.EV_KEY.KEY_F24, KEYPRS)  # F24_pressed
KBDF24_RLS = IE(LD.EV_KEY.KEY_F24, KEYRLS)  # F24_released
KBDF2_HLD = IE(LD.EV_KEY.KEY_F2, KEYHLD)  # F2_held
KBDF2_PRS = IE(LD.EV_KEY.KEY_F2, KEYPRS)  # F2_pressed
KBDF2_RLS = IE(LD.EV_KEY.KEY_F2, KEYRLS)  # F2_released
KBDF3_HLD = IE(LD.EV_KEY.KEY_F3, KEYHLD)  # F3_held
KBDF3_PRS = IE(LD.EV_KEY.KEY_F3, KEYPRS)  # F3_pressed
KBDF3_RLS = IE(LD.EV_KEY.KEY_F3, KEYRLS)  # F3_released
KBDF4_HLD = IE(LD.EV_KEY.KEY_F4, KEYHLD)  # F4_held
KBDF4_PRS = IE(LD.EV_KEY.KEY_F4, KEYPRS)  # F4_pressed
KBDF4_RLS = IE(LD.EV_KEY.KEY_F4, KEYRLS)  # F4_released
KBDF5_HLD = IE(LD.EV_KEY.KEY_F5, KEYHLD)  # F5_held
KBDF5_PRS = IE(LD.EV_KEY.KEY_F5, KEYPRS)  # F5_pressed
KBDF5_RLS = IE(LD.EV_KEY.KEY_F5, KEYRLS)  # F5_released
KBDF6_HLD = IE(LD.EV_KEY.KEY_F6, KEYHLD)  # F6_held
KBDF6_PRS = IE(LD.EV_KEY.KEY_F6, KEYPRS)  # F6_pressed
KBDF6_RLS = IE(LD.EV_KEY.KEY_F6, KEYRLS)  # F6_released
KBDF7_HLD = IE(LD.EV_KEY.KEY_F7, KEYHLD)  # F7_held
KBDF7_PRS = IE(LD.EV_KEY.KEY_F7, KEYPRS)  # F7_pressed
KBDF7_RLS = IE(LD.EV_KEY.KEY_F7, KEYRLS)  # F7_released
KBDF8_HLD = IE(LD.EV_KEY.KEY_F8, KEYHLD)  # F8_held
KBDF8_PRS = IE(LD.EV_KEY.KEY_F8, KEYPRS)  # F8_pressed
KBDF8_RLS = IE(LD.EV_KEY.KEY_F8, KEYRLS)  # F8_released
KBDF9_HLD = IE(LD.EV_KEY.KEY_F9, KEYHLD)  # F9_held
KBDF9_PRS = IE(LD.EV_KEY.KEY_F9, KEYPRS)  # F9_pressed
KBDF9_RLS = IE(LD.EV_KEY.KEY_F9, KEYRLS)  # F9_released
KBDFIND_HLD = IE(LD.EV_KEY.KEY_FIND, KEYHLD)  # FIND_held
KBDFIND_PRS = IE(LD.EV_KEY.KEY_FIND, KEYPRS)  # FIND_pressed
KBDFIND_RLS = IE(LD.EV_KEY.KEY_FIND, KEYRLS)  # FIND_released
KBDFORWARD_HLD = IE(LD.EV_KEY.KEY_FORWARD, KEYHLD)  # FORWARD_held
KBDFORWARD_PRS = IE(LD.EV_KEY.KEY_FORWARD, KEYPRS)  # FORWARD_pressed
KBDFORWARD_RLS = IE(LD.EV_KEY.KEY_FORWARD, KEYRLS)  # FORWARD_released
KBDFRONT_HLD = IE(LD.EV_KEY.KEY_FRONT, KEYHLD)  # FRONT_held
KBDFRONT_PRS = IE(LD.EV_KEY.KEY_FRONT, KEYPRS)  # FRONT_pressed
KBDFRONT_RLS = IE(LD.EV_KEY.KEY_FRONT, KEYRLS)  # FRONT_released
KBDF_HLD = IE(LD.EV_KEY.KEY_F, KEYHLD)  # F_held
KBDF_PRS = IE(LD.EV_KEY.KEY_F, KEYPRS)  # F_pressed
KBDF_RLS = IE(LD.EV_KEY.KEY_F, KEYRLS)  # F_released
KBDGRAVE_HLD = IE(LD.EV_KEY.KEY_GRAVE, KEYHLD)  # GRAVÉ_held
KBDGRAVE_PRS = IE(LD.EV_KEY.KEY_GRAVE, KEYPRS)  # GRAVÉ_pressed
KBDGRAVE_RLS = IE(LD.EV_KEY.KEY_GRAVE, KEYRLS)  # GRAVÉ_released
KBDG_HLD = IE(LD.EV_KEY.KEY_G, KEYHLD)  # G_held
KBDG_PRS = IE(LD.EV_KEY.KEY_G, KEYPRS)  # G_pressed
KBDG_RLS = IE(LD.EV_KEY.KEY_G, KEYRLS)  # G_released
KBDHANGUEL_HLD = IE(LD.EV_KEY.KEY_HANGEUL, KEYHLD)  # HANGUEL_held
KBDHANGUEL_PRS = IE(LD.EV_KEY.KEY_HANGEUL, KEYPRS)  # HANGUEL_pressed
KBDHANGUEL_RLS = IE(LD.EV_KEY.KEY_HANGEUL, KEYRLS)  # HANGUEL_released
KBDHANJA_HLD = IE(LD.EV_KEY.KEY_HANJA, KEYHLD)  # HANJA_held
KBDHANJA_PRS = IE(LD.EV_KEY.KEY_HANJA, KEYPRS)  # HANJA_pressed
KBDHANJA_RLS = IE(LD.EV_KEY.KEY_HANJA, KEYRLS)  # HANJA_released
KBDHELP_HLD = IE(LD.EV_KEY.KEY_HELP, KEYHLD)  # HELP_held
KBDHELP_PRS = IE(LD.EV_KEY.KEY_HELP, KEYPRS)  # HELP_pressed
KBDHELP_RLS = IE(LD.EV_KEY.KEY_HELP, KEYRLS)  # HELP_released
KBDHENKAN_HLD = IE(LD.EV_KEY.KEY_HENKAN, KEYHLD)  # HENKAN_held
KBDHENKAN_PRS = IE(LD.EV_KEY.KEY_HENKAN, KEYPRS)  # HENKAN_pressed
KBDHENKAN_RLS = IE(LD.EV_KEY.KEY_HENKAN, KEYRLS)  # HENKAN_released
KBDHIRAGANA_HLD = IE(LD.EV_KEY.KEY_HIRAGANA, KEYHLD)  # HIRAGANA_held
KBDHIRAGANA_PRS = IE(LD.EV_KEY.KEY_HIRAGANA, KEYPRS)  # HIRAGANA_pressed
KBDHIRAGANA_RLS = IE(LD.EV_KEY.KEY_HIRAGANA, KEYRLS)  # HIRAGANA_released
KBDHOME_HLD = IE(LD.EV_KEY.KEY_HOME, KEYHLD)  # HOME_held
KBDHOME_PRS = IE(LD.EV_KEY.KEY_HOME, KEYPRS)  # HOME_pressed
KBDHOME_RLS = IE(LD.EV_KEY.KEY_HOME, KEYRLS)  # HOME_released
KBDH_HLD = IE(LD.EV_KEY.KEY_H, KEYHLD)  # H_held
KBDH_PRS = IE(LD.EV_KEY.KEY_H, KEYPRS)  # H_pressed
KBDH_RLS = IE(LD.EV_KEY.KEY_H, KEYRLS)  # H_released
KBDINSERT_HLD = IE(LD.EV_KEY.KEY_INSERT, KEYHLD)  # INSERT_held
KBDINSERT_PRS = IE(LD.EV_KEY.KEY_INSERT, KEYPRS)  # INSERT_pressed
KBDINSERT_RLS = IE(LD.EV_KEY.KEY_INSERT, KEYRLS)  # INSERT_released
KBDI_HLD = IE(LD.EV_KEY.KEY_I, KEYHLD)  # I_held
KBDI_PRS = IE(LD.EV_KEY.KEY_I, KEYPRS)  # I_pressed
KBDI_RLS = IE(LD.EV_KEY.KEY_I, KEYRLS)  # I_released
KBDJ_HLD = IE(LD.EV_KEY.KEY_J, KEYHLD)  # J_held
KBDJ_PRS = IE(LD.EV_KEY.KEY_J, KEYPRS)  # J_pressed
KBDJ_RLS = IE(LD.EV_KEY.KEY_J, KEYRLS)  # J_released
KBDKATAKANAHIRAGANA_HLD = IE(LD.EV_KEY.KEY_KATAKANAHIRAGANA, KEYHLD)  # KATAKANAHIRAGANA_held
KBDKATAKANAHIRAGANA_PRS = IE(LD.EV_KEY.KEY_KATAKANAHIRAGANA, KEYPRS)  # KATAKANAHIRAGANA_pressed
KBDKATAKANAHIRAGANA_RLS = IE(LD.EV_KEY.KEY_KATAKANAHIRAGANA, KEYRLS)  # KATAKANAHIRAGANA_released
KBDKATAKANA_HLD = IE(LD.EV_KEY.KEY_KATAKANA, KEYHLD)  # KATAKANA_held
KBDKATAKANA_PRS = IE(LD.EV_KEY.KEY_KATAKANA, KEYPRS)  # KATAKANA_pressed
KBDKATAKANA_RLS = IE(LD.EV_KEY.KEY_KATAKANA, KEYRLS)  # KATAKANA_released
KBDKP0_HLD = IE(LD.EV_KEY.KEY_KP0, KEYHLD)  # KP0_held
KBDKP0_PRS = IE(LD.EV_KEY.KEY_KP0, KEYPRS)  # KP0_pressed
KBDKP0_RLS = IE(LD.EV_KEY.KEY_KP0, KEYRLS)  # KP0_released
KBDKP1_HLD = IE(LD.EV_KEY.KEY_KP1, KEYHLD)  # KP1_held
KBDKP1_PRS = IE(LD.EV_KEY.KEY_KP1, KEYPRS)  # KP1_pressed
KBDKP1_RLS = IE(LD.EV_KEY.KEY_KP1, KEYRLS)  # KP1_released
KBDKP2_HLD = IE(LD.EV_KEY.KEY_KP2, KEYHLD)  # KP2_held
KBDKP2_PRS = IE(LD.EV_KEY.KEY_KP2, KEYPRS)  # KP2_pressed
KBDKP2_RLS = IE(LD.EV_KEY.KEY_KP2, KEYRLS)  # KP2_released
KBDKP3_HLD = IE(LD.EV_KEY.KEY_KP3, KEYHLD)  # KP3_held
KBDKP3_PRS = IE(LD.EV_KEY.KEY_KP3, KEYPRS)  # KP3_pressed
KBDKP3_RLS = IE(LD.EV_KEY.KEY_KP3, KEYRLS)  # KP3_released
KBDKP4_HLD = IE(LD.EV_KEY.KEY_KP4, KEYHLD)  # KP4_held
KBDKP4_PRS = IE(LD.EV_KEY.KEY_KP4, KEYPRS)  # KP4_pressed
KBDKP4_RLS = IE(LD.EV_KEY.KEY_KP4, KEYRLS)  # KP4_released
KBDKP5_HLD = IE(LD.EV_KEY.KEY_KP5, KEYHLD)  # KP5_held
KBDKP5_PRS = IE(LD.EV_KEY.KEY_KP5, KEYPRS)  # KP5_pressed
KBDKP5_RLS = IE(LD.EV_KEY.KEY_KP5, KEYRLS)  # KP5_released
KBDKP6_HLD = IE(LD.EV_KEY.KEY_KP6, KEYHLD)  # KP6_held
KBDKP6_PRS = IE(LD.EV_KEY.KEY_KP6, KEYPRS)  # KP6_pressed
KBDKP6_RLS = IE(LD.EV_KEY.KEY_KP6, KEYRLS)  # KP6_released
KBDKP7_HLD = IE(LD.EV_KEY.KEY_KP7, KEYHLD)  # KP7_held
KBDKP7_PRS = IE(LD.EV_KEY.KEY_KP7, KEYPRS)  # KP7_pressed
KBDKP7_RLS = IE(LD.EV_KEY.KEY_KP7, KEYRLS)  # KP7_released
KBDKP8_HLD = IE(LD.EV_KEY.KEY_KP8, KEYHLD)  # KP8_held
KBDKP8_PRS = IE(LD.EV_KEY.KEY_KP8, KEYPRS)  # KP8_pressed
KBDKP8_RLS = IE(LD.EV_KEY.KEY_KP8, KEYRLS)  # KP8_released
KBDKP9_HLD = IE(LD.EV_KEY.KEY_KP9, KEYHLD)  # KP9_held
KBDKP9_PRS = IE(LD.EV_KEY.KEY_KP9, KEYPRS)  # KP9_pressed
KBDKP9_RLS = IE(LD.EV_KEY.KEY_KP9, KEYRLS)  # KP9_released
KBDKPCOMMA_HLD = IE(LD.EV_KEY.KEY_KPCOMMA, KEYHLD)  # KPCOMMA_held
KBDKPCOMMA_PRS = IE(LD.EV_KEY.KEY_KPCOMMA, KEYPRS)  # KPCOMMA_pressed
KBDKPCOMMA_RLS = IE(LD.EV_KEY.KEY_KPCOMMA, KEYRLS)  # KPCOMMA_released
KBDKPDOT_HLD = IE(LD.EV_KEY.KEY_KPDOT, KEYHLD)  # KPDOT_held
KBDKPDOT_PRS = IE(LD.EV_KEY.KEY_KPDOT, KEYPRS)  # KPDOT_pressed
KBDKPDOT_RLS = IE(LD.EV_KEY.KEY_KPDOT, KEYRLS)  # KPDOT_released
KBDKPENTER_HLD = IE(LD.EV_KEY.KEY_KPENTER, KEYHLD)  # KPENTER_held
KBDKPENTER_PRS = IE(LD.EV_KEY.KEY_KPENTER, KEYPRS)  # KPENTER_pressed
KBDKPENTER_RLS = IE(LD.EV_KEY.KEY_KPENTER, KEYRLS)  # KPENTER_released
KBDKPJPCOMMA_HLD = IE(LD.EV_KEY.KEY_KPJPCOMMA, KEYHLD)  # KPJPCOMMA_held
KBDKPJPCOMMA_PRS = IE(LD.EV_KEY.KEY_KPJPCOMMA, KEYPRS)  # KPJPCOMMA_pressed
KBDKPJPCOMMA_RLS = IE(LD.EV_KEY.KEY_KPJPCOMMA, KEYRLS)  # KPJPCOMMA_released
KBDKPRPAREN_HLD = IE(LD.EV_KEY.KEY_KPRIGHTPAREN, KEYHLD)  # KPRPAREN_held
KBDKPRPAREN_PRS = IE(LD.EV_KEY.KEY_KPRIGHTPAREN, KEYPRS)  # KPRPAREN_pressed
KBDKPRPAREN_RLS = IE(LD.EV_KEY.KEY_KPRIGHTPAREN, KEYRLS)  # KPRPAREN_released
KBDKPSLASH_HLD = IE(LD.EV_KEY.KEY_KPSLASH, KEYHLD)  # KPSLASH_held
KBDKPSLASH_PRS = IE(LD.EV_KEY.KEY_KPSLASH, KEYPRS)  # KPSLASH_pressed
KBDKPSLASH_RLS = IE(LD.EV_KEY.KEY_KPSLASH, KEYRLS)  # KPSLASH_released
KBDK_HLD = IE(LD.EV_KEY.KEY_K, KEYHLD)  # K_held
KBDK_PRS = IE(LD.EV_KEY.KEY_K, KEYPRS)  # K_pressed
KBDK_RLS = IE(LD.EV_KEY.KEY_K, KEYRLS)  # K_released
KBDLT_HLD = IE(LD.EV_KEY.KEY_LEFT, KEYHLD)  # LEFT_held
KBDLT_PRS = IE(LD.EV_KEY.KEY_LEFT, KEYPRS)  # LEFT_pressed
KBDLT_RLS = IE(LD.EV_KEY.KEY_LEFT, KEYRLS)  # LEFT_released
KBDL_HLD = IE(LD.EV_KEY.KEY_L, KEYHLD)  # L_held
KBDL_PRS = IE(LD.EV_KEY.KEY_L, KEYPRS)  # L_pressed
KBDL_RLS = IE(LD.EV_KEY.KEY_L, KEYRLS)  # L_released
KBDMETALT_HLD = IE(LD.EV_KEY.KEY_LEFTMETA, KEYHLD)  # LMETA_held
KBDMETALT_PRS = IE(LD.EV_KEY.KEY_LEFTMETA, KEYPRS)  # LMETA_pressed
KBDMETALT_RLS = IE(LD.EV_KEY.KEY_LEFTMETA, KEYRLS)  # LMETA_released
KBDMETART_HLD = IE(LD.EV_KEY.KEY_RIGHTMETA, KEYHLD)  # RMETA_held
KBDMETART_PRS = IE(LD.EV_KEY.KEY_RIGHTMETA, KEYPRS)  # RMETA_pressed
KBDMETART_RLS = IE(LD.EV_KEY.KEY_RIGHTMETA, KEYRLS)  # RMETA_released
KBDMINUSKP_HLD = IE(LD.EV_KEY.KEY_KPMINUS, KEYHLD)  # KPMINUS_held
KBDMINUSKP_PRS = IE(LD.EV_KEY.KEY_KPMINUS, KEYPRS)  # KPMINUS_pressed
KBDMINUSKP_RLS = IE(LD.EV_KEY.KEY_KPMINUS, KEYRLS)  # KPMINUS_released
KBDMINUS_HLD = IE(LD.EV_KEY.KEY_MINUS, KEYHLD)  # MINUS_held
KBDMINUS_PRS = IE(LD.EV_KEY.KEY_MINUS, KEYPRS)  # MINUS_pressed
KBDMINUS_RLS = IE(LD.EV_KEY.KEY_MINUS, KEYRLS)  # MINUS_released
KBDMUHENKAN_HLD = IE(LD.EV_KEY.KEY_MUHENKAN, KEYHLD)  # MUHENKAN_held
KBDMUHENKAN_PRS = IE(LD.EV_KEY.KEY_MUHENKAN, KEYPRS)  # MUHENKAN_pressed
KBDMUHENKAN_RLS = IE(LD.EV_KEY.KEY_MUHENKAN, KEYRLS)  # MUHENKAN_released
KBDMUTE_HLD = IE(LD.EV_KEY.KEY_MUTE, KEYHLD)  # MUTE_held
KBDMUTE_PRS = IE(LD.EV_KEY.KEY_MUTE, KEYPRS)  # MUTE_pressed
KBDMUTE_RLS = IE(LD.EV_KEY.KEY_MUTE, KEYRLS)  # MUTE_released
KBDM_HLD = IE(LD.EV_KEY.KEY_M, KEYHLD)  # M_held
KBDM_PRS = IE(LD.EV_KEY.KEY_M, KEYPRS)  # M_pressed
KBDM_RLS = IE(LD.EV_KEY.KEY_M, KEYRLS)  # M_released
KBDNEXTSONG_HLD = IE(LD.EV_KEY.KEY_NEXTSONG, KEYHLD)  # NEXTSONG_held
KBDNEXTSONG_PRS = IE(LD.EV_KEY.KEY_NEXTSONG, KEYPRS)  # NEXTSONG_pressed
KBDNEXTSONG_RLS = IE(LD.EV_KEY.KEY_NEXTSONG, KEYRLS)  # NEXTSONG_released
KBDNUMLK_HLD = IE(LD.EV_KEY.KEY_NUMLOCK, KEYHLD)  # NUMLOCK_held
KBDNUMLK_PRS = IE(LD.EV_KEY.KEY_NUMLOCK, KEYPRS)  # NUMLOCK_pressed
KBDNUMLK_RLS = IE(LD.EV_KEY.KEY_NUMLOCK, KEYRLS)  # NUMLOCK_released
KBDN_HLD = IE(LD.EV_KEY.KEY_N, KEYHLD)  # DOWN_held
KBDN_PRS = IE(LD.EV_KEY.KEY_N, KEYPRS)  # DOWN_pressed
KBDN_RLS = IE(LD.EV_KEY.KEY_N, KEYRLS)  # DOWN_released
KBDOPEN_HLD = IE(LD.EV_KEY.KEY_OPEN, KEYHLD)  # OPEN_held
KBDOPEN_PRS = IE(LD.EV_KEY.KEY_OPEN, KEYPRS)  # OPEN_pressed
KBDOPEN_RLS = IE(LD.EV_KEY.KEY_OPEN, KEYRLS)  # OPEN_released
KBDO_HLD = IE(LD.EV_KEY.KEY_O, KEYHLD)  # O_held
KBDO_PRS = IE(LD.EV_KEY.KEY_O, KEYPRS)  # O_pressed
KBDO_RLS = IE(LD.EV_KEY.KEY_O, KEYRLS)  # O_released
KBDPARENLT_HLD = IE(LD.EV_KEY.KEY_KPLEFTPAREN, KEYHLD)  # KPLPAREN_held
KBDPARENLT_PRS = IE(LD.EV_KEY.KEY_KPLEFTPAREN, KEYPRS)  # KPLPAREN_pressed
KBDPARENLT_RLS = IE(LD.EV_KEY.KEY_KPLEFTPAREN, KEYRLS)  # KPLPAREN_released
KBDPASTE_HLD = IE(LD.EV_KEY.KEY_PASTE, KEYHLD)  # PASTE_held
KBDPASTE_PRS = IE(LD.EV_KEY.KEY_PASTE, KEYPRS)  # PASTE_pressed
KBDPASTE_RLS = IE(LD.EV_KEY.KEY_PASTE, KEYRLS)  # PASTE_released
KBDPAUSE_HLD = IE(LD.EV_KEY.KEY_PAUSE, KEYHLD)  # PAUSE_held
KBDPAUSE_PRS = IE(LD.EV_KEY.KEY_PAUSE, KEYPRS)  # PAUSE_pressed
KBDPAUSE_RLS = IE(LD.EV_KEY.KEY_PAUSE, KEYRLS)  # PAUSE_released
KBDPGDN_HLD = IE(LD.EV_KEY.KEY_PAGEDOWN, KEYHLD)  # PGDN_held
KBDPGDN_PRS = IE(LD.EV_KEY.KEY_PAGEDOWN, KEYPRS)  # PGDN_pressed
KBDPGDN_RLS = IE(LD.EV_KEY.KEY_PAGEDOWN, KEYRLS)  # PGDN_released
KBDPGUP_HLD = IE(LD.EV_KEY.KEY_PAGEUP, KEYHLD)  # PGUP_held
KBDPGUP_PRS = IE(LD.EV_KEY.KEY_PAGEUP, KEYPRS)  # PGUP_pressed
KBDPGUP_RLS = IE(LD.EV_KEY.KEY_PAGEUP, KEYRLS)  # PGUP_released
KBDPLAYPAUSE_HLD = IE(LD.EV_KEY.KEY_PLAYPAUSE, KEYHLD)  # PLAY_held
KBDPLAYPAUSE_PRS = IE(LD.EV_KEY.KEY_PLAYPAUSE, KEYPRS)  # PLAY_pressed
KBDPLAYPAUSE_RLS = IE(LD.EV_KEY.KEY_PLAYPAUSE, KEYRLS)  # PLAY_released
KBDPLUS_HLD = IE(LD.EV_KEY.KEY_KPPLUS, KEYHLD)  # KPPLUS_held
KBDPLUS_PRS = IE(LD.EV_KEY.KEY_KPPLUS, KEYPRS)  # KPPLUS_pressed
KBDPLUS_RLS = IE(LD.EV_KEY.KEY_KPPLUS, KEYRLS)  # KPPLUS_released
KBDPOWER_HLD = IE(LD.EV_KEY.KEY_POWER, KEYHLD)  # POWER_held
KBDPOWER_PRS = IE(LD.EV_KEY.KEY_POWER, KEYPRS)  # POWER_pressed
KBDPOWER_RLS = IE(LD.EV_KEY.KEY_POWER, KEYRLS)  # POWER_released
KBDPREVIOUSSONG_HLD = IE(LD.EV_KEY.KEY_PREVIOUSSONG, KEYHLD)  # PREVSONG_held
KBDPREVIOUSSONG_PRS = IE(LD.EV_KEY.KEY_PREVIOUSSONG, KEYPRS)  # PREVSONG_pressed
KBDPREVIOUSSONG_RLS = IE(LD.EV_KEY.KEY_PREVIOUSSONG, KEYRLS)  # PREVSONG_released
KBDPROPS_HLD = IE(LD.EV_KEY.KEY_PROPS, KEYHLD)  # PROPS_held
KBDPROPS_PRS = IE(LD.EV_KEY.KEY_PROPS, KEYPRS)  # PROPS_pressed
KBDPROPS_RLS = IE(LD.EV_KEY.KEY_PROPS, KEYRLS)  # PROPS_released
KBDP_PRS = IE(LD.EV_KEY.KEY_P, KEYPRS)  # P_pressed
KBDP_RLS = IE(LD.EV_KEY.KEY_P, KEYRLS)  # P_released
KBDP_RLSHLD = IE(LD.EV_KEY.KEY_P, KEYHLD)  # P_held
KBDQ_HLD = IE(LD.EV_KEY.KEY_Q, KEYHLD)  # Q_held
KBDQ_PRS = IE(LD.EV_KEY.KEY_Q, KEYPRS)  # Q_pressed
KBDQ_RLS = IE(LD.EV_KEY.KEY_Q, KEYRLS)  # Q_released
KBDREFRESH_HLD = IE(LD.EV_KEY.KEY_REFRESH, KEYHLD)  # REFRESH_held
KBDREFRESH_PRS = IE(LD.EV_KEY.KEY_REFRESH, KEYPRS)  # REFRESH_pressed
KBDREFRESH_RLS = IE(LD.EV_KEY.KEY_REFRESH, KEYRLS)  # REFRESH_released
KBDRO_HLD = IE(LD.EV_KEY.KEY_RO, KEYHLD)  # RO_held
KBDRO_PRS = IE(LD.EV_KEY.KEY_RO, KEYPRS)  # RO_pressed
KBDRO_RLS = IE(LD.EV_KEY.KEY_RO, KEYRLS)  # RO_released
KBDRT_HLD = IE(LD.EV_KEY.KEY_RIGHT, KEYHLD)  # RIGHT_held
KBDRT_PRS = IE(LD.EV_KEY.KEY_RIGHT, KEYPRS)  # RIGHT_pressed
KBDRT_RLS = IE(LD.EV_KEY.KEY_RIGHT, KEYRLS)  # RIGHT_released
KBDR_HLD = IE(LD.EV_KEY.KEY_R, KEYHLD)  # R_HELD
KBDR_PRS = IE(LD.EV_KEY.KEY_R, KEYPRS)  # R_pressed
KBDR_RLS = IE(LD.EV_KEY.KEY_R, KEYRLS)  # R_released
KBDSCROLLDN_HLD = IE(LD.EV_KEY.KEY_SCROLLDOWN, KEYHLD)  # SCROLLDOWN_held
KBDSCROLLDN_PRS = IE(LD.EV_KEY.KEY_SCROLLDOWN, KEYPRS)  # SCROLLDOWN_pressed
KBDSCROLLDN_RLS = IE(LD.EV_KEY.KEY_SCROLLDOWN, KEYRLS)  # SCROLLDOWN_released
KBDSCROLLLK_HLD = IE(LD.EV_KEY.KEY_SCROLLLOCK, KEYHLD)  # SCROLLLOCK_held
KBDSCROLLLK_PRS = IE(LD.EV_KEY.KEY_SCROLLLOCK, KEYPRS)  # SCROLLLOCK_pressed
KBDSCROLLLK_RLS = IE(LD.EV_KEY.KEY_SCROLLLOCK, KEYRLS)  # SCROLLLOCK_released
KBDSCROLLUP_HLD = IE(LD.EV_KEY.KEY_SCROLLUP, KEYHLD)  # SCROLLUP_held
KBDSCROLLUP_PRS = IE(LD.EV_KEY.KEY_SCROLLUP, KEYPRS)  # SCROLLUP_pressed
KBDSCROLLUP_RLS = IE(LD.EV_KEY.KEY_SCROLLUP, KEYRLS)  # SCROLLUP_released
KBDSEMICOLON_HLD = IE(LD.EV_KEY.KEY_SEMICOLON, KEYHLD)  # SEMICOLON_held
KBDSEMICOLON_PRS = IE(LD.EV_KEY.KEY_SEMICOLON, KEYPRS)  # SEMICOLON_pressed
KBDSEMICOLON_RLS = IE(LD.EV_KEY.KEY_SEMICOLON, KEYRLS)  # SEMICOLON_released
KBDSHIFTLT_HLD = IE(LD.EV_KEY.KEY_LEFTSHIFT, KEYHLD)  # LSHIFT_held
KBDSHIFTLT_PRS = IE(LD.EV_KEY.KEY_LEFTSHIFT, KEYPRS)  # LSHIFT_pressed
KBDSHIFTLT_RLS = IE(LD.EV_KEY.KEY_LEFTSHIFT, KEYRLS)  # LSHIFT_released
KBDSHIFTRT_HLD = IE(LD.EV_KEY.KEY_RIGHTSHIFT, KEYHLD)  # RSHIFT_held
KBDSHIFTRT_PRS = IE(LD.EV_KEY.KEY_RIGHTSHIFT, KEYPRS)  # RSHIFT_pressed
KBDSHIFTRT_RLS = IE(LD.EV_KEY.KEY_RIGHTSHIFT, KEYRLS)  # RSHIFT_released
KBDSLASH_HLD = IE(LD.EV_KEY.KEY_SLASH, KEYHLD)  # SLASH_held
KBDSLASH_PRS = IE(LD.EV_KEY.KEY_SLASH, KEYPRS)  # SLASH_pressed
KBDSLASH_RLS = IE(LD.EV_KEY.KEY_SLASH, KEYRLS)  # SLASH_released
KBDSLEEP_HLD = IE(LD.EV_KEY.KEY_SLEEP, KEYHLD)  # SLEEP_held
KBDSLEEP_PRS = IE(LD.EV_KEY.KEY_SLEEP, KEYPRS)  # SLEEP_pressed
KBDSLEEP_RLS = IE(LD.EV_KEY.KEY_SLEEP, KEYRLS)  # SLEEP_released
KBDSPC_HLD = IE(LD.EV_KEY.KEY_SPACE, KEYHLD)  # SPACE_held
KBDSPC_PRS = IE(LD.EV_KEY.KEY_SPACE, KEYPRS)  # SPACE_pressed
KBDSPC_RLS = IE(LD.EV_KEY.KEY_SPACE, KEYRLS)  # SPACE_released
KBDSPLAT_HLD = IE(LD.EV_KEY.KEY_KPASTERISK, KEYHLD)  # KPSPLAT_held
KBDSPLAT_PRS = IE(LD.EV_KEY.KEY_KPASTERISK, KEYPRS)  # KPSPLAT_pressed
KBDSPLAT_RLS = IE(LD.EV_KEY.KEY_KPASTERISK, KEYRLS)  # KPSPLAT_released
KBDSTOPCD_HLD = IE(LD.EV_KEY.KEY_STOPCD, KEYHLD)  # STOPCD_held
KBDSTOPCD_PRS = IE(LD.EV_KEY.KEY_STOPCD, KEYPRS)  # STOPCD_pressed
KBDSTOPCD_RLS = IE(LD.EV_KEY.KEY_STOPCD, KEYRLS)  # STOPCD_released
KBDSTOP_HLD = IE(LD.EV_KEY.KEY_STOP, KEYHLD)  # STOP_held
KBDSTOP_PRS = IE(LD.EV_KEY.KEY_STOP, KEYPRS)  # STOP_pressed
KBDSTOP_RLS = IE(LD.EV_KEY.KEY_STOP, KEYRLS)  # STOP_released
KBDSYSRQ_HLD = IE(LD.EV_KEY.KEY_SYSRQ, KEYHLD)  # SYSREQ_held
KBDSYSRQ_PRS = IE(LD.EV_KEY.KEY_SYSRQ, KEYPRS)  # SYSREQ_pressed
KBDSYSRQ_RLS = IE(LD.EV_KEY.KEY_SYSRQ, KEYRLS)  # SYSREQ_released
KBDS_HLD = IE(LD.EV_KEY.KEY_S, KEYHLD)  # S_held
KBDS_PRS = IE(LD.EV_KEY.KEY_S, KEYPRS)  # S_pressed
KBDS_RLS = IE(LD.EV_KEY.KEY_S, KEYRLS)  # S_released
KBDTAB_HLD = IE(LD.EV_KEY.KEY_TAB, KEYHLD)  # TAB_held
KBDTAB_PRS = IE(LD.EV_KEY.KEY_TAB, KEYPRS)  # TAB_pressed
KBDTAB_RLS = IE(LD.EV_KEY.KEY_TAB, KEYRLS)  # TAB_released
KBDT_HLD = IE(LD.EV_KEY.KEY_T, KEYHLD)  # T_held
KBDT_PRS = IE(LD.EV_KEY.KEY_T, KEYPRS)  # T_pressed
KBDT_RLS = IE(LD.EV_KEY.KEY_T, KEYRLS)  # T_released
KBDUNDO_HLD = IE(LD.EV_KEY.KEY_UNDO, KEYHLD)  # UNDO_held
KBDUNDO_PRS = IE(LD.EV_KEY.KEY_UNDO, KEYPRS)  # UNDO_pressed
KBDUNDO_RLS = IE(LD.EV_KEY.KEY_UNDO, KEYRLS)  # UNDO_released
KBDUNKNOWN_HLD = IE(LD.EV_KEY.KEY_UNKNOWN, KEYHLD)  # UNKNOW_held
KBDUNKNOWN_PRS = IE(LD.EV_KEY.KEY_UNKNOWN, KEYPRS)  # UNKNOW_pressed
KBDUNKNOWN_RLS = IE(LD.EV_KEY.KEY_UNKNOWN, KEYRLS)  # UNKNOW_released
KBDUP_HLD = IE(LD.EV_KEY.KEY_UP, KEYHLD)  # UP_held
KBDUP_PRS = IE(LD.EV_KEY.KEY_UP, KEYPRS)  # UP_pressed
KBDUP_RLS = IE(LD.EV_KEY.KEY_UP, KEYRLS)  # UP_released
KBDU_HLD = IE(LD.EV_KEY.KEY_U, KEYHLD)  # U_held
KBDU_PRS = IE(LD.EV_KEY.KEY_U, KEYPRS)  # U_pressed
KBDU_RLS = IE(LD.EV_KEY.KEY_U, KEYRLS)  # U_released
KBDVOLDN_HLD = IE(LD.EV_KEY.KEY_VOLUMEDOWN, KEYHLD)  # VOLDN_held
KBDVOLDN_PRS = IE(LD.EV_KEY.KEY_VOLUMEDOWN, KEYPRS)  # VOLDN_pressed
KBDVOLDN_RLS = IE(LD.EV_KEY.KEY_VOLUMEDOWN, KEYRLS)  # VOLDN_released
KBDVOLUP_HLD = IE(LD.EV_KEY.KEY_VOLUMEUP, KEYHLD)  # VOLUP_held
KBDVOLUP_PRS = IE(LD.EV_KEY.KEY_VOLUMEUP, KEYPRS)  # VOLUP_pressed
KBDVOLUP_RLS = IE(LD.EV_KEY.KEY_VOLUMEUP, KEYRLS)  # VOLUP_released
KBDV_HLD = IE(LD.EV_KEY.KEY_V, KEYHLD)  # V_held
KBDV_PRS = IE(LD.EV_KEY.KEY_V, KEYPRS)  # V_pressed
KBDV_RLS = IE(LD.EV_KEY.KEY_V, KEYRLS)  # V_released
KBDWWW_HLD = IE(LD.EV_KEY.KEY_WWW, KEYHLD)  # WWW_held
KBDWWW_PRS = IE(LD.EV_KEY.KEY_WWW, KEYPRS)  # WWW_pressed
KBDWWW_RLS = IE(LD.EV_KEY.KEY_WWW, KEYRLS)  # WWW_released
KBDW_HLD = IE(LD.EV_KEY.KEY_W, KEYHLD)  # W_held
KBDW_PRS = IE(LD.EV_KEY.KEY_W, KEYPRS)  # W_pressed
KBDW_RLS = IE(LD.EV_KEY.KEY_W, KEYRLS)  # W_released
KBDX_HLD = IE(LD.EV_KEY.KEY_X, KEYHLD)  # X_held
KBDX_PRS = IE(LD.EV_KEY.KEY_X, KEYPRS)  # X_pressed
KBDX_RLS = IE(LD.EV_KEY.KEY_X, KEYRLS)  # X_released
KBDYEN_HLD = IE(LD.EV_KEY.KEY_YEN, KEYHLD)  # YEN_held
KBDYEN_PRS = IE(LD.EV_KEY.KEY_YEN, KEYPRS)  # YEN_pressed
KBDYEN_RLS = IE(LD.EV_KEY.KEY_YEN, KEYRLS)  # YEN_released
KBDY_HLD = IE(LD.EV_KEY.KEY_Y, KEYHLD)  # Y_held
KBDY_PRS = IE(LD.EV_KEY.KEY_Y, KEYPRS)  # Y_pressed
KBDY_RLS = IE(LD.EV_KEY.KEY_Y, KEYRLS)  # Y_released
KBDZENKAKUHANKAKU_HLD = IE(LD.EV_KEY.KEY_ZENKAKUHANKAKU, KEYHLD)  # ZENKAKUHANKAKU_held
KBDZENKAKUHANKAKU_PRS = IE(LD.EV_KEY.KEY_ZENKAKUHANKAKU, KEYPRS)  # ZENKAKUHANKAKU_pressed
KBDZENKAKUHANKAKU_RLS = IE(LD.EV_KEY.KEY_ZENKAKUHANKAKU, KEYRLS)  # ZENKAKUHANKAKU_released
KBDZ_HLD = IE(LD.EV_KEY.KEY_Z, KEYHLD)  # Z_held
KBDZ_PRS = IE(LD.EV_KEY.KEY_Z, KEYPRS)  # Z_pressed
KBDZ_RLS = IE(LD.EV_KEY.KEY_Z, KEYRLS)  # Z_released
MSEBTNBAK_HLD = IE(LD.EV_KEY.BTN_BACK, KEYPRS)  # MSEBTNBAK_held
MSEBTNBAK_PRSHLD = IE(LD.EV_KEY.BTN_BACK, KEYPRSHLD)  # MSEBTNBAK_pressedHeld
MSEBTNBAK_PSR = IE(LD.EV_KEY.BTN_BACK, KEYPRS)  # MSEBTNBAK_pressed
MSEBTNBAK_RLS = IE(LD.EV_KEY.BTN_BACK, KEYRLS)  # MSEBTNBAK_released
MSEBTNFWD_HLD = IE(LD.EV_KEY.BTN_FORWARD, KEYHLD)  # MSEBTNFWD_held
MSEBTNFWD_PRS = IE(LD.EV_KEY.BTN_FORWARD, KEYPRS)  # MSEBTNFWD_pressed
MSEBTNFWD_PRSHLD = IE(LD.EV_KEY.BTN_FORWARD, KEYPRSHLD)  # MSEBTNFWD_pressedHeld
MSEBTNFWD_RLS = IE(LD.EV_KEY.BTN_FORWARD, KEYRLS)  # MSEBTNFWD_released
MSEBTNLT_HLD = IE(LD.EV_KEY.BTN_LEFT, KEYHLD)  # MSE left BTN held
MSEBTNLT_PRS = IE(LD.EV_KEY.BTN_LEFT, KEYPRS)  # MSEBTNLEFT_pressed
MSEBTNLT_PRSHLD = IE(LD.EV_KEY.BTN_LEFT, KEYPRSHLD)  # MSEBTNLEFT_pressedHeld
MSEBTNLT_RLS = IE(LD.EV_KEY.BTN_LEFT, KEYRLS)  # MSEBTNLEFT_released
MSEBTNMID_HLD = IE(LD.EV_KEY.BTN_MIDDLE, KEYHLD)  # MSEBTNMID_held
MSEBTNMID_PRS = IE(LD.EV_KEY.BTN_MIDDLE, KEYPRS)  # MSEBTNMID_pressed
MSEBTNMID_PRSHLD = IE(LD.EV_KEY.BTN_MIDDLE, KEYPRSHLD)  # MSEBTNMID_pressedHeld
MSEBTNMID_RLS = IE(LD.EV_KEY.BTN_MIDDLE, KEYRLS)  # MSEBTNMID_released
MSEBTNRT_HLD = IE(LD.EV_KEY.BTN_RIGHT, KEYHLD)  # MSEBTNRIGHT_held
MSEBTNRT_PRS = IE(LD.EV_KEY.BTN_RIGHT, KEYPRS)  # MSEBTNRIGHT_pressed
MSEBTNRT_PRSHLD = IE(LD.EV_KEY.BTN_RIGHT, KEYPRSHLD)  # MSEBTNRIGHT_pressedHeld
MSEBTNRT_RLS = IE(LD.EV_KEY.BTN_RIGHT, KEYRLS)  # MSEBTNRIGHT_released
MSEBTNSIDE_HLD = IE(LD.EV_KEY.BTN_SIDE, KEYHLD)  # MSEBTNSIDE_held
MSEBTNSIDE_PRS = IE(LD.EV_KEY.BTN_SIDE, KEYPRS)  # MSEBTNSIDE_pressedHeld
MSEBTNSIDE_PRSHLD = IE(LD.EV_KEY.BTN_SIDE, KEYPRSHLD)  # MSEBTNSIDE_pressed
MSEBTNSIDE_RLS = IE(LD.EV_KEY.BTN_SIDE, KEYRLS)  # MSEBTNSIDE_released
MSEBTNTASK_HLD = IE(LD.EV_KEY.BTN_TASK, KEYHLD)  # MSEBTNTASK_held
MSEBTNTASK_PRS = IE(LD.EV_KEY.BTN_TASK, KEYPRS)  # MSEBTNTASK_pressedHeld
MSEBTNTASK_PRSHLD = IE(LD.EV_KEY.BTN_TASK, KEYPRSHLD)  # MSEBTNTASK_pressed
MSEBTNTASK_RLS = IE(LD.EV_KEY.BTN_TASK, KEYRLS)  # MSEBTNTASK_released
MSEBTNXTRA_HLD = IE(LD.EV_KEY.BTN_EXTRA, KEYHLD)  # MSEBTNEXTRA_held
MSEBTNXTRA_PRS = IE(LD.EV_KEY.BTN_EXTRA, KEYPRS)  # MSEBTNEXTRA_pressed
MSEBTNXTRA_PRSHLD = IE(LD.EV_KEY.BTN_EXTRA, KEYPRSHLD)  # MSEBTNEXTRA_pressedHeld
MSEBTNXTRA_RLS = IE(LD.EV_KEY.BTN_EXTRA, KEYRLS)  # MSEBTNEXTRA_released
MSEHRWHL_DN = IE(LD.EV_REL.REL_WHEEL_HI_RES, -WHEELDISTANCE)  # move HR MSE WHL down WHEELDISTANCE ticks
MSEHRWHL_LT = IE(LD.EV_REL.REL_HWHEEL_HI_RES, -WHEELDISTANCE)  # move HR MSE WHL left WHEELDISTANCE ticks
MSEHRWHL_RT = IE(LD.EV_REL.REL_HWHEEL_HI_RES, WHEELDISTANCE)  # move HR MSE WHL right WHEELDISTANCE ticks
MSEHRWHL_UP = IE(LD.EV_REL.REL_WHEEL_HI_RES, WHEELDISTANCE)  # move HR MSE WHL up WHEELDISTANCE ticks
MSEWHL_DN = IE(LD.EV_REL.REL_WHEEL, -WHEELDISTANCE)  # move MSE WHL down WHEELDISTANCE
MSEWHL_LT = IE(LD.EV_REL.REL_HWHEEL, -WHEELDISTANCE)  # move MSE WHL left WHEELDISTANCE
MSEWHL_RT = IE(LD.EV_REL.REL_HWHEEL, WHEELDISTANCE)  # move MSE WHL right WHEELDISTANCE
MSEWHL_UP = IE(LD.EV_REL.REL_WHEEL, WHEELDISTANCE)  # move MSE WHL up WHEELDISTANCE
MSE_DN = IE(LD.EV_REL.REL_Y, MOUSEDISTANCE)  # how far to move the mouse per event
MSE_DNA = IE(LD.EV_REL.REL_Y, MOUSEDISTANCEARB)  # how far to move the mouse per event
MSE_LT = IE(LD.EV_REL.REL_X, -MOUSEDISTANCE)  # move MSE left -MOUSEDISTANCE
MSE_LTA = IE(LD.EV_REL.REL_X, -MOUSEDISTANCEARB)  # move MSE left -MOUSEDISTANCE
MSE_RT = IE(LD.EV_REL.REL_X, MOUSEDISTANCE)  # move mouse right MOUSEDISTANCE
MSE_RTA = IE(LD.EV_REL.REL_X, MOUSEDISTANCEARB)  # move mouse right MOUSEDISTANCE
MSE_UP = IE(LD.EV_REL.REL_Y, -MOUSEDISTANCE)  # move mouse up MOUSEDISTANCE
MSE_UPA = IE(LD.EV_REL.REL_Y, -MOUSEDISTANCEARB)  # move mouse up MOUSEDISTANCE
SYNREPORT = IE(LD.EV_SYN.SYN_REPORT, 0)  # send a sync report 0


SPCLAXLIST = [
	DOVAL_SPCL_PAUSE30F,  # pause 3/10 seconds
	DOVAL_SPCL_PAUSE3S,  # pause 3 seconds
	DOVAL_SPCL_PAUSE50F,  # pause 1/2 seconds
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN43 actions to output entries
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ACTIONS = {
	AXDSKTP1: [  # desktop #1
		KBDALTLT_PRS,  # press ALT
		KBD1_PRS,  # press 1
		KBD1_RLS,  # release 1
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXDSKTP2: [  # desktop #2
		KBDALTLT_PRS,  # press ALT
		KBD2_PRS,  # press 2
		KBD2_RLS,  # release 2
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXDSKTP3: [  # desktop #3
		KBDALTLT_PRS,  # press ALT
		KBD3_PRS,  # press 3
		KBD3_RLS,  # release 3
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXDSKTP4: [  # desktop #4
		KBDALTLT_PRS,  # press ALT
		KBD4_PRS,  # press 4
		KBD4_RLS,  # release 4
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXGIMPOVWRT: [  # GIMP overwrite imported file
		KBDALTLT_PRS,  # press ALT
		SYNREPORT,  # SYNREPORT
		KBDCTRLLT_PRS,  # press LCTRL
		SYNREPORT,  # SYNREPORT
		KBDSHIFTLT_PRS,  # press LSHIFT
		SYNREPORT,  # SYNREPORT
		KBDO_PRS,  # press O
		KBDO_RLS,  # release O
		KBDSHIFTLT_RLS,  # release LSHIFT
		KBDCTRLLT_RLS,  # release LCTRL
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXHRHWLDN: [  # high rez wheel DOWN
		MSEWHL_DN,  # move WHL down 1 unit
		SYNREPORT,  # SYNREPORT
	],

	AXHRHWLLT: [  # high rez wheel LEFT
		MSEWHL_LT,  # move WHL left 1 unit
		SYNREPORT,  # SYNREPORT
	],

	AXHRHWLRT: [  # high rez wheel RIGHT
		MSEWHL_RT,  # move WHL right 1 unit
		SYNREPORT,  # SYNREPORT
	],

	AXHRHWLUP: [  # high rez wheel UP
		MSEWHL_UP,  # move WHL up 1 unit
		SYNREPORT,  # SYNREPORT
	],

	AXMCCOPY: [  # MC copy F5, ENTER
		KBDF5_PRS,  # press F5
		KBDF5_RLS,  # release F5
		SYNREPORT,  # SYNREPORT
	],

	AXMCDEL: [  # MC del F8, ENTER
		KBDF8_PRS,  # press F8
		KBDF8_RLS,  # release F8
		SYNREPORT,  # SYNREPORT
	],

	AXMCMOVE: [  # MC move F6, ENTER
		KBDF6_PRS,  # press F6
		KBDF6_RLS,  # release F6
		SYNREPORT,  # SYNREPORT
	],

	AXMCSEL: [  # MC select INS
		KBDINSERT_PRS,  # press INSERT
		KBDINSERT_RLS,  # release INSERT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNBAK: [  # MSE BTN BACK
		MSEBTNBAK_PRSHLD,  # press MSEBTNBAK
		SYNREPORT,  # SYNREPORT
		MSEBTNBAK_RLS,  # release MSEBTNBAK
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNFWD: [  # MSE BTN FWD
		MSEBTNFWD_PRSHLD,  # press MSEBTNFWD
		SYNREPORT,  # SYNREPORT
		MSEBTNFWD_RLS,  # release MSEBTNFWD
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNLT: [  # MSE BTN LEFT
		MSEBTNLT_PRSHLD,  # press MSEBTNLT
		SYNREPORT,  # SYNREPORT
		MSEBTNLT_RLS,  # release MSEBTNLT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNLT_L00: [  # MSE BTN LEFT
		MSEBTNLT_PRSHLD,  # press MSEBTNLT
		SYNREPORT,  # SYNREPORT
		MSEBTNLT_RLS,  # release MSEBTNLT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNLT_L01: [  # MSE BTN LEFT_1 pressed
		MSEBTNLT_PRSHLD,  # press MSEBTNLT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNLT_L02: [  # MSE BTN LEFT_2 released
		MSEBTNLT_RLS,  # release MSEBTNLT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNLT_T01: [  # MSE BTN LEFT_1 pressed
		MSEBTNLT_PRSHLD,  # press MSEBTNLT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNLT_T02: [  # MSE BTN LEFT_2 released
		MSEBTNLT_RLS,  # release MSEBTNLT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNMID: [  # MSE BTN MIDDLE
		MSEBTNMID_PRSHLD,  # press MSEBTNMID
		SYNREPORT,  # SYNREPORT
		MSEBTNMID_RLS,  # release MSEBTNMID
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNRT: [  # MSE BTN RIGHT
		MSEBTNRT_PRSHLD,  # press MSEBTNRT
		SYNREPORT,  # SYNREPORT
		MSEBTNRT_RLS,  # release MSEBTNRT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNRT_T01: [  # MSE BTN LEFT_1 pressed
		MSEBTNRT_PRSHLD,  # press MSEBTNRT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNRT_T02: [  # MSE BTN LEFT_2 released
		MSEBTNRT_RLS,  # release MSEBTNRT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNSIDE: [  # MSE BTN SIDE
		MSEBTNSIDE_PRSHLD,  # press MSEBTNSIDE
		SYNREPORT,  # SYNREPORT
		MSEBTNSIDE_RLS,  # release MSEBTNSIDE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEBTNTASK: [  # MSE BTN TASK
		MSEBTNTASK_PRSHLD,  # press MSEBTNTASK
		SYNREPORT,  # SYNREPORT
		MSEBTNTASK_RLS,  # release MSEBTNTASK
		SYNREPORT,  # SYNREPORT
	],

	AXMSEDN: [  # MSE DOWN
		MSE_DN,  # MSE_DN by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEDNA: [  # MSE DOWN
		MSE_DNA,  # MSE_DN by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEDNLT: [  # MSE DOWNLT
		MSE_DN,  # MSE_DN by MOUSEDISTANCE
		MSE_LT,  # MSE_LT by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEDNRT: [  # MSE DOWNRT
		MSE_DN,  # MSE_DN by MOUSEDISTANCE
		MSE_RT,  # MSE_RT by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSELT: [  # MSE LEFT
		MSE_LT,  # MSE_LT by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSELTA: [  # MSE LEFT
		MSE_LTA,  # MSE_LT by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSERT: [  # MSE RIGHT
		MSE_RT,  # MSE_RT by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSERTA: [  # MSE RIGHT
		MSE_RTA,  # MSE_RT by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEUP: [  # MSE UP
		MSE_UP,  # MSE_UP by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEUPA: [  # MSE UP
		MSE_UPA,  # MSE_UP by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEUPLT: [  # MSE UPLT
		MSE_LT,  # MSE_LT by MOUSEDISTANCE
		MSE_UP,  # MSE_UP by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEUPRT: [  # MSE UPRT
		MSE_RT,  # MSE_RT by MOUSEDISTANCE
		MSE_UP,  # MSE_UP by MOUSEDISTANCE
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLDN: [  # wheel DOWN
		MSEWHL_DN,  # wheel DOWN
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLDNLT: [  # wheel DNLT
		MSEWHL_DN,  # wheel DOWN
		MSEWHL_LT,  # wheel LEFT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLDNRT: [  # wheel DNRT
		MSEWHL_DN,  # wheel DOWN
		MSEWHL_RT,  # wheel RIGHT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLLT: [  # wheel LEFT
		MSEWHL_LT,  # wheel LEFT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLRT: [  # wheel RIGHT
		MSEWHL_RT,  # wheel RIGHT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLUP: [  # wheel UP
		MSEWHL_UP,  # wheel UP
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLUPLT: [  # wheel UPLT
		MSEWHL_UP,  # wheel UP
		MSEWHL_LT,  # wheel LEFT
		SYNREPORT,  # SYNREPORT
	],

	AXMSEWHLUPRT: [  # wheel UPRT
		MSEWHL_UP,  # wheel UP
		MSEWHL_RT,  # wheel RIGHT
		SYNREPORT,  # SYNREPORT
	],

	AXSAVE: [  # save CTRL-S
		KBDCTRLLT_PRS,  # press CTRL
		KBDS_PRS,  # press S
		KBDS_RLS,  # release S
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AXXNVCOPYTO: [  # XnViewer COPYTO ALT-C
		KBDALTLT_PRS,  # press ALT
		KBDS_PRS,  # press S
		KBDS_RLS,  # release S
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVCROP: [  # XnViewer CROP SHIFT-X
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDX_PRS,  # press X
		KBDX_RLS,  # release X
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVFLIPH: [  # XnViewer FLIP horizontal ALT-F
		KBDALTLT_PRS,  # press ALT
		KBDF_PRS,  # press F
		KBDF_RLS,  # release F
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVMOVE: [  # XnViewer MOVE ALT-M
		KBDALTLT_PRS,  # press ALT
		KBDM_PRS,  # press M
		KBDM_RLS,  # release M
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVROTLT: [  # XnViewer ROT LEFT CTRL-SHIFT-L
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDCTRLLT_PRS,  # press CTRL
		KBDL_PRS,  # press L
		KBDL_RLS,  # release L
		KBDCTRLLT_RLS,  # release CTRL
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVROTRT: [  # XnViewer ROT RIGHT CTRL-SHIFT-R
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDCTRLLT_PRS,  # press CTRL
		KBDR_PRS,  # press R
		KBDR_RLS,  # release R
		KBDCTRLLT_RLS,  # release CTRL
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVSEL2TOP: [  # XnViewer SELECT to top SHIFT-HOME, SHIFT-RIGHT
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDHOME_PRS,  # press HOME
		KBDHOME_RLS,  # release HOME
		KBDRT_PRS,  # press RIGHT
		KBDRT_RLS,  # release RIGHT
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AXXNVZOOMFULL: [  # XnViewer zoom 1:1
		KBDSPLAT_PRS,  # press *
		KBDSPLAT_RLS,  # release *
		SYNREPORT,  # SYNREPORT
	],

	AXXNVZOOMIN: [  # XnViewer zoom in/+
		KBDPLUS_PRS,  # press +
		KBDPLUS_RLS,  # release +
		SYNREPORT,  # SYNREPORT
	],

	AXXNVZOOMOUT: [  # XnViewer zoom out/-
		KBDMINUS_PRS,  # press -
		KBDMINUS_RLS,  # release -
		SYNREPORT,  # SYNREPORT
	],

	AXXNVZOOMRESET: [  # reset XnViewer zoom by back, forward, forward, back
		KBDLT_PRS,  # press KBDLT
		KBDLT_RLS,  # press KBDLT
		KBDRT_PRS,  # press KBDLT
		KBDRT_RLS,  # press KBDLT
		KBDRT_PRS,  # press KBDLT
		KBDRT_RLS,  # press KBDLT
		KBDLT_PRS,  # press KBDLT
		KBDLT_RLS,  # press KBDLT
		SYNREPORT,  # SYNREPORT
	],

	AX_ALTC: [  # ALT-C
		KBDALTLT_PRS,  # press ALT
		KBDC_PRS,  # press C
		KBDC_RLS,  # release C
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AX_ALTD: [  # ALT-D
		KBDALTLT_PRS,  # press ALT
		KBDD_PRS,  # press D
		KBDD_RLS,  # release D
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AX_ALTTAB: [  # ALT-TAB
		KBDALTLT_PRS,  # press ALT
		KBDTAB_PRS,  # press TAB
		KBDTAB_RLS,  # release TAB
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AX_ALT_T01: [  # ALT-C
		KBDALTLT_PRS,  # press ALT
		SYNREPORT,  # SYNREPORT
	],

	AX_ALT_T02: [  # ALT-C
		KBDALTLT_RLS,  # release ALT
		SYNREPORT,  # SYNREPORT
	],

	AX_CRSRDN: [  # DOWN
		KBDDN_PRS,  # press DOWN
		KBDDN_RLS,  # release DOWN
		SYNREPORT,  # SYNREPORT
	],

	AX_CRSRDNLT: [  # DOWN
		KBDDN_PRS,  # press DOWN
		KBDDN_RLS,  # release DOWN
		KBDLT_PRS,  # press LEFT
		KBDLT_RLS,  # release LEFT
		SYNREPORT,  # SYNREPORT
	],

	AX_CRSRDNRT: [  # DOWN
		KBDDN_PRS,  # press DOWN
		KBDDN_RLS,  # release DOWN
		KBDRT_PRS,  # press RIGHT
		KBDRT_RLS,  # release RIGHT
		SYNREPORT,  # SYNREPORT
	],

	AX_CRSRLT: [  # LEFT
		KBDLT_PRS,  # press LEFT
		KBDLT_RLS,  # press LEFT
		SYNREPORT,  # press LEFT
	],

	AX_CRSRRT: [  # RIGHT
		KBDRT_PRS,  # press RIGHT
		KBDRT_RLS,  # release RIGHT
		SYNREPORT,  # press RIGHT
	],

	AX_CRSRUP: [  # UP
		KBDUP_PRS,  # press UP
		KBDUP_RLS,  # press UP
		SYNREPORT,  # press UP
	],

	AX_CRSRUPLT: [  # UPLT
		KBDUP_PRS,  # press UP
		KBDUP_RLS,  # press UP
		KBDLT_PRS,  # press LT
		KBDLT_RLS,  # press LT
		SYNREPORT,  # press UP
	],

	AX_CRSRUPRT: [  # UPRT
		KBDUP_PRS,  # press UP
		KBDUP_RLS,  # press UP
		KBDRT_PRS,  # press RT
		KBDRT_RLS,  # press RT
		SYNREPORT,  # press UP
	],

	AX_CTRLA: [  # CTRL-A
		KBDCTRLLT_PRS,  # press CTRL
		KBDA_PRS,  # press A
		KBDA_RLS,  # release A
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRLPGDN: [  # CTRLPGDN
		KBDCTRLLT_PRS,  # press CTRL
		KBDPGDN_PRS,  # press PGDN
		KBDPGDN_RLS,  # release PGDN
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRLPGUP: [  # CTRLPGUP
		KBDCTRLLT_PRS,  # press CTRL
		KBDPGUP_PRS,  # press PGUP
		KBDPGUP_RLS,  # release PGUP
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRLQ: [  # CTRL-Q
		KBDCTRLLT_PRS,  # press CTRL
		KBDQ_PRS,  # press Q
		KBDQ_RLS,  # release Q
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRLS: [  # CTRL-S
		KBDCTRLLT_PRS,  # press CTRL
		KBDS_PRS,  # press S
		KBDS_RLS,  # release S
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRLTAB: [  # CTRL-TAB
		KBDCTRLLT_PRS,  # press CTRL
		KBDTAB_PRS,  # press TAB
		KBDTAB_RLS,  # release TAB
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRLW: [  # CTRL-W
		KBDCTRLLT_PRS,  # press CTRL
		KBDW_PRS,  # press W
		KBDW_RLS,  # release W
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRL_T01: [  # CTRL toggle actions
		KBDCTRLLT_PRS,  # press CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_CTRL_T02: [  # CTRL toggle actions
		KBDCTRLLT_RLS,  # release CTRL
		SYNREPORT,  # SYNREPORT
	],

	AX_DEL: [  # DEL
		KBDDEL_PRS,  # press DEL
		KBDDEL_RLS,  # release DEL
		SYNREPORT,  # SYNREPORT
	],

	AX_END: [  # END
		KBDEND_PRS,  # press END
		KBDEND_RLS,  # release END
		SYNREPORT,  # SYNREPORT
	],

	AX_ENTER: [  # ENTER
		KBDENTER_PRS,  # press ENTER
		KBDENTER_RLS,  # release ENTER
		SYNREPORT,  # SYNREPORT
	],

	AX_ESC: [  # ESC
		KBDESC_PRS,  # press ESC
		KBDESC_RLS,  # release ESC
		SYNREPORT,  # SYNREPORT
	],

	AX_F: [  # F
		KBDF_PRS,  # press F
		KBDF_RLS,  # release F
		SYNREPORT,  # SYNREPORT
	],

	AX_F10: [  # F10
		KBDF10_PRS,  # press F10
		KBDF10_RLS,  # release F10
		SYNREPORT,  # SYNREPORT
	],

	AX_F5: [  # F5
		KBDF5_PRS,  # press F5
		KBDF5_RLS,  # release F5
		SYNREPORT,  # SYNREPORT
	],

	AX_F6: [  # F6
		KBDF6_PRS,  # press F6
		KBDF6_RLS,  # release F6
		SYNREPORT,  # SYNREPORT
	],

	AX_HOME: [  # HOME
		KBDHOME_PRS,  # press HOME
		KBDHOME_RLS,  # release HOME
		SYNREPORT,  # SYNREPORT
	],

	AX_INS: [  # MC select INS
		KBDINSERT_PRS,  # press INSERT
		KBDINSERT_RLS,  # release INSERT
		SYNREPORT,  # SYNREPORT
	],

	AX_N: [  # N
		KBDN_PRS,  # press N
		KBDN_RLS,  # release N
		SYNREPORT,  # SYNREPORT
	],

	AX_PGDN: [  # PGDN
		KBDPGDN_PRS,  # press PGDN
		KBDPGDN_RLS,  # release PGDN
		SYNREPORT,  # SYNREPORT
	],

	AX_PGUP: [  # PGUP
		KBDPGUP_PRS,  # press PGUP
		KBDPGUP_RLS,  # release PGUP
		SYNREPORT,  # SYNREPORT
	],

	AX_Q: [  # Q
		KBDQ_PRS,  # press Q
		KBDQ_RLS,  # release Q
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTDN: [  # SHIFT-DN
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDDN_PRS,  # press DN
		KBDDN_RLS,  # release DN
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTDNLT: [  # SHIFT-DNLT
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDDN_PRS,  # press DN
		KBDDN_RLS,  # release DN
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
		KBDLT_PRS,  # press LT
		KBDLT_RLS,  # release LT
	],

	AX_SHIFTDNRT: [  # SHIFT-DNRT
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDDN_PRS,  # press DN
		KBDDN_RLS,  # release DN
		KBDRT_PRS,  # press RT
		KBDRT_RLS,  # release RT
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTLT: [  # SHIFT-LT
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDLT_PRS,  # press LT
		KBDLT_RLS,  # release LT
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTUPLT: [  # SHIFT-UPLT
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDUP_PRS,  # press UP
		KBDUP_RLS,  # release UP
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTRT: [  # SHIFT-RT
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDRT_PRS,  # press RT
		KBDRT_RLS,  # release RT
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTTAB: [  # ALT-SHIFT-TAB
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDTAB_PRS,  # press TAB
		KBDTAB_RLS,  # release TAB
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTUP: [  # SHIFT-UP
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDUP_PRS,  # press UP
		KBDUP_RLS,  # release UP
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTUPRT: [  # SHIFT-UPRT
		KBDSHIFTRT_PRS,  # press SHIFT
		KBDUP_PRS,  # press UP
		KBDUP_RLS,  # release UP
		KBDRT_PRS,  # press RT
		KBDRT_RLS,  # release RT
		KBDSHIFTRT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFTX: [  # SHIFT-X
		KBDSHIFTLT_PRS,  # press SHIFT
		KBDX_PRS,  # press X
		KBDX_RLS,  # release X
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFT_T01: [  # SHIFT toggle actions
		KBDSHIFTLT_PRS,  # press SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SHIFT_T02: [  # SHIFT toggle actions
		KBDSHIFTLT_RLS,  # release SHIFT
		SYNREPORT,  # SYNREPORT
	],

	AX_SPACE: [  # SPACE
		KBDSPC_PRS,  # press SPACE
		KBDSPC_RLS,  # release SPACE
		SYNREPORT,  # SYNREPORT
	],

	AX_TAB: [  # TAB
		KBDTAB_PRS,  # press TAB
		KBDTAB_RLS,  # release TAB
		SYNREPORT,  # SYNREPORT
	],

	AX_Y: [  # Y
		KBDY_PRS,  # press Y
		KBDY_RLS,  # release Y
		SYNREPORT,  # SYNREPORT
	],

}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN48 device code list and dict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
ABSREL = "ABSREL"  # EV type list entry ABSS
ABSS = "ABSS"  # EV type list entry ABSS
BTNS = "BTNS"  # EV type list BTNS entry
HATS = "HATS"  # EV type list entry HAT
LTSTK = "LTSTK"  # EV type list entry LTSTK
RAW = "RAW"  # EV type list entry ABSS
RELS = "RELS"  # EV type for RELS supported
RTSTK = "RTSTK"  # EV type list entry RTSTK
STICKS = "STICKS"  # EV type list entry STICKS
WHLS = "WHLS"  # EV type for WHLS supported


DEVTLIST = [
	ABSREL,  # EV type list entry ABSS
	ABSS,  # EV type list entry ABSS
	BTNS,  # EV type list BTNS entry
	HATS,  # EV type list entry HAT
	LTSTK,  # EV type list entry LTSTK
	RAW,  # EV type list entry ABSS
	RELS,  # EV type for RELS supported
	RTSTK,  # EV type list entry RTSTK
	STICKS,  # EV type list entry STICKS
	WHLS,  # EV type for WHLS supported
]


DEVTDICT = {
	ABSREL: [  # EV type list entry ABSS
		DEVCD_ABSRZ,  # code for right stick X entries
		DEVCD_ABSX,  # code for left stick X entries
		DEVCD_ABSY,  # code for left stick Y entries
		DEVCD_ABSZ,  # code for right stick Y entries
		DEVCD_BTNGHAT_DN,  # code for right stick Y entries
		DEVCD_BTNGHAT_DNLT,  # code for right stick Y entries
		DEVCD_BTNGHAT_DNRT,  # code for right stick Y entries
		DEVCD_BTNGHAT_LT,  # code for right stick Y entries
		DEVCD_BTNGHAT_RT,  # code for right stick Y entries
		DEVCD_BTNGHAT_UP,  # code for right stick Y entries
		DEVCD_BTNGHAT_UPLT,  # code for right stick Y entries
		DEVCD_BTNGHAT_UPRT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DN,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DNLT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DNRT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_LT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_RT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_UP,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_UPLT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_UPRT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DN,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DNLT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DNRT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_LT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_RT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_UP,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_UPLT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_UPRT,  # code for right stick Y entries
		DEVCD_BTNMWH_DN,  # BTNMWHLDN/MSE_DN on mice
		DEVCD_BTNMWH_DNLT,  # BTNMWHLDN/MSE_DNLT on mice
		DEVCD_BTNMWH_DNRT,  # BTNMWHLDN/MSE_DNRT on mice
		DEVCD_BTNMWH_LT,  # BTNMWHLLT/MSE_LT on mice
		DEVCD_BTNMWH_RT,  # BTNMWHLRT/MSE_RT on mice
		DEVCD_BTNMWH_UP,  # BTNMWHLUP/MSE_UP on mice
		DEVCD_BTNMWH_UPLT,  # BTNMWHLUP/MSE_UPLT on mice
		DEVCD_BTNMWH_UPRT,  # BTNMWHLUP/MSE_UPRT on mice
		DEVCD_BTNM_MDN,  # BTNMDN/MSE_DN on mice
		DEVCD_BTNM_MDNLT,  # BTNMDN/MSE_DNLT on mice
		DEVCD_BTNM_MDNRT,  # BTNMDN/MSE_DNRT on mice
		DEVCD_BTNM_MLT,  # BTNMLT/MSE_LT on mice
		DEVCD_BTNM_MRT,  # BTNMRT/MSE_RT on mice
		DEVCD_BTNM_MUP,  # BTNMUP/MSE_UP on mice
		DEVCD_BTNM_MUPLT,  # BTNMUP/MSE_UPLT on mice
		DEVCD_BTNM_MUPRT,  # BTNMUP/MSE_UPRT on mice
		DEVCD_HAT0X,  # code for hat X entries
		DEVCD_HAT0Y,  # code for hat Y entries
		DEVCD_RELHRHWHL,  # DEVCD_RELHRHWHL entry
		DEVCD_RELHRWHL,  # DEVCD_RELHRWHL entry
		DEVCD_RELHWHL,  # DEVCD_RELHWHL entry
		DEVCD_RELWHL,  # DEVCD_RELWHL entry
		DEVCD_RELX,  # DEVCD_RELX entry
		DEVCD_RELY,  # DEVCD_RELY entry
	],
	ABSS: [  # EV type list entry ABSS
		DEVCD_ABSRZ,  # code for right stick X entries
		DEVCD_ABSX,  # code for left stick X entries
		DEVCD_ABSY,  # code for left stick Y entries
		DEVCD_ABSZ,  # code for right stick Y entries
		DEVCD_BTNGHAT_DN,  # code for right stick Y entries
		DEVCD_BTNGHAT_DNLT,  # code for right stick Y entries
		DEVCD_BTNGHAT_DNRT,  # code for right stick Y entries
		DEVCD_BTNGHAT_LT,  # code for right stick Y entries
		DEVCD_BTNGHAT_RT,  # code for right stick Y entries
		DEVCD_BTNGHAT_UP,  # code for right stick Y entries
		DEVCD_BTNGHAT_UPLT,  # code for right stick Y entries
		DEVCD_BTNGHAT_UPRT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DN,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DNLT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DNRT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_LT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_RT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_UP,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_UPLT,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_UPRT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DN,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DNLT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DNRT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_LT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_RT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_UP,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_UPLT,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_UPRT,  # code for right stick Y entries
		DEVCD_HAT0X,  # code for hat X entries
		DEVCD_HAT0Y,  # code for hat Y entries
	],
	BTNS: [  # EV type list BTNS entry
		DEVCD_BTNGHAT_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGHAT_DN,  # DEVCD_BTNGHAT_DN entry in BTNS
		DEVCD_BTNGHAT_DNLT,  # DEVCD_BTNGHAT_DNLT entry in BTNS
		DEVCD_BTNGHAT_DNRT,  # DEVCD_BTNGHAT_DNRT entry in BTNS
		DEVCD_BTNGHAT_LT,  # DEVCD_BTNGHAT_LT entry in BTNS
		DEVCD_BTNGHAT_RT,  # DEVCD_BTNGHAT_RT entry in BTNS
		DEVCD_BTNGHAT_UP,  # DEVCD_BTNGHAT_UP entry in BTNS
		DEVCD_BTNGHAT_UPLT,  # DEVCD_BTNGHAT_UPLT entry in BTNS
		DEVCD_BTNGHAT_UPRT,  # DEVCD_BTNGHAT_UPRT entry in BTNS
		DEVCD_BTNGLTSTK_DN,  # DEVCD_BTNGLTSTK_DN entry in BTNS
		DEVCD_BTNGLTSTK_DNLT,  # DEVCD_BTNGLTSTK_DNLT entry in BTNS
		DEVCD_BTNGLTSTK_DNRT,  # DEVCD_BTNGLTSTK_DNRT entry in BTNS
		DEVCD_BTNGLTSTK_LT,  # DEVCD_BTNGLTSTK_LT entry in BTNS
		DEVCD_BTNGLTSTK_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGLTSTK_RT,  # DEVCD_BTNGLTSTK_RT entry in BTNS
		DEVCD_BTNGLTSTK_UP,  # DEVCD_BTNGLTSTK_UP entry in BTNS
		DEVCD_BTNGLTSTK_UPLT,  # DEVCD_BTNGLTSTK_UPLT entry in BTNS
		DEVCD_BTNGLTSTK_UPRT,  # DEVCD_BTNGLTSTK_UPRT entry in BTNS
		DEVCD_BTNGRTSTK_DN,  # DEVCD_BTNGRTSTK_DN entry in BTNS
		DEVCD_BTNGRTSTK_DNLT,  # DEVCD_BTNGRTSTK_DNLT entry in BTNS
		DEVCD_BTNGRTSTK_DNRT,  # DEVCD_BTNGRTSTK_DNRT entry in BTNS
		DEVCD_BTNGRTSTK_LT,  # DEVCD_BTNGRTSTK_LT entry in BTNS
		DEVCD_BTNGRTSTK_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGRTSTK_RT,  # DEVCD_BTNGRTSTK_RT entry in BTNS
		DEVCD_BTNGRTSTK_UP,  # DEVCD_BTNGRTSTK_UP entry in BTNS
		DEVCD_BTNGRTSTK_UPLT,  # DEVCD_BTNGRTSTK_UPLT entry in BTNS
		DEVCD_BTNGRTSTK_UPRT,  # DEVCD_BTNGRTSTK_UPRT entry in BTNS
		DEVCD_BTNG_01,  # DEVCD_BTNG_01 entry in BTNS
		DEVCD_BTNG_02,  # DEVCD_BTNG_02 entry in BTNS
		DEVCD_BTNG_03,  # DEVCD_BTNG_03 entry in BTNS
		DEVCD_BTNG_04,  # DEVCD_BTNG_04 entry in BTNS
		DEVCD_BTNG_05,  # DEVCD_BTNG_05 entry in BTNS
		DEVCD_BTNG_06,  # DEVCD_BTNG_06 entry in BTNS
		DEVCD_BTNG_07,  # DEVCD_BTNG_07 entry in BTNS
		DEVCD_BTNG_08,  # DEVCD_BTNG_08 entry in BTNS
		DEVCD_BTNG_09,  # DEVCD_BTNG_09 entry in BTNS
		DEVCD_BTNG_10,  # DEVCD_BTNG_10 entry in BTNS
		DEVCD_BTNG_11LTSTK,  # DEVCD_BTNG_11LTSTK entry in BTNS
		DEVCD_BTNG_12RTSTK,  # DEVCD_BTNG_12RTSTK entry in BTNS
		DEVCD_BTNG_13,  # DEVCD_BTNG_13 entry in BTNS
	],
	HATS: [  # EV type list entry HAT
		DEVCD_BTNGHAT_DN,  # code for hat as BTN
		DEVCD_BTNGHAT_DNLT,  # code for hat as BTN
		DEVCD_BTNGHAT_DNRT,  # code for hat as BTN
		DEVCD_BTNGHAT_LT,  # code for hat as BTN
		DEVCD_BTNGHAT_RLS,  # code for hat as BTN
		DEVCD_BTNGHAT_RT,  # code for hat as BTN
		DEVCD_BTNGHAT_UP,  # code for hat as BTN
		DEVCD_BTNGHAT_UPLT,  # code for hat as BTN
		DEVCD_BTNGHAT_UPRT,  # code for hat as BTN
		DEVCD_HAT0X,  # code for hat stick X entries
		DEVCD_HAT0Y,  # code for hat stick Y entries
	],
	LTSTK: [  # EV type list entry LTSTK
		DEVCD_ABSX,  # code for left stick X entries
		DEVCD_ABSY,  # code for left stick Y entries
		DEVCD_BTNGLTSTK_DN,  # DEVCD_BTNGLTSTK_DN entry in BTNS
		DEVCD_BTNGLTSTK_DNLT,  # DEVCD_BTNGLTSTK_DNLT entry in BTNS
		DEVCD_BTNGLTSTK_DNRT,  # DEVCD_BTNGLTSTK_DNRT entry in BTNS
		DEVCD_BTNGLTSTK_LT,  # DEVCD_BTNGLTSTK_LT entry in BTNS
		DEVCD_BTNGLTSTK_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGLTSTK_RT,  # DEVCD_BTNGLTSTK_RT entry in BTNS
		DEVCD_BTNGLTSTK_UP,  # DEVCD_BTNGLTSTK_UP entry in BTNS
		DEVCD_BTNGLTSTK_UPLT,  # DEVCD_BTNGLTSTK_UPLT entry in BTNS
		DEVCD_BTNGLTSTK_UPRT,  # DEVCD_BTNGLTSTK_UPRT entry in BTNS
	],
	RAW: [  # EV type list entry ABSS
		LD.EV_ABS,  # raw code for ABS
		LD.EV_REL,  # raw code for REL
		LD.EV_KEY,  # raw code for KEY
	],
	RELS: [  # EV type for RELS supported
		DEVCD_BTNMWH_DN,  # BTNMWHLDN/MSE_DN on mice
		DEVCD_BTNMWH_DNLT,  # BTNMWHLDN/MSE_DNLT on mice
		DEVCD_BTNMWH_DNRT,  # BTNMWHLDN/MSE_DNRT on mice
		DEVCD_BTNMWH_LT,  # BTNMWHLLT/MSE_LT on mice
		DEVCD_BTNMWH_RT,  # BTNMWHLRT/MSE_RT on mice
		DEVCD_BTNMWH_UP,  # BTNMWHLUP/MSE_UP on mice
		DEVCD_BTNMWH_UPLT,  # BTNMWHLUP/MSE_UPLT on mice
		DEVCD_BTNMWH_UPRT,  # BTNMWHLUP/MSE_UPRT on mice
		DEVCD_BTNM_MDN,  # BTNMDN/MSE_DN on mice
		DEVCD_BTNM_MDNLT,  # BTNMDN/MSE_DNLT on mice
		DEVCD_BTNM_MDNRT,  # BTNMDN/MSE_DNRT on mice
		DEVCD_BTNM_MLT,  # BTNMLT/MSE_LT on mice
		DEVCD_BTNM_MRT,  # BTNMRT/MSE_RT on mice
		DEVCD_BTNM_MUP,  # BTNMUP/MSE_UP on mice
		DEVCD_BTNM_MUPLT,  # BTNMUP/MSE_UPLT on mice
		DEVCD_BTNM_MUPRT,  # BTNMUP/MSE_UPRT on mice
		DEVCD_RELHRHWHL,  # DEVCD_RELHRHWHL entry
		DEVCD_RELHRWHL,  # DEVCD_RELHRWHL entry
		DEVCD_RELHWHL,  # DEVCD_RELHWHL entry
		DEVCD_RELWHL,  # DEVCD_RELWHL entry
		DEVCD_RELX,  # DEVCD_RELX entry
		DEVCD_RELY,  # DEVCD_RELY entry
	],
	RTSTK: [  # EV type list entry RTSTK
		DEVCD_ABSRZ,  # code for right stick X entries
		DEVCD_ABSZ,  # code for right stick Y entries
		DEVCD_BTNGRTSTK_DN,  # DEVCD_BTNGLTSTK_DN entry in BTNS
		DEVCD_BTNGRTSTK_DNLT,  # DEVCD_BTNGLTSTK_DNLT entry in BTNS
		DEVCD_BTNGRTSTK_DNRT,  # DEVCD_BTNGLTSTK_DNRT entry in BTNS
		DEVCD_BTNGRTSTK_LT,  # DEVCD_BTNGLTSTK_LT entry in BTNS
		DEVCD_BTNGRTSTK_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGRTSTK_RT,  # DEVCD_BTNGLTSTK_RT entry in BTNS
		DEVCD_BTNGRTSTK_UP,  # DEVCD_BTNGLTSTK_UP entry in BTNS
		DEVCD_BTNGRTSTK_UPLT,  # DEVCD_BTNGLTSTK_UPLT entry in BTNS
		DEVCD_BTNGRTSTK_UPRT,  # DEVCD_BTNGLTSTK_UPRT entry in BTNS
	],
	STICKS: [  # EV type list entry STICKS
		DEVCD_ABSRZ,  # code for right stick X entries
		DEVCD_ABSX,  # code for left stick X entries
		DEVCD_ABSY,  # code for left stick Y entries
		DEVCD_ABSZ,  # code for right stick Y entries
		DEVCD_BTNGLTSTK_DN,  # DEVCD_BTNGLTSTK_DN entry in BTNS
		DEVCD_BTNGLTSTK_DNLT,  # DEVCD_BTNGLTSTK_DNLT entry in BTNS
		DEVCD_BTNGLTSTK_DNRT,  # DEVCD_BTNGLTSTK_DNRT entry in BTNS
		DEVCD_BTNGLTSTK_LT,  # DEVCD_BTNGLTSTK_LT entry in BTNS
		DEVCD_BTNGLTSTK_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGLTSTK_RT,  # DEVCD_BTNGLTSTK_RT entry in BTNS
		DEVCD_BTNGLTSTK_UP,  # DEVCD_BTNGLTSTK_UP entry in BTNS
		DEVCD_BTNGLTSTK_UPLT,  # DEVCD_BTNGLTSTK_UPLT entry in BTNS
		DEVCD_BTNGLTSTK_UPRT,  # DEVCD_BTNGLTSTK_UPRT entry in BTNS
		DEVCD_BTNGRTSTK_DN,  # DEVCD_BTNGLTSTK_DN entry in BTNS
		DEVCD_BTNGRTSTK_DNLT,  # DEVCD_BTNGLTSTK_DNLT entry in BTNS
		DEVCD_BTNGRTSTK_DNRT,  # DEVCD_BTNGLTSTK_DNRT entry in BTNS
		DEVCD_BTNGRTSTK_LT,  # DEVCD_BTNGLTSTK_LT entry in BTNS
		DEVCD_BTNGRTSTK_RLS,  # DEVCD_BTNGHAT_RLS entry in BTNS
		DEVCD_BTNGRTSTK_RT,  # DEVCD_BTNGLTSTK_RT entry in BTNS
		DEVCD_BTNGRTSTK_UP,  # DEVCD_BTNGLTSTK_UP entry in BTNS
		DEVCD_BTNGRTSTK_UPLT,  # DEVCD_BTNGLTSTK_UPLT entry in BTNS
		DEVCD_BTNGRTSTK_UPRT,  # DEVCD_BTNGLTSTK_UPRT entry in BTNS
	],
	WHLS: [  # EV type for WHLS supported
		DEVCD_RELHRHWHL,  # DEVCD_RELHRHWHL entry
		DEVCD_RELHRWHL,  # DEVCD_RELHRWHL entry
		DEVCD_RELHWHL,  # DEVCD_RELHWHL entry
		DEVCD_RELWHL,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_DN,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_DNLT,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_DNRT,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_LT,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_RLS,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_RT,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_UP,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_UPLT,  # DEVCD_RELWHL entry
		DEVCD_BTNMWH_UPRT,  # DEVCD_RELWHL entry
	],
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN44 filled and empty device entries
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DEVICES = {  # define SCTN44 DEVICES
	DEFT: {  # define the DEFT trackball
		DEV_ABSHAT_STATUS: DIRNOT_VAL,  # no ABS to status check,
		DEV_ABSLTSTK_STATUS: DIRNOT_VAL,  # no ABS to status check,
		DEV_ABSRTSTK_STATUS: DIRNOT_VAL,  # no ABS to status check,
		DEV_BTN_STATUS: BTNS_NOT,  # no buttons held,
		DEV_DEVICETYPE: DEVICETYPE_MOUSE,  # DEFT device type flag,
		DEV_ENABLED: False,  # DEFT enabled flag,
		DEV_ERR_DELTA: 300 * 60 * 100,  # 5 minutes between error checks,
		DEV_ERR_NEXTTIME: 0,  # DEFT next time to check error status,
		DEV_FD: None,  # file descriptor for DEFT,
		DEV_GRAB: True,  # grab the device,
		DEV_HASPAUSED: False,  # DEFT name,
		DEV_NAME: "ELECOM ELECOM TrackBall Mouse",  # DEFT name,
		DEV_QUEUE: [],  # DEFT queue,
		DEV_RELMSE_STATUS: DIRNOT_VAL,  # DEFT REL status,
		DEV_RELMW_STATUS: DIRNOT_VAL,  # DEFT REL status,
		DEV_RPT_NEXTTIME: 0,  # DEFT next time to repeat,
		DEV_RPT_NEXTTIMEDELTA: DORPT_NOT,  # DEFT time between repeats,
		DEV_SPENT: False,  # DEFT queue has been sent/spent,
		DEV_STATUS: DEVICESTATUS_DISCONNECTED,  # DEFT status,
	},
	MIMD: {  # define MIMD gamepad
		DEV_ABSHAT_STATUS: DIRNOT_VAL,  # no ABS to status check,
		DEV_ABSLTSTK_STATUS: DIRNOT_VAL,  # no ABS to status check,
		DEV_ABSRTSTK_STATUS: DIRNOT_VAL,  # no ABS to status check,
		DEV_BTN_STATUS: BTNS_NOT,  # no buttons held,
		DEV_DEVICETYPE: DEVICETYPE_GAMEPAD,  # MIMD device type flag,
		DEV_ENABLED: True,  # MIMD enabled flag,
		DEV_ERR_DELTA: 30000,  # 300 seconds delta for error checking,
		DEV_ERR_NEXTTIME: 0,  # MIMD next time to check error status,
		DEV_FD: None,  # MIMD file descriptor,
		DEV_GRAB: True,  # grab the MIMD,
		DEV_HASPAUSED: False,  # MIMD name,
		DEV_NAME: "ShanWan     GAME:PAD S PRO-BLUETOOTH-V6.20",  # MIMD name,
		DEV_QUEUE: [],  # MIMD queue,
		DEV_RELMSE_STATUS: DIRNOT_VAL,  # MIMD REL status,
		DEV_RPT_NEXTTIME: 0,  # MIMD next time to repeat,
		DEV_RPT_NEXTTIMEDELTA: DORPT_NOT,  # MIMD time between repeats,
		DEV_SPENT: False,  # MIMD queue has been sent/spent,
		DEV_STATUS: DEVICESTATUS_DISCONNECTED,  # MIMD status,
	},
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN45 device profile and REPEATDICT
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
PROFILE = {  # device profile defined
	DEFT: {
		BTNM_01LT: [
			AXMSEBTNLT_L00,  # mouse left button
			AXMSEBTNLT_L01,  # mouse left button
			AXMSEBTNLT_L02,  # mouse left button
		],

		BTNM_03RT: [
			AXMSEBTNRT,  # mouse right button
		],

		BTNM_11: [
			AXMSEBTNMID,  # mouse mid button
		],

		BTNM_MDN: [
			AXMSEDN,  # mouse move down button sim
			AXMSEWHLDN,  # mouse move down button sim
		],

		BTNM_MLT: [
			AXMSELT,  # mouse move left button sim
			AXMSEWHLLT,  # mouse move left button sim
		],

		BTNM_MRT: [
			AXMSERT,  # mouse move right button sim
			AXMSEWHLRT,  # mouse move right button sim
		],

		BTNM_MUP: [
			AXMSEUP,  # mouse move up button sim
			AXMSEWHLUP,  # mouse move up button sim
		],

	},
	MIMD: {
		BTNGHAT_DN: [
			AX_CRSRDN,  # artificial button hat down DOWN
		],

		BTNGHAT_DNLT: [
			AX_CRSRDNLT,  # artificial button hat down DOWN
		],

		BTNGHAT_DNRT: [
			AX_CRSRDNRT,  # artificial button hat down DOWN
		],

		BTNGHAT_LT: [
			AX_CRSRLT,  # artificial button hat left LEFT
		],

		BTNGHAT_RT: [
			AX_CRSRRT,  # artificial button hat right RIGHT
		],

		BTNGHAT_UP: [
			AX_CRSRUP,  # artificial button hat up UP
		],

		BTNGHAT_UPLT: [
			AX_CRSRUPLT,  # artificial button hat up UP
		],

		BTNGHAT_UPRT: [
			AX_CRSRUPRT,  # artificial button hat up UP
		],

		BTNGLTSTK_DN: [
			AXMSEDN,  # artificial button left stick down MSE_DN
		],

		BTNGLTSTK_DNLT: [
			AXMSEDNLT,  # artificial button left stick down MSE_DN
		],

		BTNGLTSTK_DNRT: [
			AXMSEDNRT,  # artificial button left stick down MSE_DN
		],

		BTNGLTSTK_LT: [
			AXMSELT,  # artificial button left stick left MSE_LT
		],

		BTNGLTSTK_RT: [
			AXMSERT,  # artificial button left stick right MSE_RT
		],

		BTNGLTSTK_UP: [
			AXMSEUP,  # left stick up MSE_UP
		],

		BTNGLTSTK_UPLT: [
			AXMSEUPLT,  # left stick up MSE_UP
		],

		BTNGLTSTK_UPRT: [
			AXMSEUPRT,  # left stick up MSE_UP
		],

		BTNGRTSTK_DN: [
			AXMSEWHLDN,  # right stick down MSEWHL_DN
		],

		BTNGRTSTK_DNLT: [
			AXMSEWHLDNLT,  # right stick down MSEWHL_DN
		],

		BTNGRTSTK_DNRT: [
			AXMSEWHLDNRT,  # right stick down MSEWHL_DN
		],

		BTNGRTSTK_LT: [
			AXMSEWHLLT,  # right stick left MSEWHL_LT
		],

		BTNGRTSTK_RT: [
			AXMSEWHLRT,  # right stick right MSEWHL_RT
		],

		BTNGRTSTK_UP: [
			AXMSEWHLUP,  # right stick up MSEWHL_UP
		],

		BTNGRTSTK_UPLT: [
			AXMSEWHLUPLT,  # right stick up MSEWHL_UP
		],

		BTNGRTSTK_UPRT: [
			AXMSEWHLUPRT,  # right stick up MSEWHL_UP
		],

		BTNG_01: [
			AXXNVFLIPH,  # XnViewer flip horizontal
		],

		BTNG_02: [
			AX_ESC,  # ESC key
		],

		BTNG_03: [
			AXMSEBTNMID,  # press middle mouse button
		],

		BTNG_04: [
			AX_CTRLS,  # save/CTRL-S
		],

		BTNG_05: {  # holdable button BTNG_05
			BTNG_01: [
				AX_CTRLA,  # select all CTRL-A
			],
			BTNG_04: [
				AXXNVROTLT,  # select all CTRL-A
			],
			BTNG_02: [
				AXXNVROTRT,  # select all CTRL-A
			],
			BTNG_03: [
				AXXNVCROP,  # XnViewer CROP
			],
			BTNG_13: [
				AXXNVSEL2TOP,  # select to top SHIFT-HOME SHIFT-RT
			],
			BTNGHAT_DN: [
				AX_SHIFTDN,  # SHIFT-DN
			],
			BTNGHAT_DNLT: [
				AX_SHIFTDNLT,  # SHIFT-DNLT
			],
			BTNGHAT_DNRT: [
				AX_SHIFTDNRT,  # SHIFT-DNRT
			],
			BTNGHAT_LT: [
				AX_SHIFTLT,  # SHIFT-LT
			],
			BTNGHAT_RT: [
				AX_SHIFTRT,  # SHIFT-RT
			],
			BTNGHAT_UP: [
				AX_SHIFTUP,  # SHIFT-UP
			],
			BTNGHAT_UPLT: [
				AX_SHIFTUPLT,  # SHIFT-UPLT
			],
			BTNGHAT_UPRT: [
				AX_SHIFTUPRT,  # SHIFT-UPRT
			],
		},
		BTNG_06: {  # holdable button BTNG_06
			BTNG_01: [
				AX_Q,  # QUIT Q in many programs
			],
			BTNG_02: [
				AX_CTRLQ,  # QUIT CTRL-Q in many programs
			],
			BTNG_03: [
				AX_ALTD,  # ALT-D dismiss in some programs
			],
			BTNG_04: [
				AXGIMPOVWRT,  # gimp overwrite ALT-CTRL-SHIFT-O
				AX_ENTER,  # gimp overwrite ENTER
				AX_CTRLQ,  # gimp overwrite CTRL-Q
				AX_ALTD,  # gimp overwrite ALT-D
			],
			BTNG_11LTSTK: [
				AXMSEBTNLT_T01,  # click MSEBTNLT
				AXMSEBTNLT_T02,  # click MSEBTNLT
			],
			BTNGHAT_DN: [
				AX_PGDN,  # PGDN
			],
			BTNGHAT_LT: [
				AX_HOME,  # HOME
			],
			BTNGHAT_RT: [
				AX_END,  # END
			],
			BTNGHAT_UP: [
				AX_PGUP,  # PGUP
			],
		},
		BTNG_07: {  # holdable button BTNG_07
			BTNG_01: [
				AXDSKTP1,  # desktop 1 ALT-1
			],
			BTNG_02: [
				AXDSKTP2,  # desktop 2 ALT-2
			],
			BTNG_03: [
				AXDSKTP3,  # desktop 3 ALT-3
			],
			BTNG_04: [
				AXDSKTP4,  # desktop 4 ALT-4
			],
			BTNG_13: [
				AX_DEL,  # DEL on BTNG_0713_T01
				AX_ENTER,  # ENTER on BTNG_0713_T02
			],
			BTNGHAT_DN: [
				AXXNVZOOMIN,  # XnViewer zoom to out/-
			],
			BTNGHAT_LT: [
				AXXNVZOOMRESET,  # XnViewer zoom to default
			],
			BTNGHAT_RT: [
				AXXNVZOOMFULL,  # XnViewer zoom to 1:1
			],
			BTNGHAT_UP: [
				AXXNVZOOMOUT,  # XnViewer zoom to out/-
			],
		},
		BTNG_08: {  # holdable button BTNG_08
			BTNG_01: [
				AX_ALT_T01,  # ALT press/release toggle on BTNG_08-BTNG_13
				AX_ALT_T02,  # ALT press/release toggle on BTNG_08-BTNG_13
			],
			BTNG_02: [
				AX_CTRL_T01,  # DEL on BTNG_08-BTNG_13
				AX_CTRL_T01,  # DEL on BTNG_08-BTNG_13
			],
			BTNG_03: [
				AX_SHIFT_T01,  # SHIFT on BTNG_0804_T01
				AX_SHIFT_T02,  # SHIFT on BTNG_0804_T02
			],
			BTNG_04: [
				AX_TAB,  # SHIFT on BTNG_0804_T02
			],
			BTNG_13: [
				AX_DEL,  # DEL on BTNG_0813_T01
				AX_ENTER,  # ENTER on BTNG_0813_T02
			],
			BTNGHAT_DN: [
				AX_CTRLPGDN,  # PGDN
			],
			BTNGHAT_LT: [
				AX_ALTTAB,  # ALTTAB
			],
			BTNGHAT_RT: [
				AX_CTRLTAB,  # CTRLTAB
			],
			BTNGHAT_UP: [
				AX_CTRLPGUP,  # PGUP
			],
		},
		BTNG_09: [
			AX_ENTER,  # ENTER on BTNG_09
		],

		BTNG_10: [
			AXXNVMOVE,  # XnViewer move
		],

		BTNG_11LTSTK: [
			AXMSEBTNLT,  # left mouse button on same stick click
		],

		BTNG_12RTSTK: [
			AXMSEBTNRT,  # right mouse button on same stick click
		],

		BTNG_13: [
			AX_ENTER,  # ENTER on BTNG_0813
		],

	},
}

REPEATDICT = {
	DEFT: {
		BTNM_01LT: DORPT_NOT,  # mouse left button
		BTNM_03RT: DORPT_NOT,  # mouse right button
		BTNM_11: DORPT_NOT,  # mouse mid button
		BTNM_MDN: DORPT_NOT,  # mouse move down button sim
		BTNM_MLT: DORPT_NOT,  # mouse move left button sim
		BTNM_MRT: DORPT_NOT,  # mouse move right button sim
		BTNM_MUP: DORPT_NOT,  # mouse move up button sim
	},
	MIMD: {
		BTNGHAT_DN: DORPT_CRSR,  # artificial button hat down DOWN
		BTNGHAT_DNLT: DORPT_CRSR,  # artificial button hat down DOWN
		BTNGHAT_DNRT: DORPT_CRSR,  # artificial button hat down DOWN
		BTNGHAT_LT: DORPT_CRSR,  # artificial button hat left LEFT
		BTNGHAT_RT: DORPT_CRSR,  # artificial button hat right RIGHT
		BTNGHAT_UP: DORPT_CRSR,  # artificial button hat up UP
		BTNGHAT_UPLT: DORPT_CRSR,  # artificial button hat up UP
		BTNGHAT_UPRT: DORPT_CRSR,  # artificial button hat up UP
		BTNGLTSTK_DN: DORPT_MSE,  # artificial button left stick down MSE_DN
		BTNGLTSTK_DNLT: DORPT_MSE,  # artificial button left stick down MSE_DN
		BTNGLTSTK_DNRT: DORPT_MSE,  # artificial button left stick down MSE_DN
		BTNGLTSTK_LT: DORPT_MSE,  # artificial button left stick left MSE_LT
		BTNGLTSTK_RT: DORPT_MSE,  # artificial button left stick right MSE_RT
		BTNGLTSTK_UP: DORPT_MSE,  # left stick up MSE_UP
		BTNGLTSTK_UPLT: DORPT_MSE,  # left stick up MSE_UP
		BTNGLTSTK_UPRT: DORPT_MSE,  # left stick up MSE_UP
		BTNGRTSTK_DN: DORPT_WHL,  # right stick down MSEWHL_DN
		BTNGRTSTK_DNLT: DORPT_WHL,  # right stick down MSEWHL_DN
		BTNGRTSTK_DNRT: DORPT_WHL,  # right stick down MSEWHL_DN
		BTNGRTSTK_LT: DORPT_WHL,  # right stick left MSEWHL_LT
		BTNGRTSTK_RT: DORPT_WHL,  # right stick right MSEWHL_RT
		BTNGRTSTK_UP: DORPT_WHL,  # right stick up MSEWHL_UP
		BTNGRTSTK_UPLT: DORPT_WHL,  # right stick up MSEWHL_UP
		BTNGRTSTK_UPRT: DORPT_WHL,  # right stick up MSEWHL_UP
		BTNG_01: DORPT_NOT,  # XnViewer flip horizontal
		BTNG_02: DORPT_NOT,  # ESC key
		BTNG_03: DORPT_NOT,  # press middle mouse button
		BTNG_04: DORPT_NOT,  # save/CTRL-S
		BTNG_05: {  # holdable button BTNG_05
			BTNG_01: DORPT_NOT,  # select all CTRL-A
			BTNG_04: DORPT_NOT,  # select all CTRL-A
			BTNG_02: DORPT_NOT,  # select all CTRL-A
			BTNG_03: DORPT_NOT,  # XnViewer CROP
			BTNG_13: DORPT_NOT,  # select to top SHIFT-HOME SHIFT-RT
			BTNGHAT_DN: DORPT_CRSR,  # SHIFT-DN
			BTNGHAT_DNLT: DORPT_CRSR,  # SHIFT-DNLT
			BTNGHAT_DNRT: DORPT_CRSR,  # SHIFT-DNRT
			BTNGHAT_LT: DORPT_CRSR,  # SHIFT-LT
			BTNGHAT_RT: DORPT_CRSR,  # SHIFT-RT
			BTNGHAT_UP: DORPT_CRSR,  # SHIFT-UP
			BTNGHAT_UPLT: DORPT_CRSR,  # SHIFT-UPLT
			BTNGHAT_UPRT: DORPT_CRSR,  # SHIFT-UPRT
		},
		BTNG_06: {  # holdable button BTNG_06
			BTNG_01: DORPT_NOT,  # QUIT Q in many programs
			BTNG_02: DORPT_NOT,  # QUIT CTRL-Q in many programs
			BTNG_03: DORPT_NOT,  # ALT-D dismiss in some programs
			BTNG_04: DORPT_NOT,  # gimp overwrite ALT-D
			BTNG_11LTSTK: DORPT_NOT,  # click MSEBTNLT
			BTNGHAT_DN: DORPT_NOT,  # PGDN
			BTNGHAT_LT: DORPT_NOT,  # HOME
			BTNGHAT_RT: DORPT_NOT,  # END
			BTNGHAT_UP: DORPT_NOT,  # PGUP
		},
		BTNG_07: {  # holdable button BTNG_07
			BTNG_01: DORPT_NOT,  # desktop 1 ALT-1
			BTNG_02: DORPT_NOT,  # desktop 2 ALT-2
			BTNG_03: DORPT_NOT,  # desktop 3 ALT-3
			BTNG_04: DORPT_NOT,  # desktop 4 ALT-4
			BTNG_13: DORPT_NOT,  # ENTER on BTNG_0713_T02
			BTNGHAT_DN: DORPT_NOT,  # XnViewer zoom to out/-
			BTNGHAT_LT: DORPT_NOT,  # XnViewer zoom to default
			BTNGHAT_RT: DORPT_NOT,  # XnViewer zoom to 1:1
			BTNGHAT_UP: DORPT_NOT,  # XnViewer zoom to out/-
		},
		BTNG_08: {  # holdable button BTNG_08
			BTNG_01: DORPT_NOT,  # ALT press/release toggle on BTNG_08-BTNG_13
			BTNG_02: DORPT_NOT,  # DEL on BTNG_08-BTNG_13
			BTNG_03: DORPT_NOT,  # SHIFT on BTNG_0804_T02
			BTNG_04: DORPT_NOT,  # SHIFT on BTNG_0804_T02
			BTNG_13: DORPT_NOT,  # ENTER on BTNG_0813_T02
			BTNGHAT_DN: DORPT_NOT,  # PGDN
			BTNGHAT_LT: DORPT_NOT,  # ALTTAB
			BTNGHAT_RT: DORPT_NOT,  # CTRLTAB
			BTNGHAT_UP: DORPT_NOT,  # PGUP
		},
		BTNG_09: DORPT_NOT,  # ENTER on BTNG_09
		BTNG_10: DORPT_NOT,  # XnViewer move
		BTNG_11LTSTK: DORPT_NOT,  # left mouse button on same stick click
		BTNG_12RTSTK: DORPT_NOT,  # right mouse button on same stick click
		BTNG_13: DORPT_NOT,  # ENTER on BTNG_0813
	},
}

BTNNDXDICT = {
	DEFT: {
		BTNM_01LT: 0,  # mouse left button
		BTNM_03RT: 0,  # mouse right button
		BTNM_11: 0,  # mouse mid button
		BTNM_MDN: 0,  # mouse move down button sim
		BTNM_MLT: 0,  # mouse move left button sim
		BTNM_MRT: 0,  # mouse move right button sim
		BTNM_MUP: 0,  # mouse move up button sim
	},
	MIMD: {
		BTNGHAT_DN: 0,  # artificial button hat down DOWN
		BTNGHAT_DNLT: 0,  # artificial button hat down DOWN
		BTNGHAT_DNRT: 0,  # artificial button hat down DOWN
		BTNGHAT_LT: 0,  # artificial button hat left LEFT
		BTNGHAT_RT: 0,  # artificial button hat right RIGHT
		BTNGHAT_UP: 0,  # artificial button hat up UP
		BTNGHAT_UPLT: 0,  # artificial button hat up UP
		BTNGHAT_UPRT: 0,  # artificial button hat up UP
		BTNGLTSTK_DN: 0,  # artificial button left stick down MSE_DN
		BTNGLTSTK_DNLT: 0,  # artificial button left stick down MSE_DN
		BTNGLTSTK_DNRT: 0,  # artificial button left stick down MSE_DN
		BTNGLTSTK_LT: 0,  # artificial button left stick left MSE_LT
		BTNGLTSTK_RT: 0,  # artificial button left stick right MSE_RT
		BTNGLTSTK_UP: 0,  # left stick up MSE_UP
		BTNGLTSTK_UPLT: 0,  # left stick up MSE_UP
		BTNGLTSTK_UPRT: 0,  # left stick up MSE_UP
		BTNGRTSTK_DN: 0,  # right stick down MSEWHL_DN
		BTNGRTSTK_DNLT: 0,  # right stick down MSEWHL_DN
		BTNGRTSTK_DNRT: 0,  # right stick down MSEWHL_DN
		BTNGRTSTK_LT: 0,  # right stick left MSEWHL_LT
		BTNGRTSTK_RT: 0,  # right stick right MSEWHL_RT
		BTNGRTSTK_UP: 0,  # right stick up MSEWHL_UP
		BTNGRTSTK_UPLT: 0,  # right stick up MSEWHL_UP
		BTNGRTSTK_UPRT: 0,  # right stick up MSEWHL_UP
		BTNG_01: 0,  # XnViewer flip horizontal
		BTNG_02: 0,  # ESC key
		BTNG_03: 0,  # press middle mouse button
		BTNG_04: 0,  # save/CTRL-S
		BTNG_05: {  # holdable button BTNG_05
			BTNG_01: 0,  # select all CTRL-A
			BTNG_04: 0,  # select all CTRL-A
			BTNG_02: 0,  # select all CTRL-A
			BTNG_03: 0,  # XnViewer CROP
			BTNG_13: 0,  # select to top SHIFT-HOME SHIFT-RT
			BTNGHAT_DN: 0,  # SHIFT-DN
			BTNGHAT_DNLT: 0,  # SHIFT-DNLT
			BTNGHAT_DNRT: 0,  # SHIFT-DNRT
			BTNGHAT_LT: 0,  # SHIFT-LT
			BTNGHAT_RT: 0,  # SHIFT-RT
			BTNGHAT_UP: 0,  # SHIFT-UP
			BTNGHAT_UPLT: 0,  # SHIFT-UPLT
			BTNGHAT_UPRT: 0,  # SHIFT-UPRT
		},
		BTNG_06: {  # holdable button BTNG_06
			BTNG_01: 0,  # QUIT Q in many programs
			BTNG_02: 0,  # QUIT CTRL-Q in many programs
			BTNG_03: 0,  # ALT-D dismiss in some programs
			BTNG_04: 0,  # gimp overwrite ALT-D
			BTNG_11LTSTK: 0,  # click MSEBTNLT
			BTNGHAT_DN: 0,  # PGDN
			BTNGHAT_LT: 0,  # HOME
			BTNGHAT_RT: 0,  # END
			BTNGHAT_UP: 0,  # PGUP
		},
		BTNG_07: {  # holdable button BTNG_07
			BTNG_01: 0,  # desktop 1 ALT-1
			BTNG_02: 0,  # desktop 2 ALT-2
			BTNG_03: 0,  # desktop 3 ALT-3
			BTNG_04: 0,  # desktop 4 ALT-4
			BTNG_13: 0,  # ENTER on BTNG_0713_T02
			BTNGHAT_DN: 0,  # XnViewer zoom to out/-
			BTNGHAT_LT: 0,  # XnViewer zoom to default
			BTNGHAT_RT: 0,  # XnViewer zoom to 1:1
			BTNGHAT_UP: 0,  # XnViewer zoom to out/-
		},
		BTNG_08: {  # holdable button BTNG_08
			BTNG_01: 0,  # ALT press/release toggle on BTNG_08-BTNG_13
			BTNG_02: 0,  # DEL on BTNG_08-BTNG_13
			BTNG_03: 0,  # SHIFT on BTNG_0804_T02
			BTNG_04: 0,  # SHIFT on BTNG_0804_T02
			BTNG_13: 0,  # ENTER on BTNG_0813_T02
			BTNGHAT_DN: 0,  # PGDN
			BTNGHAT_LT: 0,  # ALTTAB
			BTNGHAT_RT: 0,  # CTRLTAB
			BTNGHAT_UP: 0,  # PGUP
		},
		BTNG_09: 0,  # ENTER on BTNG_09
		BTNG_10: 0,  # XnViewer move
		BTNG_11LTSTK: 0,  # left mouse button on same stick click
		BTNG_12RTSTK: 0,  # right mouse button on same stick click
		BTNG_13: 0,  # ENTER on BTNG_0813
	},
}

BTNTYPEDICT = {
	DEFT: {
		BTNM_01LT: BTNAXTYPE_LOCKING,  # mouse left button
		BTNM_03RT: BTNAXTYPE_NORMAL,  # mouse right button
		BTNM_11: BTNAXTYPE_NORMAL,  # mouse mid button
		BTNM_MDN: BTNAXTYPE_MODED,  # mouse move down button sim
		BTNM_MLT: BTNAXTYPE_MODED,  # mouse move left button sim
		BTNM_MRT: BTNAXTYPE_MODED,  # mouse move right button sim
		BTNM_MUP: BTNAXTYPE_MODED,  # mouse move up button sim
	},
	MIMD: {
		BTNGHAT_DN: BTNAXTYPE_NORMAL,  # artificial button hat down DOWN
		BTNGHAT_DNLT: BTNAXTYPE_NORMAL,  # artificial button hat down DOWN
		BTNGHAT_DNRT: BTNAXTYPE_NORMAL,  # artificial button hat down DOWN
		BTNGHAT_LT: BTNAXTYPE_NORMAL,  # artificial button hat left LEFT
		BTNGHAT_RT: BTNAXTYPE_NORMAL,  # artificial button hat right RIGHT
		BTNGHAT_UP: BTNAXTYPE_NORMAL,  # artificial button hat up UP
		BTNGHAT_UPLT: BTNAXTYPE_NORMAL,  # artificial button hat up UP
		BTNGHAT_UPRT: BTNAXTYPE_NORMAL,  # artificial button hat up UP
		BTNGLTSTK_DN: BTNAXTYPE_NORMAL,  # artificial button left stick down MSE_DN
		BTNGLTSTK_DNLT: BTNAXTYPE_NORMAL,  # artificial button left stick down MSE_DN
		BTNGLTSTK_DNRT: BTNAXTYPE_NORMAL,  # artificial button left stick down MSE_DN
		BTNGLTSTK_LT: BTNAXTYPE_NORMAL,  # artificial button left stick left MSE_LT
		BTNGLTSTK_RT: BTNAXTYPE_NORMAL,  # artificial button left stick right MSE_RT
		BTNGLTSTK_UP: BTNAXTYPE_NORMAL,  # left stick up MSE_UP
		BTNGLTSTK_UPLT: BTNAXTYPE_NORMAL,  # left stick up MSE_UP
		BTNGLTSTK_UPRT: BTNAXTYPE_NORMAL,  # left stick up MSE_UP
		BTNGRTSTK_DN: BTNAXTYPE_NORMAL,  # right stick down MSEWHL_DN
		BTNGRTSTK_DNLT: BTNAXTYPE_NORMAL,  # right stick down MSEWHL_DN
		BTNGRTSTK_DNRT: BTNAXTYPE_NORMAL,  # right stick down MSEWHL_DN
		BTNGRTSTK_LT: BTNAXTYPE_NORMAL,  # right stick left MSEWHL_LT
		BTNGRTSTK_RT: BTNAXTYPE_NORMAL,  # right stick right MSEWHL_RT
		BTNGRTSTK_UP: BTNAXTYPE_NORMAL,  # right stick up MSEWHL_UP
		BTNGRTSTK_UPLT: BTNAXTYPE_NORMAL,  # right stick up MSEWHL_UP
		BTNGRTSTK_UPRT: BTNAXTYPE_NORMAL,  # right stick up MSEWHL_UP
		BTNG_01: BTNAXTYPE_NORMAL,  # XnViewer flip horizontal
		BTNG_02: BTNAXTYPE_NORMAL,  # ESC key
		BTNG_03: BTNAXTYPE_NORMAL,  # press middle mouse button
		BTNG_04: BTNAXTYPE_NORMAL,  # save/CTRL-S
		BTNG_05: {  # holdable button BTNG_05
			BTNG_01: BTNAXTYPE_NORMAL,  # select all CTRL-A
			BTNG_04: BTNAXTYPE_NORMAL,  # select all CTRL-A
			BTNG_02: BTNAXTYPE_NORMAL,  # select all CTRL-A
			BTNG_03: BTNAXTYPE_NORMAL,  # XnViewer CROP
			BTNG_13: BTNAXTYPE_NORMAL,  # select to top SHIFT-HOME SHIFT-RT
			BTNGHAT_DN: BTNAXTYPE_NORMAL,  # SHIFT-DN
			BTNGHAT_DNLT: BTNAXTYPE_NORMAL,  # SHIFT-DNLT
			BTNGHAT_DNRT: BTNAXTYPE_NORMAL,  # SHIFT-DNRT
			BTNGHAT_LT: BTNAXTYPE_NORMAL,  # SHIFT-LT
			BTNGHAT_RT: BTNAXTYPE_NORMAL,  # SHIFT-RT
			BTNGHAT_UP: BTNAXTYPE_NORMAL,  # SHIFT-UP
			BTNGHAT_UPLT: BTNAXTYPE_NORMAL,  # SHIFT-UPLT
			BTNGHAT_UPRT: BTNAXTYPE_NORMAL,  # SHIFT-UPRT
		},
		BTNG_06: {  # holdable button BTNG_06
			BTNG_01: BTNAXTYPE_NORMAL,  # QUIT Q in many programs
			BTNG_02: BTNAXTYPE_NORMAL,  # QUIT CTRL-Q in many programs
			BTNG_03: BTNAXTYPE_NORMAL,  # ALT-D dismiss in some programs
			BTNG_04: BTNAXTYPE_TOGGLE,  # gimp overwrite ALT-D
			BTNG_11LTSTK: BTNAXTYPE_TOGGLE,  # click MSEBTNLT
			BTNGHAT_DN: BTNAXTYPE_NORMAL,  # PGDN
			BTNGHAT_LT: BTNAXTYPE_NORMAL,  # HOME
			BTNGHAT_RT: BTNAXTYPE_NORMAL,  # END
			BTNGHAT_UP: BTNAXTYPE_NORMAL,  # PGUP
		},
		BTNG_07: {  # holdable button BTNG_07
			BTNG_01: BTNAXTYPE_NORMAL,  # desktop 1 ALT-1
			BTNG_02: BTNAXTYPE_NORMAL,  # desktop 2 ALT-2
			BTNG_03: BTNAXTYPE_NORMAL,  # desktop 3 ALT-3
			BTNG_04: BTNAXTYPE_NORMAL,  # desktop 4 ALT-4
			BTNG_13: BTNAXTYPE_TOGGLE,  # ENTER on BTNG_0713_T02
			BTNGHAT_DN: BTNAXTYPE_NORMAL,  # XnViewer zoom to out/-
			BTNGHAT_LT: BTNAXTYPE_NORMAL,  # XnViewer zoom to default
			BTNGHAT_RT: BTNAXTYPE_NORMAL,  # XnViewer zoom to 1:1
			BTNGHAT_UP: BTNAXTYPE_NORMAL,  # XnViewer zoom to out/-
		},
		BTNG_08: {  # holdable button BTNG_08
			BTNG_01: BTNAXTYPE_TOGGLE,  # ALT press/release toggle on BTNG_08-BTNG_13
			BTNG_02: BTNAXTYPE_NORMAL,  # DEL on BTNG_08-BTNG_13
			BTNG_03: BTNAXTYPE_TOGGLE,  # SHIFT on BTNG_0804_T02
			BTNG_04: BTNAXTYPE_TOGGLE,  # SHIFT on BTNG_0804_T02
			BTNG_13: BTNAXTYPE_TOGGLE,  # ENTER on BTNG_0813_T02
			BTNGHAT_DN: BTNAXTYPE_NORMAL,  # PGDN
			BTNGHAT_LT: BTNAXTYPE_NORMAL,  # ALTTAB
			BTNGHAT_RT: BTNAXTYPE_NORMAL,  # CTRLTAB
			BTNGHAT_UP: BTNAXTYPE_NORMAL,  # PGUP
		},
		BTNG_09: BTNAXTYPE_NORMAL,  # ENTER on BTNG_09
		BTNG_10: BTNAXTYPE_NORMAL,  # XnViewer move
		BTNG_11LTSTK: BTNAXTYPE_NORMAL,  # left mouse button on same stick click
		BTNG_12RTSTK: BTNAXTYPE_NORMAL,  # right mouse button on same stick click
		BTNG_13: BTNAXTYPE_NORMAL,  # ENTER on BTNG_0813
	},
}

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN46 device XLATE table
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
XLATETABLE = {
	DEFT: {
		LD.EV_KEY.BTN_LEFT: BTNM_01LT,  # DEFT:LT=BTNM_01LT
		LD.EV_KEY.BTN_MIDDLE: BTNM_02MD,  # DEFT:LT=BTNM_02MD
		LD.EV_KEY.BTN_RIGHT: BTNM_03RT,  # DEFT:LT=BTNM_03RT
		LD.EV_KEY.BTN_EXTRA: BTNM_08,  # DEFT:LT=BTNM_08
		LD.EV_KEY.BTN_SIDE: BTNM_09,  # DEFT:LT=BTNM_09
		LD.EV_KEY.BTN_FORWARD: BTNM_10,  # DEFT:LT=BTNM_10
		LD.EV_KEY.BTN_BACK: BTNM_11,  # DEFT:LT=BTNM_11
		LD.EV_KEY.BTN_TASK: BTNM_12,  # DEFT:RT=BTNM_12
	},
	MIMD: {
		LD.EV_KEY.BTN_SOUTH: BTNG_01,  # MIMD:01=BTN_SOUTH
		LD.EV_KEY.BTN_EAST: BTNG_02,  # MIMD:02=BTN_EAST
		LD.EV_KEY.BTN_C: BTNG_03,  # MIMD:03=BTN_C
		LD.EV_KEY.BTN_NORTH: BTNG_04,  # MIMD:04=BTN_NORTH
		LD.EV_KEY.BTN_WEST: BTNG_05,  # MIMD:05=BTN_WEST
		LD.EV_KEY.BTN_Z: BTNG_06,  # MIMD:06=BTN_Z
		LD.EV_KEY.BTN_TL: BTNG_07,  # MIMD:07=BTN_TL
		LD.EV_KEY.BTN_TR: BTNG_08,  # MIMD:08=BTN_TR
		LD.EV_KEY.BTN_TL2: BTNG_09,  # MIMD:09=BTN_TL2
		LD.EV_KEY.BTN_TR2: BTNG_10,  # MIMD:10=BTN_TR2
		LD.EV_KEY.BTN_SELECT: BTNG_11LTSTK,  # MIMD:11=BTN_SELECT
		LD.EV_KEY.BTN_START: BTNG_12RTSTK,  # MIMD:12=BTN_START
		LD.EV_KEY.BTN_MODE: BTNG_13,  # MIMD:13=BTN_MODE
	},
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * SCTN49 DIR to BTN SIM translation
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DIR2BTN = {
	HATS: {  # table to convert between directions and buttons
		DIRNOT_VAL: BTNGHAT_RLS,  # release hat sim buttons
		DIRUP_VAL: BTNGHAT_UP,  # table to convert between directions and buttons
		DIRRT_VAL: BTNGHAT_RT,  # table to convert between directions and buttons
		DIRUPRT_VAL: BTNGHAT_UPRT,  # table to convert between directions and buttons
		DIRDN_VAL: BTNGHAT_DN,  # table to convert between directions and buttons
		DIRDNUP_VAL: BTNGHAT_RLS,  # table to convert between directions and buttons
		DIRDNRT_VAL: BTNGHAT_DNRT,  # table to convert between directions and buttons
		DIRDNRTUP_VAL: BTNGHAT_RLS,  # table to convert between directions and buttons
		DIRLT_VAL: BTNGHAT_LT,  # table to convert between directions and buttons
		DIRUPLT_VAL: BTNGHAT_UPLT,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
		DIRLTRT_VAL: BTNGHAT_RLS,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
		DIRLTRTUP_VAL: BTNGHAT_RLS,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
		DIRDNLT_VAL: BTNGHAT_DNLT,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
		DIRLTDNUP_VAL: BTNGHAT_RLS,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
		DIRLTDNRT_VAL: BTNGHAT_RLS,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
		DIRLTDNRTUP_VAL: BTNGHAT_RLS,  # convert DIRUPLT_VAL to BTNGHAT_UPLT
	},
	LTSTK: {  # table to convert between directions and buttons
		DIRNOT_VAL: BTNGLTSTK_RLS,  # release hat sim buttons
		DIRUP_VAL: BTNGLTSTK_UP,  # table to convert between directions and buttons
		DIRRT_VAL: BTNGLTSTK_RT,  # table to convert between directions and buttons
		DIRUPRT_VAL: BTNGLTSTK_UPRT,  # table to convert between directions and buttons
		DIRDN_VAL: BTNGLTSTK_DN,  # table to convert between directions and buttons
		DIRDNUP_VAL: BTNGLTSTK_RLS,  # table to convert between directions and buttons
		DIRDNRT_VAL: BTNGLTSTK_DNRT,  # table to convert between directions and buttons
		DIRDNRTUP_VAL: BTNGLTSTK_RLS,  # table to convert between directions and buttons
		DIRLT_VAL: BTNGLTSTK_LT,  # table to convert between directions and buttons
		DIRUPLT_VAL: BTNGLTSTK_UPLT,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
		DIRLTRT_VAL: BTNGLTSTK_RLS,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
		DIRLTRTUP_VAL: BTNGLTSTK_RLS,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
		DIRDNLT_VAL: BTNGLTSTK_DNLT,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
		DIRLTDNUP_VAL: BTNGLTSTK_RLS,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
		DIRLTDNRT_VAL: BTNGLTSTK_RLS,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
		DIRLTDNRTUP_VAL: BTNGLTSTK_RLS,  # convert DIRUPLT_VAL to BTNGLTSTK_UPLT
	},
	RTSTK: {  # table to convert between directions and buttons
		DIRNOT_VAL: BTNGRTSTK_RLS,  # release hat sim buttons
		DIRUP_VAL: BTNGRTSTK_UP,  # table to convert between directions and buttons
		DIRRT_VAL: BTNGRTSTK_RT,  # table to convert between directions and buttons
		DIRUPRT_VAL: BTNGRTSTK_UPRT,  # table to convert between directions and buttons
		DIRDN_VAL: BTNGRTSTK_DN,  # table to convert between directions and buttons
		DIRDNUP_VAL: BTNGRTSTK_RLS,  # table to convert between directions and buttons
		DIRDNRT_VAL: BTNGRTSTK_DNRT,  # table to convert between directions and buttons
		DIRDNRTUP_VAL: BTNGRTSTK_RLS,  # table to convert between directions and buttons
		DIRLT_VAL: BTNGRTSTK_LT,  # table to convert between directions and buttons
		DIRUPLT_VAL: BTNGRTSTK_UPLT,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
		DIRLTRT_VAL: BTNGRTSTK_RLS,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
		DIRLTRTUP_VAL: BTNGRTSTK_RLS,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
		DIRDNLT_VAL: BTNGRTSTK_DNLT,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
		DIRLTDNUP_VAL: BTNGRTSTK_RLS,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
		DIRLTDNRT_VAL: BTNGRTSTK_RLS,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
		DIRLTDNRTUP_VAL: BTNGRTSTK_RLS,  # convert DIRUPLT_VAL to BTNGRTSTK_UPLT
	},
}


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of managed section of DO.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of not managed section of DO
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# isMatch
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def isMatch(eventCD1_, eventCD2_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	valToRtn_ = False
	# print(f"isMatch eventCD1_ {eventCD1_}   eventCD2_ {eventCD2_}{CF.NEWLINE}")

	if eventCD1_[0] == eventCD2_[0]:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		return True
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif eventCD1_[0] in DEVTDICT[LTSTK] and eventCD2_[0] in DEVTDICT[LTSTK]:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		return True
		# print(f"LTSTK")
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif eventCD1_[0] in DEVTDICT[RTSTK] and eventCD2_[0] in DEVTDICT[RTSTK]:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		return True
		# print(f"RTSTK")
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif eventCD1_[0] in DEVTDICT[HATS] and eventCD2_[0] in DEVTDICT[HATS]:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		return True
		# print(f"HATS")
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	return valToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# deleteReleasedEvent
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deleteReleasedEvent(queueIn_, eventIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	queueOut_ = []
	if queueIn_ is None or queueIn_ == []:
		return queueOut_
	for thisEvent_ in queueIn_:
		if not isMatch(thisEvent_, eventIn_):
			queueOut_.append(thisEvent_)
	return queueOut_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# fixQueue
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fixQueue(queueIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	queueLen_ = len(queueIn_)

	if queueLen_ == 1 and queueIn_[0][1] != KEYRLS:
		print(f"queueIn_ {queueIn_}")
		return queueIn_
	elif queueLen_ > 4 or (queueLen_ == 1 and queueIn_[0][1] == KEYRLS):
		return []

	for thisEvent_ in queueIn_:
		if thisEvent_[1] == KEYRLS:
			queueIn_ = deleteReleasedEvent(queueIn_, thisEvent_)

	queueLen_ = len(queueIn_)
	if queueLen_ == 1:
		return queueIn_

	elif queueLen_ == 0:
		return []

	queueOut_ = []
	queueMaybe_ = []
	for thisEvent_ in queueIn_:
		if thisEvent_[1] == KEYHLD:
			queueOut_.append(thisEvent_)
		else:
			queueMaybe_.append(thisEvent_)
	if queueMaybe_ == []:
		return queueOut_
	queueMaybeLen_ = len(queueMaybe_)
	if queueMaybeLen_ == 1:
		queueOut_.append(queueMaybe_[0])
		return queueOut_
	elif queueMaybeLen_ > 2:
		return []
	elif (queueMaybe_[0][0] in DEVTDICT[HATS] and queueMaybe_[1][0] in DEVTDICT[HATS]) or \
			(queueMaybe_[0][0] in DEVTDICT[LTSTK] and queueMaybe_[1][0] in DEVTDICT[LTSTK]) or \
			(queueMaybe_[0][0] in DEVTDICT[RTSTK] and queueMaybe_[1][0] in DEVTDICT[RTSTK]):
		queueOut_.append((queueMaybe_[1][0], queueMaybe_[1][1]))
		return queueOut_
	# print(f"DO.fixQueue not yet supported queue {queueIn_}")
	return []
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# setRptTime
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def setRptTime(thisDevice_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	thisQueue_ = DEVICES[thisDevice_][DEV_QUEUE]
	if thisQueue_ is None:
		thisQueue_ = []
		DEVICES[thisDevice_][DEV_QUEUE] = []

	if (thisQueue_ == []) or \
			(thisQueue_[-1][1] == KEYHLD):
		DEVICES[thisDevice_][DEV_RPT_NEXTTIMEDELTA] = 0
		DEVICES[thisDevice_][DEV_RPT_NEXTTIME] = 0
		DEVICES[thisDevice_][DEV_SPENT] = True
		return
	thisQueueLen_ = len(thisQueue_)
	try:
		if thisQueueLen_ == 1:
			rptToSet_ = REPEATDICT[thisDevice_][thisQueue_[0][0]]
		elif thisQueueLen_ == 2:
			rptToSet_ = REPEATDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]]
		elif thisQueueLen_ == 3:
			rptToSet_ = REPEATDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]]
		else:
			rptToSet_ = 0
		if DEVICES[thisDevice_][DEV_HASPAUSED] is False:
			DEVICES[thisDevice_][DEV_RPT_NEXTTIME] = CF.MTSPlus(rptToSet_ + DORPT_PAUSE)
		DEVICES[thisDevice_][DEV_RPT_NEXTTIMEDELTA] = rptToSet_
		DEVICES[thisDevice_][DEV_SPENT] = False
		return
	except KeyError:
		DEVICES[thisDevice_][DEV_RPT_NEXTTIMEDELTA] = 0
		DEVICES[thisDevice_][DEV_RPT_NEXTTIME] = 0
		DEVICES[thisDevice_][DEV_SPENT] = True
		return
	except TypeError:
		DEVICES[thisDevice_][DEV_RPT_NEXTTIMEDELTA] = 0
		DEVICES[thisDevice_][DEV_RPT_NEXTTIME] = 0
		DEVICES[thisDevice_][DEV_SPENT] = True
		return
	except KeyboardInterrupt:
		exit()
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# fixBtn
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fixBtn(DEVTCode_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	codeToRtn_ = None
	for thisDevice_, entries_ in XLATETABLE.items():
		if DEVTCode_ in entries_:
			codeToRtn_ = entries_[DEVTCode_]
	return codeToRtn_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# openOutputDevice
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def openOutputDevice(lookingForDeviceName_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	for myTEvent in os.listdir('/dev/input'):
		# print(myTEvent)
		try:
			fdJoyStick_ = open('/dev/input/' + myTEvent, "rb")
			fcntl.fcntl(fdJoyStick_, fcntl.F_SETFL, os.O_NONBLOCK)
			myLDJoyStick_ = LD.Device(fdJoyStick_)
			if myLDJoyStick_.name == lookingForDeviceName_:
				return myLDJoyStick_
			fdJoyStick_.close()
		except IOError:
			pass
	print("failed to find the", lookingForDeviceName_)
	return None
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# SPCL_
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def SPCL_(spclEvent_, spclVal_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if spclEvent_ == DO.SPCL_PAUSE:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		CF.mySleep(spclVal_)
		return True
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif spclEvent_ == DO.SPCL_PAUSE3S:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		CF.mySleep(300)
		return True
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif spclEvent_ == DO.SPCL_PAUSE30F:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		CF.mySleep(30)
		return True
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif spclEvent_ == DO.SPCL_PAUSE50F:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		CF.mySleep(50)
		return True
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	else:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		print(f"{CF.NEWLINE}unknown special event |{spclEvent_}|{spclVal_}|{CF.NEWLINE}")
		return None
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# queueEvents
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def queueEvents(thisDevice_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if DEVICES[thisDevice_][DEV_STATUS] != DEVICESTATUS_CONNECTED:
		return
	for eventToFix_ in DEVICES[thisDevice_][DEV_FD].events():
		thisCode_ = eventToFix_.code
		thisType_ = eventToFix_.type
		thisValue_ = eventToFix_.value
		if thisType_ not in DEVTDICT[RAW]:
			continue
		# CF.displayStats(10, 0, f"""queue events new event {eventToFix_}{CF.CLREOL}{CF.NEWLINE}{CF.MTSclr()}""")
		eventToRtn_ = (None, None)
		# print(f"""{CF.getDebugInfo()} eventToFix_1 {eventToFix_} eventToRtn_ {eventToRtn_}""")
		if thisCode_ in DEVTDICT[HATS]:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			dir1_ = DEVICES[thisDevice_][DEV_ABSHAT_STATUS]

			if thisValue_ == HATMIN:
				# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
				if thisCode_ == DEVCD_HAT0X:
					dir3_ = DIRLT_OR(DIRY_AND(dir1_))
				else:
					dir3_ = DIRUP_OR(DIRY_AND(dir1_))
				pressRelease_ = KEYPRS
				# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

			elif thisValue_ == HATMAX:
				# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
				if thisCode_ == DEVCD_HAT0X:
					dir3_ = DIRRT_OR(dir1_)
				else:
					dir3_ = DIRDN_OR(dir1_)
				pressRelease_ = KEYPRS
				# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

			else:
				# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
				if thisCode_ == DEVCD_HAT0X:
					dir3_ = DIRY_AND(dir1_)
				else:
					dir3_ = DIRX_AND(dir1_)
				pressRelease_ = KEYRLS
				# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

			DEVICES[thisDevice_][DEV_ABSHAT_STATUS] = dir3_
			dirBtn_ = DIR2BTN[HATS][dir3_]
			eventToRtn_ = (dirBtn_, pressRelease_)
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisCode_ in DEVTDICT[STICKS]:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisCode_ in [DEVCD_ABSX, DEVCD_ABSY]:
				dir1_ = DEVICES[thisDevice_][DEV_ABSLTSTK_STATUS]
				stk1_ = DEV_ABSLTSTK_STATUS
				stk2_ = LTSTK
			else:
				dir1_ = DEVICES[thisDevice_][DEV_ABSRTSTK_STATUS]
				stk1_ = DEV_ABSRTSTK_STATUS
				stk2_ = RTSTK

			if thisValue_ < (JOYSTICKMID - JOYSTICKDEAD):
				# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
				if thisCode_ == DEVCD_ABSX:
					dir3_ = DIRLT_OR(dir1_)
				elif thisCode_ == DEVCD_ABSY:
					dir3_ = DIRUP_OR(dir1_)
				elif thisCode_ == DEVCD_ABSRZ:
					dir3_ = DIRUP_OR(dir1_)
				elif thisCode_ == DEVCD_ABSZ:
					dir3_ = DIRLT_OR(dir1_)
				pressRelease_ = KEYPRS
				# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

			elif thisValue_ > (JOYSTICKMID + JOYSTICKDEAD):
				# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
				if thisCode_ == DEVCD_ABSX:
					dir3_ = DIRRT_OR(dir1_)
				elif thisCode_ == DEVCD_ABSY:
					dir3_ = DIRDN_OR(dir1_)
				elif thisCode_ == DEVCD_ABSRZ:
					dir3_ = DIRDN_OR(dir1_)
				elif thisCode_ == DEVCD_ABSZ:
					dir3_ = DIRRT_OR(dir1_)
				pressRelease_ = KEYPRS
				# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

			else:  # thisValue_ == JOYSTICKMID +- JOYSTICKDEAD
				# fold here ⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3⥥3
				if thisCode_ in DEVTDICT[LTSTK]:
					if thisCode_ == DEVCD_ABSX:
						dir3_ = DIRY_AND(dir1_)
					else:
						dir3_ = DIRY_AND(dir1_)
				else:
					if thisCode_ == DEVCD_ABSZ:
						dir3_ = DIRX_AND(dir1_)
					else:
						dir3_ = DIRX_AND(dir1_)
				pressRelease_ = KEYRLS
				# fold here ⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3⥣3

			DEVICES[thisDevice_][stk1_] = dir3_
			dirBtn_ = DIR2BTN[stk2_][dir3_]
			eventToRtn_ = (dirBtn_, pressRelease_)
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisType_ == LD.EV_KEY:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisValue_ == KEYPRS:
				eventToRtn_ = (fixBtn(thisCode_), KEYPRS)
				if eventToRtn_[0] in BTNSHOLDABLELIST:
					eventToRtn_ = (eventToRtn_[0], KEYHLD)
			elif thisValue_ == KEYRLS:
				eventToRtn_ = (fixBtn(thisCode_), KEYRLS)
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif thisType_ == LD.EV_REL:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if thisCode_ == DEVCD_RELX:
				if thisValue_ < 0:
					MOUSEDISTANCEARB = thisValue_
					eventToRtn_ = (BTNM_MLTA, KEYPRS)
				elif thisValue_ > 0:
					MOUSEDISTANCEARB = thisValue_
					eventToRtn_ = (BTNM_MRTA, KEYPRS)
			elif thisCode_ == DEVCD_RELY:
				if thisValue_ < 0:
					MOUSEDISTANCEARB = thisValue_
					eventToRtn_ = (BTNM_MUPA, KEYPRS)
				elif thisValue_ > 0:
					MOUSEDISTANCEARB = thisValue_
					eventToRtn_ = (BTNM_MDNA, KEYPRS)
			print(f"queueEvents EV_REL eventToFix_ {eventToFix_}  eventToRtn_ {eventToRtn_}")
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		else:
			return


		setRptTime(thisDevice_)
		queueToFix_ = DEVICES[thisDevice_][DEV_QUEUE]
		queueToFix_.append(eventToRtn_)
		queueToRtn_ = fixQueue(queueToFix_)
		setRptTime(thisDevice_)
		thisDeviceType_ = DEVICES[thisDevice_][DEV_DEVICETYPE]
		if queueToRtn_ == []:
			DEVICES[thisDevice_][DEV_HASPAUSED] = False
			DEVICES[thisDevice_][DEV_RPT_NEXTTIME] = 0
			DEVICES[thisDevice_][DEV_RPT_NEXTTIMEDELTA] = 0
			if thisDeviceType_ == DEVICETYPE_GAMEPAD:
				DEVICES[thisDevice_][DEV_ABSHAT_STATUS] = DIRNOT_VAL
				DEVICES[thisDevice_][DEV_ABSLTSTK_STATUS] = DIRNOT_VAL
				DEVICES[thisDevice_][DEV_ABSRTSTK_STATUS] = DIRNOT_VAL
			elif thisDeviceType_ == DEVICETYPE_MOUSE:
				DEVICES[thisDevice_][DEV_RELMSE_STATUS] = DIRNOT_VAL
				DEVICES[thisDevice_][DEV_RELMW_STATUS] = DIRNOT_VAL
		print(f"""queueEvents exit queue {queueToRtn_}{CF.CLREOL}{CF.NEWLINE}{CF.MTSclr()}""")
		DEVICES[thisDevice_][DEV_QUEUE] = queueToRtn_
		if queueToRtn_ != []:
			DEVICES[thisDevice_][DEV_SPENT] = False
		# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# incNdx
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def incNdx(AXLst_, currentNDX_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	AXLstLen_ = len(AXLst_)
	currentNDX_ += 1
	if currentNDX_ == AXLstLen_:
		currentNDX_ = 0
	return currentNDX_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of DO.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
