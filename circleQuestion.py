import pygame
import math

pygame.init()
# setting up variables
WIDTH, HEIGHT = 900, 900
pygame.display.set_caption("Orbit Visualization")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
distance = 100
orbit_color = (0, 0, 0)
white = (255,255,255)
black = (0, 0, 0)

center_pos_x = 450
center_pos_y = 450
orbit_current_pos_x = 450 + distance #x, y
orbit_current_pos_y = 0 #x, y
orbit_origin_pos_x = orbit_current_pos_x 
orbit_origin_pos_y = orbit_current_pos_y 
theta = math.radians(45)


# create and display objects on the screen
def draw_window(orbit_current_pos):
    pygame.draw.circle(WIN, white, [ center_pos_x, center_pos_y ] , 10)
    pygame.draw.circle(WIN, white, [orbit_current_pos_x, orbit_current_pos_y], 10)
    pygame.display.update()

#function to move the orbiting item around the stationary item
def moveY():
    global orbit_current_pos_x
    global orbit_current_pos_y
    global center_pos_x
    global center_pos_y
    global theta
    #sin == y & cos == x
    omega = 0.1 #Angular velocity
    x = center_pos_x + distance * math.cos(theta)
    y = center_pos_y - distance * math.sin(theta)
    theta += omega # New angle, we add angular velocity
    orbit_current_pos_x = x + distance * omega * math.cos(theta + math.pi / 2)
    orbit_current_pos_y = y - distance * omega * math.sin(theta + math.pi / 2)


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
