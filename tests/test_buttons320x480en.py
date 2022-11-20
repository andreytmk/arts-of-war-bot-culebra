#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from tests.buttonstestutils import SampleSnapshot, checkSampleSnapshot
from scenario import Action
from buttons320x480en import LoadButtons

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_SNAPS_PATH = os.path.join(SCRIPT_PATH, 'testsnaps320x480en')

BUTTONS = LoadButtons()


def processCheck(samplesnap: str, actions: list[Action]):
    sampleSnap = SampleSnapshot().setData(samplesnap, actions)
    sampleSnap.loadSnap(TEST_SNAPS_PATH)
    checkSampleSnapshot(sampleSnap, BUTTONS)


def test_mainScreen1() -> None:
    processCheck('mainScreen1.png', [Action.MAIN_BATTLE, Action.TERRITORY])


def test_mainScreen2() -> None:
    processCheck('mainScreen2.png', [Action.MAIN_BATTLE, Action.TERRITORY])


def test_googlePlay1() -> None:
    processCheck('googlePlay1.png', [Action.CLOSE_GOOGLE_PLAY])


def test_googlePlay2() -> None:
    processCheck('googlePlay2.png', [Action.CLOSE_GOOGLE_PLAY])


def test_levelBattle1() -> None:
    processCheck('levelBattle1.png', [Action.LEVEL_START_BATTLE])


def test_nextLevel1() -> None:
    processCheck('nextLevel1.png', [Action.NEXT_LEVEL])


def test_defeatLevel1() -> None:
    processCheck('defeatLevel1.png', [Action.DEFEAT_NEXT_LEVEL])


def test_territoryScreen1() -> None:
    processCheck('territoryScreen1.png', [Action.HEADHUNT])


def test_territoryScreen2() -> None:
    processCheck('territoryScreen2.png', [Action.HEADHUNT])


def test_headhuntScreen1() -> None:
    processCheck('headhuntScreen1.png', [Action.TREASURE_EASY_ATTACK,
                                         Action.TREASURE_HARD_ATTACK,
                                         Action.INFINITY_ATTACK])


def test_headhuntEasy1() -> None:
    processCheck('headhuntEasy1.png', [Action.FIGHT])


def test_headhuntWin1() -> None:
    processCheck('headhuntWin1.png', [Action.HEADHUNT_NEXT])


def test_headhuntHard1() -> None:
    processCheck('headhuntHard1.png', [Action.FIGHT])


def test_headhuntWin2() -> None:
    processCheck('headhuntWin2.png', [Action.HEADHUNT_NEXT])


def test_infinityMenu1() -> None:
    processCheck('infinityMenu1.png', [Action.INFINITY_MENU_ATTACK])


def test_infinityMenu2() -> None:
    processCheck('infinityMenu2.png', [Action.INFINITY_MENU_ATTACK])


def test_infinityMenu3() -> None:
    processCheck('infinityMenu3.png', [Action.INFINITY_MENU_ATTACK])


def test_infinityMenu4() -> None:
    processCheck('infinityMenu4.png', [])


def test_infinityBattle1() -> None:
    processCheck('infinityBattle1.png', [Action.FIGHT])


def test_infinityNext1() -> None:
    processCheck('infinityNext1.png', [Action.INFINITY_NEXT])


def test_retryScreen1() -> None:
    processCheck('retryScreen1.png', [Action.RETRY_CONNECTION])
