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

        #Coordonées de la souris
        self.mx = 0
        self.my = 0

        #Dictionnaire sous la forme : {(x, y): image}
        self.blocks = {}


    def update_mouse_pos(self):
        self.mx, self.my = pygame.mouse.get_pos()
        self.mx = (self.mx / 32) * 32
        self.my = (self.my / 32) * 32

    def drawBlocks(self):
        #On dessine les images grâce à leurs coordonées
        self.screen.blit(pygame.image.load(self.blocks[self.mx, self.my]), (self.mx, self.my))
        pygame.display.flip()

    def removeBlock(self):
        #On supprime la clé
        del self.blocks[(self.mx, self.my)]
        #On crée un background de la taille d'une image et de la couleur du bacground de la fenêtre (noir)
        blank = pygame.Surface((32,32))
        blank.fill((0,0,0))
        self.screen.blit(blank, (self.mx, self.my))
        pygame.display.flip()

    def mainLoop(self):
        notQuit = True
        while notQuit:
            event = pygame.event.wait()
            if event.type == QUIT: 
                print "Nombre total de blocks : %d" % (len(self.blocks))
                notQuit= False
            if pygame.mouse.get_pressed() == (1,0,0):
                self.blocks[(self.mx, self.my)] = self.image
                self.drawBlocks()
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                #Si les coordonées sont dans self.blocks (un block est déja à cette place)
                if (self.mx, self.my) in self.blocks:
                    #On le dégage
                    self.removeBlock()
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

            self.update_mouse_pos()
            pygame.display.set_caption("PyCraft 2D - Selection: %s" %(self.selec.capitalize()))
            self.image = "img/%s.png" % (self.selec)

if __name__ == '__main__':
    game = Game()
    game.mainLoop()   
