import pygame
from pygame.locals import *

class player(pygame.sprite.Sprite):

    def __init__(self, posicion):

        self.sheet = pygame.image.load('images/sprites/takumi.png')

        self.sheet.set_clip(pygame.Rect(97, 4, 29, 55))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.frame = 0
        self.left_states ={0: (7,116,30,52), 1:(38,116,32,53), 2:(71,116,32,53), 3:(104,116,30,53), 4:(134,116,30,53)}
        self.right_states = {0: (7, 170, 30, 53), 1: (38, 170, 32, 53), 2: (71, 170, 32, 53), 3: (104, 170, 29, 53), 4: (134, 170, 30, 53), 4:(165,170,30,53)}
        self.up_states = {0: (40,338,33,55), 1:(74,338,33,55)}
        self.down_states = {0:(222,4,32,40)}
        self.posicion2 = ''

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def keys(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP] and player.jumping == False and player.jump_offset == 0:
            player.jumping = True

    def do_jumping(self):
        jump_height = self.jump_height

        if player.jumping:
            player.jump_offset += 1
            if player.jump_offset >= jump_height:
                player.jumping = False
        elif player.jump_offset > 0 and player.jumping == False:
            player.jump_offset -= 1

    def update(self, posicion):
        if posicion == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
            self.posicion2 = posicion
        if posicion == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
            self.posicion2 = posicion
        if posicion == 'up':
            if self.posicion2 == 'left' or self.posicion2 == 'stand_left':
                self.clip(self.up_states[0])
                self.rect.y -= 5
            elif self.posicion2 == 'right' or self.posicion2 == 'stand_right':
                self.clip(self.up_states[1])
                self.rect.y += 5



        if posicion == 'stand_left':
            self.clip(self.left_states[0])
            self.posicion2 = posicion
        if posicion == 'stand_right':
            self.clip(self.right_states[0])
            self.posicion2 = posicion

        if self.rect.left < 0:
            self.rect.x += 5
        if self.rect.right > 640:
            self.rect.x -= 5
        if self.rect.top < 0:
            self.rect.y += 5
        if self.rect.bottom > 480:
            self.rect.y -= 5

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')


