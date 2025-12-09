import pygame
from pygame.locals import *
import math
import random

class Collidable:
    def __init__(self,x,y,w,h,my_color):
        self.mc = my_color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def collision(self, called_hitboxes):
        x_check_one = self.x < (called_hitboxes[0] + called_hitboxes[2])
        x_check_two = (self.x + self.w) > called_hitboxes[0]
        y_check_one = self.y < (called_hitboxes[1] + called_hitboxes[3])
        y_check_two = (self.y + self.h) > called_hitboxes[1]

        if (x_check_one and x_check_two and
                y_check_one and y_check_two):
            return True
        else:
            return False

    def call_hitbox(self):
        return self.x,self.y,self.w,self.h

    def move(self,x_dir=0, y_dir=0):
        self.x += x_dir
        self.y -= y_dir

    def draw_self(self,screen_canvas,border=True, pillar=0):
        if pillar == 1:
            screen_canvas.blit(pygame.transform.scale(pygame.image.load("pillar_top.png"), (self.w, self.h)), (self.x, self.y))
        elif pillar == 2:
            screen_canvas.blit(pygame.transform.scale(pygame.image.load("pillar_bot.png"), (self.w, self.h)), (self.x, self.y))
        else:
            pygame.draw.rect(screen_canvas, self.mc,
                        (self.x,self.y,self.w,self.h),
                        0)
        if border:
            pygame.draw.rect(screen_canvas, pygame.Color("black"),
                            (self.x, self.y,self.w, self.h),
                            1)
