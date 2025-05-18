import pygame, time, random

pygame.init()

# Set screen size
SCREEN_WIDTH = 1640
SCREEN_HEIGHT = 924
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and scale the background image to fit the screen
background = pygame.transform.scale(pygame.image.load('background-img.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption('Ball Bounce Simulation')

class ball:
    # Load and scale the ball image (50x50 px)
    ball_image = pygame.transform.scale(pygame.image.load('ball.png'), (50, 50))
    ball_width = ball_image.get_width()
    ball_height = ball_image.get_height()
    g = 1  # gravity

    def __init__(self):
        self.velocityX = random.choice([-4, 4])
        self.velocityY = random.choice([-4, 4])
        self.X = random.randint(0, SCREEN_WIDTH - ball.ball_width)
        self.Y = random.randint(0, SCREEN_HEIGHT // 2)

    def render_ball(self):
        screen.blit(ball.ball_image, (self.X, self.Y))

    def move_ball(self):
        # Apply gravity
        self.velocityY += ball.g

        # Update position
        self.X += self.velocityX
        self.Y += self.velocityY

        # Collision with side walls
        if self.X <= 0 or self.X >= SCREEN_WIDTH - ball.ball_width:
            self.velocityX *= -1
            self.X = max(0, min(self.X, SCREEN_WIDTH - ball.ball_width))

        # Collision with top
        if self.Y <= 0 and self.velocityY < 0:
            self.velocityY *= -1
            self.Y = 0

        # Collision with bottom
        if self.Y >= SCREEN_HEIGHT - ball.ball_height and self.velocityY > 0:
            self.velocityY *= -1
            self.Y = SCREEN_HEIGHT - ball.ball_height

# Create multiple balls
Ball_List = [ball() for _ in range(100)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.02)
    screen.blit(background, (0, 0))

    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()

    pygame.display.update()
