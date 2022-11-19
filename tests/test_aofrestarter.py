#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import timedelta
import time
from unittest.mock import Mock, create_autospec

from com.dtmilano.android.adb.adbclient import AdbClient

from aofrestarter import AofRestarter

def test_RestartAof_pause() -> None:
    adbClientMoc = create_autospec(AdbClient)
    AofRestarter.RESTART_TIMEDELTA = timedelta(milliseconds = 100)
    AofRestarter.RESTART_SLEEP_SECONDS = 0
    aofRestarter = AofRestarter(adbClientMoc)
    assert aofRestarter.RestartAof()
    assert not aofRestarter.RestartAof()
    assert not aofRestarter.RestartAof()
    time.sleep(0.1)
    assert aofRestarter.RestartAof()
    assert not aofRestarter.RestartAof()
    assert not aofRestarter.RestartAof()

def test_RestartAof_StartAof() -> None:
    adbClientMoc = create_autospec(AdbClient)
    aofRestarter = AofRestarter(adbClientMoc)
    assert aofRestarter.StartAof()
    assert not aofRestarter.StartAof()
    assert not aofRestarter.StartAof()
    assert adbClientMoc.startActivity.call_count == 1

def test_RestartAof_StopAof() -> None:
    adbClientMoc = create_autospec(AdbClient)
    aofRestarter = AofRestarter(adbClientMoc)
    assert not aofRestarter.StopAof()
    assert aofRestarter.StartAof()
    assert aofRestarter.StopAof()
    assert not aofRestarter.StopAof()
    assert not aofRestarter.StopAof()
    assert adbClientMoc.startActivity.call_count == 1
    assert adbClientMoc.shell.call_count == 1
