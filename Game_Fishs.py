import pygame, random
from Game_Sources import*

class Fishs:
    def __init__(self):
        self.x = 0
        self.y =  random.randint(50, 1030)
        self.rr = random.randint(1,2)

    def move(self):
        self.x += 2 # 물고기의 움직임
             
    def draw(self):
        if self.rr == 1:
            screen.blit(fish_mackerel_image, (self.x, self.y)) # 그리기
        if self.rr == 2:
            screen.blit(fish_silverfish_image, (self.x, self.y)) # 그리기

    def off_screen(self):
        return (self.x > 1800) # 화면을 넘어갔을 때

    #def touching(self, missile):
        self.space_trach_rect = pygame.Rect(self.x, self.y, 80, 80) ##추가
        return self.space_trach_rect.colliderect(missile.character_rect)##추가