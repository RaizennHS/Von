import pygame

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
        self.up_states = {0: (40,338,33,55), 1:(40,398,33,55)}
        self.down_states = {0:(222,4,32,40)}
        self.posicion2 = ''

        self.onGround = False
        self.xvel = 0
        self.yvel = 0

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

    def update(self, posicion):

        if posicion == 'left':
            self.clip(self.left_states)
            self.xvel = -5
            self.posicion2 = posicion
        if posicion == 'right':
            self.clip(self.right_states)
            self.xvel = 5
            self.posicion2 = posicion
        if posicion == 'up':
            if self.posicion2 == 'left' or self.posicion2 == 'stand_left':
                self.clip(self.up_states[0])
                if self.onGround:
                    self.yvel -= 7
            elif self.posicion2 == 'right' or self.posicion2 == 'stand_right':
                self.clip(self.up_states[1])
                if self.onGround:
                    self.yvel -= 7
        if posicion == 'down':
            pass
        if posicion == 'corre':
            if self.posicion2 == 'left':
                self.clip(self.left_states)
                self.xvel = -7
            elif self.posicion2 == 'right':
                self.clip(self.right_states)
                self.xvel = 7

        if not self.onGround:
            self.yvel += 0.3

        if self.yvel > 100:
            self.yvel = 100

        if posicion == 'stand_left':
            self.clip(self.left_states[0])
            self.posicion2 = posicion
            self.xvel = 0

        if posicion == 'stand_right':
            self.clip(self.right_states[0])
            self.posicion2 = posicion
            self.xvel = 0

        if self.rect.left < 0:
            self.xvel += 5
        if self.rect.right > 800:
            self.xvel -= 5
        if self.rect.bottom >= 458:
            self.yvel = 0
            self.onGround = True

        self.rect.left += self.xvel

        self.rect.top += self.yvel

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):

        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_z:
                self.update('corre')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.arriba = False
            if event.key == pygame.K_DOWN:
                self.abajo = False
            if event.key == pygame.K_z:
                self.runnig = False


"""Aca van las clases de los enemigos"""



class Mudai(pygame.sprite.Sprite):

        def __init__(self, posicion):
            self.sheet = pygame.image.load('images/sprites/Mudai.png')
            self.sheet.set_clip(pygame.Rect(0, 0, 35, 42))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.rect.topleft = posicion
            self.frame = 0
            self.left_states = {0: (0, 173, 35, 34), 1: (0, 86, 35, 42), 2: (36, 86, 40, 41), 3: (77, 86, 37, 40)}
            self.right_states = {0: (108, 171, 35, 36), 1: (115, 86, 35, 42), 2: (151, 86, 40, 41), 3: (192, 86, 37, 40)}
            self.velocidad = [5, 0]

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

        def update(self):

            if self.rect.left < 0 or self.rect.right > 800:
                self.velocidad[0] = -self.velocidad[0]

            if self.velocidad[0] > 0:
                self.clip(self.right_states)
            elif self.velocidad[0] < 0:
                self.clip(self.left_states)
            self.rect.move_ip((self.velocidad[0], self.velocidad[1]))
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        def colision(self, objetivo):
            if self.rect.colliderect(objetivo.rect):
                #return True
                self.velocidad[0] = -self.velocidad[0]

        def eliminar(self, estado):
            if estado:
                self.rect = None



class Assassin(pygame.sprite.Sprite):

    def __init__(self, posicion):

        self.sheet = pygame.image.load('images/sprites/Assassin.png')

        self.sheet.set_clip(pygame.Rect(185, 0, 44, 52))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.frame = 0
        self.left_states ={0: (9, 126, 44, 61), 1: (54, 126, 44, 63), 2: (99, 126, 44, 62)}
        self.right_states = {0: (144, 126, 44, 61), 1: (189, 126, 44, 63), 2: (234, 126, 44, 62)}
        self.velocidad = [5, 0]

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

    def update(self):

        if self.velocidad[0] == 5:
            self.clip(self.right_states)
        elif self.velocidad[0] == -5:
            self.clip(self.left_states)

        if self.rect.left < 593 or self.rect.right > 800:
            self.velocidad[0] = -self.velocidad[0]

        self.rect.move_ip((self.velocidad[0], self.velocidad[1]))
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def colisiones(self, objetivos):

        if self.rect.colliderect(objetivos[0].rect):
            self.velocidad[0] = -self.velocidad[0]