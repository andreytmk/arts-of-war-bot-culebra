#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from tests.buttonstestutils import SampleSnapshot, checkSampleSnapshot
from scenario import Action
from buttons320x480en import LoadButtons

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_SNAPS_PATH  = os.path.join(SCRIPT_PATH, 'testsnaps320x480en')

BUTTONS = LoadButtons()

def processCheck(samplesnap: str, actions: list[Action]):
    sampleSnap = SampleSnapshot().setData(samplesnap, actions)
    sampleSnap.loadSnap(TEST_SNAPS_PATH)
    checkSampleSnapshot(sampleSnap, BUTTONS)

def test_mainScreen1() -> None:
    processCheck('mainScreen1.png', [Action.MAIN_BATTLE])
