# 라이브러리, 클래스 불러오기
import pygame, time
from Game_Sources import*
from Game_Fishs import*

class Button: # 버튼 클래스
    def __init__(self, img_in, x, y, type):
        mouse = pygame.mouse.get_pos()

        if type == 'start':
            start_button_rect.left = x
            start_button_rect.top = y

        elif type == 'book':
            fish_book_button_rect.left = x
            fish_book_button_rect.top = y

        elif type == 'return':
            return_button_rect.left = x
            return_button_rect.top = y

        elif type == 'description':
            game_description_button_rect.left = x
            game_description_button_rect.top = y

        screen.blit(img_in,(x,y))

class Stages: # 스테이지 클래스
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def homescreen(self): # 게임 메인화면
        screen.blit(home_screen_image, (self.x, self.y))
        Button(start_button_image,780,520,'start')
        Button(game_description_button_image,210,520,'description')

    def descriptionscreen(self): # 게임 설명화면
        screen.blit(game_description_image, (self.x, self.y))
        Button(start_button_image,780,520,'start')

    def fishbookscreen(self): # 물고기 도감화면
        screen.blit(fish_book_image, (self.x, self.y))
        Button(return_button_image,0,574,'return')

    def backgroundscreen(self, last_fish_spawn_time, fishs): # 게임 진행 배경
        screen.blit(game_background_image, (self.x, self.y))
        spawn = True
        if time.time() - last_fish_spawn_time > 0.5 and spawn == True: # 물고기들 스폰
                fishs.append(Fishs())

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
        
        Button(fish_book_button_image,967,0,'book')