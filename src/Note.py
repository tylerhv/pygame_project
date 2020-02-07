import pygame
class Note(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, color):
        """
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height]).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 9

    def move(self):
        """
        Moves the notes.
        self.rect.y (int) Takes the position of the note and adds it to self.speed
        return: self.rect.y (int) The new position of self.rect.y is returned
        """
        self.rect.y += self.speed


        

