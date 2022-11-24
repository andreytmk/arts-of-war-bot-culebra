#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from unittest.mock import create_autospec

from aofcounter import AofCounter
from scenario import Action


def test_AofCounter_LogAction():
    loggerMoc = create_autospec(logging.Logger)
    aofCounter = AofCounter(loggerMoc)

    aofCounter.LogAction(Action.NEXT_LEVEL)
    assert loggerMoc.info.call_count == 1

    aofCounter.LogAction(Action.HEADHUNT_NEXT)
    assert loggerMoc.info.call_count == 2

    aofCounter.LogAction(Action.HONOR_NEXT1)
    assert loggerMoc.info.call_count == 3
