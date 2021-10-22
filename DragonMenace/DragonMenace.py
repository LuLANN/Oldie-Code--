"""
Name: Lucy An
Date: May 2, 2018
Description: A Role playing battle game where the player must defeat the menacing Dragon by
using the arrow keys to evade fire attacks and collect the dragon's lives.
"""
#!/usr/local/bin/python3.x
# I - IMPORT AND INITIALIZE
import pygame, random, newdragonsprites
pygame.init()
pygame.mixer.init()


def main():
    """This main game loop will deal with the menu controls and calling the game loop"""
    menu = True
    restart = False
    pygame.display.set_caption("Dragon Menace")
    screen = pygame.display.set_mode((800,600))

    startmenu = pygame.image.load("startmenu.png")
    play = pygame.image.load("startbutton.png")
    historymural = pygame.image.load("history.png")
    startmenu.blit(play, (300, 480))
    startmenu.blit(historymural, (200, 250))

    while menu == True or keepGoing == True:
        screen.blit(startmenu,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y  = pygame.mouse.get_pos()

                # Checking if the mouse had clicked on any part of the play button
                if 300 <= x <= 500 and 480 <= y <= 570:
                    menu = False
                    replay = True
                    while replay:
                        # This line is needed or else the scorekeeper's font is not initialized causing the program to crash.
                        pygame.init()
                        DragonMenace()
                        pygame.time.delay(3000)

                        endgame()
                        # If the player chooses to play again the while loop will repeat.
                        if endgame() == True:
                            replay = True

def endgame():
    """This function will define the window that will appear when the game ends."""
    screen = pygame.display.set_mode((800,600))
    endpage = pygame.image.load("arena.png")

    historymural = pygame.image.load("history.png")
    # This image will be the replay button
    restart = pygame.image.load("replay.png")
    endpage.blit(restart, (200, 300))
    endpage.blit(historymural, (200, 50))

    keepGoing = True
    while keepGoing:
        screen.blit(endpage, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 200 <= x <= 500 and 300 <= y <= 390:
                    return True

def DragonMenace():
    '''This function defines the 'mainline logic for the game'''
    # DISPLAY

    pygame.display.set_caption("Dragon Menace")
    screen = pygame.display.set_mode((800,600))

    # ENTITIES

    background = pygame.image.load("arena.png")
    screen.blit(background, (0, 0))

    # UPDATE: Music files no longer crash the game. Maybe because it got turned into an .exe
    pygame.mixer.music.load("darkworld.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    roar = pygame.mixer.Sound("roar.wav")
    roar.set_volume(0.1)
    explode = pygame.mixer.Sound("explode.wav")
    explode.set_volume(0.1)

    # Instantiating sprites and images

    link = newdragonsprites.Link(screen)
    dragon = newdragonsprites.DragonTyrant(screen)
    scorekeeper = newdragonsprites.ScoreKeeper(screen)

    win = pygame.image.load("youwin.png")
    lose = pygame.image.load("youlose.png")
    tie = pygame.image.load("tie.png")

    alldragonlives = pygame.sprite.Group()
    allblasts = pygame.sprite.Group()
    midblasts = pygame.sprite.Group()
    allSprites = pygame.sprite.Group(link, dragon, scorekeeper)

    # ACTION
    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True

    pygame.mouse.set_visible(False)

    # Counter will count each frame that passes once the game starts
    counter = 0
    victory = True

    # LOOP
    while keepGoing:

        # TIME
        clock.tick(30)

        # EVENT HANDLING

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(2000)
                keepGoing = False
                # Unhide the mouse pointer
                pygame.mouse.set_visible(True)

                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    link.resetMove(screen, 0)

                if event.key == pygame.K_RIGHT:
                    link.resetMove(screen, 1)

                if event.key == pygame.K_UP:
                    link.resetMove(screen, 2)

                if event.key == pygame.K_DOWN:
                    link.resetMove(screen, 3)

        # This variable will keep track of the number of frames
        counter += 1

        dragonlives = []

        # Instantiating the fire blasts and the dragon lives

        if counter % 25 == 0:

            allblasts.add(newdragonsprites.Firestorm(screen, dragon.rect.centerx, dragon.rect.centery, link.rect.centerx, link.rect.centery))
            allSprites = pygame.sprite.Group(link, dragon, scorekeeper, allblasts)

        if counter % 60 == 0:
            alldragonlives.add(newdragonsprites.LifePillar(screen))
            allSprites = pygame.sprite.Group(link, dragon, scorekeeper, allblasts, alldragonlives)

        # Collision Detection and setting explosions

        for blast in allblasts:
            if pygame.sprite.spritecollide(link, allblasts, False):
                blast.set_explode()
                explode.play()
                scorekeeper.reduce_LinkLP()

        for life in alldragonlives:
            if pygame.sprite.spritecollide(link, alldragonlives, True):
                scorekeeper.reduce_DragonLP()
                roar.play()

        # Checking if either link has died or if the dragon has been defeated therefore ending the game.

        if scorekeeper.check_Link() <= 0.0:
            link.set_explode()
            # If the class returns True meaning ALL images of the explosion have been shown, end the game
            if link.update():
            # Blitting the you lose! sign
                dragon.kill()
                scorekeeper.gameover(screen,allblasts,alldragonlives)
                screen.blit(lose, (200,300))
                pygame.time.delay(3000)
                keepGoing = False

        if scorekeeper.check_Dragon() <= 0.0:
            dragon.set_explode()
            # If the class returns True meaning ALL images of the explosion have been shown, end the game
            if dragon.update():
                link.kill()
                scorekeeper.gameover(screen, allblasts,alldragonlives)
                screen.blit(win, (200,200))
                pygame.time.delay(2000)
                keepGoing = False

        if scorekeeper.check_Dragon() <= 0.0 and scorekeeper.check_Link() <= 0.0:
            if link.update() and dragon.update():
                link.kill()
                dragon.kill()
                scorekeeper.gameover(screen,allblasts,alldragonlives)
                screen.blit(tie, (200,200))
                pygame.time.delay(3000)
                keepGoing = False


        # REFRESH SCREEN
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()

# Call the main function
main()
