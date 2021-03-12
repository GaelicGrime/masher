

#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# SCTN50 start of HBI
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#


from time import sleep
import libevdev as LD


import CF


def IDB():
	devHBI = LD.Device()
	devHBI.name = "HBI hot beef injector"

	devHBI.enable(LD.EV_KEY.BTN_LEFT)  # ability to send MSEBTNLT
	devHBI.enable(LD.EV_KEY.BTN_MIDDLE)  # ability to send MSEBTNMID
	devHBI.enable(LD.EV_KEY.BTN_RIGHT)  # ability to send MSEBTNRT
	devHBI.enable(LD.EV_KEY.BTN_EXTRA)  # ability to send MSEBTNXTRA
	devHBI.enable(LD.EV_KEY.BTN_SIDE)  # ability to send MSEBTNSIDE
	devHBI.enable(LD.EV_KEY.BTN_FORWARD)  # ability to send MSEBTNFWD
	devHBI.enable(LD.EV_KEY.BTN_BACK)  # ability to send MSEBTNBAK
	devHBI.enable(LD.EV_KEY.BTN_TASK)  # ability to send MSEBTNTASK

	devHBI.enable(LD.EV_KEY.KEY_0)  # ability to send KEY_0
	devHBI.enable(LD.EV_KEY.KEY_1)  # make KEY_1 available
	devHBI.enable(LD.EV_KEY.KEY_102ND)  # make KEY_102ND available
	devHBI.enable(LD.EV_KEY.KEY_2)  # make KEY_2 available
	devHBI.enable(LD.EV_KEY.KEY_3)  # make KEY_3 available
	devHBI.enable(LD.EV_KEY.KEY_4)  # make KEY_4 available
	devHBI.enable(LD.EV_KEY.KEY_5)  # make KEY_5 available
	devHBI.enable(LD.EV_KEY.KEY_6)  # make KEY_6 available
	devHBI.enable(LD.EV_KEY.KEY_7)  # make KEY_7 available
	devHBI.enable(LD.EV_KEY.KEY_8)  # make KEY_8 available
	devHBI.enable(LD.EV_KEY.KEY_9)  # make KEY_9 available
	devHBI.enable(LD.EV_KEY.KEY_A)  # make KEY_A available
	devHBI.enable(LD.EV_KEY.KEY_AGAIN)  # make KEY_AGAIN available
	devHBI.enable(LD.EV_KEY.KEY_APOSTROPHE)  # make KEY_APOSTROPHE available
	devHBI.enable(LD.EV_KEY.KEY_B)  # make KEY_B available
	devHBI.enable(LD.EV_KEY.KEY_BACK)  # make KEY_BACK available
	devHBI.enable(LD.EV_KEY.KEY_BACKSLASH)  # make KEY_BACKSLASH available
	devHBI.enable(LD.EV_KEY.KEY_BACKSPACE)  # make KEY_BACKSPACE available
	devHBI.enable(LD.EV_KEY.KEY_C)  # make KEY_C available
	devHBI.enable(LD.EV_KEY.KEY_CALC)  # make KEY_CALC available
	devHBI.enable(LD.EV_KEY.KEY_CAPSLOCK)  # make KEY_CAPSLOCK available
	devHBI.enable(LD.EV_KEY.KEY_COFFEE)  # make KEY_COFFEE available
	devHBI.enable(LD.EV_KEY.KEY_COMMA)  # make KEY_COMMA available
	devHBI.enable(LD.EV_KEY.KEY_COMPOSE)  # make KEY_COMPOSE available
	devHBI.enable(LD.EV_KEY.KEY_COPY)  # make KEY_COPY available
	devHBI.enable(LD.EV_KEY.KEY_CUT)  # make KEY_CUT available
	devHBI.enable(LD.EV_KEY.KEY_D)  # make KEY_D available
	devHBI.enable(LD.EV_KEY.KEY_DELETE)  # make KEY_DELETE available
	devHBI.enable(LD.EV_KEY.KEY_DOT)  # make KEY_DOT available
	devHBI.enable(LD.EV_KEY.KEY_DOWN)  # make KEY_DOWN available
	devHBI.enable(LD.EV_KEY.KEY_E)  # make KEY_E available
	devHBI.enable(LD.EV_KEY.KEY_EDIT)  # make KEY_EDIT available
	devHBI.enable(LD.EV_KEY.KEY_EJECTCD)  # make KEY_EJECTCD available
	devHBI.enable(LD.EV_KEY.KEY_END)  # make KEY_END available
	devHBI.enable(LD.EV_KEY.KEY_ENTER)  # make KEY_ENTER available
	devHBI.enable(LD.EV_KEY.KEY_EQUAL)  # make KEY_EQUAL available
	devHBI.enable(LD.EV_KEY.KEY_ESC)  # make KEY_ESC available
	devHBI.enable(LD.EV_KEY.KEY_F)  # make KEY_F available
	devHBI.enable(LD.EV_KEY.KEY_F1)  # make KEY_F1 available
	devHBI.enable(LD.EV_KEY.KEY_F10)  # make KEY_F10 available
	devHBI.enable(LD.EV_KEY.KEY_F11)  # make KEY_F11 available
	devHBI.enable(LD.EV_KEY.KEY_F12)  # make KEY_F12 available
	devHBI.enable(LD.EV_KEY.KEY_F13)  # make KEY_F13 available
	devHBI.enable(LD.EV_KEY.KEY_F14)  # make KEY_F14 available
	devHBI.enable(LD.EV_KEY.KEY_F15)  # make KEY_F15 available
	devHBI.enable(LD.EV_KEY.KEY_F16)  # make KEY_F16 available
	devHBI.enable(LD.EV_KEY.KEY_F17)  # make KEY_F17 available
	devHBI.enable(LD.EV_KEY.KEY_F18)  # make KEY_F18 available
	devHBI.enable(LD.EV_KEY.KEY_F19)  # make KEY_F19 available
	devHBI.enable(LD.EV_KEY.KEY_F2)  # make KEY_F2 available
	devHBI.enable(LD.EV_KEY.KEY_F20)  # make KEY_F20 available
	devHBI.enable(LD.EV_KEY.KEY_F21)  # make KEY_F21 available
	devHBI.enable(LD.EV_KEY.KEY_F22)  # make KEY_F22 available
	devHBI.enable(LD.EV_KEY.KEY_F23)  # make KEY_F23 available
	devHBI.enable(LD.EV_KEY.KEY_F24)  # make KEY_F24 available
	devHBI.enable(LD.EV_KEY.KEY_F3)  # make KEY_F3 available
	devHBI.enable(LD.EV_KEY.KEY_F4)  # make KEY_F4 available
	devHBI.enable(LD.EV_KEY.KEY_F5)  # make KEY_F5 available
	devHBI.enable(LD.EV_KEY.KEY_F6)  # make KEY_F6 available
	devHBI.enable(LD.EV_KEY.KEY_F7)  # make KEY_F7 available
	devHBI.enable(LD.EV_KEY.KEY_F8)  # make KEY_F8 available
	devHBI.enable(LD.EV_KEY.KEY_F9)  # make KEY_F9 available
	devHBI.enable(LD.EV_KEY.KEY_FIND)  # make KEY_FIND available
	devHBI.enable(LD.EV_KEY.KEY_FORWARD)  # make KEY_FORWARD available
	devHBI.enable(LD.EV_KEY.KEY_FRONT)  # make KEY_FRONT available
	devHBI.enable(LD.EV_KEY.KEY_G)  # make KEY_G available
	devHBI.enable(LD.EV_KEY.KEY_GRAVE)  # make KEY_GRAVE available
	devHBI.enable(LD.EV_KEY.KEY_H)  # make KEY_H available
	devHBI.enable(LD.EV_KEY.KEY_HANGEUL)  # make KEY_HANGEUL available
	devHBI.enable(LD.EV_KEY.KEY_HANJA)  # make KEY_HANJA available
	devHBI.enable(LD.EV_KEY.KEY_HELP)  # make KEY_HELP available
	devHBI.enable(LD.EV_KEY.KEY_HENKAN)  # make KEY_HENKAN available
	devHBI.enable(LD.EV_KEY.KEY_HIRAGANA)  # make KEY_HIRAGANA available
	devHBI.enable(LD.EV_KEY.KEY_HOME)  # make KEY_HOME available
	devHBI.enable(LD.EV_KEY.KEY_I)  # make KEY_I available
	devHBI.enable(LD.EV_KEY.KEY_INSERT)  # make KEY_INSERT available
	devHBI.enable(LD.EV_KEY.KEY_J)  # make KEY_J available
	devHBI.enable(LD.EV_KEY.KEY_K)  # make KEY_K available
	devHBI.enable(LD.EV_KEY.KEY_KATAKANA)  # make KEY_KATAKANA available
	devHBI.enable(LD.EV_KEY.KEY_KATAKANAHIRAGANA)  # make KEY_KATAKANAHIRAGANA available
	devHBI.enable(LD.EV_KEY.KEY_KP0)  # make KEY_KP0 available
	devHBI.enable(LD.EV_KEY.KEY_KP1)  # make KEY_KP1 available
	devHBI.enable(LD.EV_KEY.KEY_KP2)  # make KEY_KP2 available
	devHBI.enable(LD.EV_KEY.KEY_KP3)  # make KEY_KP3 available
	devHBI.enable(LD.EV_KEY.KEY_KP4)  # make KEY_KP4 available
	devHBI.enable(LD.EV_KEY.KEY_KP5)  # make KEY_KP5 available
	devHBI.enable(LD.EV_KEY.KEY_KP6)  # make KEY_KP6 available
	devHBI.enable(LD.EV_KEY.KEY_KP7)  # make KEY_KP7 available
	devHBI.enable(LD.EV_KEY.KEY_KP8)  # make KEY_KP8 available
	devHBI.enable(LD.EV_KEY.KEY_KP9)  # make KEY_KP9 available
	devHBI.enable(LD.EV_KEY.KEY_KPASTERISK)  # make KEY_KPASTERISK available
	devHBI.enable(LD.EV_KEY.KEY_KPCOMMA)  # make KEY_KPCOMMA available
	devHBI.enable(LD.EV_KEY.KEY_KPDOT)  # make KEY_KPDOT available
	devHBI.enable(LD.EV_KEY.KEY_KPENTER)  # make KEY_KPENTER available
	devHBI.enable(LD.EV_KEY.KEY_KPEQUAL)  # make KEY_KPEQUAL available
	devHBI.enable(LD.EV_KEY.KEY_KPJPCOMMA)  # make KEY_KPJPCOMMA available
	devHBI.enable(LD.EV_KEY.KEY_KPLEFTPAREN)  # make KEY_KPLEFTPAREN available
	devHBI.enable(LD.EV_KEY.KEY_KPMINUS)  # make KEY_KPMINUS available
	devHBI.enable(LD.EV_KEY.KEY_KPPLUS)  # make KEY_KPPLUS available
	devHBI.enable(LD.EV_KEY.KEY_KPRIGHTPAREN)  # make KEY_KPRIGHTPAREN available
	devHBI.enable(LD.EV_KEY.KEY_KPSLASH)  # make KEY_KPSLASH available
	devHBI.enable(LD.EV_KEY.KEY_L)  # make KEY_L available
	devHBI.enable(LD.EV_KEY.KEY_LEFT)  # make KEY_LEFT available
	devHBI.enable(LD.EV_KEY.KEY_LEFTALT)  # make KEY_LEFTALT available
	devHBI.enable(LD.EV_KEY.KEY_LEFTBRACE)  # make KEY_LEFTBRACE available
	devHBI.enable(LD.EV_KEY.KEY_LEFTCTRL)  # make KEY_LEFTCTRL available
	devHBI.enable(LD.EV_KEY.KEY_LEFTMETA)  # make KEY_LEFTMETA available
	devHBI.enable(LD.EV_KEY.KEY_LEFTSHIFT)  # make KEY_LEFTSHIFT available
	devHBI.enable(LD.EV_KEY.KEY_M)  # make KEY_M available
	devHBI.enable(LD.EV_KEY.KEY_MINUS)  # make KEY_MINUS available
	devHBI.enable(LD.EV_KEY.KEY_MUHENKAN)  # make KEY_MUHENKAN available
	devHBI.enable(LD.EV_KEY.KEY_MUTE)  # make KEY_MUTE available
	devHBI.enable(LD.EV_KEY.KEY_N)  # make KEY_N available
	devHBI.enable(LD.EV_KEY.KEY_NEXTSONG)  # make KEY_NEXTSONG available
	devHBI.enable(LD.EV_KEY.KEY_NUMLOCK)  # make KEY_NUMLOCK available
	devHBI.enable(LD.EV_KEY.KEY_O)  # make KEY_O available
	devHBI.enable(LD.EV_KEY.KEY_OPEN)  # make KEY_OPEN available
	devHBI.enable(LD.EV_KEY.KEY_P)  # make KEY_P available
	devHBI.enable(LD.EV_KEY.KEY_PAGEDOWN)  # make KEY_PAGEDOWN available
	devHBI.enable(LD.EV_KEY.KEY_PAGEUP)  # make KEY_PAGEUP available
	devHBI.enable(LD.EV_KEY.KEY_PASTE)  # make KEY_PASTE available
	devHBI.enable(LD.EV_KEY.KEY_PAUSE)  # make KEY_PAUSE available
	devHBI.enable(LD.EV_KEY.KEY_PLAYPAUSE)  # make KEY_PLAYPAUSE available
	devHBI.enable(LD.EV_KEY.KEY_POWER)  # make KEY_POWER available
	devHBI.enable(LD.EV_KEY.KEY_PREVIOUSSONG)  # make KEY_PREVIOUSSONG available
	devHBI.enable(LD.EV_KEY.KEY_PROPS)  # make KEY_PROPS available
	devHBI.enable(LD.EV_KEY.KEY_Q)  # make KEY_Q available
	devHBI.enable(LD.EV_KEY.KEY_R)  # make KEY_R available
	devHBI.enable(LD.EV_KEY.KEY_REFRESH)  # make KEY_REFRESH available
	devHBI.enable(LD.EV_KEY.KEY_RIGHT)  # make KEY_RIGHT available
	devHBI.enable(LD.EV_KEY.KEY_RIGHTALT)  # make KEY_RIGHTALT available
	devHBI.enable(LD.EV_KEY.KEY_RIGHTBRACE)  # make KEY_RIGHTBRACE available
	devHBI.enable(LD.EV_KEY.KEY_RIGHTCTRL)  # make KEY_RIGHTCTRL available
	devHBI.enable(LD.EV_KEY.KEY_RIGHTMETA)  # make KEY_RIGHTMETA available
	devHBI.enable(LD.EV_KEY.KEY_RIGHTSHIFT)  # make KEY_RIGHTSHIFT available
	devHBI.enable(LD.EV_KEY.KEY_RO)  # make KEY_RO available
	devHBI.enable(LD.EV_KEY.KEY_S)  # make KEY_S available
	devHBI.enable(LD.EV_KEY.KEY_SCROLLDOWN)  # make KEY_SCROLLDOWN available
	devHBI.enable(LD.EV_KEY.KEY_SCROLLLOCK)  # make KEY_SCROLLLOCK available
	devHBI.enable(LD.EV_KEY.KEY_SCROLLUP)  # make KEY_SCROLLUP available
	devHBI.enable(LD.EV_KEY.KEY_SEMICOLON)  # make KEY_SEMICOLON available
	devHBI.enable(LD.EV_KEY.KEY_SLASH)  # make KEY_SLASH available
	devHBI.enable(LD.EV_KEY.KEY_SLEEP)  # make KEY_SLEEP available
	devHBI.enable(LD.EV_KEY.KEY_SPACE)  # make KEY_SPACE available
	devHBI.enable(LD.EV_KEY.KEY_STOP)  # make KEY_STOP available
	devHBI.enable(LD.EV_KEY.KEY_STOPCD)  # make KEY_STOPCD available
	devHBI.enable(LD.EV_KEY.KEY_SYSRQ)  # make KEY_SYSRQ available
	devHBI.enable(LD.EV_KEY.KEY_T)  # make KEY_T available
	devHBI.enable(LD.EV_KEY.KEY_TAB)  # make KEY_TAB available
	devHBI.enable(LD.EV_KEY.KEY_U)  # make KEY_U available
	devHBI.enable(LD.EV_KEY.KEY_UNDO)  # make KEY_UNDO available
	devHBI.enable(LD.EV_KEY.KEY_UNKNOWN)  # make KEY_UNKNOWN available
	devHBI.enable(LD.EV_KEY.KEY_UP)  # make KEY_UP available
	devHBI.enable(LD.EV_KEY.KEY_V)  # make KEY_V available
	devHBI.enable(LD.EV_KEY.KEY_VOLUMEDOWN)  # make KEY_VOLUMEDOWN available
	devHBI.enable(LD.EV_KEY.KEY_VOLUMEUP)  # make KEY_VOLUMEUP available
	devHBI.enable(LD.EV_KEY.KEY_W)  # make KEY_W available
	devHBI.enable(LD.EV_KEY.KEY_WWW)  # make KEY_WWW available
	devHBI.enable(LD.EV_KEY.KEY_X)  # make KEY_X available
	devHBI.enable(LD.EV_KEY.KEY_Y)  # make KEY_Y available
	devHBI.enable(LD.EV_KEY.KEY_YEN)  # make KEY_YEN available
	devHBI.enable(LD.EV_KEY.KEY_Z)  # make KEY_Z available
	devHBI.enable(LD.EV_KEY.KEY_ZENKAKUHANKAKU)  # make KEY_ZENKAKUHANKAKU available

	devHBI.enable(LD.EV_REL.REL_HWHEEL)  # make REL_HWHEEL available
	devHBI.enable(LD.EV_REL.REL_HWHEEL_HI_RES)  # make REL_HWHEEL_HI_RES available
	devHBI.enable(LD.EV_REL.REL_WHEEL)  # make REL_WHEEL available
	devHBI.enable(LD.EV_REL.REL_WHEEL_HI_RES)  # make REL_WHEEL_HI_RES available
	devHBI.enable(LD.EV_REL.REL_X)  # make REL_X available
	devHBI.enable(LD.EV_REL.REL_Y)  # make REL_Y available

	hbiDevice = devHBI.create_uinput_device()
	print(f"New device at {hbiDevice.devnode} ({hbiDevice.syspath})")
	sleep(1)
	return hbiDevice


#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# SCTN50 end of HBI
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#


