#importing libraries
import pygame as pg, random as r, Consts as co

#initialises pygame
pg.init()

#create clock
clock = pg.time.Clock()

#creates the window and sets its size
win = pg.display.set_mode((co.screen_width, co.screen_height))
pg.display.set_caption("Aim Training")

#Load images
target_image = pg.image.load("assets/Target.png").convert_alpha()

#Target Class
class Target(pg.sprite.Sprite) :
    def __init__(self, x, y) :
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale((target_image), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

#create target group
target_group = pg.sprite.Group()

#changing variables
on_target = False
last_target_spawned = pg.time.get_ticks()
target_clicked = False

#gameplay loop
run = True
while run :

    clock.tick(co.FPS)

    target_group.update()

    #print(pg.time.get_ticks())

    win.fill((136, 47, 196))

    target_group.draw(win)

    #get mouse position
    pos = pg.mouse.get_pos()

    for target in target_group :
        if target.rect.collidepoint(pos) :
            on_target = True
        else : 
            on_target = False

    if pg.mouse.get_pressed()[0] and on_target :
          
        targets.kill()
        
        last_target_spawned = pg.time.get_ticks()

    if len(target_group) == 0 and pg.time.get_ticks() - last_target_spawned > co.target_spawn_delay :
        targets = Target(r.randint(0,400), r.randint(0,400))
        target_group.add(targets)

    if len(target_group) == 1 and pg.time.get_ticks() - last_target_spawned > co.target_despawn_time :
        targets.kill()
        last_target_spawned = pg.time.get_ticks()


    #event handler
    for event in pg.event.get() :    

        #if I hit the X
        if event.type == pg.QUIT: 
            run = False

    #update the display
    pg.display.flip()


pg.quit()
