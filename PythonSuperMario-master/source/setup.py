__author__ = 'marble_xu'

import os,sys
import pygame as pg
from . import constants as c
from . import tools

def resource_path(path):
    """Return the correct path to a resource, works for dev or PyInstaller exe."""
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, path)


pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

GFX = tools.load_all_gfx(resource_path(os.path.join("resources","graphics")))
