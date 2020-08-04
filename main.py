import pygame
import random
import os



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25


image_path = os.path.join('pong.png')
class Ball:
   def __init__(self):
       Ball.image = pygame.image.load("pong.png")
       self.image = Ball.image
       self.image = pygame.transform.scale(self.image,(250,200))
       """
    Class to keep track of a ball's location and vector.
    """
def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.hitbox = (self.x - 25,self.y - 25,55,55)

def draw(self, surface):
        surface.blit(self.image,(self.x,self.y))
        def __init__(self):
         pygame.sprite.Sprite.__init__(self)
 
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ball

    
    
    def collison():
        if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
            ball.change_y *= 1
        if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
 
class Paddle():
   def __init__(self):
       Paddle.image = pygame.image.load("rect.png")
       self.image = Paddle.image
       self.image = pygame.transform.scale(self.image,(250,200))
       self.y= 0
       self.hitbox = (self.x - 25,self.y - 25,55,55)
       def draw(self, surface):
            surface.blit(self.image,(self.x,self.y))
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
def makePaddle(self):
    paddle = Paddle()
    rect_width = 15
    rect_height = 100
    screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.fill = BLACK 
    pygame.draw.rect(screen,WHITE, rect_width, rect_height)
    def paddle_movment():
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.y += 1
            if key[pygame.K_UP]:
                self.y -= 1
                return paddle
class Wall():
    def __init__(self):
        def wall(width,height,x,y):
          screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
          pygame.draw.rect(screen, BLACK, 0,SCREEN_WIDTH)
          pygame.draw.rect(screen, BLACK, 0,SCREEN_HEIGHT)
          pygame.draw.rect(screen, BLACK, 250,SCREEN_WIDTH)


pygame.init()
pygame.display.set_caption("Pong")

running = True
while running:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit() # quit the screen
        running = False
        screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.fill((255,255,255))
        Ball.draw
        Paddle.draw
        Wall.draw

clock = pygame.time.Clock()
clock.tick(60)