import pygame

class Time():
    def __init__(self):
        """
        Initialize time.
        """
        self.clock = pygame.time.Clock()
        self.fps = 30

    def frames(self):
        """
        Sets the frame to 30fps
        arg: None
        return: (int) Milliseconds of game
        """
        self.clock.tick(self.fps)

            
    
