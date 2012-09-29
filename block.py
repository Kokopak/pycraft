#!/usr/bin/env python

import pygame
from pygame.locals import *

class Block:

    def __init__(self, x=0, y=0, nom=""):
        self.x, self.y = x, y
        self.nom = nom

    def get_block_position(self):
        return (self.x, self.y)
    
    def get_image(self):
        ig = "img/%s.png" % (self.nom)
        return ig

