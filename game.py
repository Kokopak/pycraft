#!/usr/bin/env python
#-*-coding: utf-8 -*-

import pygame
import ast

from pygame.locals import *

VIDE = -1

class Game:

    def __init__(self, largeur, hauteur):
        pygame.init()
        self.size = 32
        self.largeur = largeur
        self.hauteur = hauteur
        self.fond = pygame.Color(23,147,205)
        self.screen = pygame.display.set_mode((largeur * self.size, hauteur * self.size), DOUBLEBUF | HWSURFACE)
        self.screen.fill(self.fond)
        self.blank = pygame.Surface((self.size, self.size))
        self.blank.fill(self.fond)
        pygame.display.update()

        tileset = pygame.image.load("img/terrain.png")
        self.typeBlocks = [("Tile %2d-%2d" % (x,y), pygame.transform.scale(tileset.subsurface(16*x, 16*y, 16, 16), (self.size, self.size))) for x in range(16) for y in range(16)]
        self.nselec = 0
        pygame.display.set_caption("PyCraft - Selection: %s" % (self.typeBlocks[self.nselec][0].capitalize()))
        self.blocks = {(x, y): VIDE for x in range(self.largeur) for y in range(self.hauteur)}

    def get_mouse(self):
        mx, my = pygame.mouse.get_pos()
        mx = mx / self.size
        my = my / self.size
        return mx, my

    def mainLoop(self):
        notQuit = True
        while notQuit:
            event = pygame.event.wait()
            if event.type == QUIT:
                print [s for s in self.blocks.iteritems() if s[1] != VIDE]
                print "Nombre total de blocks : %d" % (len([s for s in self.blocks.itervalues() if s != VIDE]))
                notQuit= False
            if pygame.mouse.get_pressed() in ((1,0,0), (0, 0, 1)):
                mx, my = self.get_mouse()
                self.screen.blit(self.blank, (mx*self.size, my*self.size))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    self.blocks[mx, my] = self.nselec
                    self.screen.blit(self.typeBlocks[self.nselec][1], (mx*self.size, my*self.size))
                else :
                    self.blocks[mx, my] = VIDE
                pygame.display.update()
            #Gestion de la molette
            elif event.type == MOUSEBUTTONDOWN and event.button == 4:
                self.nselec += 1
                if self.nselec == len(self.typeBlocks):
                    self.nselec = 0
                pygame.display.set_caption("PyCraft - Selection: %s" % (self.typeBlocks[self.nselec][0].capitalize()))
            elif event.type == MOUSEBUTTONDOWN and event.button == 5:
                self.nselec -= 1
                if self.nselec == -1:
                    self.nselec = len(self.typeBlocks) - 1
                pygame.display.set_caption("PyCraft - Selection: %s" % (self.typeBlocks[self.nselec][0].capitalize()))

if __name__ == '__main__':
    game = Game(30, 25)
    game.mainLoop()
