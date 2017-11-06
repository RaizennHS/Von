import pygame, informacion, jugador


pygame.init()

size = informacion.SIZE
screen = pygame.display.set_mode(size)
pygame.display.set_caption("VON")
clock = pygame.time.Clock()
player = jugador.player((10, 458))
mudai = jugador.Mudai((412,242))
fantasma = jugador.Assassin((652,458))


sprites = [player, mudai, fantasma]

player = sprites[0]
mudai = sprites[1]
fantasma = sprites[2]

#fondo = otros.cargar_imagen("images/mapas/e1.png")

game_over = False


while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)

    screen.fill(pygame.Color('blue'))
    #screen.blit(fondo, (0, 0))

    try:

        mudai.update()
        screen.blit(mudai.image, mudai.rect)

        """if mudai.colision(player):
            mudai.eliminar(True)
            sprites.remove(mudai)
            print("eliminado mudai")
            print("=" * 50)"""

        #screen.blit(mudai.image, mudai.rect)

    except:
        "algo"
    try:
        fantasma.update()
        screen.blit(fantasma.image, fantasma.rect)
        fantasma.colisiones(sprites)
    except:
        "algo"

    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(10)



pygame.quit()