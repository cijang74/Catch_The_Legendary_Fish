# 라이브러리, 클래스 불러오기
import pygame, random
from Game_Sources import*
from Game_Player import*

class Fish:
    def __init__(self):
        # 쓰레기 이미지 회전 위한 것
        self.trash_can_img = trash_can_image
        self.trash_strow_img = trash_strow_image
        
        self.x = -200
        self.y =  random.randint(300, 600)
        self.width = 70
        self.height = 30
        self.rr = random.randint(1,104) # 물고기의 등장확률을 계산
        self.type = None # self.rr을 바탕으로 종류를 선택
        self.isCatched = 0

        ## 각 물고기 별 렉트 값 설정 ##
        # 고등어 #
        fish_mackerel_rect.left = self.x
        fish_mackerel_rect.top = self.y

        # 은갈치 #
        fish_silverfish_rect.left = self.x
        fish_silverfish_rect.top = self.y

    def selcet_type(self):
        global mackerel #고등어
        global Snooze
        global Cod
        global Silverfish
        global Bluegill
        global Bass
        global Bigmouse_Bass
        global Piranha

        ## 아래 물고기는 총 20%의 확률로 등장함 #5차이
        if 1 <= self.rr and self.rr <= 8:  #1<=5
            self.type = "mackerel"
        
        if 5 <= self.rr and self.rr <= 12: #5<=10
            self.type = "Snooze"

        if 10 <= self.rr and self.rr <= 17:
            self.type = "Cod"

        if 13 <= self.rr and self.rr <= 20:
            self.type = "Silverfish"

        ## 아래 물고기는 총 60%의 확률로 등장함 #15차이, 총 60
        if 20 <= self.rr and self.rr  <= 35: #20<=35
            self.type = "Bluegill"

        if 35 <= self.rr and self.rr  <= 50:
            self.type = "Bass"

        if 50 <= self.rr and self.rr  <= 65:
            self.type = "Bigmouse_Bass"

        if 65 <= self.rr and self.rr  <= 80:
            self.type = "Piranha"

        ## 쓰레기 20% 
        if 80 <= self.rr and self.rr  <= 90:
            self.type = "trash_can"

        if 90 <= self.rr and self.rr  <= 100:
            self.type = "trash_strow"

        ## 무지개 물고기
        if 100 <= self.rr and self.rr  <= 104:
            self.type = "Rainbow"

    def move(self): # 물고기의 움직임 #3이상이면 빨라짐.

        ## 아래 물고기는 총 20%의 확률로 등장함

        ## 너무 빠르게 하면 인덱스 빵꾸남 그래서 일단 임의로 줄여놓음~
            if self.type == "mackerel":
                self.x += 0.6 # 고등어 속도 #초기 2

            if self.type == "Snooze":
                self.x += 0.7 # 도루묵 속도 #초기 3

            if self.type == "Cod":
                self.x += 0.6 # 대구 속도 #초기 2

            if self.type == "Silverfish":
                self.x += 1.1 # 은갈치 속도 #초기 3

        ## 아래 물고기는 총 60%의 확률로 등장함
            if self.type == "Bluegill":
                self.x += 0.5 # 블루길 속도 #초기 1

            if self.type == "Bass":
                self.x += 0.8 # 베스 속도 #초기 1

            if self.type == "Bigmouse_Bass":
                self.x += 0.9 # 큰입베스 속도 #초기 2

            if self.type == "Piranha":
                self.x += 1.1 # 피라냐 속도 #초기 3

            if self.type == "trash_can":
                self.x += 0.5  #초기 0.5
                if self.x % 180 == 0 :
                    self.trash_can_img = pygame.transform.rotate(self.trash_can_img, 90)

            if self.type == "trash_strow":
                self.x += 0.5 #초기 0.5
                if self.x % 180 == 0 :
                    self.trash_strow_img = pygame.transform.rotate(self.trash_strow_img, 90)

            if self.type == "Rainbow":
                self.x += 1.3

        ## 무지개 물고기
             
    def draw(self):

        ## 타입별로 물고기 마다 다른 이미지를 그림
        if self.type == "mackerel":
            screen.blit(fish_mackerel_image, (self.x, self.y))

        if self.type == "Snooze":
            screen.blit(fish_snooze_image, (self.x, self.y))

        if self.type == "Cod":
            screen.blit(fish_cod_image, (self.x, self.y))

        if self.type == "Silverfish":
            screen.blit(fish_silverfish_image, (self.x, self.y))

        if self.type == "Bluegill":
            screen.blit(fish_bluegill_image, (self.x, self.y))

        if self.type == "Bass":
            screen.blit(fish_bass_image, (self.x, self.y))

        if self.type == "Bigmouse_Bass":
            screen.blit(fish_bigmouse_bass_image, (self.x, self.y))

        if self.type == "Piranha":
            screen.blit(fish_piranha_image, (self.x, self.y))

        if self.type == "trash_can":
            screen.blit(self.trash_can_img, (self.x, self.y))

        if self.type == "trash_strow":
            screen.blit(self.trash_strow_img , (self.x, self.y))

        if self.type == "Rainbow":
            screen.blit(fish_rainbow_image , (self.x, self.y))

    def fish_catched(self):
        # 도감 관련 전역 변수들 사용
        global mackerel
        global Snooze
        global Cod
        global Silverfish
        global Bluegill
        global Bass
        global Bigmouse_Bass
        global Piranha
        global Rainbow

        if self.isCatched == 1:
            # 물고기들 종류별로 잡았다는 표시를 함
            if self.type == "mackerel":
                mackerel = True

            if self.type == "Snooze":
                Snooze = True

            if self.type == "Cod":
                Cod = True

            if self.type == "Silverfish":
                Silverfish = True

            if self.type == "Bluegill":
                Bluegill = True

            if self.type == "Bass":
                Bass = True

            if self.type == "Bigmouse_Bass":
                Bigmouse_Bass = True

            if self.type == "Piranha":
                Piranha = True

            if self.type == "Rainbow":
                Rainbow = True

    def off_screen(self):
        return (self.x > 1400) # 화면을 넘어갔을 때 물고기 없앰

    def make_fish(self):
        i = 0
        while i < len(fish): #i가 현재 물고기의 개체수 보다 작을 때 동안 반복
            fish[i].move()# 움직임
            fish[i].draw()# 그리기
            
            if fish[i].off_screen(): #만약에 화면을 넘어가면
                del fish[i] # 물고기 삭제
                i -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성

            #elif fish[i].touching(character):##추가
                #character.hp -= 1##추가
                #del fish[i]##추가
                #i -= 1##추가
            i += 1

    #def touching(self, missile):
        #self.space_trach_rect = pygame.Rect(self.x, self.y, 80, 80) ##추가
        #return self.space_trach_rect.colliderect(missile.character_rect)##추가