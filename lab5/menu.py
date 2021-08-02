import pygame
import os

from pygame.constants import BUTTON_RIGHT

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))
class UpgradeMenu:
    def __init__(self, x, y):
        self.__buttons = [Button(UPGRADE_IMAGE,'upgrade',x,y+55),Button(SELL_IMAGE,'sell',x,y-55)]  # (Q2) Add buttons here and move the center of button
        self.image = pygame.transform.scale(MENU_IMAGE, (150, 150))  # image of the menu
        self.rect = self.image.get_rect()   
        self.rect.center = (x, y)  # center of the menu
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image, self.rect)     #show menu
        # draw button
        for btn in self.__buttons:          #show button
            win.blit(btn.image, btn.rect)
        # (Q2) Draw buttons here
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons   #return button list
        


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        if self.name == 'upgrade':  #choose the size of image
            self.image=pygame.transform.scale(image, (60,30))
        else:
            self.image=pygame.transform.scale(image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the button
        

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False  #return true if button is clicked
        

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name        #response the button type
        






