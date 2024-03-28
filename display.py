import sys
import pygame

pygame.init()

# setting clock
clock = pygame.time.Clock()

# create window
win_width = 1200
win_height = 800
gameWindow = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Just One")

# initialize constants
font = pygame.font.SysFont("comicsansns", 30)
small_font = pygame.font.SysFont("comicsansns", 14)
white = [255, 255, 255]

# load images
just_one_logo = pygame.image.load("justonelogo.png")



# function to create button
def make_button(picture, coords, surface):
    image = pygame.image.load(picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image, imagerect)
    return (image, imagerect)

# function to run intro screen
def intro_screen():
    # load image
    # create start button
    # create instructions button
    # while true loop
    while True:
        # white background
        gameWindow.fill("white")
        # game logo
        gameWindow.blit(just_one_logo, (600, 300))

    # create exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# game loop 
def main():
    running = True
    intro_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(15)

    
    pygame.display.quit()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()