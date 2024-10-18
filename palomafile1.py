import pygame
import sys
pygame.init()
# Screen dimensions
width, height = 1500, 560
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Ball")
# load BMP image
image1_path = 'nukepy.bmp'
image1 = pygame.image.load(image1_path)
image1 = pygame.transform.scale(image1, (255, 255))
image_path = 'dovepy.bmp'
circle_image = pygame.image.load(image_path)
circle_image = pygame.transform.scale(circle_image, (60, 60))  # resize
#dove setting
circle_x, circle_y = 100, height // 2  # Start position
circle_vel = 3  # vel for downward fall
circle_horispeed = 3.412  # Speed of hori movement
count = 0
#color RGB
brown = (60, 30, 15)
cyan = (0, 200, 200)
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # auto move dove til it hits bottom
    if circle_y + circle_image.get_height() < height:
        circle_y += circle_vel  # Continue falling down
    # move dove hori
    if circle_x + circle_image.get_width() < width:
        circle_x += circle_horispeed
    else:
        #Reset position and increment count when it goes off the right edge
        circle_x = 0
        count += 1
    #button click settings
    mouse_buttons = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if mouse_buttons[0] and circle_y > 0:
        circle_y -= 8.7  # move left-mouse left click
    if keys[pygame.K_UP] and circle_y > 0:
        circle_y -= 8.7  # move-left-up click
    circle_rect = pygame.Rect(circle_x, circle_y, circle_image.get_width(), circle_image.get_height())
    nukepy_rect = pygame.Rect(0, height // 2, image1.get_width(), image1.get_height())
    # Check for collision
    if circle_rect.colliderect(nukepy_rect):
        is_moving = False  # Stop movement on collision

    # Update the screen
    screen.fill(brown)
    screen.blit(image1, (0, -30))
    screen.blit(image1, (200, 313))
    screen.blit(image1, (480, 10))
    screen.blit(image1, (700, 100))
    screen.blit(image1, (400, 360))
    screen.blit(image1, (1000, 30))
    screen.blit(image1, (800, 433))
    screen.blit(image1, (1220, 170))
    screen.blit(image1, (700, 100))
    screen.blit(image1, (400, 360))

    screen.blit(circle_image, (circle_x, int(circle_y)))

    # Display the count of how many times the circle has gone off the screen
    font = pygame.font.Font(pygame.font.match_font('Time New Roman 24 Bold'), 36)
    count_text = font.render(f'Count: {count}', True, cyan)
    screen.blit(count_text, (10, 10))
    pygame.display.flip()
    pygame.time.Clock().tick(80)
# Quit game
pygame.quit()
sys.exit()
