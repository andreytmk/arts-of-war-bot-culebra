#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import timedelta
import time
from unittest.mock import Mock, create_autospec

from com.dtmilano.android.adb.adbclient import AdbClient

from aofrestarter import AofRestarter

class TestAofRestarter:
    adbClientMoc = create_autospec(AdbClient)
    adbClientMoc.shell.return_value = None

    def test_RestartAof_pause(self) -> None:
        AofRestarter.RESTART_TIMEDELTA = timedelta(milliseconds = 100)
        AofRestarter.RESTART_SLEEP_SECONDS = 0
        aofRestarter = AofRestarter(TestAofRestarter.adbClientMoc)
        assert aofRestarter.RestartAof()
        assert not aofRestarter.RestartAof()
        assert not aofRestarter.RestartAof()
        time.sleep(0.1)
        assert aofRestarter.RestartAof()
        assert not aofRestarter.RestartAof()
        assert not aofRestarter.RestartAof()
