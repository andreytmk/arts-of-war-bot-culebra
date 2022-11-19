#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
import time

from com.dtmilano.android.adb.adbclient import AdbClient

class AofRestarter:
    RESTART_TIMEDELTA = timedelta(minutes = 10)
    RESTART_SLEEP_SECONDS = 1

    def __init__(self, device: AdbClient) -> None:
        self.device = device
        self.lastRestartDT = None
    
    def RestartAof(self) -> bool:
        currentDT = datetime.utcnow()
        if (self.lastRestartDT and currentDT - self.lastRestartDT < AofRestarter.RESTART_TIMEDELTA):
            return False

        self.device.shell("am force-stop com.addictive.strategy.army")
        time.sleep(AofRestarter.RESTART_SLEEP_SECONDS)
        self.device.startActivity('com.addictive.strategy.army/.UnityPlayerActivity')
        self.lastRestartDT = currentDT
        return True
