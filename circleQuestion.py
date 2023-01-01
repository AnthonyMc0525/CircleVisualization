import pygame
import math

pygame.init()
# setting up variables
WIDTH, HEIGHT = 900, 900
pygame.display.set_caption("Orbit Visualization")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 5
distance = 100
orbit_color = (0, 0, 0)
white = (255,255,255)
black = (0, 0, 0)

center_pos = [450, 450]

orbit_current_pos_x = 450 + distance #x, y
orbit_current_pos_y = 0 #x, y
speed = 10 #speed of the dot in orbit
orbit_origin_pos_x = orbit_current_pos_x 
orbit_origin_pos_y = orbit_current_pos_y 


# create and display objects on the screen
def draw_window(orbit_current_pos):
    pygame.draw.circle(WIN, white, center_pos , 10)
    pygame.draw.circle(WIN, white, [orbit_current_pos_x, orbit_current_pos_y], 10)
    pygame.display.update()

def degreesToRadians(degree):
    return degree * (math.pi/180)


#function to move the orbiting item around the stationary item
def moveY():
    global orbit_current_pos_x
    global orbit_current_pos_y
    #sin == y & cos == x
    tan = math.tan(orbit_current_pos_y/orbit_current_pos_x)
    theta = math.acos(degreesToRadians(tan))
    x = math.cos(theta + degreesToRadians(speed)) * distance
    y = math.sin(theta + degreesToRadians(speed)) * distance
    orbit_current_pos_x = x + orbit_current_pos_x
    orbit_current_pos_y = y + orbit_current_pos_y
    print("x: " + str(orbit_current_pos_x))
    print("y: " + str(orbit_current_pos_y))
    print("-------------------------------------")

# starting point and contains game loop
def main():
    clock = pygame.time.Clock()
    run = True
    # main game loop
    while run:
        WIN.fill(black)
        draw_window([ orbit_current_pos_x, orbit_current_pos_x  ])
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        moveY() 
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
