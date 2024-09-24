import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,1,0)
    kuk_img = pg.image.load("fig/3.png")
    kuk_img = pg.transform.flip(kuk_img,1,0)
    kuk_rct = kuk_img.get_rect()
    kuk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2,[x+1600,0])
        screen.blit(bg_img, [x+3200, 0])
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kuk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kuk_rct.move_ip((0, 1))
        if key_lst[pg.K_RIGHT]:
            kuk_rct.move_ip((1, 0))
        if key_lst[pg.K_LEFT]:
            kuk_rct.move_ip((-1, 0))
        screen.blit(kuk_img,kuk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()