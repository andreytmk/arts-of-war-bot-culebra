#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
import time

from com.dtmilano.android.adb.adbclient import AdbClient


class AofRestarter:
    ACTIVITY_NAME = 'com.addictive.strategy.army/.UnityPlayerActivity'
    RESTART_TIMEDELTA = timedelta(minutes=10)
    CHECK_ACTIVITY_TIMEDELTA = timedelta(minutes=1)
    RESTART_SLEEP_SECONDS = 1

    def __init__(self, device: AdbClient) -> None:
        self.device = device
        self.lastRestartDT = None
        self.lastCheckActivityDT = datetime.utcnow()
        self.isRunning = False

    def RestartAof(self) -> bool:
        currentDT = datetime.utcnow()
        if (self.lastRestartDT and currentDT - self.lastRestartDT
                < AofRestarter.RESTART_TIMEDELTA):
            return False

        self.isRunning = True
        self.StopAof()
        time.sleep(AofRestarter.RESTART_SLEEP_SECONDS)
        self.StartAof()
        self.lastRestartDT = currentDT
        return True

    def StartAof(self) -> bool:
        if self.isRunning:
            currentDT = datetime.utcnow()
            if (currentDT - self.lastCheckActivityDT
                    < AofRestarter.CHECK_ACTIVITY_TIMEDELTA):
                return False
            self.lastCheckActivityDT = currentDT
            if self.device.getTopActivityName() == AofRestarter.ACTIVITY_NAME:
                return False

        self.device.startActivity(AofRestarter.ACTIVITY_NAME)
        self.isRunning = True
        return True

    def StopAof(self) -> bool:
        if not self.isRunning:
            return False
        self.device.shell("am force-stop com.addictive.strategy.army")
        self.isRunning = False
        return True
