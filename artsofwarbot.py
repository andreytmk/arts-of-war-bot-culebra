#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from com.dtmilano.android.adb.adbclient import AdbClient
from com.dtmilano.android.viewclient import ViewClient

from botbase import Button
from buttons320x480en import LoadButtons
from unknownsnapssaver import UnknownSnapsSaver
from scenario import SCENARIO_BASE
from PIL import Image

import os
import logging
import random
import sys
import time
from datetime import datetime

LOOP_SECONDS = 1
TOUCH_PADDING = 3

DEVICE_ARGS = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

buttons = LoadButtons()

logging.basicConfig(
    filename=os.path.join(SCRIPT_PATH, 'logs/artsofwarbot.log'),
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

logging.info("Starting ARTS OF WAR bot")

def checkButton(device: AdbClient, snap: Image, button: Button) -> None:
    snapButton = snap.crop((button.x, button.y, button.x + button.width, button.y + button.height))
    snapSame = AdbClient.sameAs(snapButton, button.img, 0.9)
    if snapSame:
        touchX = random.randint(button.x + TOUCH_PADDING, button.x + button.width - TOUCH_PADDING)
        touchY = random.randint(button.y + TOUCH_PADDING, button.y + button.height - TOUCH_PADDING)
        sleepSeconds = random.randint(1, 10) / 10.0
        logging.debug("touch -> image: %s; x: %d; y: %d; sleepSeconds: %f"
                     % (button.imgfile, touchX, touchX, sleepSeconds))
        time.sleep(sleepSeconds)
        device.touch(touchX, touchY, eventType=AdbClient.DOWN_AND_UP)
        return True
    return False

def processLoopAction(device: AdbClient, buttons: Button, unknownSnapsSaver: UnknownSnapsSaver) -> None:
    snap = device.takeSnapshot(reconnect=True)
    currentDT = datetime.utcnow()
    currentTime = currentDT.time()

    availableActions = set()
    for scenarioAction in SCENARIO_BASE:
        if scenarioAction.fromTime <= currentTime and currentTime <= scenarioAction.toTime:
            for action in scenarioAction.actions:
                availableActions.add(action)

    if len(availableActions) == 0:
        return

    for button in buttons:
        if button.action in availableActions:
            if checkButton(device, snap, button):
                return
    
    unknownSnapsSaver.ProcessUnknownSnap(snap)

def getSnapshot(device: AdbClient) -> None:
    snap = device.takeSnapshot()
    dtStr = datetime.now().strftime("%Y%m%d%H%M%S")
    snapshotFileName = os.path.join(SCRIPT_PATH, "snaps/snap-%s.png") % dtStr
    snap.save(snapshotFileName,'png')

def runLoop(infinite: bool) -> None:
    (device, serialno) = ViewClient.connectToDeviceOrExit(**DEVICE_ARGS)
    buttons = LoadButtons()
    unknownSnapsSaver = UnknownSnapsSaver(device)

    if infinite:
        while True:
            processLoopAction(device, buttons, unknownSnapsSaver)
            time.sleep(LOOP_SECONDS)
    else:
        processLoopAction(device, buttons, unknownSnapsSaver)

def printHelp() -> None:
    print("Available commands:")
    print("--runloop - run infinte loop and checking screen with LOOP_SECONDS interval.")
    print("--processaction - execute one iteration of the loop and exit")
    print("--snapshot - take snapshot and exit")

if len(sys.argv) < 2:
    printHelp()
elif sys.argv[1] == "--runloop":
    runLoop(True)
elif sys.argv[1] == "--processaction":
    runLoop(False)
elif sys.argv[1] == "--snapshot":
    (device, serialno) = ViewClient.connectToDeviceOrExit(**DEVICE_ARGS)
    getSnapshot(device)
else:
    printHelp()

logging.info("ARTS OF WAR end of script")
