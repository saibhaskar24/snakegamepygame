import pygame
import time
import random
pygame.init()
dis_width = 600
dis_height = 400
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
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop():
    game_over = False
    game_close = False
    x = dis_width/2
    y = dis_height/2
    snake_List = []
    Length_of_snake = 1
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
            x+=temp_x
            y+=temp_y
            dis.fill(black)
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
            # pygame.draw.rect(dis,green,[x,y,snake_block,snake_block])
            snake_Head = []
            snake_Head.append(x)
            snake_Head.append(y)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
            our_snake(snake_List)
            pygame.display.update()

            # print(x,y,foodx,foody)
            if x == foodx and y == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
            clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()