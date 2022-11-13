#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from com.dtmilano.android.adb.adbclient import AdbClient
from datetime import datetime
from datetime import timedelta
from PIL import Image

import logging
import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

class UnknownSnapsSaver:
    SNAPS_MIN_TIMEDELTA = timedelta(minutes = 5)
    MAX_UNKNOWN_SNAPS_COUNT = 6

    def __init__(self, device: AdbClient) -> None:
        self.device = device
        self.unknownSnapsCount = 0
        self.lastUnknownSnapDT = datetime.utcnow()

    def ProcessUnknownSnap(self, snap: Image) -> None:
        if self.unknownSnapsCount >= UnknownSnapsSaver.MAX_UNKNOWN_SNAPS_COUNT:
            return
        
        currentDT = datetime.utcnow()
        if currentDT - self.lastUnknownSnapDT < UnknownSnapsSaver.SNAPS_MIN_TIMEDELTA:
            return

        logging.info("unknown screen snap")
        dtStr = datetime.now().strftime("%Y%m%d%H%M%S")
        screenFileName = os.path.join(SCRIPT_PATH, "logs/unknown-%s.png") % dtStr
        snap.writeToFile(screenFileName,'png')
