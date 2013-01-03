#!/usr/bin/env python

import pygame
import ast

from pygame.locals import *
from block import Block

screen_mode = (640, 480)
flags = DOUBLEBUF | HWSURFACE

timer = pygame.time.Clock()
fps = 30

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_mode, flags)
        self.blo = Block()
        self.lis_blo = []

        self.font = pygame.font.Font(None, 17)

        self.blocks = [
                "cobblestone",
                "wooden_plank",
                "stone",
                "grass",
                "glass",
                "brick"]

        self.selec = "cobblestone" 
        pygame.display.set_caption("PyCraft 2D - Selection: %s" %(self.selec.capitalize()))

        self.back = pygame.image.load("img/grille.png").convert()
        self.lis_blo = list(set(self.lis_blo))

        self.ax = 0
        self.ay = 0

    def update(self) : 
        self.sx = (pygame.mouse.get_pos()[0]/32) * 32
        self.sy = (pygame.mouse.get_pos()[1]/32) * 32

    def draw(self):
        self.screen.blit(self.back, (0,0))
        self.te = "img/"+self.selec+".png"
        self.screen.blit(pygame.image.load(self.te), (self.sx, self.sy))
        for el in self.lis_blo:
            self.screen.blit(pygame.image.load(el[1]), (el[0][0], el[0][1]))
        pygame.display.flip()

    def aff_li(self):
        print self.lis_blo

    def mainLoop(self):
        timer.tick(fps)
        while True:
            event = pygame.event.wait()
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                break
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.ax = (pygame.mouse.get_pos()[0]/32) * 32
                self.ay = (pygame.mouse.get_pos()[1]/32) * 32
                self.blo = Block(self.ax,self.ay,self.selec)
                if ((self.ax, self.ay), self.blo.get_image(), self.selec) not in self.lis_blo :
                    self.lis_blo.append((self.blo.get_block_position(), self.blo.get_image(), self.selec))
                    for ind, el in enumerate(self.lis_blo) :
                        if (self.ax, self.ay) == el[0] :
                            self.lis_blo[self.lis_blo.index(el)] = (self.blo.get_block_position(), self.blo.get_image(), self.selec) 
                            self.lis_blo = list(set(self.lis_blo))
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                x = (pygame.mouse.get_pos()[0]/32) * 32
                y = (pygame.mouse.get_pos()[1]/32) * 32
                for el in self.lis_blo:
                    if el[0] == (x, y):
                        self.lis_blo.remove(el)
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.lis_blo = []
            elif event.type == KEYDOWN and event.key == K_s:
                print "===SAUVEGARDE==="
                desti = raw_input("Destination : ")
                with open(desti, "w") as f:
                    f.write(str(self.lis_blo))
            elif event.type == KEYDOWN and event.key == K_l:
                print "===LECTURE==="
                desti = raw_input("Destination : ")
                with open(desti, "r") as f:
                    for line in f:
                        f_list = ast.literal_eval(line)
                self.lis_blo = []
                self.lis_blo = f_list
            elif event.type == MOUSEBUTTONDOWN and event.button == 4:
                if self.blocks.index(self.selec) == len(self.blocks) - 1:
                    self.selec = self.blocks[0]
                else:
                    self.selec = self.blocks[self.blocks.index(self.selec) + 1]
            elif event.type == MOUSEBUTTONDOWN and event.button == 5:
                if self.blocks.index(self.selec) == len(self.blocks) + 1:
                    self.selec = self.blocks[0]
                else:
                    self.selec = self.blocks[self.blocks.index(self.selec) - 1]
            pygame.display.set_caption("PyCraft 2D - Selection: %s" %(self.selec.capitalize()))
            self.screen.blit(self.back, (0,0))
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.mainLoop()   
    game.aff_li()
