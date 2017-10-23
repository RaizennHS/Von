import pygame, informacion, jugador, otros, enemigos


pygame.init()

size = informacion.SIZE
screen = pygame.display.set_mode(size)
pygame.display.set_caption("VON")
clock = pygame.time.Clock()
player = jugador.player((10, 458))
mudai = enemigos.Mudai((412,242))
fantasma = enemigos.Assassin((652,458))


sprites = [player, mudai, fantasma]

player = sprites[0]
mudai = sprites[1]
fantasma = sprites[2]

fondo = otros.cargar_imagen("images/mapas/e1.png")

game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    """player.handle_event(event)
    mudai.update()
    mudai.colision(player)
    #screen.fill(pygame.Color('blue'))
    screen.blit(fondo, (0, 0))
    screen.blit(player.image, player.rect)
    screen.blit(mudai.image, mudai.rect)"""

    player.handle_event(event)
    #mudai.update()
    #mudai.colision(player)

    screen.fill(pygame.Color('blue'))
    #screen.blit(fondo, (0, 0))

    #if len(sprites) == 2:
    try:

        mudai.update()
        fantasma.update()
        if mudai.colision(player) == True:
            mudai.eliminar(True)
            sprites.remove(mudai)
            print("eliminado mudai")
            print("=" * 50)

        if fantasma.colisiones(player) == True:
            fantasma.eliminarr(True)
            sprites.remove(fantasma)
            print("eliminado assassin")
            print("=" * 50)

        screen.blit(mudai.image, mudai.rect)
        screen.blit(fantasma.image, fantasma.rect)
    except:
        "algo"

    screen.blit(player.image, player.rect)


    pygame.display.flip()
    clock.tick(10)

pygame.quit()