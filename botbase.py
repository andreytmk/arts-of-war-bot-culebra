#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, time, timedelta, datetime


class Button:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.imgfile = None
        self.action = None
        self.img = None

    def setData(self, x, y, width, height, imgfile, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imgfile = imgfile
        self.action = action
        return self

    def __str__(self):
        s = ""
        s += "x: %d, " % self.x
        s += "y: %d, " % self.y
        s += "width: %d, " % self.width
        s += "height: %d, " % self.height
        s += "imgfile: %s, " % self.imgfile
        s += "action: %s, " % self.action
        return s


class ScenarioActions:
    TIME_SHIFT = timedelta(hours=0)

    def __init__(self):
        self.fromTime: time
        self.toTime: time
        self.actions: list[int]

    def setData(self, fromTime: time, toTime: time, actions: list[int]):
        fromTimeShifted = (datetime.combine(date.today(), fromTime) +
                           ScenarioActions.TIME_SHIFT)
        self.fromTime = fromTimeShifted.time()

        toTimeShifted = (datetime.combine(date.today(), toTime) +
                         ScenarioActions.TIME_SHIFT)
        self.toTime = toTimeShifted.time()

        self.actions = actions
        return self

    def IsActionTime(self, currentDT: time):
        return (self.fromTime <= currentDT and
                currentDT <= self.toTime)
