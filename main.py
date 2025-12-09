## THE DRAGON CODE
import random
import sys
from xml.dom.expatbuilder import theDOMImplementation

import pygame as pyg
from pygame import *

from collision import Collidable
from global_constants import *

from Dragon import Dragon
from Pillars import Pillars

def main():
    FPS = 60
    time = 0
    canvas = pyg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    canvas.fill(pyg.Color("grey"))

    # setup_game()
    clock = pyg.time.Clock()

    the_player = Dragon(pyg.Color("purple"),random.randint(25,75))
    pillars = []
    border = [Collidable(0,-25,WINDOW_WIDTH,25, pyg.Color("black")),
              Collidable(0,WINDOW_HEIGHT,WINDOW_WIDTH,25, pyg.Color("black"))]
    while True:
        time += 1
        clock.tick(FPS)
        handle_events(the_player,canvas,time, pillars, border)
        # active_main_loop()

def spawn_pillar(time, pillars,spawn_int):

    if time%spawn_int == 0:
        return pillars.append(pillar_hole())

def pillar_hole():
    hole_size = WINDOW_HEIGHT/3
    hole = random.randint(0,int(WINDOW_HEIGHT-hole_size))

    width= WINDOW_WIDTH/20

    return [Collidable(WINDOW_WIDTH,0,width, hole, pyg.Color("yellow")),
            Collidable(WINDOW_WIDTH, hole+hole_size, width, WINDOW_HEIGHT-(hole+hole_size), pyg.Color("yellow"))]


def handle_events(the_player,canvas,time, pillars, border):
    canvas.blit(pyg.transform.scale(pyg.image.load('background.png'), (WINDOW_WIDTH, WINDOW_HEIGHT)), (0, 0))
    events = pyg.event.get()
    keys_pr = pyg.key.get_pressed()
    pillar = 0
    while pillar < (len(pillars)):
        if pillars[pillar][0].x +pillars[pillar][0].w < 0:
            pillars.pop(pillar)
        else:
            for wall in range(len(pillars[pillar])):
                if the_player.collision(pillars[pillar][wall].call_hitbox()):
                    pyg.event.wait()
                    main()
                pillars[pillar][wall].move(-2)
                pillars[pillar][wall].draw_self(canvas,False, wall+1)
            pillar += 1
    for borders in border:
        if the_player.collision(borders.call_hitbox()):
            the_player.y = borders.y + the_player.h



    the_player.change_velocity()
    the_player.move(0,the_player.velocity)

    the_player.draw_self(canvas, (int(time/3))%6)

    spawn_pillar(time, pillars, 300)
    flapped = False

    for evt in events:
        if evt.type == QUIT:
            pyg.quit()
            sys.exit()
        if keys_pr[K_SPACE]:
            flapped = True
        if keys_pr[K_r]:
            main()


    the_player.flap(flapped)

    pyg.display.update()



pyg.init()

if __name__ == "__main__":
    main()