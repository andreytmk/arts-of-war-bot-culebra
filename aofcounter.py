#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from scenario import Action


class AofCounter:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger
        self.passedLevels = 0
        self.passedHeadhunt = 0
        self.passedHonor = 0
        self.passedArena = 0
        self.passedInfinity = 0

    def LogAction(self, action: Action) -> None:
        if action == Action.NEXT_LEVEL:
            self.passedLevels += 1
            self.logger.info(f'passed {self.passedLevels} levels')
        elif action == Action.HEADHUNT_NEXT:
            self.passedHeadhunt += 1
            self.logger.info(f'passed {self.passedHeadhunt} headhunts')
        elif action == Action.HONOR_NEXT1:
            self.passedHonor += 1
            self.logger.info(f'passed {self.passedHonor} honors')
        elif action == Action.ADS_CLOSE1:
            self.logger.info('ADS_CLOSE1 event')
        elif action == Action.ADS_CLOSE2:
            self.logger.info('ADS_CLOSE2 event')
        elif action == Action.REVARD_COLLECT:
            self.logger.info('REVARD_COLLECT event')
        elif (action == Action.ARENA_VICTORY_NEXT or
              action == Action.ARENA_DEFEAT_NEXT):
            self.passedArena += 1
            self.logger.info(f'passed {self.passedArena} arena')
        elif action == Action.INFINITY_NEXT:
            self.passedInfinity += 1
            self.logger.info(f'passed {self.passedInfinity} infinity')
