#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from PIL import Image
from com.dtmilano.android.adb.adbclient import AdbClient

from botbase import Button
from scenario import Action


class SampleSnapshot:
    def __init__(self) -> None:
        self.samplesnap = None
        self.actions = []
        self.snap = None

    def setData(self,
                samplesnap: str,
                actions: list[Action]) -> 'SampleSnapshot':
        self.samplesnap = samplesnap
        self.actions = actions
        return self

    def loadSnap(self, snapsDir: str) -> None:
        self.snap = Image.open(os.path.join(snapsDir, self.samplesnap))


def checkSampleSnapshot(sampleSnap: SampleSnapshot,
                        buttons: list[Button]) -> None:
    expected = set(sampleSnap.actions)
    actual = set()
    for button in buttons:
        snapButton = sampleSnap.snap.crop((button.x,
                                           button.y,
                                           button.x + button.width,
                                           button.y + button.height))
        snapSame = AdbClient.sameAs(snapButton, button.img, 0.9)
        if snapSame:
            actual.add(button.action)
    assert actual == expected
