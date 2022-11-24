#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from botbase import Button
from scenario import Action

from PIL import Image

import os

BUTTONS320x480EN_PATH = 'buttons320x480en'

BUTTONS320x480EN = [
    Button().setData(89, 166, 13, 12,
                     'stashRevard.png',
                     Action.STASH_REWARD),

    Button().setData(127, 375, 68, 28,
                     'mainBattle.png',
                     Action.MAIN_BATTLE),

    Button().setData(39, 299, 136, 26,
                     'closeGooglePlay.png',
                     Action.CLOSE_GOOGLE_PLAY),

    Button().setData(111, 384, 52, 23,
                     'levelStartBattle.png',
                     Action.LEVEL_START_BATTLE),

    Button().setData(179, 342, 46, 22,
                     'nextLevel.png',
                     Action.NEXT_LEVEL),

    Button().setData(180, 345, 43, 22,
                     'defeatNextLevel.png',
                     Action.DEFEAT_NEXT_LEVEL),

    Button().setData(200, 452, 35, 17,
                     'territory.png',
                     Action.TERRITORY),

    Button().setData(228, 221, 27, 20,
                     'headhunt.png',
                     Action.HEADHUNT),

    Button().setData(219, 289, 40, 15,
                     'treasureEasyAttack.png',
                     Action.TREASURE_EASY_ATTACK),

    Button().setData(220, 417, 40, 14,
                     'treasureHardAttack.png',
                     Action.TREASURE_HARD_ATTACK),

    Button().setData(217, 162, 44, 20,
                     'infinityAttack.png',
                     Action.INFINITY_ATTACK),

    Button().setData(136, 385, 49, 23,
                     'fight.png',
                     Action.FIGHT),

    Button().setData(181, 295, 43, 24,
                     'headhuntNext.png',
                     Action.HEADHUNT_NEXT),

    Button().setData(160, 440, 22, 23,
                     'infinityMenuAttack.png',
                     Action.INFINITY_MENU_ATTACK),

    Button().setData(138, 295, 45, 25,
                     'infinityNext.png',
                     Action.INFINITY_NEXT),

    Button().setData(134, 294, 57, 21,
                     'retryConnection.png',
                     Action.RETRY_CONNECTION),

    Button().setData(118, 296, 82, 28,
                     'revardCollect.png',
                     Action.REVARD_COLLECT),

    Button().setData(251, 124, 14, 14,
                     'adsClose1.png',
                     Action.ADS_CLOSE1),

    Button().setData(73, 212, 8, 8,
                     'honorHunting.png',
                     Action.HONOR_HUNTING),

    Button().setData(170, 396, 74, 22,
                     'honorChallenge1.png',
                     Action.HONOR_CHALLENGE1),

    Button().setData(138, 342, 46, 22,
                     'honorNext1.png',
                     Action.HONOR_NEXT1),

    Button().setData(260, 85, 14, 14,
                     'adsClose2.png',
                     Action.ADS_CLOSE2),

    Button().setData(256, 467, 28, 11,
                     'arena.png',
                     Action.ARENA),

    Button().setData(121, 406, 76, 22,
                     'arenaChallenge.png',
                     Action.ARENA_CHALLENGE),

    Button().setData(207, 330, 52, 16,
                     'arenaSelect.png',
                     Action.ARENA_SELECT),

    Button().setData(136, 342, 50, 23,
                     'arenaVictoryNext.png',
                     Action.ARENA_VICTORY_NEXT),

    Button().setData(139, 345, 43, 22,
                     'arenaDefeatNext.png',
                     Action.ARENA_DEFEAT_NEXT),

    Button().setData(137, 363, 48, 21,
                     'congratClose.png',
                     Action.CONGRAT_CLOSE),
]


def LoadButtons():
    for button in BUTTONS320x480EN:
        button.img = Image.open(os.path.join(BUTTONS320x480EN_PATH,
                                             button.imgfile))
    return sorted(BUTTONS320x480EN, key=lambda x: x.action)
