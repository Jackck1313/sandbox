import pygame, sys
import random, time
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT, K_w, K_a, K_s, K_d, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------


player_x = 300
player_y = 200
player_x_change = 0
player_y_change = 0
player_colour = (0,0,255)
player_size = 40
speed = 5
interval = 0
health = 3
heart = pygame.image.load('pixel-heart.png')
heart = pygame.transform.scale(heart,(40,40))
collision_count = 0

enemy_count = 10
enemy_size = 20
enemy_colour = (255,0,0)
enemy_speed = 80

score = 0
font = pygame.font.SysFont(None, 100)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def new_enemys():
    global enemys
    enemys = []
    for i in range(enemy_count):
        placement = random.randint(1,2)
        placement_segment = random.randint(1,2)
        if placement == 1:
            enemy_x = random.randint(-100, WIDTH + 100)
            if placement_segment == 1:
                enemy_y = random.randint(HEIGHT, HEIGHT + 100)
            if placement_segment == 2:
                enemy_y = random.randint(-100, 0)
        if placement == 2:
            enemy_y = random.randint(-100, HEIGHT + 100)
            if placement_segment == 1:
                enemy_x = random.randint(WIDTH, WIDTH + 100)
            if placement_segment == 2:
                enemy_x = random.randint(-100, 0)
        
        
        enemy_dx,enemy_dy = 0, 0
        while enemy_dx == 0 and enemy_dy == 0:
            enemy_dx = ((enemy_x - player_x) / enemy_speed) * -1

            
            enemy_dy = ((enemy_y - player_y) / enemy_speed) * -1
            
        


        enemy_attributes = [enemy_x,enemy_y,enemy_dx,enemy_dy,enemy_size,enemy_colour]
        enemys.append(enemy_attributes)

def draw_enemy():
    global new_enemys, enemys, enemy_collision, health, collision_count, collision_time, player_colour, score, enemy_speed, healItem_x, healItem_y, healItem_colour, heal_check
    for i in range(enemy_count):
        enemy_x, enemy_y, enemy_dx, enemy_dy, enemy_size, enemy_colour = enemys[i]
        
        (enemy_x, enemy_y) = (enemy_x + enemy_dx, enemy_y + enemy_dy)
        enemys[i] = (enemy_x, enemy_y, enemy_dx, enemy_dy, enemy_size, enemy_colour)
        

    for enemy_x, enemy_y, enemy_dx, enemy_dy, enemy_size, enemy_colour in enemys:

        enemy_collision = pygame.Rect(enemy_x,enemy_y,enemy_size,enemy_size)

        if player_collision.colliderect(enemy_collision):
            enemy_colour = (255, 120, 185)
            if collision_count == 0:
                health -= 1
                player_colour = (235, 144, 40)
                
                collision_count += 1
                collision_time = pygame.time.get_ticks()

                
        
            
        pygame.draw.rect(screen, enemy_colour, enemy_collision)
       
   
    newWave_x = round((enemys[0])[0]) - round((enemys[4])[0])
    newWave_y = round((enemys[0])[1]) - round((enemys[4])[1])
    if newWave_x == 0 and newWave_y == 0:
        new_enemys()
        score += 1
        if enemy_speed>40:
            enemy_speed -= 2
        if heal_check == 1 and score % 7 == 0:
            healItem_x = random.randint(heal_item_size, WIDTH - heal_item_size)
            healItem_y = random.randint(heal_item_size, HEIGHT - heal_item_size)
            healItem_colour = (0,255,0)
            heal_check = 0
 
def draw_hearts():
    for health_point in range(health):
        screen.blit(heart,(health_point*35,1))

heal_item_size = 20
heal_check = 1
healItem_x = -100
healItem_y = -100
healItem_colour = (0,255,0)

def heal_item():
    global healItem_x, healItem_y, health, heal_check
    healItem_collision = pygame.Rect(healItem_x, healItem_y, heal_item_size, heal_item_size)
    pygame.draw.rect(screen, healItem_colour, healItem_collision)
    if player_collision.colliderect(healItem_collision) and heal_check == 0:
        health += 1
        heal_check += 1
        healItem_x = -100
        healItem_y = -100

boss_x = 300
boss_y = 700
boss_size = 100
boss_colour = (135, 3, 3)

def boss():
    global boss_x, boss_y, boss_speed_x, boss_speed_y, collision_time, boss_colour, collision_count, player_colour, health
    boss_collision = pygame.Rect(boss_x,boss_y,boss_size,boss_size)
    pygame.draw.rect(screen, boss_colour, boss_collision)
    boss_colour = (135, 3, 3)
    if boss_x == -100 or boss_x == 800 or boss_y == -100 or boss_y == 700:
        placement = random.randint(1,2)
        placement_segment = random.randint(1,2)
        if placement == 1:
            if placement_segment == 1:
                boss_x = player_x
                boss_y = -100
                boss_speed_y = 5
                boss_speed_x = 0
            if placement_segment == 2:
                boss_x = player_x
                boss_y = 700
                boss_speed_y = -5
                boss_speed_x = 0
            

        if placement == 2:
            if placement_segment == 1:
                boss_y = player_y
                boss_x = -100
                boss_speed_x = 5
                boss_speed_y = 0
            if placement_segment == 2:
                boss_y = player_y
                boss_x = 800
                boss_speed_x = -5
                boss_speed_y = 0
    boss_x += boss_speed_x
    boss_y += boss_speed_y
    if player_collision.colliderect(boss_collision):
        boss_colour = (255, 120, 185)
        if collision_count == 0:
            health -= 1
            player_colour = (235, 144, 40)
                
            collision_count += 1
            collision_time = pygame.time.get_ticks()

# ---------------------------

# ---------------------------
size = (700, 500)
menu_font = pygame.font.SysFont(None, 20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()
mainClock = pygame.time.Clock()
pygame.init()
screen.fill([230,230,250])


def main_menu():
    while True:

      mx, my = pygame.mouse.get_pos()
      button_1 = pygame.Rect(270, 200, 140, 50)


      screen.fill((255,255,255)) 
      pygame.draw.rect(screen, (255, 255, 255), button_1)
      pygame.draw.rect(screen, [255,255,255], button_1)
      pygame.draw.rect(screen, [50, 48, 45], button_1,7)
      draw_text('Start', menu_font, (0, 0, 0), 325,217)



      draw_text("Made By: Darrius, Evan, Jack, Jaden", menu_font, (0,0,0),10,10)

 
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
          if button_1.collidepoint((mx, my)):
            game()
            pygame.quit()

 
 
      pygame.display.flip()
      mainClock.tick(60)

#elif event.key == K_SPACE:
                #screen.fill((random.randint(1,255),random.randint(1,255),random.randint(1,255)))

def game():
    global player_x,player_y, player_colour,player_size, collision_count, player_collision, player_x_change, player_y_change, quit
    running = True
    w_pressed = 0
    s_pressed = 0
    a_pressed = 0
    d_pressed = 0
    quit = 0
    new_enemys()
    pygame.display.set_caption("Game")
    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == pygame.K_UP:
                    w_pressed = 1
                if event.key == K_s or event.key == pygame.K_DOWN:
                    s_pressed = 1
                if event.key == K_d or event.key == pygame.K_RIGHT:
                    d_pressed = 1
                if event.key == K_a or event.key == pygame.K_LEFT:
                    a_pressed = 1
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
                quit += 1
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    d_pressed = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    a_pressed = 0
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    w_pressed = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    s_pressed = 0
            if w_pressed == 1 and s_pressed == 1:
                player_y_change = 0
            elif w_pressed == 1 and s_pressed == 0:
                player_y_change = -speed
            elif w_pressed == 0 and s_pressed == 1:
                player_y_change = speed
            elif w_pressed == 0 and s_pressed == 0:
                player_y_change = 0
            if a_pressed == 1 and d_pressed == 1:
                player_x_change = 0
            elif a_pressed == 1 and d_pressed == 0:
                player_x_change = -speed
            elif a_pressed == 0 and d_pressed == 1:
                player_x_change = speed
            elif a_pressed == 0 and d_pressed == 0:
                player_x_change = 0
        
        screen.fill((255, 255, 255))  

        player_collision = pygame.Rect(player_x,player_y, player_size, player_size)
        
        
        draw_text(f"{score}", font, (0,0,0), 300, 10)
        pygame.draw.rect(screen, player_colour, player_collision)

        player_x += player_x_change
        player_y += player_y_change

        #SCREEN BORDER

        if player_x <= 0:
            player_x = 0
        if player_x >= WIDTH - player_size:
            player_x = WIDTH - player_size
        if player_y <= 0:
            player_y = 0
        if player_y >= HEIGHT - player_size:
            player_y = HEIGHT - player_size

        if collision_count == 1:
            if collision_time + 1000 <= pygame.time.get_ticks():  
                collision_count = 0
                player_colour = (0, 0,255)
        
        if health == 0:
            endscreen()

        draw_enemy()
        draw_hearts()

        if score >= 30:
            boss()
        heal_item()
        

        pygame.display.flip()
        clock.tick(30)
        #---------------------------
def endscreen():
  
  pygame.display.set_caption("Game Over")

  while True:
      draw_text('GAME OVER', font, (0, 0, 0), 140,215)

      

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(30)

main_menu()
pygame.quit()
