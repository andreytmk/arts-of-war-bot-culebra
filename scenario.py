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
    ADS_CLOSE2 = 210
    ARENA = 220
    ARENA_CHALLENGE = 230
    ARENA_SELECT = 240
    ARENA_VICTORY_NEXT = 250
    ARENA_DEFEAT_NEXT = 260
    CONGRAT_CLOSE = 270
    HEROTRIAL = 280
    HEROTRIAL_GO = 290
    HEROTRIAL_CHALLENGE = 300
    HEROTRIAL_SELECT = 310
    HEROTRIAL_FIGHT = 320
    HEROTRIAL_VICTORY_NEXT = 330
    HEROTRIAL_DEFEAT_NEXT = 340
    PLAYERSCREEN_CLOSE = 350


COMMON_ACTIONS = [
    Action.CLOSE_GOOGLE_PLAY,
    Action.RETRY_CONNECTION,
    Action.ADS_CLOSE1,
    Action.ADS_CLOSE2,
    Action.CONGRAT_CLOSE,
    Action.PLAYERSCREEN_CLOSE,
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

ARENA_ACTIONS = [
    Action.ARENA,
    Action.ARENA_CHALLENGE,
    Action.ARENA_SELECT,
    Action.FIGHT,
    Action.ARENA_VICTORY_NEXT,
    Action.ARENA_DEFEAT_NEXT,
]

INFINIT_ACTIONS = [
    Action.TERRITORY,
    Action.HEADHUNT,
    Action.INFINITY_ATTACK,
    Action.FIGHT,
    Action.INFINITY_MENU_ATTACK,
    Action.INFINITY_NEXT,
]

HEROTRIAL_ACTIONS = [
    Action.TERRITORY,
    Action.HEROTRIAL,
    Action.HEROTRIAL_GO,
    Action.HEROTRIAL_CHALLENGE,
    Action.HEROTRIAL_SELECT,
    Action.HEROTRIAL_FIGHT,
    Action.HEROTRIAL_VICTORY_NEXT,
    Action.HEROTRIAL_DEFEAT_NEXT,
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

    # Arena
    ScenarioActions().setData(time(hour=00, minute=42, second=00),
                              time(hour=1, minute=00, second=00),
                              ARENA_ACTIONS),

    # Infinit war
    ScenarioActions().setData(time(hour=1, minute=3, second=00),
                              time(hour=1, minute=23, second=00),
                              INFINIT_ACTIONS),

    # Hero Trial
    ScenarioActions().setData(time(hour=1, minute=25, second=00),
                              time(hour=1, minute=55, second=00),
                              HEROTRIAL_ACTIONS),

    # Levels
    ScenarioActions().setData(time(hour=2, minute=00, second=00),
                              time(hour=23, minute=55, second=00),
                              LEVELS_ACTIONS),
]
