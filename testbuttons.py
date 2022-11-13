#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from com.dtmilano.android.adb.adbclient import AdbClient
from buttons320x480en import LoadButtons
from botbase import TestSnapshot
from scenario import Action

from PIL import Image
import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

BUTTONS320x480EN_TESTPATH = 'buttons320x480en/testsnaps'

BUTTONS320x480EN_TESTS = [
    TestSnapshot().setData('mainScreen1.png'        , [Action.MAIN_BATTLE])
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def LoadTestButtons():
    for button in BUTTONS320x480EN_TESTS:
        button.snap = Image.open(os.path.join(SCRIPT_PATH, BUTTONS320x480EN_TESTPATH, button.testsnap));
    return BUTTONS320x480EN_TESTS

failedTests = 0;
successTests = 0

def runTest(testSnap, buttons):
    global failedTests
    global successTests

    expected = set(testSnap.actions)
    actual = set()
    for button in buttons:
        snapButton = testSnap.snap.crop((button.x, button.y, button.x + button.width, button.y + button.height))
        snapSame = AdbClient.sameAs(snapButton, button.img, 0.9)
        if snapSame:
            actual.add(button.action)
    if expected > actual:
        print(bcolors.FAIL + "[MISSED ACTIONS]" + bcolors.ENDC + " snapshot file: %s" % (testSnap.testsnap))
        print(expected - actual)
        failedTests += 1
    elif actual > expected:
        print(bcolors.FAIL + "[UNEXPECTED ACTIONS]" + bcolors.ENDC + " snapshot file: %s" % (testSnap.testsnap))
        print(actual - expected)
        failedTests += 1
    else:
        successTests += 1

buttonTests = LoadTestButtons()
buttons = LoadButtons();

for testSnap in buttonTests:
    runTest(testSnap, buttons)

if failedTests == 0:
    print(bcolors.OKGREEN + "[TESTS PASSED (%d/%d)]" % (successTests, successTests + failedTests) + bcolors.ENDC)
else:
    print(bcolors.FAIL + "[TESTS FAILED (%d/%d)]" % (successTests, successTests + failedTests) + bcolors.ENDC)
