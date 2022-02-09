import pygame, random, sys

screen = pygame.display.set_mode([1280, 720])
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
pygame.display.set_caption("Witness the Starfall")
clock = pygame.time.Clock()

# Lists that will house the stars
slowStars = []
mediumStars = []
fastStars = []

# For loops creating stars
for slow_stars in range(50):
    starLocX = random.randrange(0, width)
    starLocY = random.randrange(0, height)
    slowStars.append([starLocX, starLocY])

for med_stars in range(25):
    starLocX = random.randrange(0, width)
    starLocY = random.randrange(0, height)
    mediumStars.append([starLocX, starLocY])

for fast_stars in range(5):
    starLocX = random.randrange(0, width)
    starLocY = random.randrange(0, height)
    fastStars.append([starLocX, starLocY])
# Colors
Black = (0, 0, 0,)
DGrey = (128, 128, 128)
LGrey = (192, 192, 192)
White = (255, 255, 255)

pygame.init()

# Engine of all
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Show is Over")
            pygame.quit()
            sys.exit()
    screen.fill(Black)

    for star in slowStars:
        star[1] += 3
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, DGrey, star, 3)
    for star in mediumStars:
        star[1] += 6
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, LGrey, star, 2)
    for star in fastStars:
        star[1] += 9
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, White, star, 1)

    pygame.display.flip()
    clock.tick(30)