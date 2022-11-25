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
    processCheck('mainScreen1.png', [Action.MAIN_BATTLE,
                                     Action.TERRITORY,
                                     Action.STASH_REWARD,
                                     Action.ARENA])


def test_mainScreen2() -> None:
    processCheck('mainScreen2.png', [Action.MAIN_BATTLE,
                                     Action.TERRITORY,
                                     Action.STASH_REWARD,
                                     Action.ARENA])


def test_mainScreen3() -> None:
    processCheck('mainScreen3.png', [Action.MAIN_BATTLE,
                                     Action.TERRITORY,
                                     Action.STASH_REWARD,
                                     Action.ARENA])


def test_mainScreen4() -> None:
    processCheck('mainScreen4.png', [Action.MAIN_BATTLE,
                                     Action.TERRITORY,
                                     Action.STASH_REWARD,
                                     Action.ARENA])


def test_googlePlay1() -> None:
    processCheck('googlePlay1.png', [Action.CLOSE_GOOGLE_PLAY])


def test_googlePlay2() -> None:
    processCheck('googlePlay2.png', [Action.CLOSE_GOOGLE_PLAY])


def test_googlePlay3() -> None:
    processCheck('googlePlay3.png', [Action.CLOSE_GOOGLE_PLAY])


def test_levelBattle1() -> None:
    processCheck('levelBattle1.png', [Action.LEVEL_START_BATTLE])


def test_nextLevel1() -> None:
    processCheck('nextLevel1.png', [Action.NEXT_LEVEL])


def test_defeatLevel1() -> None:
    processCheck('defeatLevel1.png', [Action.DEFEAT_NEXT_LEVEL])


def test_territoryScreen1() -> None:
    processCheck('territoryScreen1.png', [Action.HEADHUNT,
                                          Action.HONOR_HUNTING,
                                          Action.ARENA,
                                          Action.HEROTRIAL])


def test_territoryScreen2() -> None:
    processCheck('territoryScreen2.png', [Action.HEADHUNT,
                                          Action.HONOR_HUNTING,
                                          Action.ARENA,
                                          Action.HEROTRIAL])


def test_territoryScreen3() -> None:
    processCheck('territoryScreen3.png', [Action.HEADHUNT,
                                          Action.HONOR_HUNTING,
                                          Action.ARENA,
                                          Action.HEROTRIAL])


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


def test_revardCollect1() -> None:
    processCheck('revardCollect1.png', [Action.REVARD_COLLECT])


def test_adsScreen1() -> None:
    processCheck('adsScreen1.png', [Action.ADS_CLOSE1])


def test_adsScreen2() -> None:
    processCheck('adsScreen2.png', [Action.ADS_CLOSE1])


def test_honorIceDragonMenu1() -> None:
    processCheck('honorIceDragonMenu1.png', [Action.HONOR_CHALLENGE1])


def test_honorIceDragonFight1() -> None:
    processCheck('honorIceDragonFight1.png', [Action.FIGHT])


def test_honorIceDragonComplete1() -> None:
    processCheck('honorIceDragonComplete1.png',
                 [Action.HONOR_NEXT1,
                  Action.ARENA_VICTORY_NEXT,
                  Action.HEROTRIAL_VICTORY_NEXT])


def test_adsScreen3() -> None:
    processCheck('adsScreen3.png', [Action.ADS_CLOSE2])


def test_arenaMain1() -> None:
    processCheck('arenaMain1.png', [Action.ARENA_CHALLENGE])


def test_arenaSelect1() -> None:
    processCheck('arenaSelect1.png', [Action.ARENA_SELECT])


def test_arenaFight1() -> None:
    processCheck('arenaFight1.png', [Action.FIGHT])


def test_arenaVictory1() -> None:
    processCheck('arenaVictory1.png', [Action.ARENA_VICTORY_NEXT,
                                       Action.HONOR_NEXT1,
                                       Action.HEROTRIAL_VICTORY_NEXT])


def test_arenaDefeat1() -> None:
    processCheck('arenaDefeat1.png', [Action.ARENA_DEFEAT_NEXT,
                                      Action.HEROTRIAL_DEFEAT_NEXT])


def test_congrat1() -> None:
    processCheck('congrat1.png', [Action.CONGRAT_CLOSE])


def test_herotrialScreen1() -> None:
    processCheck('herotrialScreen1.png', [Action.HEROTRIAL_GO])


def test_herotrialMenu1() -> None:
    processCheck('herotrialMenu1.png', [Action.HEROTRIAL_CHALLENGE])


def test_herotrialSelect1() -> None:
    processCheck('herotrialSelect1.png', [Action.HEROTRIAL_SELECT])


def test_herotrialFight1() -> None:
    processCheck('herotrialFight1.png', [Action.HEROTRIAL_FIGHT])


def test_heroTrialVictory1() -> None:
    processCheck('heroTrialVictory1.png', [Action.HEROTRIAL_VICTORY_NEXT,
                                           Action.HONOR_NEXT1,
                                           Action.ARENA_VICTORY_NEXT])


def test_heroTrialDefeat1() -> None:
    processCheck('heroTrialDefeat1.png', [Action.HEROTRIAL_DEFEAT_NEXT,
                                          Action.ARENA_DEFEAT_NEXT])


def test_playerScreen1() -> None:
    processCheck('playerScreen1.png', [Action.PLAYERSCREEN_CLOSE])
