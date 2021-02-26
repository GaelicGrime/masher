#!/usr/bin/python


import CF
import DO
import gc
import HBI


gc.enable()
HBIDev = HBI.IDB()


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# setRptTime
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def setRptTime(device_, delta_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	# print(f"setting repeat time for {device_} to {delta_}")

	if delta_ == 0:
		DO.DEVICES[device_][DO.DEV_RPT_NEXTTIME] = 0
		DO.DEVICES[device_][DO.DEV_RPT_NEXTTIMEDELTA] = 0

	else:
		DO.DEVICES[device_][DO.DEV_RPT_NEXTTIME] = CF.MTSPlus(delta_)
		DO.DEVICES[device_][DO.DEV_RPT_NEXTTIMEDELTA] = delta_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


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
# deleteReleasedEvent
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deleteReleasedEvent(queueIn_, eventIn_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	queueOut_ = []
	for thisEvent_ in queueIn_:
		if not DO.isMatch(thisEvent_, eventIn_):
			queueOut_.append(thisEvent_)
	return queueOut_
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# checkDevices check all enabled and connected devices for input, add/subtract from the queue
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkDevices():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	for thisDevice_ in DO.DEVICES:
		# ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1 ⥥1
		if DO.DEVICES[thisDevice_][DO.DEV_STATUS] == DO.DEVICESTATUS_CONNECTED and DO.DEVICES[thisDevice_][DO.DEV_ENABLED] is True:
			# ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2
			for thisEvent_ in DO.DEVICES[thisDevice_][DO.DEV_FD].events():
				# ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3 ⥥3
				thisEventOut_ = DO.fixEvent(thisDevice_, thisEvent_)
				if thisEventOut_[1] == 0:
					# ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4
					newQueue_ = deleteReleasedEvent(DO.DEVICES[thisDevice_][DO.DEV_QUEUE], thisEventOut_)
					if newQueue_ == []:
						deviceType_ = DO.DEVICES[thisDevice_][DO.DEV_DEVICETYPE]
						if deviceType_ == DO.DEVICETYPE_GAMEPAD:
							DO.DEVICES[thisDevice_][DO.DEV_ABSHAT_STATUS] = DO.DIRNOT_VAL
							DO.DEVICES[thisDevice_][DO.DEV_ABSLTSTK_STATUS] = DO.DIRNOT_VAL
							DO.DEVICES[thisDevice_][DO.DEV_ABSRTSTK_STATUS] = DO.DIRNOT_VAL
						elif deviceType_ == DO.DEVICETYPE_MOUSE:
							DO.DEVICES[thisDevice_][DO.DEV_RELMSE_STATUS] = DO.DIRNOT_VAL
							DO.DEVICES[thisDevice_][DO.DEV_RELMW_STATUS] = DO.DIRNOT_VAL
					DO.DEVICES[thisDevice_][DO.DEV_QUEUE] = newQueue_
					DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME] = 0
					DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIMEDELTA] = 0
					DO.DEVICES[thisDevice_][DO.DEV_SPENT] = False
					# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4
				elif thisEventOut_[0] is not None and thisEventOut_[1] is not None and thisEventOut_ not in DO.DEVICES[thisDevice_][DO.DEV_QUEUE]:
					# ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4 ⥥4
					DO.DEVICES[thisDevice_][DO.DEV_QUEUE].append(thisEventOut_)
					DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME] = 0
					DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIMEDELTA] = 0
					DO.DEVICES[thisDevice_][DO.DEV_SPENT] = False
					# ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4 ⥣4

				# ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3 ⥣3

			# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2
		elif DO.DEVICES[thisDevice_][DO.DEV_STATUS] == DO.DEVICESTATUS_ERROR and CF.isPast(DO.DEVICES[thisDevice_][DO.DEV_ERR_NEXTTIME]) is True:
			# ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2 ⥥2
			thisResult_ = checkDeviceConnect()
			# ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2 ⥣2

		# ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1 ⥣1

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# doAX
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def doAX(AXToDo_):
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	if DO.SPCL_PAUSE in AXToDo_:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# do something with a pause
		list1_ = []
		list2_ = []
		listSpcl_ = []
		for LDEVToSend_ in AXToDo_:
			if LDEVToSend_ not in DO.SPCLAXLIST and listSpcl_ is []:
				list1_.append(LDEVToSend_)
			elif LDEVToSend_ in DO.SPCLAXLIST:
				listSpcl_.append(LDEVToSend_)
			elif LDEVToSend_ not in DO.SPCLAXLIST and listSpcl_ is not []:
				list2_.append(LDEVToSend_)
		print(f"doAX+SPCL_ list1_ {list1_} listSpcl_ {listSpcl_} list2_ {list2_}")
		# HBIDev.send_events(*AXToDo_)
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2
	else:
		# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
		# print(f"doAX sending {DO.ACTIONS[AXToDo_]}{CF.NEWLINE}")
		HBIDev.send_events(DO.ACTIONS[AXToDo_])
		# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# dispatchEvents
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def dispatchEvents():
	# fold here ⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1⥥1
	for thisDevice_ in DO.DEVICES:
		thisQueue_ = DO.DEVICES[thisDevice_][DO.DEV_QUEUE]
		# print(f"""dispatchEvents queue {thisDevice_} {thisQueue_}""")
		QLen_ = len(thisQueue_)
		if QLen_ == 0 or QLen_ > 3:
			continue
		spent_ = DO.DEVICES[thisDevice_][DO.DEV_SPENT]
		nextDelta_ = DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIMEDELTA]
		isPast_ = CF.isPast(DO.DEVICES[thisDevice_][DO.DEV_RPT_NEXTTIME])
		if (spent_ is True and nextDelta_ != 0 and isPast_ is True) or (spent_ is False):
			try:
				if QLen_ == 1:
					# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
					if thisQueue_[0][1] == 1:
						# CF.displayStats(10, 0, f"not holdable 1st queue {thisQueue_} spent_ {spent_}{CF.NEWLINE} DEVICES {DO.DEVICES[thisDevice_]}")
						thisRepeat_ = DO.REPEATDICT[thisDevice_][thisQueue_[0][0]]
						if thisRepeat_ == 0:
							setRptTime(thisDevice_, thisRepeat_)
						elif spent_ is False:
							setRptTime(thisDevice_, thisRepeat_ + DO.DORPT_PAUSE)
						else:
							setRptTime(thisDevice_, thisRepeat_)
						# CF.displayStats(20, 0, f"""doAX(DO.PROFILE[{thisDevice_}][{thisQueue_[0][0]}]) {DO.PROFILE[thisDevice_][thisQueue_[0][0]]}""")
						doAX(DO.PROFILE[thisDevice_][thisQueue_[0][0]])
					# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

				elif QLen_ == 2:
					# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
					if thisQueue_[0][1] == 2 and thisQueue_[1][1] == 1:
						thisRepeat_ = DO.REPEATDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]]
						if thisRepeat_ == 0:
							setRptTime(thisDevice_, thisRepeat_)
						elif spent_ is False:
							setRptTime(thisDevice_, thisRepeat_ + DO.DORPT_PAUSE)
						else:
							setRptTime(thisDevice_, thisRepeat_)
						doAX(DO.PROFILE[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]])
					# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

				elif QLen_ == 3:
					# fold here ⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2⥥2
					if thisQueue_[0][1] == 2 and thisQueue_[1][1] == 2 and thisQueue_[2][1] == 1:
						thisRepeat_ = DO.REPEATDICT[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]]
						if thisRepeat_ == 0:
							setRptTime(thisDevice_, thisRepeat_)
						elif spent_ is False:
							setRptTime(thisDevice_, thisRepeat_ + DO.DORPT_PAUSE)
						else:
							setRptTime(thisDevice_, thisRepeat_)
						doAX(DO.PROFILE[thisDevice_][thisQueue_[0][0]][thisQueue_[1][0]][thisQueue_[2][0]])
					# fold here ⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2⥣2

				DO.DEVICES[thisDevice_][DO.DEV_SPENT] = True
				spent_ = True
				continue

			except KeyError:
				DO.DEVICES[thisDevice_][DO.DEV_SPENT] = True
				spent_ = True
				continue
			except KeyboardInterrupt:
				exit()

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
			checkDevices()
			# CF.displayStats(25, 0, f"""MIMD[queue] {DO.DEVICES[DO.MIMD][DO.DEV_QUEUE]}{CF.CLREOL}""")
		# except IOError:
			# pass
		except DO.LD.EventsDroppedException:
			print(f"dropped events{CF.NEWLINE}")
		except OSError as e:
			if e.strerror == 'No such device':
				# handle lost device
				print("lost device")
		except KeyboardInterrupt:
			exit()

		dispatchEvents()
	# fold here ⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1⥣1


if __name__ == "__main__":
	__main__()
