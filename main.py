import pygame
import time
import random
pygame.init()
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption("My Snake Game")
red = ((255,0,0))
green = ((0,255,0))
white = (255, 255, 255)
yellow = ((255,255,0))
black = ((0,0,0))
snake_block = 10
snake_speed = 30
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False
    x = dis_width/2
    y = dis_height/2
    temp_x = 0
    temp_y = 0
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    temp_x = -20
                    temp_y = 0
                elif event.key == pygame.K_RIGHT:
                    temp_x = 20
                    temp_y = 0
                elif event.key == pygame.K_UP:
                    temp_x = 0
                    temp_y = -20
                elif event.key == pygame.K_DOWN:
                    temp_x = 0
                    temp_y = 20
            if x >= dis_width or x < 0 or y >= dis_height or y < 0:
                game_close = True
            x+=temp_x
            y+=temp_y
            dis.fill(black)
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(dis,green,[x,y,snake_block,snake_block])
            pygame.display.update()
            # print(x,y,foodx,foody)
            if x == foodx and y == foody:
                print("Yummy!!")
            clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()