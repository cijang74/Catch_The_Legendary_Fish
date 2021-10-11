import pygame
from Game_Sources import*
from pygame.locals import *

class Boy:
    def __init__(self):
        ## 소년 관련 초기값 ##
        self.boy_x = 100
        self.boy_y = 100
        self.boy_dx = 0 # 원래 변수명: boy_x_change
        self.boy_speed = 1

        ## 갈고리 관련 초기값 ##
        self.isHookDown = 0
        self.isHookUp = 1

        self.hook_x = self.boy_x + 125
        self.hook_y = self.boy_y + 150
        self.hook_speed = 1

        hook_rect.left = self.hook_x
        hook_rect.top = self.hook_y

    def downHook(self):
            if (self.hook_y < 710):
                    self.hook_y += self.hook_speed
                    self.isHookDown = 1
                    self.isHookUp = 0
            else:
                self.isHookDown = 0
                self.isHookUp = 1
                
    def upHook(self):
        if (self.hook_y > self.boy_y + 150):
                self.hook_y -= self.hook_speed
                self.isHookUp = 1
                self.isHookDown = 0
        else:
                self.isHookup = 0

    def move(self, pressed_keys):
        if pressed_keys[K_LEFT] and not(self.isHookDown) and(self.isHookUp) : # 주인공 이동
            if (boy.hook_y == 250):
                if self.boy_x > -1:
                    self.boy_x -= self.boy_speed # 왼쪽으로 이동
                    self.hook_x -= self.boy_speed

        elif pressed_keys[K_RIGHT] and not(self.isHookDown) and self.isHookUp :
            if(boy.hook_y == 250):
                if self.boy_x < 1139: 
                    self.boy_x += self.boy_speed # 오른쪽으로 이동
                    self.hook_x += self.boy_speed

        elif pressed_keys[K_DOWN]:# and self.isHookUp :# 낚시바늘 내리기
            if(boy.hook_y == 250):
                self.downHook()


    def draw(self):
        screen.blit(boy_image, (self.boy_x, self.boy_y))
        screen.blit(hook_image, (self.hook_x, self.hook_y))

        pygame.draw.line(screen, (0, 0, 0), [self.boy_x + 139, self.boy_y + 140], [self.hook_x + 14, self.hook_y], 1)
       #pygame.draw.line(화면을 선언한 변수 값, 선의 색깔 (R, G, B), 선이 시작하는 점[x, y], 선이 끝나는 점[x, y], 선의 굵기)

boy = Boy() # boy 객체 생성