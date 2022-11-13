#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from botbase import Button
from scenario import Action

from PIL import Image

import os

BUTTONS320x480EN_PATH = 'buttons320x480en'

BUTTONS320x480EN = [
    Button().setData(127 ,375 ,68  ,28  ,'mainBattle.png'         ,Action.MAIN_BATTLE            )
]

def LoadButtons():
    for button in BUTTONS320x480EN:
        button.img = Image.open(os.path.join(BUTTONS320x480EN_PATH, button.imgfile));
    return BUTTONS320x480EN