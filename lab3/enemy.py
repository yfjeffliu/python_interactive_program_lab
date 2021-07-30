import pygame
import math
import os
from settings import PATH1, RED , PATH2,GREEN

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self,PATH=PATH1): #怪物的路徑非預設 而是宣告時輸入 預設path1
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]
        

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        # ...(to be done)
        pygame.draw.rect(win, RED, [self.x - self.width // 2, self.y - self.height // 2 -8, 40, 8]) #色碼,X點、Y點、寬、高
        pygame.draw.rect(win, RED, [GREEN - self.width // 2, self.y - self.height // 2 -8, 40*self.health/self.max_health, 8]) #色碼,X點、Y點、寬、高
        pass

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        # ...(to be done)
        
        
        if self.path_pos == len(self.path)-1:   #預防list爆炸
            return
        ax, ay = self.path[self.path_pos]  # x, y 初始位置
        bx, by = self.path[self.path_pos+1] # x , y 目標位置
        distance_A_B = math.sqrt((ax - bx)**2 + (ay - by)**2)
        max_count = int(distance_A_B / self.stride)  # total footsteps that needed from A to B
        #print(self.move_count,self.path_pos)   #debug專用
        if self.move_count < max_count:         #移動
            unit_vector_x = (bx - ax) / distance_A_B
            unit_vector_y = (by - ay) / distance_A_B
            delta_x = unit_vector_x * self.stride
            delta_y = unit_vector_y * self.stride

            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
            pass
        else :
            self.path_pos +=1   #下一個位置
            self.move_count=0   #重製
            

       


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = []  # don't change this line until you do the EX.3 
        self.path_ctrl = True  #控制哪一條路徑
    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """

        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)
        
        if self.gen_count >= self.gen_period and not self.is_empty():   #時間到且有怪物待產生
            self.expedition.append(self.reserved_members.pop())     #新增怪物
            #print('app') #產生於螢幕上
            self.gen_count = 0
            
        else:
            self.gen_count+=1
        pass

    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # ...(to be done)
        
        if self.path_ctrl:  #路徑變更
            PATH=PATH1
            self.path_ctrl=False
        else:
            PATH=PATH2
            self.path_ctrl=True
        for i in range(0,num):  #新增怪物至產生序列
            self.reserved_members.append(Enemy(PATH))
        
        pass

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





