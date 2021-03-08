#!/usr/bin/python


import CF
import DO
import gc
import HBI


gc.enable()
HBIDev = HBI.IDB()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# checkDeviceConnect check and try to (re)connect all enabled devices
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkDeviceConnect():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	for thisDevice_, theseParms_ in DO.DEVICES.items():
		# ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1
		if theseParms_[DO.DEV_ENABLED] is True and theseParms_[DO.DEV_STATUS] == DO.DEVICESTATUS_CONNECTED:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			continue
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif theseParms_[DO.DEV_ENABLED] is True and theseParms_[DO.DEV_STATUS] == DO.DEVICESTATUS_DISCONNECTED:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			TFD = DO.openOutputDevice(theseParms_[DO.DEV_NAME])
			if TFD is None:
				# ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2
				DO.DEVICES[thisDevice_][DO.DEV_STATUS] = DO.DEVICESTATUS_ERROR
				DO.DEVICES[thisDevice_][DO.DEV_ERR_NEXTTIME] = CF.MTSPlus(theseParms_[DO.DEV_ERR_DELTA])
				DO.DEVICES[thisDevice_][DO.DEV_FD] = TFD
				continue
				# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
			else:
				# ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2
				DO.DEVICES[thisDevice_][DO.DEV_STATUS] = DO.DEVICESTATUS_CONNECTED
				DO.DEVICES[thisDevice_][DO.DEV_FD] = TFD
				if DO.DEVICES[thisDevice_][DO.DEV_GRAB] is True:
					DO.DEVICES[thisDevice_][DO.DEV_FD].grab()
				continue
				# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		elif theseParms_[DO.DEV_ENABLED] is True and theseParms_[DO.DEV_STATUS] == DO.DEVICESTATUS_ERROR:
			# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
			if CF.isPast(DO.DEVICES[DO.DEV_ERR_NEXTTIME]) is True:
				# ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2
				TFD = DO.openOutputDevice(theseParms_[DO.DEV_NAME])

				if TFD is None:
					# ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3
					DO.DEVICES[thisDevice_][DO.DEV_STATUS] = DO.DEVICESTATUS_ERROR
					DO.DEVICES[thisDevice_][DO.DEV_ERR_NEXTTIME] = CF.MTSPlus(theseParms_[DO.DEV_ERR_DELTA])
					DO.DEVICES[thisDevice_][DO.DEV_FD] = TFD
					continue
					# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

				else:
					# ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3
					DO.DEVICES[thisDevice_][DO.DEV_STATUS] = DO.DEVICESTATUS_CONNECTED
					DO.DEVICES[thisDevice_][DO.DEV_FD] = TFD
					continue
					# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

				# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

			# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

		# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doAX
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doAX(AXToDo_, btnNdx_, btnAxType_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if btnAxType_ == DO.BTNAXTYPE_NORMAL:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# print(f"doAX sending {DO.ACTIONS[AXToDo_]}{CF.NEWLINE}")
		HBIDev.send_events(DO.ACTIONS[AXToDo_[0]])
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif btnAxType_ == DO.BTNAXTYPE_TOGGLE:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# print(f"doAX sending {DO.ACTIONS[AXToDo_]}{CF.NEWLINE}")
		HBIDev.send_events(DO.ACTIONS[AXToDo_[btnNdx_]])
		btnNdx_ = DO.incNdx(AXToDo_, btnNdx_)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif btnAxType_ == DO.BTNAXTYPE_LOCKING:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# print(f"doAX sending {DO.ACTIONS[AXToDo_]}{CF.NEWLINE}")
		btnNdx_ = 0
		HBIDev.send_events(DO.ACTIONS[AXToDo_[btnNdx_]])
		# btnNdx_ = DO.incNdx(AXToDo_, btnNdx_)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	elif btnAxType_ == DO.BTNAXTYPE_MODED:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		print(f"doAX sending {DO.ACTIONS[AXToDo_]}{CF.NEWLINE}")
		btnNdx_ = 0
		HBIDev.send_events(DO.ACTIONS[AXToDo_[btnNdx_]])
		# btnNdx_ = DO.incNdx(AXToDo_, btnNdx_)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	return btnNdx_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# dispatchEvents
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dispatchEvents(thisDevice_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
#	for thisDevice_ in DO.DEVICES:
#		# ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1
	thisQueue_ = DO.DEVICES[thisDevice_][DO.DEV_QUEUE]
	if thisQueue_ is None:
		thisQueue_ = []
	queueLen_ = len(thisQueue_)
	if (queueLen_ == 0) or \
			(queueLen_ > 3) or \
			(thisQueue_[-1][1] != DO.KEYPRS):
		# print(f"invalid queue {thisQueue_}")
		return  # continue
	print(f"""thisQueue_ {thisQueue_}{CF.CLREOL}{CF.NEWLINE}{CF.MTSclr()}""")
	spent_ = DO.DEVICES[thisDevice_][DO.DEV_SPENT]
	nextDelta_ = DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIMEDELTA]
	isPast_ = CF.isPast(DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME])
	hasPaused_ = DO.DEVICES[thisDevice_][DO.DEV_HASPAUSED]
	print(f"spent_ {spent_} nextDelta_ {nextDelta_} isPast_ {isPast_} hasPaused_ {hasPaused_}")
	if (spent_ is True and nextDelta_ != 0 and isPast_ is True) or (spent_ is False):
		try:
			if queueLen_ == 1:
				newNdx_ = doAX(
					DO.PROFILE[thisDevice_][thisQueue_[0][0]],
					DO.BTNNDXDICT[thisDevice_][thisQueue_[0][0]],
					DO.BTNTYPEDICT[thisDevice_][thisQueue_[0][0]])
				DO.BTNNDXDICT[thisDevice_][thisQueue_[0][0]] = newNdx_

			elif queueLen_ == 2:
				newNdx_ = doAX(
					DO.PROFILE[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]],
					DO.BTNNDXDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]],
					DO.BTNTYPEDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]])
				DO.BTNNDXDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]] = newNdx_

			elif queueLen_ == 3:
				newNdx_ = doAX(
					DO.PROFILE[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]],
					DO.BTNNDXDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]],
					DO.BTNTYPEDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]])
				DO.BTNNDXDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]] = newNdx_

			if isPast_ is True and DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME] != 0:
				DO.DEVICES[thisDevice_][DO.DEV_HASPAUSED] = True

			DO.DEVICES[thisDevice_][DO.DEV_SPENT] = True
			if nextDelta_ != 0:
				if hasPaused_ is False:
					DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME] = CF.MTSPlus(nextDelta_ + DO.DORPT_PAUSE)
				else:
					DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME] = CF.MTSPlus(nextDelta_)
			else:
				DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME] = 0

		except KeyError:
			DO.DEVICES[thisDevice_][DO.DEV_SPENT] = True
			print("KeyError")
			return  # continue
		except KeyboardInterrupt:
			exit()
#		# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1
	DO.DEVICES[thisDevice_][DO.DEV_SPENT] = True

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# __main__
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def __main__():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	checkDeviceConnect()
	# print(f"{CF.CLRALL}")
	while True:
		try:
			for thisDevice_ in DO.DEVICES:
				DO.queueEvents(thisDevice_)
				dispatchEvents(thisDevice_)
		except DO.LD.EventsDroppedException:
			print(f"dropped events{CF.NEWLINE}")
		except OSError as e:
			if e.strerror == 'No such device':
				# handle lost device
				print("lost device")
		except KeyboardInterrupt:
			exit()

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


if __name__ == "__main__":
	__main__()
