#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from com.dtmilano.android.adb.adbclient import AdbClient
from com.dtmilano.android.viewclient import ViewClient
from aofcounter import AofCounter
from aofrestarter import AofRestarter

from botbase import Button
from buttons320x480en import LoadButtons
from unknownsnapssaver import UnknownSnapsSaver
from scenario import COMMON_ACTIONS, SCENARIO_BASE
from PIL import Image

import os
import logging
import random
import sys
import time
from datetime import datetime

LOOP_SECONDS = 1
TOUCH_PADDING = 3

DEVICE_ARGS = {
    'ignoreversioncheck': False,
    'verbose': False,
    'ignoresecuredevice': False
    }

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
buttons = LoadButtons()

logging.basicConfig(
    filename=os.path.join(SCRIPT_PATH, 'logs/artsofwarbot.log'),
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

logging.info("Starting ARTS OF WAR bot")


def checkButton(snap: Image, button: Button) -> bool:
    snapButton = snap.crop((
        button.x,
        button.y,
        button.x + button.width,
        button.y + button.height
        ))
    snapSame = AdbClient.sameAs(snapButton, button.img, 0.9)
    if snapSame:
        return True
    return False


def processButtonClick(device: AdbClient, button: Button) -> None:
    touchX = random.randint(button.x + TOUCH_PADDING,
                            button.x + button.width - TOUCH_PADDING)
    touchY = random.randint(button.y + TOUCH_PADDING,
                            button.y + button.height - TOUCH_PADDING)
    sleepSeconds = random.randint(1, 10) / 10.0
    logging.debug("touch -> action: %d; x: %d; y: %d; sleepSeconds: %f"
                  % (button.action, touchX, touchX, sleepSeconds))
    time.sleep(sleepSeconds)
    device.touch(touchX, touchY, eventType=AdbClient.DOWN_AND_UP)


def processLoopAction(
        device: AdbClient,
        buttons: Button,
        unknownSnapsSaver: UnknownSnapsSaver,
        aofRestarter: AofRestarter,
        aofCounter: AofCounter
        ) -> None:

    snap = device.takeSnapshot(reconnect=True)
    currentDT = datetime.utcnow()
    currentTime = currentDT.time()

    availableActions = set()
    for scenarioAction in SCENARIO_BASE:
        if scenarioAction.IsActionTime(currentTime):
            for action in scenarioAction.actions:
                availableActions.add(action)

    if len(availableActions) == 0:
        aofRestarter.StopAof()
        return

    aofRestarter.StartAof()

    for button in buttons:
        if button.action in COMMON_ACTIONS:
            if checkButton(snap, button):
                processButtonClick(device, button)
                unknownSnapsSaver.ResetLastUnknownSnapDT()
                aofCounter.LogAction(button.action)
                return

    for button in buttons:
        if button.action in availableActions:
            if checkButton(snap, button):
                processButtonClick(device, button)
                unknownSnapsSaver.ResetLastUnknownSnapDT()
                aofCounter.LogAction(button.action)
                return

    unknownSnapsSaver.ProcessUnknownSnap(snap)
    if unknownSnapsSaver.IsUnknownLimitReached():
        if aofRestarter.RestartAof():
            unknownSnapsSaver.ResetSnapSaver()


def getSnapshot(device: AdbClient) -> None:
    snap = device.takeSnapshot()
    dtStr = datetime.now().strftime("%Y%m%d%H%M%S")
    snapshotFileName = os.path.join(SCRIPT_PATH, "snaps/snap-%s.png") % dtStr
    snap.save(snapshotFileName, 'png')


def runLoop(infinite: bool) -> None:
    (device, serialno) = ViewClient.connectToDeviceOrExit(**DEVICE_ARGS)
    buttons = LoadButtons()
    unknownSnapsSaver = UnknownSnapsSaver()
    aofRestarter = AofRestarter(device)
    aofCounter = AofCounter(logging.getLogger())

    if infinite:
        while True:
            processLoopAction(device,
                              buttons,
                              unknownSnapsSaver,
                              aofRestarter,
                              aofCounter)
            time.sleep(LOOP_SECONDS)
    else:
        processLoopAction(device,
                          buttons,
                          unknownSnapsSaver,
                          aofRestarter,
                          aofCounter)


def printHelp() -> None:
    print("Available commands:")
    print("--runloop - run infinte loop and " +
          "checking screen with LOOP_SECONDS interval.")
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
