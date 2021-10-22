"""
Name: Lucy An
Date: May 2, 2018
Description: A Role playing battle game where the player must defeat the menacing Dragon by 
using the arrow keys to evade fire attacks and collect the dragon's lives. 

"""
import pygame, random


class Link(pygame.sprite.Sprite):
    """This class will control Link's movements"""
    
    def __init__(self,screen):
        """This method will initialize the list that contains all the Link images."""
        pygame.sprite.Sprite.__init__(self)
        
        self.__imageindex = 0
        self.__explode = False
  
        self.__explodeImages = [pygame.image.load("ex1.png"), pygame.image.load("ex2.png"), pygame.image.load("ex3.png"), pygame.image.load("ex4.png"),pygame.image.load("ex5.png"), pygame.image.load("ex6.png"), pygame.image.load("ex7.png"), pygame.image.load("ex8.png"), pygame.image.load("ex9.png")]        
         
        self.image = pygame.image.load("linkup.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width()/3.0 
        self.rect.centery = screen.get_height()/3.0 * 2      
        
        self.__dx, self.__dy = 0,0
        
    def resetMove(self, screen, direction):
        """This method loads new images of Link when the arrow keys are pressed."""
        
        linkImages = [pygame.image.load("linkleft.png"), pygame.image.load("linkright.png"),pygame.image.load("linkup.png"), pygame.image.load("linkdown.png")]
        
        self.image = linkImages[direction]
        
        lastx_position = self.rect.centerx
        lasty_position = self.rect.centery
        self.rect.centerx = lastx_position
        self.rect.centery = lasty_position
        
        if direction == 0:
            #Left
            self.__dx = -12
            self.__dy = 0
        elif direction == 1:
            #Right
            self.__dx = 12
            self.__dy = 0 
        elif direction == 2:
            #Up
            self.__dy = -12
            self.__dx = 0
        else:
            #Down
            self.__dy = 12
            self.__dx = 0 
            
    def set_explode(self):
        """This method alerts the update the start changing images for the explosion."""
        self.__explode = True
        
    def update(self):
        """Automatically updates Link's position """
        
        if self.__explode:
            self.image = self.__explodeImages[self.__imageindex]
            self.__imageindex += 1 
            if self.__imageindex == 9:
            # The True value will notify the main game loop that all images of the explosion have been shown 
                self.kill()
                return True
        
        else:
        
            self.rect.centerx += self.__dx
            self.rect.centery += self.__dy       
        
            if self.rect.centerx < 5:
                self.rect.centerx = 800
            if self.rect.centerx > 800:
                self.rect.centerx = 5 
            if self.rect.centery < 5:
                self.rect.centery = 600
            if self.rect.centery > 600:
                self.rect.centery = 5
        
        
class DragonTyrant(pygame.sprite.Sprite):
    """This class will control the Dragon Tyrant)"""
    
    def __init__(self, screen):
        """This method initializes the rect attributes of the Dragon sprite."""
        
        pygame.sprite.Sprite.__init__(self)
        
        self.__explodeImages = [pygame.image.load("ex1.png"), pygame.image.load("ex2.png"), pygame.image.load("ex3.png"), pygame.image.load("ex4.png"),pygame.image.load("ex5.png"), pygame.image.load("ex6.png"), pygame.image.load("ex7.png"), pygame.image.load("ex8.png"), pygame.image.load("ex9.png")]        
        self.__explode = False
        self.__imageindex = 0
        
        self.image = pygame.image.load("dragondown.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.rect.centerx = screen.get_width()/2.0
        self.rect.centery = screen.get_height()/3.5 
        
    def set_explode(self):
        """This method alerts the update method to start changing images for the explosion effect."""
        self.__explode = True
        
    def update(self):
        """This method will update the dragon's position"""
        
        if self.__explode:
            self.image = self.__explodeImages[self.__imageindex]
            self.__imageindex += 1 
            if self.__imageindex == 9:
                # The True value will notify the main game loop that all images of the explosion have been shown
                self.kill()
                return True
        
class Firestorm(pygame.sprite.Sprite):
    """This class will deal with the firestorm attacks."""
    
    def __init__(self, screen, dragonx, dragony, linkx, linky):
        """This method initializes the rect attributes of the firestorm sprite"""
        pygame.sprite.Sprite.__init__(self)
        
        self.__dragonx = dragonx 
        self.__dragony = dragony 
        self.__linkx = linkx
        self.__linky = linky 
        self.__imageindex = 0
        self.__explode = False
  
        self.__explodeImages = [pygame.image.load("ex1.png"), pygame.image.load("ex2.png"), pygame.image.load("ex3.png"), pygame.image.load("ex4.png"),pygame.image.load("ex5.png"), pygame.image.load("ex6.png"), pygame.image.load("ex7.png"), pygame.image.load("ex8.png"), pygame.image.load("ex9.png")]        
        
        self.image = pygame.image.load("blast.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.__dragonx 
        self.rect.centery = self.__dragony + 40
        
        self.__dx = (dragonx - linkx + 90) / 12
        self.__dy = (dragony - linky + 90) / 12
        
    
    def set_explode(self):
        """This mutator method will set the update method to start changing images for the explosion"""
        self.__explode = True
        
    
    def update(self):
        """This method will automatically update the firestorm's position."""
       
        if self.__explode:
            self.image = self.__explodeImages[self.__imageindex]
            self.__imageindex += 1 
        if self.__imageindex == 9:
            self.kill()
            
        self.rect.centerx -= self.__dx 
        self.rect.centery -= self.__dy
        

class LifePillar(pygame.sprite.Sprite):
    "This class defines the attributes for the dragon's lives/hearts that will appear on screen."
    
    def __init__(self, screen):
        "This method initializes its position. "
        pygame.sprite.Sprite.__init__(self)
        
        x_point = [100, 200,600, 700,500]
        y_point = [500,300,400,200]
        
        self.image = pygame.image.load("heart.png")
        self.rect = self.image.get_rect()
        n = random.randint(0,3)
        self.rect.centerx = x_point[n]
        self.rect.centery = y_point[n]
        

class ScoreKeeper(pygame.sprite.Sprite):
    """This class will deal with the score as the game progresses."""
    
    def __init__(self, screen):
        """This method will initialize the custom font, and the default number of life points for both the Dragon Tyrant and Link."""
        
        pygame.sprite.Sprite.__init__(self)
        
        self.__linkLP = 20
        self.__dragonLP = 30
        
        self.__font = pygame.font.Font("techno_hideo.ttf", 30)
        
    
    def reduce_DragonLP(self):
        """This method will reduce the Dragon Tyrant's Life Points."""
        
        self.__dragonLP -= 5       
        
    def reduce_LinkLP(self):
        """This method will reduce the Link's Life Points."""
       
        self.__linkLP -= 0.5
       
    def check_Dragon(self):
        """This method will return Link's remaining number of life points"""
        
        return self.__dragonLP
        
    def check_Link(self):
        """This method will return Link's remaining number of life points""" 
        
        return self.__linkLP
    
    def gameover(self,screen, allblasts,alldragonlives):
        """This method will notify the game loop to start erasing the blasts and hearts and make the ending process more efficient."""
        
        for blast in allblasts:
            blast.kill()
        for heart in alldragonlives:
            heart.kill()
    
        pygame.time.delay(2000)        
     
        
    def update(self):
        """This method will update and display the remaining number of life points of both the the Dragon Tyrant and Link as the game progresses."""
        
        linkLP, dragonLP = str(self.__linkLP), str(self.__dragonLP)
        if self.__linkLP < 0:
            self.__linkLP = 0
        if self.__dragonLP < 0:
            self.__dragonLP = 0
            
        message = "Link: " + linkLP + " Dragon Tyrant: " + dragonLP
        self.image = self.__font.render(message, 1, (224,238,238))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)
        

        
        
        
    
    
    
        
    