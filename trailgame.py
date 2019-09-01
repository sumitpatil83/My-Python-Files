#You can also draw objects to the screen using coordinates, which we will cover later.
#Here, we've created some award-winning graphics that we definitely want in our game,
#so we want to know how to get it to show up.

import pygame

pygame.init()

display_width = 900
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(' This Is Title ')

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
car_width = 73

#clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar2.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
            elif event.key == pygame.K_RIGHT:
                x_change = 2
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change
    
    gameDisplay.fill(white)
    car(x,y)
    
    if x > display_width - car_width or x < 0:
            gameExit = True
            
    pygame.display.update()
  #  clock.tick(60)

pygame.quit()
quit()
