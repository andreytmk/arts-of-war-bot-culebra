#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from botbase import ScenarioActions

from datetime import time


class Action:
    STASH_REWARD = 5
    MAIN_BATTLE = 10
    CLOSE_GOOGLE_PLAY = 20
    LEVEL_START_BATTLE = 30
    NEXT_LEVEL = 40
    DEFEAT_NEXT_LEVEL = 50
    TERRITORY = 60
    HEADHUNT = 70
    TREASURE_EASY_ATTACK = 80
    TREASURE_HARD_ATTACK = 90
    INFINITY_ATTACK = 100
    FIGHT = 110
    HEADHUNT_NEXT = 120
    INFINITY_MENU_ATTACK = 130
    INFINITY_NEXT = 140
    RETRY_CONNECTION = 150
    REVARD_COLLECT = 160
    ADS_CLOSE1 = 170
    HONOR_HUNTING = 180
    HONOR_CHALLENGE1 = 190
    HONOR_NEXT1 = 200


COMMON_ACTIONS = [
    Action.CLOSE_GOOGLE_PLAY,
    Action.RETRY_CONNECTION,
    Action.ADS_CLOSE1,
]

LEVELS_ACTIONS = [
    Action.STASH_REWARD,
    Action.MAIN_BATTLE,
    Action.LEVEL_START_BATTLE,
    Action.NEXT_LEVEL,
    Action.DEFEAT_NEXT_LEVEL,
    Action.REVARD_COLLECT,
]

HEADHUNT_ACTIONS = [
    Action.TERRITORY,
    Action.HEADHUNT,
    Action.TREASURE_EASY_ATTACK,
    Action.TREASURE_HARD_ATTACK,
    Action.FIGHT,
    Action.HEADHUNT_NEXT,
]

HONOR_ACTIONS = [
    Action.TERRITORY,
    Action.HONOR_HUNTING,
    Action.HONOR_CHALLENGE1,
    Action.FIGHT,
    Action.HONOR_NEXT1,
]

# All time in UTC
SCENARIO_BASE = [
    # Headhunt
    ScenarioActions().setData(time(hour=00, minute=1, second=00),
                              time(hour=00, minute=15, second=00),
                              HEADHUNT_ACTIONS),

    # Honor hunting
    ScenarioActions().setData(time(hour=00, minute=20, second=00),
                              time(hour=00, minute=40, second=00),
                              HONOR_ACTIONS),

    # Levels
    ScenarioActions().setData(time(hour=00, minute=45, second=00),
                              time(hour=20, minute=55, second=00),
                              LEVELS_ACTIONS),
]
