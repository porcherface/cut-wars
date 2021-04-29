#!/usr/bin/env python3
''' 
| - visualize.py
'''
import time 
import pygame
import os
import random
from typing import Tuple

fps = 30
SIZE_X = 1080
SIZE_Y = 1080

size_x = SIZE_X
size_y = SIZE_Y

pygame.init()
clock = pygame.time.Clock()

#if your audio driver sucks 
# comment the call to this function
def music(musicpath):
    pygame.mixer.init()
    pygame.mixer.music.load(musicpath)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)

#chooses the artboard, one each second
def choose(millis):
    if millis < 0:
        return 0

    if(millis >= 9000):
        return 8

    return int(millis/1000) % 9

# defines the opacity envelope
# this is a quadratic envelope with period 1
def choose_alpha(millis):
    if millis < 0:
        return 0

    first = int(millis/1000)
    second = first + 1
    now = millis/1000

    alpha = 4 * 255 * (second - now) * (now - first)


        
    if (millis > 8500):
        alpha = 255

    return alpha

def alpha_star(millis, start):
    if (millis > start):
        alpha = (255 / 2) * ((millis - start )/1000)
        if alpha > 255:
            alpha = 255
        return alpha
    return 0


def shade_pro(image, mirrored, millis, depth = 100):

    surflist = []
    offset = int(millis/1000) # the rounded second
    param = millis - 1000 * offset # milliseconds since last second

    param = (param/1000 - 0.1)  * depth * 12/10 #goes from 0 to depth 

    for i in range(depth):
        if param > i :
            surflist.append(image.copy())
        else: 
            surflist.append(mirrored.copy())

    out = pygame.transform.average_surfaces(surflist)
    return out

def rescaling(in_val, size):
    return in_val
    #return pygame.transform.scale(in_val, size)

def set_scale(image, millis):

    scale_factor = 1* (millis - 8500) / 1000 #a number from 0 to 1?
    if scale_factor > 1:
        scale_factor = 1

    rect = image.get_rect()
    x = rect.width
    y = rect.height

    x = int(x*scale_factor)
    y = int(y*scale_factor)

    return pygame.transform.scale(image, (x,y))


if __name__ == "__main__":


    # screen preparation
    screen =  pygame.display.set_mode([size_x, size_y])

    images = []
    backgrounds = []
    mirrored = []
    boxes = []
    masks = []
    maskbox = []
    size_x = int(SIZE_X * 1/6)
    size_y = int(SIZE_Y * 1/6)
    logo = rescaling(pygame.image.load("images/logograndee.png").convert_alpha(), [size_x,size_y] ) 
    sm   = rescaling(pygame.image.load("images/SM.png").convert_alpha(), [64,64] ) 
    smbox = sm.get_rect()
    smbox.center = (1035,1035)
    # imagesize
    size_x = int(SIZE_X * 3/4)#1376
    size_y = int(SIZE_Y * 3/4)#768
    
    #bb8 shift x 540 y 437.02
    # load our assets, the more we have before runtime, the better it is
    images.append(rescaling(pygame.image.load("images/vader.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/BB8.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/C3P0.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/kyloren.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/R2.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/rebel_3.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/storm.png").convert_alpha(), [size_x,size_y] ) )
    images.append(rescaling(pygame.image.load("images/mandalorian.png").convert_alpha(), [size_x,size_y] ) )
        
    mirrored.append(rescaling(pygame.image.load("images/vader_2.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/BB8_2.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/C3P0_2.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/kyloren_2.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/R2_2.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/rebel_4.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/storm_2.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/mandalorian_2.png").convert_alpha(), [size_x,size_y] ) )

    #background size
    size_x = SIZE_X#1376
    size_y = int(SIZE_Y*3/4) #768

    images.append(rescaling(pygame.image.load("images/StarWars.png").convert_alpha(), [size_x,size_y] ) )
    mirrored.append(rescaling(pygame.image.load("images/StarWars.png").convert_alpha(), [size_x,size_y] ) )

    count = 0
    for img in images:
        boxes.append(img.get_rect())
        boxes[count].center = screen.get_rect().center
        count += 1

    boxes[1].center = (540, 437)
    size_y = SIZE_Y

    backgrounds.append(rescaling(pygame.image.load("images/sfondo_vader.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_bb8.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_c3p0.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_kyloren.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_r2.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_rebel.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_storm.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_mandalorian.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/sfondo_starwars.jpg").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/fuochi.png").convert_alpha(), [size_x,size_y] ) )
    backgrounds.append(rescaling(pygame.image.load("images/star.png").convert_alpha(), [size_x,size_y] ) )
    

    masks.append(rescaling(pygame.image.load("images/mask_vader.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_bb8.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_c3p0.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_kyloren.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_r2.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_rebel.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_storm.png").convert_alpha(), [size_x,size_y] ) )
    masks.append(rescaling(pygame.image.load("images/mask_mandalorian.png").convert_alpha(), [size_x,size_y] ) )

    count = 0

    center = screen.get_rect().center

    for img in images:
        maskbox.append(screen.get_rect())
        maskbox[count].center = center
        count +=1

    #small shift mando mask
    maskbox[7].center = (540, 536)

    logobox = logo.get_rect()
    logobox.center = center


    blackscreen = pygame.Surface([size_x, size_y]).convert()
    blackscreen.fill([0,0,0])
    backbox = blackscreen.get_rect()
    backbox.center = center

    #motoreiii
    duration = 12000 #millisecondi
    timer_go = True
    events = pygame.event.get()
    pygame.display.update()

    #input("Press Enter to continue...")
    press = False
    snapcount = 0
    snaps = []
    
    t0 = pygame.time.get_ticks() 
    t1 = t0-500 #+8000

    seconds = 0
    
    #music("audio/theme_cut.mp3")
#eeeee          AZZZZZZIONE!
    while timer_go==True and False==press:

        seconds+=1

        if seconds % 10 == 0:
            print("tick")

        # we measure time
        t1 = t1 + (1000./30)
        #t1 =pygame.time.get_ticks() - 500   
        timer_go = ((t1-t0) < (duration-500))

        # all our effects (choose, choose alpha and shade)
        # are time based. they are hardcoded with a time period
        #of 1000 milliseconds, we will work on that later
        
        this_alpha = choose_alpha((t1-t0))
        idx = choose((t1-t0))

        #in the first 8000 ms we switch between idx
        thisbackground = backgrounds[idx].copy()
        if((t1-t0) < 8000):
            #this_image = images[idx]#
            this_image = shade_pro(images[idx], mirrored[idx], (t1-t0))
        else:
            this_image = images[idx]

        imagebox = boxes[idx]

        #if(t1-t0)>8000:
        #    backgrounds[idx + 1].set_alpha(alpha_star(t1-t0, 8500))
        #    thisbackground.blit(backgrounds[idx+1],backbox) 

        if(t1-t0)>8500:    
            backgrounds[idx + 2].set_alpha(alpha_star(t1-t0, 9000))
            thisbackground.blit(backgrounds[idx+2],backbox) 

        thisbackground.blit(this_image, imagebox)
        if((t1-t0) < 8000):
            thisbackground.blit(masks[idx], maskbox[idx] )
    
        thisbackground.set_alpha(this_alpha,0)


        if (t1-t0) > 9000:
            scaled = set_scale(logo, (t1-t0))
            scaledbox = scaled.get_rect()
            scaledbox.center = center
            thisbackground.blit(scaled, scaledbox )

        #couple of blits (first the blackscreen, then the composite image)
        screen.blit(blackscreen, backbox)
        screen.blit(thisbackground, backbox)
        screen.blit(sm,smbox)
        # one is display, the other is ram-save:
        #pygame.display.update()
        # you can comment one of these two for better view/save
        # performances
        snaps.append(screen.copy())
        
        # the spacebar acts like a stop button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    press = True

        #clock.tick(fps)

    for idx, snap in enumerate(snaps):
        print("saving frame ",idx)
        pygame.image.save_extended(snap, "snaps/snap"+'{:03d}'.format(idx)+".png")

    print("Captured {} snapshots, for frame rate of {} fps".format(len(snaps), len(snaps)*1000/duration ) )

