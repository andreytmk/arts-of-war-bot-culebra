#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from botbase import ScenarioActions

from datetime import time


class Action:
    MAIN_BATTLE = 1
    CLOSE_GOOGLE_PLAY = 2
    LEVEL_START_BATTLE = 3
    NEXT_LEVEL = 4
    DEFEAT_NEXT_LEVEL = 5
    TERRITORY = 6
    HEADHUNT = 7
    TREASURE_EASY_ATTACK = 8
    TREASURE_HARD_ATTACK = 9
    INFINITY_ATTACK = 10
    FIGHT = 11
    HEADHUNT_NEXT = 12
    INFINITY_MENU_ATTACK = 13
    INFINITY_NEXT = 14
    RETRY_CONNECTION = 15


COMMON_ACTIONS = [
    Action.CLOSE_GOOGLE_PLAY,
    Action.RETRY_CONNECTION,
]

LEVELS_ACTIONS = [
    Action.MAIN_BATTLE,
    Action.LEVEL_START_BATTLE,
    Action.NEXT_LEVEL,
    Action.DEFEAT_NEXT_LEVEL,
]

HEADHUNT_ACTIONS = [
    Action.TERRITORY,
    Action.HEADHUNT,
    Action.TREASURE_EASY_ATTACK,
    Action.TREASURE_HARD_ATTACK,
    Action.FIGHT,
    Action.HEADHUNT_NEXT
]

# All time in UTC
SCENARIO_BASE = [
    # Headhunt
    ScenarioActions().setData(time(hour=00, minute=1, second=00),
                              time(hour=00, minute=15, second=00),
                              HEADHUNT_ACTIONS),

    # Levels
    ScenarioActions().setData(time(hour=00, minute=20, second=00),
                              time(hour=23, minute=00, second=00),
                              LEVELS_ACTIONS),
]
