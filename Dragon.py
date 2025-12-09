import pygame
from pygame.locals import *
import math
import random
from collision import Collidable
from global_constants import *

class Dragon(Collidable):
    def __init__(self,my_color,m):
        super().__init__(((WINDOW_WIDTH-(m*4))/3),((WINDOW_HEIGHT-(2*m))/2),m*4,m*2,my_color)
        self.m = m
        self.velocity = -2
        self.flaps = []
        self.flap_avg = 0
        self.time = 0
        self.size_scale = 3
        self.flap_frq = 3.98*(self.m**(-0.27))

    def flap(self, click=False):

        if len(self.flaps) >= 30:
            del self.flaps[0]
        if click:
            self.flaps.append(1)
        else:
            self.flaps.append(0)
        yeah = 0
        for flap in self.flaps:
            yeah += flap
        yeah /= len(self.flaps)
        self.flap_avg = yeah*60

    def change_velocity(self):
        self.velocity = -5 + (self.flap_avg/self.flap_frq)


    def use_stamina(self):
        pass

    def draw_self(self,screen_canvas,frame):
        screen_canvas.blit(pygame.transform.scale(pygame.image.load('Dragon-Frames/Dragon-'+ str(frame+1) +'.png'),(self.w,self.h)),(self.x,self.y))


    def collision(self, called_hitboxes):
        x_check_one = self.x < (called_hitboxes[0] + called_hitboxes[2])
        x_check_two = (self.x + self.w) > called_hitboxes[0]
        y_check_one = (self.y + self.h*(1/4)) < (called_hitboxes[1] + called_hitboxes[3])
        y_check_two = (self.y + self.h*(3/4)) > called_hitboxes[1]

        if (x_check_one and x_check_two and
                y_check_one and y_check_two):
            return True
        else:
            return False
