from turtle import Screen
from pygame.locals import *
import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

def main():
    clock = pg.time.Clock()

    # 練習1：スクリーンと背景画像
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rct = screen_sfc.get_rect()            # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rct = bgimg_sfc.get_rect()              # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    # 練習3：こうかとん
    kkimg_sfc = pg.image.load("fig/6.png")    # Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  # Surface
    kkimg_rct = kkimg_sfc.get_rect()          # Rect
    kkimg_rct.center = 900, 400

    #player2
    plimg_sfc = pg.image.load("fig/bomhei4.png")
    plimg_sfc = pg.transform.rotozoom(plimg_sfc, 0, 0.3)
    plimg_rct = plimg_sfc.get_rect()
    plimg_rct.center = 200,100

    # 練習5：爆弾
    #bmimg_sfc = pg.Surface((20, 20)) # Surface
    #bmimg_sfc.set_colorkey((0, 0, 0)) 
    #pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)

    bmimg_sfc = pg.image.load("fig/bomhei1.png")
    bmimg_sfc = pg.transform.scale(bmimg_sfc,(100,100))
    bmimg_rct = bmimg_sfc.get_rect() # Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1

    bmimg2_sfc = pg.image.load("fig/bomhei2.png")
    bmimg2_sfc = pg.transform.scale(bmimg2_sfc,(100,100))
    bmimg2_rct = bmimg2_sfc.get_rect() # Rect
    bmimg2_rct.centerx = random.randint(0, screen_rct.width)
    bmimg2_rct.centery = random.randint(0, screen_rct.height)

    vx2, vy2 = +1, +1
    #net
    pushed = False

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #プレイヤー2による罠設置機能
        key_states3 = pg.key.get_pressed()
        if key_states3[pg.K_r] == True:
            pushed = True

        # 練習4
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 2
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 2
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 2
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 2
        
        # 練習7
        if check_bound(kkimg_rct, screen_rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 2
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 2
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 2
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 2
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        key_states2 = pg.key.get_pressed() # 辞書
        if key_states2[pg.K_w]    == True: plimg_rct.centery -= 1
        if key_states2[pg.K_s]  == True: plimg_rct.centery += 1
        if key_states2[pg.K_a]  == True: plimg_rct.centerx -= 1
        if key_states2[pg.K_d] == True: plimg_rct.centerx += 1

        #プレイヤー2の変身
        if key_states2[pg.K_f] == True:
                plimg_sfc = pg.image.load("fig/bomhei3.png")
                plimg_sfc = pg.transform.rotozoom(plimg_sfc, 0, 0.7)
                chimg_rct = plimg_sfc.get_rect()
                #fchimg_rct.center = 400,400
                screen_sfc.blit(plimg_sfc, chimg_rct)
        # 練習7
        if check_bound(plimg_rct, screen_rct) != (1, 1): # 領域外だったら
            if key_states2[pg.K_w]    == True: plimg_rct.centery += 1
            if key_states2[pg.K_s]  == True: plimg_rct.centery -= 1
            if key_states2[pg.K_a]  == True: plimg_rct.centerx += 1
            if key_states2[pg.K_d] == True: plimg_rct.centerx -= 1


        screen_sfc.blit(plimg_sfc, plimg_rct)
        if pushed == True:
            itimg_sfc = pg.image.load("fig/net.png")
            itimg_sfc = pg.transform.rotozoom(itimg_sfc, 0, 0.5)
            itimg_rct = itimg_sfc.get_rect()
            itimg_rct.center = 400,400
            screen_sfc.blit(itimg_sfc, itimg_rct)

        # 練習6
        bmimg_rct.move_ip(vx, vy)
        bmimg2_rct.move_ip(vx2, vy2)
        # 練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        screen_sfc.blit(bmimg2_sfc, bmimg2_rct)
        # 練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        yoko2, tate2 = check_bound(bmimg2_rct, screen_rct)
        vx *= yoko
        vy *= tate
        vx2 *= yoko2
        vy2 *= tate2

        # 練習8
        if kkimg_rct.colliderect(bmimg_rct): return 
        elif kkimg_rct.colliderect(bmimg2_rct): return
        #_rct.collidedict(itimg_rct): 
         #   key_states = pg.key.get_pressed() # 辞書
          #  if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
           # if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
           # if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
           # if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1

            #screen_sfc.blit(kkimg_sfc, kkimg_rct)

        if plimg_rct.colliderect(kkimg_rct): return  

        


        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate ,yoko2, tate2 = +1, +1, +1 , +1# 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko2 = -1  # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate2 = -1 # 領域外
    return yoko, tate 

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()