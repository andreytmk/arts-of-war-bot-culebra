#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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

class TestSnapshot:
    def __init__(self):
        self.testsnap = None
        self.actions = []
        self.snap = None

    def setData(self, testsnap, actions):
        self.testsnap = testsnap
        self.actions = actions
        return self

class ScenarioActions:
    def __init__(self):
        self.fromTime = None
        self.toTime = None
        self.actions = None

    def setData(self, fromTime, toTime, actions):
        self.fromTime = fromTime
        self.toTime = toTime
        self.actions = actions
        return self
