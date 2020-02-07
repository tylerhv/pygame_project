import pygame
from src import Note
from src import Song
from src import Button
from src import ScoreTracker
from src import Time

class Controller:
    def __init__(self, width = 1000, height = 700):
        #this flag is for buffering the drawing of the screen
        flags = pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode((width, height), flags)
        self.screen.set_alpha(None)
        self.width = width
        self.height = height
        self.TestButton = Button.Button(55,30,"assets/PianoStartButton.png")
             
        self.state = "Start"
        self.music = Song.Song()
        pygame.font.init()

        """
        Creates the Key location.
        args: (int) Location for the key. Color for the keys.
        return: None
        """
        self.KeyC = Note.Note((240,550),70,150,(255,255,255))
        self.KeyD = Note.Note((315,550),70,150,(255,255,255))
        self.KeyE = Note.Note((390,550),70,150,(255,255,255))
        self.KeyF = Note.Note((465,550),70,150,(255,255,255))
        self.KeyG = Note.Note((540,550),70,150,(255,255,255))
        self.KeyA = Note.Note((615,550),70,150,(255,255,255))
        self.KeyB = Note.Note((690,550),70,150,(255,255,255))

        """
        Create the notes for the game.
        args: (int) Location for the note for gameplay. Color for the notes
        return: None
        """
        self.note1 = Note.Note((240,-1750),70,150,(255,255,200))
        self.note2 = Note.Note((540,-1900),70,150,(255,255,200))
        self.note3 = Note.Note((315,-2050),70,150,(255,255,200))
        self.note4 = Note.Note((690,-2220),70,150,(255,255,200))
        self.note5 = Note.Note((240,-2350),70,150,(255,255,200))
        self.note6 = Note.Note((615,-2500),70,150,(255,255,200))
        self.note7 = Note.Note((240,-2650),70,150,(255,255,200))
        self.note8 = Note.Note((465,-2800),70,150,(255,255,200))
        self.note9 = Note.Note((240,-2950),70,150,(255,255,200))
        self.note10 = Note.Note((465,-3095),70,150,(255,255,200))
        self.note11 = Note.Note((390,-3240),70,150,(255,255,200))
        self.note12 = Note.Note((465,-3385),70,150,(255,255,200))
        self.note13 = Note.Note((240,-3530),70,150,(255,255,200))
        self.note14 = Note.Note((315,-3675),70,150,(255,255,200))
        self.note15 = Note.Note((615,-3820),70,150,(255,255,200))
        self.note16 = Note.Note((390,-3970),70,150,(255,255,200))
        self.note17 = Note.Note((540,-4120),70,150,(255,255,200))
        self.note18 = Note.Note((240,-4200),70,150,(255,255,200))
        self.note19 = Note.Note((690,-4430),70,150,(255,255,200))
        self.note20 = Note.Note((540,-4580),70,150,(255,255,200))
        self.note21 = Note.Note((390,-4200),70,150,(255,255,200))
        self.note22 = Note.Note((615,-4370),70,150,(255,255,200))
        self.note23 = Note.Note((240,-4505),70,150,(255,255,200))
        self.note24 = Note.Note((540,-4650),70,150,(255,255,200))
        self.note25 = Note.Note((315,-4795),70,150,(255,255,200))
        self.note26 = Note.Note((615,-4940),70,150,(255,255,200))
        self.note27 = Note.Note((390,-5085),70,150,(255,255,200))
        self.note28 = Note.Note((690,-5255),70,150,(255,255,200))
        self.note29 = Note.Note((315,-5425),70,150,(255,255,200))
        self.note30 = Note.Note((465,-5595),70,150,(255,255,200))
        self.note31 = Note.Note((240,-5765),70,150,(255,255,200))
        self.note32 = Note.Note((540,-5935),70,150,(255,255,200))
        self.note33 = Note.Note((390,-5955),70,150,(255,255,200))
        self.note34 = Note.Note((465,-6105),70,150,(255,255,200))
        self.note35 = Note.Note((540,-6275),70,150,(255,255,200))
        self.note36 = Note.Note((240,-6445),70,150,(255,255,200))
        self.note37 = Note.Note((690,-6615),70,150,(255,255,200))
        self.note38 = Note.Note((465,-6785),70,150,(255,255,200))
        self.note39 = Note.Note((540,-6955),70,150,(255,255,200))
        self.note40 = Note.Note((240,-7125),70,150,(255,255,200))
        self.note41 = Note.Note((240,-7400),70,150,(255,255,200))
        self.note42 = Note.Note((540,-7565),70,150,(255,255,200))
        self.note43 = Note.Note((465,-7730),70,150,(255,255,200))
        self.note44 = Note.Note((615,-7895),70,150,(255,255,200)) 
        self.note45 = Note.Note((240,-8060),70,150,(255,255,200))
        self.note46 = Note.Note((465,-8225),70,150,(255,255,200))
        self.note47 = Note.Note((540,-8395),70,150,(255,255,200))
        self.note48 = Note.Note((240,-8560),70,150,(255,255,200))
        self.note49 = Note.Note((690,-8725),70,150,(255,255,200))
        #next section of the song
        self.note50 = Note.Note((390,-8890),70,150,(255,255,200))
        self.note51 = Note.Note((240,-9045),70,150,(255,255,200))
        self.note52 = Note.Note((540,-9200),70,150,(255,255,200))
        self.note53 = Note.Note((615,-9355),70,150,(255,255,200))
        self.note54 = Note.Note((690,-9510),70,150,(255,255,200))
        self.note55 = Note.Note((240,-9665),70,150,(255,255,200))
        self.note56 = Note.Note((615,-9820),70,150,(255,255,200))
        self.note57 = Note.Note((240,-9975),70,150,(255,255,200))
        self.note58 = Note.Note((465,-10130),70,150,(255,255,200))
        self.note59 = Note.Note((240,-10285),70,150,(255,255,200))
        self.note60 = Note.Note((465,-10535),70,150,(255,255,200))
        self.note61 = Note.Note((240,-10700),70,150,(255,255,200))
        self.note62 = Note.Note((540,-10865),70,150,(255,255,200))
        self.note63 = Note.Note((615,-11030),70,150,(255,255,200))
        self.note64 = Note.Note((690,-11190),70,150,(255,255,200))
        self.note65 = Note.Note((240,-11330),70,150,(255,255,200))
        self.note66 = Note.Note((615,-11510),70,150,(255,255,200))
        self.note67 = Note.Note((240,-11670),70,150,(255,255,200))
        self.note68 = Note.Note((465,-11830),70,150,(255,255,200))
        #next section of the song
        self.note69 = Note.Note((240,-12000),70,150,(255,255,200))
        self.note70 = Note.Note((465,-12155),70,150,(255,255,200))
        self.note71 = Note.Note((240,-12325),70,150,(255,255,200))
        self.note72 = Note.Note((540,-12475),70,150,(255,255,200))
        self.note73 = Note.Note((615,-12635),70,150,(255,255,200))
        self.note74 = Note.Note((690,-12795),70,150,(255,255,200))
        self.note75 = Note.Note((240,-12955),70,150,(255,255,200))
        self.note76 = Note.Note((615,-13120),70,150,(255,255,200))
        self.note77 = Note.Note((240,-13280),70,150,(255,255,200))
        self.note78 = Note.Note((465,-13440),70,150,(255,255,200))
        self.note79 = Note.Note((240,-13600),70,150,(255,255,200))
        self.note80 = Note.Note((465,-13760),70,150,(255,255,200))
        self.note81 = Note.Note((240,-13920),70,150,(255,255,200))
        self.note82 = Note.Note((540,-14080),70,150,(255,255,200))
        self.note83 = Note.Note((315,-14240),70,150,(255,255,200))
        self.note84 = Note.Note((690,-14395),70,150,(255,255,200))
        self.note85 = Note.Note((240,-14550),70,150,(255,255,200))
        self.note86 = Note.Note((615,-14705),70,150,(255,255,200))
        self.note87 = Note.Note((240,-14860),70,150,(255,255,200))
        self.note88 = Note.Note((465,-15015),70,150,(255,255,200))
        self.note89 = Note.Note((240,-15170),70,150,(255,255,200))
        self.note90 = Note.Note((465,-15325),70,150,(255,255,200))
        self.note91 = Note.Note((240,-15480),70,150,(255,255,200))
        self.note92 = Note.Note((540,-15635),70,150,(255,255,200))
        self.note93 = Note.Note((315,-15790),70,150,(255,255,200))
        self.note94 = Note.Note((690,-15945),70,150,(255,255,200))
        #next section of song
        self.note95 = Note.Note((240,-16145),70,150,(255,255,200))
        self.note96 = Note.Note((615,-16320),70,150,(255,255,200))
        self.note97 = Note.Note((690,-16480),70,150,(255,255,200))
        self.note98 = Note.Note((615,-16740),70,150,(255,255,200))
        self.note99 = Note.Note((690,-16900),70,150,(255,255,200))
        self.note100 = Note.Note((615,-17055),70,150,(255,255,200))
        self.note101 = Note.Note((540,-17210),70,150,(255,255,200))
        self.note102 = Note.Note((465,-17365),70,150,(255,255,200))
        self.note103 = Note.Note((240,-17430),70,150,(255,255,200))
        self.note104 = Note.Note((465,-17585),70,150,(255,255,200))
        self.note105 = Note.Note((540,-17840),70,150,(255,255,200))
        self.note106 = Note.Note((465,-17995),70,150,(255,255,200))
        self.note107 = Note.Note((615,-18150),70,150,(255,255,200))
        self.note108 = Note.Note((540,-18305),70,150,(255,255,200))
        self.note109 = Note.Note((240,-18460),70,150,(255,255,200))
        self.note110 = Note.Note((615,-18615),70,150,(255,255,200))
        self.note111 = Note.Note((540,-18770),70,150,(255,255,200))
        self.note112 = Note.Note((465,-18925),70,150,(255,255,200))
        self.note113 = Note.Note((240,-19080),70,150,(255,255,200))
        self.note114 = Note.Note((465,-19235),70,150,(255,255,200))
        self.note115 = Note.Note((540,-19390),70,150,(255,255,200))
        self.note116 = Note.Note((465,-19545),70,150,(255,255,200))
        self.note117 = Note.Note((615,-19700),70,150,(255,255,200))
        self.note118 = Note.Note((540,-19855),70,150,(255,255,200))
        self.note119 = Note.Note((240,-20010),70,150,(255,255,200))
        self.note120 = Note.Note((615,-20330),70,150,(255,255,200))
        self.note121 = Note.Note((465,-20490),70,150,(255,255,200))
        self.note122 = Note.Note((540,-20660),70,150,(255,255,200))
        #next section of music
        self.note123 = Note.Note((240,-20730),70,150,(255,255,200))
        self.note124 = Note.Note((690,-20900),70,150,(255,255,200))
        self.note125 = Note.Note((240,-21070),70,150,(255,255,200))
        self.note126 = Note.Note((615,-21240),70,150,(255,255,200))
        self.note127 = Note.Note((240,-21410),70,150,(255,255,200))
        self.note128 = Note.Note((465,-21580),70,150,(255,255,200))
        self.note129 = Note.Note((240,-21750),70,150,(255,255,200))
        self.note130 = Note.Note((465,-21920),70,150,(255,255,200))
        self.note131 = Note.Note((240,-22090),70,150,(255,255,200))


        """
        Add the keys and notes to a sprite group.
        args: None
        return: None
        """
        
        #the sprite groups
        self.notes = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        
        #adding keys to self.keys
        self.keys.add(self.KeyC)
        self.keys.add(self.KeyD)
        self.keys.add(self.KeyE)
        self.keys.add(self.KeyF)
        self.keys.add(self.KeyG)
        self.keys.add(self.KeyA)
        self.keys.add(self.KeyB)
        
        #adding notes to self.notes
        self.notes.add(self.note1)
        self.notes.add(self.note2)
        self.notes.add(self.note3)
        self.notes.add(self.note4)
        self.notes.add(self.note5)
        self.notes.add(self.note6)
        self.notes.add(self.note7)
        self.notes.add(self.note8)
        self.notes.add(self.note9)
        self.notes.add(self.note10)
        self.notes.add(self.note11)
        self.notes.add(self.note12)
        self.notes.add(self.note13)
        self.notes.add(self.note14)
        self.notes.add(self.note15)
        self.notes.add(self.note16)
        self.notes.add(self.note17)
        self.notes.add(self.note18)
        self.notes.add(self.note19)
        self.notes.add(self.note20)
        self.notes.add(self.note21)
        self.notes.add(self.note22)
        self.notes.add(self.note23)
        self.notes.add(self.note24)
        self.notes.add(self.note25)
        self.notes.add(self.note26)
        self.notes.add(self.note27)
        self.notes.add(self.note28)
        self.notes.add(self.note29)
        self.notes.add(self.note30)
        self.notes.add(self.note31)
        self.notes.add(self.note32)
        self.notes.add(self.note33)
        self.notes.add(self.note34)
        self.notes.add(self.note35)
        self.notes.add(self.note36)
        self.notes.add(self.note37)
        self.notes.add(self.note38)
        self.notes.add(self.note39)
        self.notes.add(self.note40)
        self.notes.add(self.note41)
        self.notes.add(self.note42)
        self.notes.add(self.note43)
        self.notes.add(self.note44)
        self.notes.add(self.note45)
        self.notes.add(self.note46)
        self.notes.add(self.note47)
        self.notes.add(self.note48)
        self.notes.add(self.note49)
        self.notes.add(self.note50)
        self.notes.add(self.note51)
        self.notes.add(self.note52)
        self.notes.add(self.note53)
        self.notes.add(self.note54)
        self.notes.add(self.note55)
        self.notes.add(self.note56)
        self.notes.add(self.note57)
        self.notes.add(self.note58)
        self.notes.add(self.note59)
        self.notes.add(self.note60)
        self.notes.add(self.note61)
        self.notes.add(self.note62)
        self.notes.add(self.note63)
        self.notes.add(self.note64)
        self.notes.add(self.note65)
        self.notes.add(self.note66)
        self.notes.add(self.note67)
        self.notes.add(self.note68)
        self.notes.add(self.note69)
        self.notes.add(self.note70)
        self.notes.add(self.note71)
        self.notes.add(self.note72)
        self.notes.add(self.note73)
        self.notes.add(self.note74)
        self.notes.add(self.note75)
        self.notes.add(self.note76)
        self.notes.add(self.note77)
        self.notes.add(self.note78)
        self.notes.add(self.note79)
        self.notes.add(self.note80)
        self.notes.add(self.note81)
        self.notes.add(self.note82)
        self.notes.add(self.note83)
        self.notes.add(self.note84)
        self.notes.add(self.note85)
        self.notes.add(self.note86)
        self.notes.add(self.note87)
        self.notes.add(self.note88)
        self.notes.add(self.note89)
        self.notes.add(self.note90)
        self.notes.add(self.note91)
        self.notes.add(self.note92)
        self.notes.add(self.note93)
        self.notes.add(self.note94)
        self.notes.add(self.note95)
        self.notes.add(self.note96)
        self.notes.add(self.note97)
        self.notes.add(self.note98)
        self.notes.add(self.note99)
        self.notes.add(self.note100)
        self.notes.add(self.note101)
        self.notes.add(self.note102)
        self.notes.add(self.note103)
        self.notes.add(self.note104)
        self.notes.add(self.note105)
        self.notes.add(self.note106)
        self.notes.add(self.note107)
        self.notes.add(self.note108)
        self.notes.add(self.note109)
        self.notes.add(self.note110)
        self.notes.add(self.note111)
        self.notes.add(self.note112)
        self.notes.add(self.note113)
        self.notes.add(self.note114)
        self.notes.add(self.note115)
        self.notes.add(self.note116)
        self.notes.add(self.note117)
        self.notes.add(self.note118)
        self.notes.add(self.note119)
        self.notes.add(self.note120)
        self.notes.add(self.note121)
        self.notes.add(self.note122)
        self.notes.add(self.note123)
        self.notes.add(self.note124)
        self.notes.add(self.note125)
        self.notes.add(self.note126)
        self.notes.add(self.note127)
        self.notes.add(self.note128)
        self.notes.add(self.note129)
        self.notes.add(self.note130)
        self.notes.add(self.note131)
        
    def mainloop(self):
        """
        Main loop. Depending on the game state, the game will go through the function specified.
        args: None
        return: None
        """
        while True:
            if self.state == "Start":
                self.startloop()
            elif self.state == "Instruction":
                self.instructionloop()
            elif self.state == "Game":
                self.gameloop()
            elif self.state == "End":
                self.endloop()

    def startloop(self):
        """
        Start loop. Opens to the start screen. The intro music plays. The start button is in the bottom left corner.
        args: None
        return: Either quits the game or goes to the instruction screen
        """

        StartButton = Button.Button(75,52,"assets/PianoStartButton.png")
        QuitButton = Button.Button(75,52,"assets/PianoQuitButton.png")
        self.music.startMusic("assets/liszt.ogg", self.state)
        while self.state == "Start":
            self.background = pygame.image.load("assets/PianoStartScreen.png").convert_alpha()
            for event in pygame.event.get():
                #this event quits the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #this event goes to the instruction screen
                    if (95 >= pygame.mouse.get_pos()[0] >= 20
                    and 680 >= pygame.mouse.get_pos()[1] >= 628):
                        self.state = "Instruction"
                    if (980 >= pygame.mouse.get_pos()[0] >= 905
                    and 680 >= pygame.mouse.get_pos()[1] >= 628):
                        pygame.quit()
            self.screen.blit(self.background,(0,0))
            self.screen.blit(StartButton.image, (20,628))
            self.screen.blit(QuitButton.image, (905, 628))
            pygame.display.flip()

    def instructionloop(self):  
        """
        Instruction loop. Opens to the instruction screen. Music from start screen continues to play. Gives insturctions on how to play.
        args: None
        return: Starts the game or goes back
        """
        PerformButton = Button.Button(75,52,"assets/PianoPerformButton.png")
        BackButton = Button.Button(75,52, "assets/PianoBackButton.png")
        while self.state == "Instruction":
            self.background = pygame.image.load("assets/PianoInstructionScreen.png").convert_alpha()
            for event in pygame.event.get():
                #this event quits the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                #this event starts the game
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (175 >= pygame.mouse.get_pos()[0] >= 100
                    and 622 >= pygame.mouse.get_pos()[1] >= 570):
                        self.state = "Game"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (900 >= pygame.mouse.get_pos()[0] >= 825
                    and 622 >= pygame.mouse.get_pos()[1] >= 570):
                        self.state = "Start"
            #gives instruction on how to play
            self.screen.blit(self.background, (0,0))
            self.screen.blit(PerformButton.image, (100,570))
            self.screen.blit(BackButton.image, (825, 570))
            pygame.display.flip()


    def gameloop(self):
        """
        Game loop. Actual gameplay happens here. Intro music stops, game music begins.
        Notes start to fall from the top. By clicking the respective keys on the notes, the note will be destroyed and the player score will increase.
        args: None
        return: self.tracker (int) increase score
        return: Exits game
        """
        ExitButton = Button.Button(75,52,"assets/PianoExitButton.png")
        self.music.stopMusic()
        self.tracker = ScoreTracker.ScoreTracker(self.notes)

        #times the game. Once it reachers 87 seconds, the game automatically goes to the end screen
        CurrentTime = 0
        self.time = pygame.time.Clock()
        self.clock = Time.Time()
        SWITCH_STATE = pygame.USEREVENT + 1
        pygame.time.set_timer(SWITCH_STATE, 87000)

        
        self.music.gameMusic("assets/rachmaninoff.ogg")
        self.background = pygame.image.load("assets/PianoGameScreen.png").convert_alpha()

        while self.state == "Game":
            for event in pygame.event.get():
                #this event quits the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                #this event goes to the End screen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (95 >= pygame.mouse.get_pos()[0] >= 20
                    and 680 >= pygame.mouse.get_pos()[1] >= 628):
                        self.state = "End"
                if event.type == SWITCH_STATE:
                    self.state = "End"
                #these events destroys the notes
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if pygame.sprite.spritecollide(self.KeyC, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyC, self.notes, True):
                            self.notes.kill()

                    elif event.key == pygame.K_d:
                        if pygame.sprite.spritecollide(self.KeyD, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyD, self.notes, True):
                            self.notes.kill()

                    elif event.key == pygame.K_f:
                        if pygame.sprite.spritecollide(self.KeyE, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyE, self.notes, True):
                            self.notes.kill()
                            
                    elif event.key == pygame.K_j:
                        if pygame.sprite.spritecollide(self.KeyF, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyF, self.notes, True):
                            self.notes.kill()

                    elif event.key == pygame.K_k:
                        if pygame.sprite.spritecollide(self.KeyG, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyG, self.notes, True):
                            self.notes.kill()
 
                    elif event.key == pygame.K_l:
                        if pygame.sprite.spritecollide(self.KeyA, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyA, self.notes, True):
                            self.notes.kill()
                            self.tracker.scoreUpdate()
                            
                    elif event.key == pygame.K_SEMICOLON:
                        if pygame.sprite.spritecollide(self.KeyB, self.notes, True):
                            self.tracker.scoreUpdate()
                        else:
                            self.tracker.scoreLoss()
                        if pygame.sprite.spritecollide(self.KeyB, self.notes, True):
                            self.notes.kill()
                            
            #draws the key images
            self.screen.blit(self.background, (0,0))
            self.screen.blit(ExitButton.image, (20,628))
            self.keys.draw(self.screen)
            
            #makes all the notes in the sprite class move
            for i in self.notes:
                i.move()
    
            self.notes.draw(self.screen)
            pygame.display.update()
            self.clock.frames()
            


    def endloop(self):
        pygame.time.delay(5)
        """
        End loop. Brings player to the end screen. The player score is displayed here. No music should be playing
        args: None
        return:
        """
        RetryButton = Button.Button(75,51,"assets/PianoRetryButton.png")
        QuitButton = Button.Button(75,51,"assets/PianoQuitButton.png")
        MenuButton = Button.Button(75,51, "assets/PianoMenuButton.png")
        self.background = pygame.image.load("assets/PianoEndScreen.png").convert_alpha()
        self.tracker.scorePrint(self.background, self.state)
        self.music.stopMusic()
        self.reaction= Song.Song()
        self.reaction.musicSelection(self.state, self.tracker.percent, "assets/LongApplause.ogg", "assets/CrowdBoo.wav", "assets/FakeApplause.ogg")
        for event in pygame.event.get():
            #this event quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
            #this event goes back to the start screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if (375 >= pygame.mouse.get_pos()[0] >= 300
                    and 622 >= pygame.mouse.get_pos()[1] >= 570):
                    self.state = "Game"
                elif (537 >= pygame.mouse.get_pos()[0] >= 462
                    and 622 >= pygame.mouse.get_pos()[1] >= 570):
                    self.state = "Instruction"
                    self.music.startMusic("assets/liszt.ogg", self.state)
                elif (700 >= pygame.mouse.get_pos()[0] >= 625
                    and 622 >= pygame.mouse.get_pos()[1] >= 570):
                    pygame.quit()

        #this is just a copy from above. Recreates all the notes.
        self.screen.blit(self.background, (0,0))
        self.screen.blit(RetryButton.image, (300,570))
        self.screen.blit(QuitButton.image, (625,570))
        self.screen.blit(MenuButton.image, (462,570))


        """
        Creates the Key location.
        args: (int) Location for the key. Color for the keys.
        return: None
        """
        self.KeyC = Note.Note((240,550),70,150,(255,255,255))
        self.KeyD = Note.Note((315,550),70,150,(255,255,255))
        self.KeyE = Note.Note((390,550),70,150,(255,255,255))
        self.KeyF = Note.Note((465,550),70,150,(255,255,255))
        self.KeyG = Note.Note((540,550),70,150,(255,255,255))
        self.KeyA = Note.Note((615,550),70,150,(255,255,255))
        self.KeyB = Note.Note((690,550),70,150,(255,255,255))

        """
        Create the notes for the game.
        args: (int) Location for the note for gameplay. Color for the notes
        return: None
        """
        self.note1 = Note.Note((240,-1750),70,150,(255,255,200))
        self.note2 = Note.Note((540,-1900),70,150,(255,255,200))
        self.note3 = Note.Note((315,-2050),70,150,(255,255,200))
        self.note4 = Note.Note((690,-2220),70,150,(255,255,200))
        self.note5 = Note.Note((240,-2350),70,150,(255,255,200))
        self.note6 = Note.Note((615,-2500),70,150,(255,255,200))
        self.note7 = Note.Note((240,-2650),70,150,(255,255,200))
        self.note8 = Note.Note((465,-2800),70,150,(255,255,200))
        self.note9 = Note.Note((240,-2950),70,150,(255,255,200))
        self.note10 = Note.Note((465,-3095),70,150,(255,255,200))
        self.note11 = Note.Note((390,-3240),70,150,(255,255,200))
        self.note12 = Note.Note((465,-3385),70,150,(255,255,200))
        self.note13 = Note.Note((240,-3530),70,150,(255,255,200))
        self.note14 = Note.Note((315,-3675),70,150,(255,255,200))
        self.note15 = Note.Note((615,-3820),70,150,(255,255,200))
        self.note16 = Note.Note((390,-3970),70,150,(255,255,200))
        self.note17 = Note.Note((540,-4120),70,150,(255,255,200))
        self.note18 = Note.Note((240,-4200),70,150,(255,255,200))
        self.note19 = Note.Note((690,-4430),70,150,(255,255,200))
        self.note20 = Note.Note((540,-4580),70,150,(255,255,200))
        self.note21 = Note.Note((390,-4200),70,150,(255,255,200))
        self.note22 = Note.Note((615,-4370),70,150,(255,255,200))
        self.note23 = Note.Note((240,-4505),70,150,(255,255,200))
        self.note24 = Note.Note((540,-4650),70,150,(255,255,200))
        self.note25 = Note.Note((315,-4795),70,150,(255,255,200))
        self.note26 = Note.Note((615,-4940),70,150,(255,255,200))
        self.note27 = Note.Note((390,-5085),70,150,(255,255,200))
        self.note28 = Note.Note((690,-5255),70,150,(255,255,200))
        self.note29 = Note.Note((315,-5425),70,150,(255,255,200))
        self.note30 = Note.Note((465,-5595),70,150,(255,255,200))
        self.note31 = Note.Note((240,-5765),70,150,(255,255,200))
        self.note32 = Note.Note((540,-5935),70,150,(255,255,200))
        self.note33 = Note.Note((390,-5955),70,150,(255,255,200))
        self.note34 = Note.Note((465,-6105),70,150,(255,255,200))
        self.note35 = Note.Note((540,-6275),70,150,(255,255,200))
        self.note36 = Note.Note((240,-6445),70,150,(255,255,200))
        self.note37 = Note.Note((690,-6615),70,150,(255,255,200))
        self.note38 = Note.Note((465,-6785),70,150,(255,255,200))
        self.note39 = Note.Note((540,-6955),70,150,(255,255,200))
        self.note40 = Note.Note((240,-7125),70,150,(255,255,200))
        self.note41 = Note.Note((240,-7400),70,150,(255,255,200))
        self.note42 = Note.Note((540,-7565),70,150,(255,255,200))
        self.note43 = Note.Note((465,-7730),70,150,(255,255,200))
        self.note44 = Note.Note((615,-7895),70,150,(255,255,200)) 
        self.note45 = Note.Note((240,-8060),70,150,(255,255,200))
        self.note46 = Note.Note((465,-8225),70,150,(255,255,200))
        self.note47 = Note.Note((540,-8395),70,150,(255,255,200))
        self.note48 = Note.Note((240,-8560),70,150,(255,255,200))
        self.note49 = Note.Note((690,-8725),70,150,(255,255,200))
        #next section of the song
        self.note50 = Note.Note((390,-8890),70,150,(255,255,200))
        self.note51 = Note.Note((240,-9045),70,150,(255,255,200))
        self.note52 = Note.Note((540,-9200),70,150,(255,255,200))
        self.note53 = Note.Note((615,-9355),70,150,(255,255,200))
        self.note54 = Note.Note((690,-9510),70,150,(255,255,200))
        self.note55 = Note.Note((240,-9665),70,150,(255,255,200))
        self.note56 = Note.Note((615,-9820),70,150,(255,255,200))
        self.note57 = Note.Note((240,-9975),70,150,(255,255,200))
        self.note58 = Note.Note((465,-10130),70,150,(255,255,200))
        self.note59 = Note.Note((240,-10285),70,150,(255,255,200))
        self.note60 = Note.Note((465,-10535),70,150,(255,255,200))
        self.note61 = Note.Note((240,-10700),70,150,(255,255,200))
        self.note62 = Note.Note((540,-10865),70,150,(255,255,200))
        self.note63 = Note.Note((615,-11030),70,150,(255,255,200))
        self.note64 = Note.Note((690,-11190),70,150,(255,255,200))
        self.note65 = Note.Note((240,-11330),70,150,(255,255,200))
        self.note66 = Note.Note((615,-11510),70,150,(255,255,200))
        self.note67 = Note.Note((240,-11670),70,150,(255,255,200))
        self.note68 = Note.Note((465,-11830),70,150,(255,255,200))
        #next section of the song
        self.note69 = Note.Note((240,-12000),70,150,(255,255,200))
        self.note70 = Note.Note((465,-12155),70,150,(255,255,200))
        self.note71 = Note.Note((240,-12325),70,150,(255,255,200))
        self.note72 = Note.Note((540,-12475),70,150,(255,255,200))
        self.note73 = Note.Note((615,-12635),70,150,(255,255,200))
        self.note74 = Note.Note((690,-12795),70,150,(255,255,200))
        self.note75 = Note.Note((240,-12955),70,150,(255,255,200))
        self.note76 = Note.Note((615,-13120),70,150,(255,255,200))
        self.note77 = Note.Note((240,-13280),70,150,(255,255,200))
        self.note78 = Note.Note((465,-13440),70,150,(255,255,200))
        self.note79 = Note.Note((240,-13600),70,150,(255,255,200))
        self.note80 = Note.Note((465,-13760),70,150,(255,255,200))
        self.note81 = Note.Note((240,-13920),70,150,(255,255,200))
        self.note82 = Note.Note((540,-14080),70,150,(255,255,200))
        self.note83 = Note.Note((315,-14240),70,150,(255,255,200))
        self.note84 = Note.Note((690,-14395),70,150,(255,255,200))
        self.note85 = Note.Note((240,-14550),70,150,(255,255,200))
        self.note86 = Note.Note((615,-14705),70,150,(255,255,200))
        self.note87 = Note.Note((240,-14860),70,150,(255,255,200))
        self.note88 = Note.Note((465,-15015),70,150,(255,255,200))
        self.note89 = Note.Note((240,-15170),70,150,(255,255,200))
        self.note90 = Note.Note((465,-15325),70,150,(255,255,200))
        self.note91 = Note.Note((240,-15480),70,150,(255,255,200))
        self.note92 = Note.Note((540,-15635),70,150,(255,255,200))
        self.note93 = Note.Note((315,-15790),70,150,(255,255,200))
        self.note94 = Note.Note((690,-15945),70,150,(255,255,200))
        #next section of song
        self.note95 = Note.Note((240,-16145),70,150,(255,255,200))
        self.note96 = Note.Note((615,-16320),70,150,(255,255,200))
        self.note97 = Note.Note((690,-16480),70,150,(255,255,200))
        self.note98 = Note.Note((615,-16740),70,150,(255,255,200))
        self.note99 = Note.Note((690,-16900),70,150,(255,255,200))
        self.note100 = Note.Note((615,-17055),70,150,(255,255,200))
        self.note101 = Note.Note((540,-17210),70,150,(255,255,200))
        self.note102 = Note.Note((465,-17365),70,150,(255,255,200))
        self.note103 = Note.Note((240,-17430),70,150,(255,255,200))
        self.note104 = Note.Note((465,-17585),70,150,(255,255,200))
        self.note105 = Note.Note((540,-17840),70,150,(255,255,200))
        self.note106 = Note.Note((465,-17995),70,150,(255,255,200))
        self.note107 = Note.Note((615,-18150),70,150,(255,255,200))
        self.note108 = Note.Note((540,-18305),70,150,(255,255,200))
        self.note109 = Note.Note((240,-18460),70,150,(255,255,200))
        self.note110 = Note.Note((615,-18615),70,150,(255,255,200))
        self.note111 = Note.Note((540,-18770),70,150,(255,255,200))
        self.note112 = Note.Note((465,-18925),70,150,(255,255,200))
        self.note113 = Note.Note((240,-19080),70,150,(255,255,200))
        self.note114 = Note.Note((465,-19235),70,150,(255,255,200))
        self.note115 = Note.Note((540,-19390),70,150,(255,255,200))
        self.note116 = Note.Note((465,-19545),70,150,(255,255,200))
        self.note117 = Note.Note((615,-19700),70,150,(255,255,200))
        self.note118 = Note.Note((540,-19855),70,150,(255,255,200))
        self.note119 = Note.Note((240,-20010),70,150,(255,255,200))
        self.note120 = Note.Note((615,-20330),70,150,(255,255,200))
        self.note121 = Note.Note((465,-20490),70,150,(255,255,200))
        self.note122 = Note.Note((540,-20660),70,150,(255,255,200))
        #next section of music
        self.note123 = Note.Note((240,-20730),70,150,(255,255,200))
        self.note124 = Note.Note((690,-20900),70,150,(255,255,200))
        self.note125 = Note.Note((240,-21070),70,150,(255,255,200))
        self.note126 = Note.Note((615,-21240),70,150,(255,255,200))
        self.note127 = Note.Note((240,-21410),70,150,(255,255,200))
        self.note128 = Note.Note((465,-21580),70,150,(255,255,200))
        self.note129 = Note.Note((240,-21750),70,150,(255,255,200))
        self.note130 = Note.Note((465,-21920),70,150,(255,255,200))
        self.note131 = Note.Note((240,-22090),70,150,(255,255,200))

        """
        Add the keys and notes to a sprite group.
        args: None
        return: None
        """
        self.keys = pygame.sprite.Group()
        self.keys.add(self.KeyC)
        self.keys.add(self.KeyD)
        self.keys.add(self.KeyE)
        self.keys.add(self.KeyF)
        self.keys.add(self.KeyG)
        self.keys.add(self.KeyA)
        self.keys.add(self.KeyB)
    
        self.notes = pygame.sprite.Group()
        self.notes.add(self.note1)
        self.notes.add(self.note2)
        self.notes.add(self.note3)
        self.notes.add(self.note4)
        self.notes.add(self.note5)
        self.notes.add(self.note6)
        self.notes.add(self.note7)
        self.notes.add(self.note8)
        self.notes.add(self.note9)
        self.notes.add(self.note10)
        self.notes.add(self.note11)
        self.notes.add(self.note12)
        self.notes.add(self.note13)
        self.notes.add(self.note14)
        self.notes.add(self.note15)
        self.notes.add(self.note16)
        self.notes.add(self.note17)
        self.notes.add(self.note18)
        self.notes.add(self.note19)
        self.notes.add(self.note20)
        self.notes.add(self.note21)
        self.notes.add(self.note22)
        self.notes.add(self.note23)
        self.notes.add(self.note24)
        self.notes.add(self.note25)
        self.notes.add(self.note26)
        self.notes.add(self.note27)
        self.notes.add(self.note28)
        self.notes.add(self.note29)
        self.notes.add(self.note30)
        self.notes.add(self.note31)
        self.notes.add(self.note32)
        self.notes.add(self.note33)
        self.notes.add(self.note34)
        self.notes.add(self.note35)
        self.notes.add(self.note36)
        self.notes.add(self.note37)
        self.notes.add(self.note38)
        self.notes.add(self.note39)
        self.notes.add(self.note40)
        self.notes.add(self.note41)
        self.notes.add(self.note42)
        self.notes.add(self.note43)
        self.notes.add(self.note44)
        self.notes.add(self.note45)
        self.notes.add(self.note46)
        self.notes.add(self.note47)
        self.notes.add(self.note48)
        self.notes.add(self.note49)
        self.notes.add(self.note50)
        self.notes.add(self.note51)
        self.notes.add(self.note52)
        self.notes.add(self.note53)
        self.notes.add(self.note54)
        self.notes.add(self.note55)
        self.notes.add(self.note56)
        self.notes.add(self.note57)
        self.notes.add(self.note58)
        self.notes.add(self.note59)
        self.notes.add(self.note60)
        self.notes.add(self.note61)
        self.notes.add(self.note62)
        self.notes.add(self.note63)
        self.notes.add(self.note64)
        self.notes.add(self.note65)
        self.notes.add(self.note66)
        self.notes.add(self.note67)
        self.notes.add(self.note68)
        self.notes.add(self.note69)
        self.notes.add(self.note70)
        self.notes.add(self.note71)
        self.notes.add(self.note72)
        self.notes.add(self.note73)
        self.notes.add(self.note74)
        self.notes.add(self.note75)
        self.notes.add(self.note76)
        self.notes.add(self.note77)
        self.notes.add(self.note78)
        self.notes.add(self.note79)
        self.notes.add(self.note80)
        self.notes.add(self.note81)
        self.notes.add(self.note82)
        self.notes.add(self.note83)
        self.notes.add(self.note84)
        self.notes.add(self.note85)
        self.notes.add(self.note86)
        self.notes.add(self.note87)
        self.notes.add(self.note88)
        self.notes.add(self.note89)
        self.notes.add(self.note90)
        self.notes.add(self.note91)
        self.notes.add(self.note92)
        self.notes.add(self.note93)
        self.notes.add(self.note94)
        self.notes.add(self.note95)
        self.notes.add(self.note96)
        self.notes.add(self.note97)
        self.notes.add(self.note98)
        self.notes.add(self.note99)
        self.notes.add(self.note100)
        self.notes.add(self.note101)
        self.notes.add(self.note102)
        self.notes.add(self.note103)
        self.notes.add(self.note104)
        self.notes.add(self.note105)
        self.notes.add(self.note106)
        self.notes.add(self.note107)
        self.notes.add(self.note108)
        self.notes.add(self.note109)
        self.notes.add(self.note110)
        self.notes.add(self.note111)
        self.notes.add(self.note112)
        self.notes.add(self.note113)
        self.notes.add(self.note114)
        self.notes.add(self.note115)
        self.notes.add(self.note116)
        self.notes.add(self.note117)
        self.notes.add(self.note118)
        self.notes.add(self.note119)
        self.notes.add(self.note120)
        self.notes.add(self.note121)
        self.notes.add(self.note122)
        self.notes.add(self.note123)
        self.notes.add(self.note124)
        self.notes.add(self.note125)
        self.notes.add(self.note126)
        self.notes.add(self.note127)
        self.notes.add(self.note128)
        self.notes.add(self.note129)
        self.notes.add(self.note130)
        self.notes.add(self.note131)

        self.all_sprites = pygame.sprite.Group()

        pygame.display.flip()
