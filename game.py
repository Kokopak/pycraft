#!/usr/bin/env python

import pygame

from pygame.locals import *
from block import Block

screen_mode = (640, 480)

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_mode)
        pygame.display.set_caption("PyCraft 2D")
        self.quit = False
        self.blo = Block()
        self.lis_blo = []

        self.font = pygame.font.Font(None, 17)

        self.blocks = [
                "cobble",
                "plank",
                "stone"]

        self.selec = "cobble" 
        self.font = pygame.font.Font(None, 19)
        self.text = self.font.render("Selection: %s" % self.selec, True, (0,0,0))

        self.back = pygame.image.load("img/grille.png").convert()


    def aff_li(self):
        print self.lis_blo

    def update(self):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            x = (pygame.mouse.get_pos()[0]/32) * 32
            y = (pygame.mouse.get_pos()[1]/32) * 32
            self.blo = Block(x,y,self.selec)
            self.lis_blo.append((self.blo.get_block_position(), self.blo.get_image()))

    def draw(self):
        self.screen.blit(self.back, (0,0))
        self.screen.blit(self.text, (0,1))
        for el in self.lis_blo:
            self.screen.blit(el[1], (el[0][0], el[0][1] ))
        pygame.display.flip()

    def mainLoop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit = True
                if event.type == MOUSEBUTTONDOWN and event.button == 4:
                    if self.blocks.index(self.selec) == len(self.blocks) - 1:
                        self.selec = self.blocks[0]
                    else:
                        self.selec = self.blocks[self.blocks.index(self.selec) + 1]
                if event.type == MOUSEBUTTONDOWN and event.button == 5:
                    if self.blocks.index(self.selec) == len(self.blocks) + 1:
                        self.selec = self.blocks[0]
                    else:
                        self.selec = self.blocks[self.blocks.index(self.selec) - 1]
                self.text = self.font.render("Selection: %s" % self.selec, True, (0,0,0))
            self.screen.blit(self.back, (0,0))
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.mainLoop()
