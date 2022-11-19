#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from botbase import Button
from scenario import Action

from PIL import Image

import os

BUTTONS320x480EN_PATH = 'buttons320x480en'

BUTTONS320x480EN = [
    Button().setData(127 ,375 ,68  ,28  ,'mainBattle.png'         ,Action.MAIN_BATTLE            ),
    Button().setData(39  ,299 ,136 ,26  ,'closeGooglePlay.png'    ,Action.CLOSE_GOOGLE_PLAY      ),
    Button().setData(111 ,384 ,52  ,23  ,'levelStartBattle.png'   ,Action.LEVEL_START_BATTLE     ),
    Button().setData(179 ,342 ,46  ,22  ,'nextLevel.png'          ,Action.NEXT_LEVEL             ),
    Button().setData(180 ,345 ,43  ,22  ,'defeatNextLevel.png'    ,Action.DEFEAT_NEXT_LEVEL      ),
]

def LoadButtons():
    for button in BUTTONS320x480EN:
        button.img = Image.open(os.path.join(BUTTONS320x480EN_PATH, button.imgfile));
    return BUTTONS320x480EN