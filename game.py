#!/usr/bin/env python
#-*-coding: utf-8 -*-

import pygame
import ast

from pygame.locals import *

screen_mode = (640, 480)
flags = DOUBLEBUF | HWSURFACE

timer = pygame.time.Clock()

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_mode, flags)
        self.fond = pygame.Color(23,147,205)
        self.size = 32
        self.background = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.background.fill(self.fond)
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()

        self.nameBlocks = [
                "cobblestone",
                "wooden_plank",
                "stone",
                "grass",
                "glass",
                "brick"]

        self.selec = "cobblestone"
        self.image = "img/%s.png" % (self.selec)
        pygame.display.set_caption("PyCraft 2D - Selection: %s" %(self.selec.capitalize()))

        #Dictionnaire sous la forme : {(x, y): image}
        self.blocks = {}

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
                print "Nombre total de blocks : %d" % (len(self.blocks))
                notQuit= False
            if pygame.mouse.get_pressed() == (1,0,0):
                mx, my = self.get_mouse()
                self.blocks[mx, my] = self.image
                self.screen.blit(pygame.image.load(self.blocks[mx, my]), (mx*self.size, my*self.size))
                pygame.display.flip()
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                mx, my = self.get_mouse()
                #Si les coordonées sont dans self.blocks (un block est déja à cette place)
                if (mx, my) in self.blocks:
                    #On supprime la clé
                    del self.blocks[mx, my]
                    #On crée un background de la taille d'une image et de la couleur du bacground de la fenêtre (noir)
                    blank = pygame.Surface((self.size, self.size))
                    blank.fill(self.fond)
                    self.screen.blit(blank, (mx*self.size, my*self.size))
                    pygame.display.flip()
            #Gestion de la molette
            elif event.type == MOUSEBUTTONDOWN and event.button == 4:
                if self.nameBlocks.index(self.selec) == len(self.nameBlocks) - 1:
                    self.selec = self.nameBlocks[0]
                else:
                    self.selec = self.nameBlocks[self.nameBlocks.index(self.selec) + 1]
            elif event.type == MOUSEBUTTONDOWN and event.button == 5:
                if self.nameBlocks.index(self.selec) == len(self.nameBlocks) + 1:
                    self.selec = self.nameBlocks[0]
                else:
                    self.selec = self.nameBlocks[self.nameBlocks.index(self.selec) - 1]
            pygame.display.set_caption("PyCraft 2D - Selection: %s" %(self.selec.capitalize()))
            self.image = "img/%s.png" % (self.selec)

if __name__ == '__main__':
    game = Game()
    game.mainLoop()
