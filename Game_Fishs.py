# 라이브러리, 클래스 불러오기
import pygame, random
from Game_Sources import*
from Game_Player import*

class Fishs:
    def __init__(self):
        self.x = -200
        self.y =  random.randint(150, 600)
        self.width = 70
        self.height = 30
        self.rr = random.randint(1,2) # 물고기의 종류를 선택
        self.isCatched = 0

        ## 각 물고기 별 렉트 값 설정 ##
        # 고등어 #
        fish_mackerel_rect.left = self.x
        fish_mackerel_rect.top = self.y

        # 은갈치 #
        fish_silverfish_rect.left = self.x
        fish_silverfish_rect.top = self.y

    def move(self): # 물고기의 움직임
            if self.rr == 1:
                self.x += 1 # 만약에 고등어면 보통으로 움직임

            if self.rr == 2:
                self.x += 3 # 만약에 은갈치면 존내 빠르게 움직임
             
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

    def touching(self): # 플레이어의 낚시 바늘 제어 / 낚시 바늘과 물고기의 충돌 여부
        # 다 올렸을 때
        if boy.hook_y < boy.boy_y + boy.boy_height :
            if self.isCatched :
                self.isCatched = 0
                pygame.time.delay(500)
            boy.hook_y = boy.boy_y + boy.boy_height
            boy.hook_dy = 0
            self.isHookUp = 1
        
        # 낚시바늘 올리기
        elif boy.hook_y > screen_height - boy.hook_height - 50 or self.isCatched :
            self.isHookDown = 0
            if boy.hook_dy >= 0 :
                boy.hook_dy -= boy.hook_speed

        # 낚시바늘-물고기 충돌 체크
        if hook_rect.colliderect(fish_mackerel_rect or fish_silverfish_rect) :
            self.x = boy.hook_x + boy.hook_width / 2 - boy.hook_width / 2
            self.y = boy.hook_y + boy.hook_height / 2 - boy.hook_height / 2
            self.isCatched = 1

    #def touching(self, missile):
        #self.space_trach_rect = pygame.Rect(self.x, self.y, 80, 80) ##추가
        #return self.space_trach_rect.colliderect(missile.character_rect)##추가