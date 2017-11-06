import pygame
from pygame import *

ANCHO = 1024
ALTO = 640

DISPLAY = (ANCHO,ALTO)
DEPTH = 32
FLAGS = 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Von 0.0.0.0.0.0.00.0.00.0.0.00.0.0.0...01")
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#55d4dd"))
    entities = pygame.sprite.Group()
    player = Player(32, 64)
    platforms = []
    paused = False


    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P          PPPP               EP",
        "P                            PPP",
        "P                              P",
        "P                 PPPPPPP      P",
        "P    PPPP                      P",
        "PA                             P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)



            x += 32
        y += 32
        x = 0

    entities.add(player)


    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False

            if e.type == "q" and e.key == K_q:
                paused = not paused



        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))



        player.update(up, down, left, right, running, platforms)
        entities.draw(screen)
        if not paused:
            pygame.display.update()

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32,64))
        self.image.fill(Color("#ffffff"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 64)

    def update(self, up, down, left, right, running, platforms):
        if up:

            if self.onGround: self.yvel -= 7
        if down:
            pass
        if running:
            self.xvel = 8
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:

            self.yvel += 0.3

            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0

        self.rect.left += self.xvel

        self.collide(self.xvel, 0, platforms)

        self.rect.top += self.yvel

        self.onGround = False;

        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#fe8479"))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#7f5885"))

if __name__ == "__main__":
    main()
