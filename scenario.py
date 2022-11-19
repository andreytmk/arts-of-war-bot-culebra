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

COMMON_ACTIONS = [
    Action.CLOSE_GOOGLE_PLAY,
]

LEVELS_START_TIME = time(hour=21, minute=39, second=00)
LEVELS_END_TIME = time(hour=21, minute=42, second=00)

SCENARIO_BASE = [
    ScenarioActions().setData(LEVELS_START_TIME, LEVELS_END_TIME, [Action.MAIN_BATTLE]),
    ScenarioActions().setData(LEVELS_START_TIME, LEVELS_END_TIME, [Action.LEVEL_START_BATTLE]),
    ScenarioActions().setData(LEVELS_START_TIME, LEVELS_END_TIME, [Action.NEXT_LEVEL]),
    ScenarioActions().setData(LEVELS_START_TIME, LEVELS_END_TIME, [Action.DEFEAT_NEXT_LEVEL]),
]
