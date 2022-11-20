#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import timedelta
import time
from unittest.mock import create_autospec
from unknownsnapssaver import UnknownSnapsSaver
from PIL import Image


def test_UnknownSnapsSaver():
    UnknownSnapsSaver.MAX_UNKNOWN_SNAPS_COUNT = 2
    UnknownSnapsSaver.SNAPS_MIN_TIMEDELTA = timedelta(milliseconds=100)

    snapMoc = create_autospec(Image.Image)
    snapsSaver = UnknownSnapsSaver()
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    time.sleep(0.1)
    assert snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    time.sleep(0.1)
    assert snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    time.sleep(0.1)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)

    snapsSaver.ResetSnapSaver()

    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    time.sleep(0.1)
    assert snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    time.sleep(0.1)
    assert snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    time.sleep(0.1)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)
    assert not snapsSaver.ProcessUnknownSnap(snapMoc)

    assert snapMoc.save.call_count == 4
