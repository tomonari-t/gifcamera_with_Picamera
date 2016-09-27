#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def makeGif():
    print('Generating...')
    cmdStr = "/usr/bin/convert -layers optimize -loop 0 -delay 30 ./photo/*.jpg ./html/gif/anime.gif"
    os.system(cmdStr)
    print('Done!!')