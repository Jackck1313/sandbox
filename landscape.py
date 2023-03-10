import pygame, random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables


cloud_x = 200
cloud_y = 120
cloud_count = 0

plane_x = 200
plane_y = 200

sun_x = 600

moon_x = 700


sky_R = 38
sky_G = 193
sky_B = 224




# ---------------------------

clouds = []
cloud_colour = (240,240,240)
cloud_size = 30
cloud_count = 7

#Function for cloud movement based on:
#https://petlja.github.io/TxtProgInPythonEng/03_PyGame/03_PyGame_25_Animation_Multiple.html


for i in range(cloud_count):
    cloud_x = random.randint(cloud_size, WIDTH)
    cloud_y = random.randint(-200, HEIGHT)
    cloud_dx,cloud_dy = 0, 0
    while cloud_dx == 0 and cloud_dy == 0:
        cloud_dx += random.randint(6, 10)    
        cloud_dy += 2
    clouds.append((cloud_x,cloud_y,cloud_dx,cloud_dy,cloud_size,cloud_colour))

def draw_cloud():
    global clouds
    for i in range(cloud_count):
        cloud_x, cloud_y, cloud_dx, cloud_dy, cloud_size, cloud_colour = clouds[i]
        
        (cloud_x, cloud_y) = (cloud_x - cloud_dx, cloud_y + cloud_dy)
        if cloud_x + cloud_size < -100 and sun_x >= 0:
            cloud_x = random.randint(WIDTH + 100, WIDTH + 200)
        if cloud_y + cloud_size > HEIGHT + 100 and sun_x >= 0:
            if cloud_x > 0:
                cloud_x = WIDTH + 100
            cloud_y = random.randint(-150,300)

        clouds[i] = (cloud_x, cloud_y, cloud_dx, cloud_dy, cloud_size, cloud_colour)
        
    for cloud_x, cloud_y, cloud_dx, cloud_dy, cloud_size, cloud_colour in clouds:
        pygame.draw.circle(screen, cloud_colour, (cloud_x, cloud_y), cloud_size)
        pygame.draw.circle(screen, cloud_colour, (cloud_x + 35 , cloud_y -15), cloud_size)
        pygame.draw.circle(screen, cloud_colour, (cloud_x + 80, cloud_y -8), cloud_size)
        pygame.draw.circle(screen, cloud_colour, (cloud_x + 70, cloud_y + 30), cloud_size)
        pygame.draw.circle(screen, cloud_colour, (cloud_x + 25, cloud_y + 30), cloud_size)
        
stars = []

for i in range(20):
    star_x = random.randint(0,WIDTH)
    star_y = random.randint(0,HEIGHT)
    star_size = random.randint(1,4)
    stars.append((star_x,star_y,star_size))
def draw_stars():
    global stars
    star_growth = 0
    if moon_x < WIDTH:
        star_growth = random.randint(0,2)
    for star_x, star_y, star_size in stars:
        pygame.draw.circle(screen,(255,255,255), (star_x, star_y), star_size + star_growth)

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING

    screenfill_sky = (sky_R, sky_G, sky_B)
    screen.fill((screenfill_sky))  # always the first drawing command
    
    
    def day():
        global sun_x, moon_x, plane_x
        pygame.draw.circle(screen, (235, 199, 0), (sun_x,0), 90)
        sun_x -= 2
        if plane_x < 200:
            plane_x += 2
        if sun_x <= -100:
            moon_x = 700
            
            


    
    def night():
        global moon_x, sun_x, plane_x
        draw_stars()
        pygame.draw.circle(screen, (153, 148, 142), (moon_x,0), 60)
        moon_x -= 2
        plane_x += 2
        if plane_x >= WIDTH + 50:
            plane_x = -300
        if moon_x <= -100:
            sun_x = 700

    
    if sun_x <= -100:
        night()
        if sky_G > 35:
            sky_G -= 6
        if sky_B > 35:
            sky_B -= 6
    else:
        day()
        if sky_G < 193:
            sky_G += 6
        if sky_B < 224:
            sky_B += 6
            
    draw_cloud()

    window_colour = (9, 136, 186)
    plane_colour = (188, 196, 191)
    wing_colour =(114, 117, 115)



    pygame.draw.polygon(screen, plane_colour, [(plane_x + 107, plane_y + 98), (plane_x + 25, plane_y + 99), (plane_x - 30, plane_y - 5), (plane_x + 5, plane_y - 33)])
    pygame.draw.ellipse(screen, plane_colour, (plane_x,plane_y, 280,100))

    pygame.draw.ellipse(screen, window_colour, (plane_x + 190 ,plane_y + 20, 80, 30))
    pygame.draw.ellipse(screen, window_colour, (plane_x + 150, plane_y + 25, 20, 20))
    pygame.draw.ellipse(screen, window_colour, (plane_x + 110, plane_y + 25, 20, 20))
    pygame.draw.ellipse(screen, window_colour, (plane_x + 70, plane_y + 25, 20, 20))
    pygame.draw.ellipse(screen, window_colour, (plane_x + 30, plane_y + 25, 20, 20))

    pygame.draw.polygon(screen, wing_colour, [(plane_x + 183, plane_y + 65), (plane_x + 119, plane_y + 72), (plane_x + 119, plane_y + 154)])  
    pygame.draw.polygon(screen, wing_colour, [(plane_x + 120, plane_y + 1), (plane_x + 120, plane_y - 41), (plane_x + 159, plane_y + 2)])


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
