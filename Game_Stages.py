# 라이브러리, 클래스 불러오기
import pygame
from Game_Sources import*

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

    def backgroundscreen(self): # 게임 뒷배경
        screen.blit(game_background_image, (self.x, self.y))
        Button(fish_book_button_image,967,0,'book')