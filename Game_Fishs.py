# 라이브러리, 클래스 불러오기
import pygame, random
from Game_Sources import*
from Game_Player import*

class Fishs:
    def __init__(self):
        self.x = -200
        self.y =  random.randint(300, 600)
        self.width = 70
        self.height = 30
        self.rr = random.randint(1,100) # 물고기의 등장확률을 계산
        self.type = None # self.rr을 바탕으로 종류를 선택
        self.isCatched = 0

        ## 각 물고기 별 렉트 값 설정 ##
        # 고등어 #
        fish_mackerel_rect.left = self.x
        fish_mackerel_rect.top = self.y

        # 은갈치 #
        fish_silverfish_rect.left = self.x
        fish_silverfish_rect.top = self.y

    def selcet(self):
        ## 아래 물고기는 총 20%의 확률로 등장함
        if 1 <= self.rr and self.rr <= 5:
            self.type = "mackerel"
        
        elif 5 <= self.rr and self.rr <= 10:
            self.type = "Snooze"

        elif 10 <= self.rr and self.rr <= 15:
            self.type = "Cod"

        elif 15 <= self.rr and self.rr <= 20:
            self.type = "Silverfish"

        ## 아래 물고기는 총 60%의 확률로 등장함
        elif 20 <= self.rr and self.rr  <= 35:
            self.type = "Bluegill"

        elif 35 <= self.rr and self.rr  <= 50:
            self.type = "Bass"

        elif 50 <= self.rr and self.rr  <= 65:
            self.type = "Bigmouse_Bass"

        elif 65 <= self.rr and self.rr  <= 80:
            self.type = "Piranha"

        # elif 20 <= self.rr and self.rr  <= 35: //후에 추가
        #     self.type = "Rainbow"

    def move(self): # 물고기의 움직임

        ## 아래 물고기는 20%의 확률로 등장함
            if self.type == "mackerel":
                self.x += 8 # 만약에 고등어면 보통으로 움직임

            if self.type == "Snooze":
                self.x += 11 # 만약에 은갈치면 존내 빠르게 움직임

            if self.type == "Cod":
                self.x += 11 # 만약에 은갈치면 존내 빠르게 움직임

            if self.type == "Silverfish":
                self.x += 11 # 만약에 은갈치면 존내 빠르게 움직임

            if self.type == "Bluegill":
                self.x += 11 # 만약에 은갈치면 존내 빠르게 움직임

            if self.type == "Bass":
                self.x += 11 # 만약에 은갈치면 존내 빠르게 움직임

            if self.type == "Bigmouse_Bass":
                self.x += 11 # 만약에 은갈치면 존내 빠르게 움직임

            if self.type == "Piranha":
                self.x += 1
             
    def draw(self):
        if self.rr == 1:
            screen.blit(fish_mackerel_image, (self.x, self.y)) # 그리기
        if self.rr == 2:
            screen.blit(fish_silverfish_image, (self.x, self.y)) # 그리기

    def off_screen(self):
        return (self.x > 1800) # 화면을 넘어갔을 때 물고기 없앰

    def make_fish(self):
        i = 0
        while i < len(fishs): #i가 현재 물고기의 개체수 보다 작을 때 동안 반복
            fishs[i].move()# 움직임
            fishs[i].draw()# 그리기
            
            if fishs[i].off_screen(): #만약에 화면을 넘어가면
                del fishs[i] # 물고기 삭제
                i -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성

            #elif fishs[i].touching(character):##추가
                #character.hp -= 1##추가
                #del fishs[i]##추가
                #i -= 1##추가
            i += 1

    #def touching(self, missile):
        #self.space_trach_rect = pygame.Rect(self.x, self.y, 80, 80) ##추가
        #return self.space_trach_rect.colliderect(missile.character_rect)##추가