import pygame
class Button():
    def __init__(self, width, height, image):
        """
        Initializes the state of the button.
        width: (int) width of the button
        height: (int) height of the button
        image: (str) name of image
        """
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
