import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Player(pygame.sprite.Sprite):  # This class represents the bar at the bottom that the player controls
    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):

        super().__init__()
        
        self.image = pygame.Surface([15, 15]) # Set height, width
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect() # Make our top-left corner the passed-in location.
        self.rect.y = y
        self.rect.x = x

    def change_speed(self, x, y):  # Change the speed of the player. Called with a keypress
        self.change_x += x
        self.change_y += y

    def move(self, walls):  # Find a new position for the player
        self.rect.x += self.change_x  # Move left or right

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right # Otherwise if we are moving left, do the opposite.

                
        self.rect.y += self.change_y # Move up/down

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
