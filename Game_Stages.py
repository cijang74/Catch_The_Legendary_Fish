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

        elif type == 'close':
            close_button_rect.left = x
            close_button_rect.top = y

        elif type == 'mackerel':
            fish_book_button_mackerel_rect.left = x
            fish_book_button_mackerel_rect.top = y

        elif type == 'Snooze':
            fish_book_button_Snooze_rect.left = x
            fish_book_button_Snooze_rect.top = y

        elif type == 'Cod':
            fish_book_button_Cod_rect.left = x
            fish_book_button_Cod_rect.top = y

        elif type == 'Silverfish':
            fish_book_button_Silverfish_rect.left = x
            fish_book_button_Silverfish_rect.top = y

        elif type == 'Bluegill':
            fish_book_button_Bluegill_rect.left = x
            fish_book_button_Bluegill_rect.top = y

        elif type == 'Bass':
            fish_book_button_Bass_rect.left = x
            fish_book_button_Bass_rect.top = y

        elif type == 'Bigmouse_Bass':
            fish_book_button_Bigmouse_Bass_rect.left = x
            fish_book_button_Bigmouse_Bass_rect.top = y

        elif type == 'Piranha':
            fish_book_button_Piranha_rect.left = x
            fish_book_button_Piranha_rect.top = y

        elif type == 'Rainbow':
            fish_book_button_Rainbow_rect.left = x
            fish_book_button_Rainbow_rect.top = y

        screen.blit(img_in,(x,y))

class Stages: # 스테이지 클래스
    def __init__(self):
        self.x = 0
        self.y = 0
        self.mackerel_count = 0
        self.Snooze_count = 0
        self.Cod_count = 0
        self.Silverfish_count = 0
        self.Bluegill_count = 0
        self.Bass_count = 0
        self.Bigmouse_Bass_count = 0
        self.Piranha_count = 0
        self.Rainbow_count = 0
        
    def homescreen(self): # 게임 메인화면
        screen.blit(home_screen_image, (self.x, self.y))
        Button(start_button_image,780,520,'start')
        Button(game_description_button_image,210,520,'description')

    def descriptionscreen(self): # 게임 설명화면
        screen.blit(game_description_image, (self.x, self.y))
        Button(start_button_image,780,520,'start')

    def fishbookscreen(self): # 물고기 도감화면

        # 모든 물고기가 ??? 상태인 기본 그리드 그려주기
        screen.blit(fish_book_image, (self.x, self.y))

        # 물고기가 잡힌것이 확인 되면 해당 물고기 이미지 띄워주기
        if Snooze == False:
            screen.blit(fish_book_Snooze_image, (188, 58))

        if Cod == False:
            screen.blit(fish_book_Cod_image, (488, 58))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        # 각 물고기 설명을 보여주는 버튼
        if Snooze == False:
            Button(fish_book_button_Snooze_image,240,214,'Snooze')

        if Cod == False:
            Button(fish_book_button_Cod_image,541,214,'Cod')

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (185, 54))

        # 게임으로 돌아가는 버튼
        Button(return_button_image,10,574,'return')

    def backgroundscreen(self, fishs, start_time, pressed_keys): # 게임 진행 배경
        global last_fish_spawn_time
        global pause
        global limit
        global stop
        global mackerel
        global Snooze
        global Cod
        global Silverfish
        global Bluegill
        global Bass
        global Bigmouse_Bass
        global Piranha
        global Rainbow
        global count_o
        global count_s

        """
        if count_o == 0:
            pygame.mixer.music.load('sounds/오프닝.wav') #배경 음악
            pygame.mixer.music.play(0)
            while (time.time() - start_time <= 21): # 인트로 띄워주기
                if time.time() - start_time <= 7 and time.time() - start_time >= 0:
                    screen.blit(game_intro_1_image, (self.x,self.y))

                if time.time() - start_time <= 14 and time.time() - start_time >= 7:
                    screen.blit(game_intro_2_image, (self.x, self.y))

                if time.time() - start_time <= 21 and time.time() - start_time >= 14:
                    screen.blit(game_intro_3_image, (self.x, self.y))
                    count_o = 1

                pygame.display.update()
        """
        
        screen.blit(game_background_image, (self.x, self.y))

        if count_s == 0:
            stage_music = pygame.mixer.Sound('sounds/인게임.wav')
            stage_music.play(-1) #음악 반복 재생
        count_s += 1

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
                i -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 물고기 생성

            if fishs[i].y < boy.hook_y + 15 and boy.hook_y < fishs[i].y + 60 and fishs[i].x < boy.hook_x + 30 and boy.hook_x < fishs[i].x + 160 and limit == False:
                fishs[i].isCatched = 1
                
                # 물고기들 종류별로 잡았다는 표시를 함
                if fishs[i].type == "mackerel":
                    self.mackerel_count += 1
                    mackerel = True

                if fishs[i].type == "Snooze":
                    self.Snooze_count += 1
                    Snooze = True

                if fishs[i].type == "Cod":
                    Cod = True

                if fishs[i].type == "Silverfish":
                    Silverfish = True

                if fishs[i].type == "Bluegill":
                    Bluegill = True
                    print(Bluegill)

                if fishs[i].type == "Bass":
                    Bass = True

                if fishs[i].type == "Bigmouse_Bass":
                    Bigmouse_Bass = True

                if fishs[i].type == "Piranha":
                    Piranha = True

                if fishs[i].type == "Rainbow":
                    Rainbow = True
                
                limit = True

            if fishs[i].isCatched == 1:
                fishs[i].x = boy.hook_x - 50
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
        
        ### 물고기 처음 잡았을 때 도감 띄워주는거 ###

        if self.mackerel_count == 1:
            if (time.time() - stop) > 1:
                screen.blit(first_catch_mackerel_window_image, (0, 0))
                pygame.display.update()
                stop = time.time()

        if self.Snooze_count == 1:
            if (time.time() - stop) > 1:
                screen.blit(first_catch_Snooze_window_image, (0, 0))
                pygame.display.update()
                stop = time.time()
        
        if pygame.mouse.get_pressed()[0] and pause_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pause == False:
                pause_button_sound = pygame.mixer.Sound('sounds/버튼_일시정지.wav')
                pause_button_sound.play(0) #음악 반복 재생
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
                weak_button_sound = pygame.mixer.Sound('sounds/버튼_힘없음.wav')
                weak_button_sound.play(0) #음악 반복 재생
                pause = False
            
            Button(game_end_button_image,520,373,'end')