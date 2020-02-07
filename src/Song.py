import pygame

class Song():

    def __init__(self):
        """
	Initializes the pygame mixer.
	args: none
        return: None
	"""
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()

    def startMusic(self, intro, state):
        """
        Sets up the music for the start screen.
        args: (str) the filename of the song played. The state of the game
        return: none
        """
        if pygame.mixer.music.get_busy != True:
            pygame.mixer.music.load(intro)
            pygame.mixer.music.set_volume(.6)
            pygame.mixer.music.play(-1)
            


    def gameMusic(self, song):
        """
        Plays the music for the game loop.
        args: (str) filename for the game loop song.
        return: none
        """
        pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(0)


    def endMusic(self, state, reaction):
        """
        Plays the music on the endscreen.
        args: (str) the state of the game and the file name of the ending sound.
        return: none
        """
        if state == "End":
            sound = pygame.mixer.Sound(reaction)
            sound.set_volume(.15)
            pygame.mixer.Sound.play(sound)


    def musicSelection (self, state, percent, mp31, mp32, mp33):
        """
        Uses the percentage score to decide which sound is played for the endscreen.
        args: state(str): The state of the game.
        args: mp31 (str): File name for the positive audience reaction.
        args: mp32 (str): File name for the negative audience reaction.
        args: mp33 (str): File name for the middling audience reaction.
        args: percent(float): the percentage of the maximum socre the user got.
        return: none
        """
        if percent >= 60:
            self.endMusic(state, mp31)

        elif percent <= 45:
            self.endMusic(state, mp32)

        else:
            self.endMusic(state, mp33)



    def stopMusic(self):
        """
        Stop the music
        args: none
        return: none
        """
        pygame.mixer.music.stop()

    
