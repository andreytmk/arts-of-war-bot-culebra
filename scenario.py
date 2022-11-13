#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from botbase import ScenarioActions

from datetime import time

class Action:
    MAIN_BATTLE = 1

SCENARIO_BASE = [
    ScenarioActions().setData(time(hour=10, minute=00, second=00), time(hour=23, minute=00, second=00), [Action.MAIN_BATTLE])
]
