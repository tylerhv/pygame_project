import pygame

class ScoreTracker():
    def __init__(self, group):
        """
	Initializes the score of the game as 0.
	args: group (str): The name of the Sprite Group.
	return: self.score (int): Intializes score as 0.
	return: self.num_notes (int): Number of sprites in the group.
	"""
        self.score = 0
        self.num_notes = len(group)

    def scoreUpdate(self):
        """
	Adds a point to the final score whenever the correct key input matches the note. Returns the final score.
	args: None
	return: self.score (int): The final score of the game.
	"""
        self.score += 1

    def scoreLoss(self):
        """
        Takes away half a point for an incorrect key input.
        args: none
        return: (float): The final score of the game
        """
        self.score -= .5

    def scorePrint(self, screen, state):
        """
        Takes the player score and prints it onto the screen as a percentage and as a fraction
        state: (str) State of the game
        return: (float) Return the final score in a fraction
        return: (float) Return the final score in a percentage
        """
        self.finalscore = self.score
        self.percent = self.finalscore / self.num_notes * 100
        self.font_choice = pygame.font.SysFont('courier', 45)
        self.scoreFont = self.font_choice.render(str(self.finalscore), 1, (0,0,0))
        self.percentFont = self.font_choice.render(str("{:.2f}".format(self.percent)) + "%", 1, (0, 0, 0))
        self.scorePosition = self.scoreFont.get_rect()
        self.scorePosition.x = 450
        self.scorePosition.y = 390
        self.percentPosition = self.percentFont.get_rect()
        self.percentPosition.x = 535
        self.percentPosition.y = 302
        screen.blit(self.scoreFont, self.scorePosition)
        screen.blit(self.percentFont, self.percentPosition)

        if state != "End":
             self.score = 0
