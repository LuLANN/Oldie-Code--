"""
Name: Lucy An
Date: May 2, 2018
Description: Role playing battle game. 

"""
# I - IMPORT AND INITIALIZE
import pygame, random, dragonsprites
pygame.init()
pygame.mixer.init()

def main():
    '''This function defines the 'mainline logic'''
    # DISPLAY
    pygame.display.set_caption("Dragon Menace")
    background = pygame.image.load("arena.png")
    screen = pygame.display.set_mode((800,600))
    screen.blit(background, (0, 0))
    
    #menu()
    
    """pygame.mixer.music.load("darkworld.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)"""
    
    roar = pygame.mixer.Sound("roar.wav")
    hit.set_volume(0.4)
    
    explode  = pygame.mixer.Sound("explode.wav")
    gameover.set_volume(0.7)    
    
    link = dragonsprites.Link(screen)
    dragon = dragonsprites.DragonTyrant(screen)
    scorekeeper = dragonsprites.ScoreKeeper(screen)
    allblasts = pygame.sprite.Group()
    allSprites = pygame.sprite.Group(link, dragon, scorekeeper)
    
    # ACTION
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    
   
    
    pygame.mouse.set_visible(False)
    
    # Counter will count each frame that passes once the game starts 
    counter = 0
    
    # LOOP
    while keepGoing:
         
        # TIME
        clock.tick(30)
        
        # EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.mixer.music.fadeout(2000)
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_LEFT:
                    link.resetMove(screen, 0)
                    
                elif event.key == pygame.K_RIGHT:
                    link.resetMove(screen, 1)
                    
                elif event.key == pygame.K_UP:
                    link.resetMove(screen, 2)
                    
                elif event.key == pygame.K_DOWN:
                    link.resetMove(screen, 3)
                    
        counter += 1
        duration = 150
        
        # Decrease the amount of time each set of firestorms appear as the Dragon's life points decreases
        
        if scorekeeper.check_Dragon() < 30 and  scorekeeper.check_Dragon() > 25:
            duration = 90
        elif scorekeeper.check_Dragon() < 25 and  scorekeeper.check_Dragon() > 20:
            duration = 60
        else:
            duration = 30
        
        
        blasts = [] 
             
        if counter % duration == 0:
        
            blasts.append(dragonsprites.Firestorm(screen, dragon.rect.centerx, dragon.rect.centery, link.rect.centerx, link.rect.centery))
            
            allblasts = pygame.sprite.Group(blasts)
            
            allSprites = pygame.sprite.Group(link, dragon, allblasts,scorekeeper)
            
        
        # Collision Detection between Link, and the Firestorms 
        for firestorm in allblasts:
            if pygame.sprite.spritecollide(link,allblasts, True):
                firestorm.explode()
                
                scorekeeper.reduce_LinkLP()         
        
        # Collision Detection between Dragon and Link
       
        if dragon.rect.colliderect(link.rect):
            scorekeeper.reduce_DragonLP()
            
        if scorekeeper.check_Link() == 0:
            gameover = dragonsprites.GameOverLabel(screen, 1)
            
            keepGoing = False
        
        # REFRESH SCREEN
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)        
        pygame.display.flip()
             
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
     
    pygame.quit()     
         
# Call the main function
main()
