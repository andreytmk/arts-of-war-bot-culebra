#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import time, timedelta

from botbase import ScenarioActions


def test_ScenarioActions():
    entry = ScenarioActions()
    startTime = time(hour=1)
    endTime = time(hour=3)
    entry.setData(startTime, endTime, [])
    assert not entry.IsActionTime(time(hour=0))
    assert entry.IsActionTime(time(hour=1))
    assert entry.IsActionTime(time(hour=2))
    assert entry.IsActionTime(time(hour=3))
    assert not entry.IsActionTime(time(hour=4))


def test_ScenarioActionsShift1():
    entry = ScenarioActions()
    ScenarioActions.TIME_SHIFT = timedelta(hours=1)
    startTime = time(hour=1)
    endTime = time(hour=3)
    entry.setData(startTime, endTime, [])
    assert not entry.IsActionTime(time(hour=0))
    assert not entry.IsActionTime(time(hour=1))
    assert entry.IsActionTime(time(hour=2))
    assert entry.IsActionTime(time(hour=3))
    assert entry.IsActionTime(time(hour=4))


def test_ScenarioActionsShift2():
    entry = ScenarioActions()
    ScenarioActions.TIME_SHIFT = timedelta(hours=-1)
    startTime = time(hour=1)
    endTime = time(hour=3)
    entry.setData(startTime, endTime, [])
    assert entry.IsActionTime(time(hour=0))
    assert entry.IsActionTime(time(hour=1))
    assert entry.IsActionTime(time(hour=2))
    assert not entry.IsActionTime(time(hour=3))
    assert not entry.IsActionTime(time(hour=4))
