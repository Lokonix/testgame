import pygame


background_color = (255,255,255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Recreate')

map = pygame.image.load("map_test.bmp")



def silnik():
    pygame.display.flip()

    screen.blit(map, (0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit game")
            Game = False

Game = True
while Game:
    silnik()
