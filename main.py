import pygame
pygame.init()
dis = pygame.display.set_mode((700,500))
pygame.display.update()
pygame.display.set_caption("My Snake Game")
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        print(event)
pygame.quit()
quit()