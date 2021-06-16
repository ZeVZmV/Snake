import pygame 
import random
import tkinter as tk

pygame.init()

white = (255,255,255) 
red = (255,0,0) 
green = (95, 183, 30)
brown = (61, 57, 50)


snake_head_down = pygame.image.load("snake_head.png") 
snake_head_up = pygame.image.load("snake_head_up.png") 
snake_head_left = pygame.image.load("snake_head_left.png") 
snake_head_right = pygame.image.load("snake_head_right.png") 

snake_head = snake_head_up 
 

def draw_snake(snake_list, size): 
    for i in snake_list: 
        root.blit(snake_head,(i[0],i[1]))

def message(msg, color):
    mesg = l_score.render(msg, True, color)
    root.blit(mesg, [root_x/2 - 200, root_y/2])

def message_start(msg, color):
    mesg = l_score.render(msg, True, color)
    root.blit(mesg, [root_x/2 - 30, root_y/2 - 15])

def message_meny(msg, color):
    mesg = l_score.render(msg, True, color)
    root.blit(mesg, [root_x - 150, 15])

def messge_score(score):
    value = l_score.render("Счёт:" + str(score), True, brown)
    root.blit(value, [10, 5])

def big_apple_score(score):
    score = str(score)
    value = l_score.render("Осталось:" +score[:3], True, brown)
    root.blit(value, [root_x/2 - 60,root_y - 40])


def Game():
    global snake_head
    big_apple_count = 6

    game_false = False
    
    size = 10 

    x=200 
    y=200 
    
    y_change = 0 
    x_change = 0 
    
    food_x = round(random.randrange(0, root_x - size) / 10.0) * 10.0 
    food_y = round(random.randrange(0, root_y - size) / 10.0) * 10.0 

    big_food_x = round(random.randrange(0, root_x - size*3) / 30.0) * 30.0 
    big_food_y = round(random.randrange(0, root_y - size*3) / 30.0) * 30.0 
    
    clock = pygame.time.Clock() 
    max_apple_point = 0
    snake_len = 1 
    snake_list = []
    count_apple = 0 
    
    while True:

        while game_false==True:
            root.fill(white)
            message("Вы проиграли! Нажмите R - что бы продолжить!", brown)
            messge_score(snake_len - 1)

            pygame.draw.rect(root, brown, [root_x - 165, 10, 155, 35])
            message_meny("Главное меню", white)

            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        Game()

                mouse_meny = pygame.mouse.get_pressed()

                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                if mouse_meny[0] and mouse_x >= root_x - 165 and mouse_x <= root_x - 10 and mouse_y>= 10 and mouse_y <= 45:
                    starts()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                exit() 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP: 
                    y_change =-10 
                    x_change = 0 
                    snake_head = snake_head_up 
                elif event.key == pygame.K_DOWN: 
                    y_change =10 
                    x_change = 0 
                    snake_head = snake_head_down 
                elif event.key == pygame.K_LEFT: 
                    x_change =-10 
                    y_change = 0 
                    snake_head = snake_head_left 
                elif event.key == pygame.K_RIGHT: 
                    x_change =10 
                    y_change = 0 
                    snake_head = snake_head_right 
    
        y+=y_change 
        x+=x_change  
    
        if x > root_x or x < 0 or y > root_y or y < 0: 
            game_false = True 
    
        root.fill(white) 
        pygame.draw.rect(root, green, [food_x, food_y, size, size])
        if count_apple >= 5 and big_apple_count >= 0:
            pygame.draw.rect(root, red, [big_food_x, big_food_y, size*3, size*3]) 
            big_apple_count -= 0.02
            big_apple_score(big_apple_count)
        snake_head_list = [] 
        snake_head_list.append(x) 
        snake_head_list.append(y) 
        snake_list.append(snake_head_list)


    
        if len(snake_list) > snake_len: 
            del snake_list[0] 
        
        for x_1 in snake_list[:-1]:
            if snake_head_list == x_1:
                game_false = True

        draw_snake(snake_list, size)
        messge_score(snake_len - 1) 
        pygame.display.update() 
    
        if x == food_x and y == food_y: 
            food_x = round(random.randrange(0, root_x - size) / 10.0) * 10.0 
            food_y = round(random.randrange(0, root_y - size) / 10.0) * 10.0 
            snake_len += 1
            count_apple +=1

        if count_apple >= 5:
            if x == big_food_x and y == big_food_y or x == big_food_x + size and y == big_food_y + size or x == big_food_x + size*2 and y == big_food_y + size*2:
                big_food_x = round(random.randrange(0, root_x - size*3) / 30.0) * 30.0 
                big_food_y = round(random.randrange(0, root_y - size*3) / 30.0) * 30.0
                count_apple = 0
                if big_apple_count >= 5:
                    snake_len *= 2
                if big_apple_count >= 4 and big_apple_count <5:
                    snake_len += 20
                if big_apple_count >= 3 and big_apple_count <4:
                    snake_len += 20
                if big_apple_count >= 2 and big_apple_count <3:
                    snake_len += 10 
                if big_apple_count >= 1 and big_apple_count <2:
                    snake_len += 5
                big_apple_count = 6
        if big_apple_count <= 0:
            big_food_x = round(random.randrange(0, root_x - size*3) / 30.0) * 30.0 
            big_food_y = round(random.randrange(0, root_y - size*3) / 30.0) * 30.0 
            big_apple_count = 6
            count_apple = 0
        clock.tick(snake_speed)

    pygame.quit 
    quit()


def start_window():
    global root_x
    global root_y
    global game_start
    global root
    global root1
    global snake_speed

    root_x = int(xe.get())
    root_y = int(ye.get())
    snake_speed = int(se.get())
    root1.destroy()

    root = pygame.display.set_mode((root_x,root_y))

    while game_start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()     

            mouse_pressed = pygame.mouse.get_pressed()

            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

            if mouse_pressed[0] and mouse_x >= root_x/2 - 50 and mouse_x <= root_x/2 + 50 and mouse_y>= root_y/2 - 25 and mouse_y <= root_y/2 + 25:
                Game()

        root.fill(white)
        pygame.draw.rect(root, brown, [root_x/2 - 50, root_y/2 - 25, 100, 50])
        message_start("Начать", white)
        pygame.display.update()

def starts():
    global xe
    global ye
    global root1
    global l_score
    global game_start
    global se
    game_start = True

    l_score = pygame.font.SysFont("Arial",22)

    root1=tk.Tk()
    root1.geometry("300x268")
    root1["bg"]="#EC3A3A"
    root1.title("Змейка")

    tk.Label(root1, text="Размер по ширине:").grid()
    xe=tk.Entry(root1, font=("Arial",15), width=15)
    xe.grid()
    tk.Label(root1, text="Размер по высоте:").grid()
    ye=tk.Entry(root1, font=("Arial",15), width=15)
    ye.grid()
    tk.Label(root1, text="Скорость:").grid()
    se=tk.Entry(root1, font=("Arial",15), width=15)
    se.grid()
    tk.Button(text="Начать игру",command=start_window, font=("Arial", 13), bg="#00FFB8").grid(stick="wens",padx=5,pady=5)


    root1.mainloop()

starts()