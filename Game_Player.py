import pygame
from Game_Sources import*
from pygame.locals import *

class Boy:
    def __init__(self):
        ## 소년 관련 초기값 ##
        self.boy_x = 100
        self.boy_y = 100
        self.boy_speed = 1

        self.boy_image = boyR_stay_image
        
        ## 갈고리 관련 초기값 ##
        self.isHookDown = 0
        self.isHookUp = 1
# 여기 수정
        self.hook_image = hookR_image
        self.hook_rect = self.hook_image.get_rect()

        self.isRight = True
        self.isLeft = False
        self.tmp_x = 12
        self.tmp_y = 35
        self.hook_x = self.boy_x + 123 - self.tmp_x
        self.hook_y = self.boy_y + 150 - self.tmp_y
# 여기까지
        self.hook_speed = 1

        self.hook_rect.left = self.hook_x
        self.hook_rect.top = self.hook_y

    def downHook(self):
# 여기 수정 (추가)
        if self.isRight :
            self.boy_image = boyR_fishing_image
        elif self.isLeft :
            self.boy_image = boyL_fishing_image
# 여기까지
        
        if (self.hook_y < 710):
            self.hook_y += self.hook_speed
            self.isHookDown = 1
            self.isHookUp = 0
        else:
            self.isHookDown = 0
            self.isHookUp = 1
                
    def upHook(self):
        if (self.hook_y > self.boy_y + 150 - self.tmp_y):   # - self.tmp_y 추가
                self.hook_y -= self.hook_speed
                self.isHookUp = 1
                self.isHookDown = 0
        else:
                self.isHookup = 0

    def move(self, pressed_keys):
        if pressed_keys[K_LEFT] and not(self.isHookDown) and(self.isHookUp) : # 주인공 이동
            if (boy.hook_y == 250 - self.tmp_y): # - self.tmp_y 추가
                if self.boy_x > -1: # 바로 밑에 한 줄 추가
                    self.hook_x = self.boy_x + 1 + self.tmp_x       # 갈고리 위치 변경
                    self.boy_x -= self.boy_speed # 왼쪽으로 이동
                    self.hook_x -= self.boy_speed
# 여기 수정 (추가)
                    self.boy_image = boyL_stay_image        # 이미지 반전
                    self.hook_image = hookL_image
                    self.isRight = False
                    self.isLeft = True
# 여기까지

        elif pressed_keys[K_RIGHT] and not(self.isHookDown) and self.isHookUp :
            if(boy.hook_y == 250 - self.tmp_y): # - self.tmp_y 추가
                if self.boy_x < 1139: # 바로 밑에 한 줄 추가
                    self.hook_x = self.boy_x + 123 - self.tmp_x     # 갈고리 위치 변경
                    self.boy_x += self.boy_speed # 오른쪽으로 이동
                    self.hook_x += self.boy_speed
# 여기 수정 (추가)
                    self.boy_image = boyR_stay_image
                    self.hook_image = hookR_image
                    self.isLeft = False
                    self.isRight = True
# 여기까지

        elif pressed_keys[K_DOWN]:# and self.isHookUp :# 낚시바늘 내리기
            if(boy.hook_y == 250 - self.tmp_y): # - self.tmp_y 추가
                
                fishing_music = pygame.mixer.Sound('sounds/Rake_Swing_Whoosh_Close.wav')
                fishing_music.play(0) #음악 반복 재생
                self.downHook()


    def draw(self):
        screen.blit(self.boy_image, (self.boy_x, self.boy_y))
        screen.blit(self.hook_image, (self.hook_x, self.hook_y))
# 여기 수정 (추가)
        if self.isRight :
            pygame.draw.line(screen, (0, 0, 0), [self.boy_x + 139 - (self.tmp_x + 5), self.boy_y + 140 - (self.tmp_y - 20)], [self.hook_x + 11, self.hook_y], 3)
        elif self.isLeft :
            pygame.draw.line(screen, (0, 0, 0), [self.boy_x + (self.tmp_x + 5), self.boy_y + 140 - (self.tmp_y - 20)], [self.hook_x + 4, self.hook_y], 3)
# 여기까지
       #pygame.draw.line(화면을 선언한 변수 값, 선의 색깔 (R, G, B), 선이 시작하는 점[x, y], 선이 끝나는 점[x, y], 선의 굵기)

boy = Boy() # boy 객체 생성
