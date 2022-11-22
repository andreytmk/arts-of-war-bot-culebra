#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from PIL import Image

import logging
import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))


class UnknownSnapsSaver:
    SNAPS_MIN_TIMEDELTA = timedelta(minutes=5)
    MAX_UNKNOWN_SNAPS_COUNT = 3

    def __init__(self) -> None:
        self.unknownSnapsCount = 0
        self.lastUnknownSnapDT = datetime.utcnow()

    def ProcessUnknownSnap(self, snap: Image.Image) -> bool:
        if self.unknownSnapsCount >= UnknownSnapsSaver.MAX_UNKNOWN_SNAPS_COUNT:
            return False

        currentDT = datetime.utcnow()
        if (currentDT - self.lastUnknownSnapDT <
                UnknownSnapsSaver.SNAPS_MIN_TIMEDELTA):
            return False

        logging.info("unknown screen snap")
        dtStr = datetime.now().strftime("%Y%m%d%H%M%S")
        screenFileName = os.path.join(SCRIPT_PATH,
                                      "logs/unknown-%s.png") % dtStr
        snap.save(screenFileName, 'png')
        self.lastUnknownSnapDT = currentDT
        self.unknownSnapsCount += 1
        return True

    def ResetSnapSaver(self):
        self.unknownSnapsCount = 0
        self.lastUnknownSnapDT = datetime.utcnow()

    def ResetLastUnknownSnapDT(self):
        self.lastUnknownSnapDT = datetime.utcnow()

    def IsUnknownLimitReached(self):
        return (self.unknownSnapsCount >=
                UnknownSnapsSaver.MAX_UNKNOWN_SNAPS_COUNT)
