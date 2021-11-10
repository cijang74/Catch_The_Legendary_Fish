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

        elif type == 'pause':
            pause_button_rect.left = x
            pause_button_rect.top = y

        elif type == 'countinue':
            countinue_button_rect.left = x
            countinue_button_rect.top = y

        elif type == 'end':
            game_end_button_rect.left = x
            game_end_button_rect.top = y

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

    def backgroundscreen(self, fishs, start_time, pressed_keys): # 게임 진행 배경
        global last_fish_spawn_time
        global pause
        global limit

        # while (time.time() - start_time <= 10): # 인트로 띄워주기
        #         if time.time() - start_time <= 5 and time.time() - start_time >= 0:
        #             screen.blit(game_intro_1_image, (self.x,self.y))

        #         if time.time() - start_time <= 10 and time.time() - start_time >= 5:
        #             screen.blit(game_intro_2_image, (self.x, self.y))

        #         pygame.display.update()
        
        screen.blit(game_background_image, (self.x, self.y))

        boy.move(pressed_keys)
        
        if (boy.isHookDown == 1):
            boy.downHook()
        
        if (boy.isHookUp == 1):
            boy.upHook()
        boy.draw()

        if time.time() - last_fish_spawn_time > 0.2 and pause == False: # 물고기들 스폰
                fishs.append(Fishs())
                last_fish_spawn_time = time.time()

        i = 0
        while i < len(fishs): # i가 현재 물고기의 개체수 보다 작을 때 동안 반복
            fishs[i].selcet_type()
            if pause == False:
                fishs[i].move() # 움직임
            fishs[i].draw() # 그리기
            
            if fishs[i].off_screen(): # 만약에 화면을 넘어가면
                del fishs[i] # 물고기 삭제
                i -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성

            if fishs[i].y < boy.hook_y + 15 and boy.hook_y < fishs[i].y + 60 and fishs[i].x < boy.hook_x + 30 and boy.hook_x < fishs[i].x + 160 and limit == False:
                fishs[i].isCatched = 1
                limit = True

            if fishs[i].isCatched == 1:
                fishs[i].x = boy.hook_x - 150
                fishs[i].y = boy.hook_y
                fishs[i].isCatched = 1
                
            if(fishs[i].y == 250):
                fishs[i].isCatched = 0
                limit = False
                del fishs[i]


            #elif fishs[i].touching(character):##추가
                #character.hp -= 1##추가
                #del fishs[i]##추가
                #i -= 1##추가
            i += 1

        Button(fish_book_button_image,1061,0,'book')
        Button(pause_button_image,1190,0,'pause')
            
        if pygame.mouse.get_pressed()[0] and pause_button_rect.collidepoint(pygame.mouse.get_pos()):
            pause = True

        if pause == True:
            #일시정지 하면 뒤에 배경 불투명한 검정색 칠하기#
            pause_screen_color = screen.convert_alpha()
            pause_screen_color.fill((0, 0, 0, 0))                    # t_surface 전체를 투명한 검정색으로 지운다
            
            pygame.draw.rect(pause_screen_color, (0, 0, 0, 150), (0, 0, 1280, 720))  # t_surface에 투명도를 적용하여 그려줌, (surface, color, Rect(x,y,w,h), Width = 0)
            screen.blit(pause_screen_color, (0, 0))                  # t_surface를 기본 Surface에 blit
            #############################################
            screen.blit(pause_screen_image, (0, 0))
            Button(countinue_button_image,520,270,'countinue')

            if pygame.mouse.get_pressed()[0] and countinue_button_rect.collidepoint(pygame.mouse.get_pos()):
                pause = False
            
            Button(game_end_button_image,520,373,'end')