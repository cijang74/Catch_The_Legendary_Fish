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

        elif type == 'ending':
            game_ending_button_rect.left = x
            game_ending_button_rect.top = y

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
        self.stage_music = pygame.mixer.Sound('sounds/인게임.wav')
        
    def homescreen(self): # 게임 메인화면
        screen.blit(home_screen_image, (self.x, self.y))
        Button(start_button_image,780,520,'start')
        Button(game_description_button_image,210,520,'description')

    def descriptionscreen(self): # 게임 설명화면
        screen.blit(game_description_image, (self.x, self.y))
        Button(start_button_image,780,520,'start')

    def endingscreen(self): # 엔딩화면
        global count_e
        self.stage_music.stop()
        ending_start_time = time.time()

        if count_e == 0:
            pygame.mixer.music.load('sounds/엔딩.wav') #배경 음악
            pygame.mixer.music.play(0)
            while (time.time() - ending_start_time <= 21): # 인트로 띄워주기
                if time.time() - ending_start_time <= 7 and time.time() - ending_start_time >= 0:
                    screen.blit(game_ending_1_image, (self.x,self.y))

                if time.time() - ending_start_time <= 14 and time.time() - ending_start_time >= 7:
                    screen.blit(game_ending_2_image, (self.x, self.y))

                if time.time() - ending_start_time <= 21 and time.time() - ending_start_time >= 14:
                    screen.blit(game_ending_3_image, (self.x, self.y))
                    count_e = 1

                pygame.display.update()
                pygame.time.delay(100)

    def fishbookscreen(self): # 물고기 도감화면

        # 모든 물고기가 ??? 상태인 기본 그리드 그려주기
        screen.blit(fish_book_image, (self.x, self.y))

        # 물고기가 잡힌것이 확인 되면 해당 물고기 이미지 띄워주기
        if Snooze == True:
            screen.blit(fish_book_Snooze_image, (188, 58))

        if Cod == True:
            screen.blit(fish_book_Cod_image, (488, 58))

        if mackerel == True:
            screen.blit(fish_book_mackerel_image, (789, 58))

        if Bluegill == True:
            screen.blit(fish_book_Bluegill_image, (188, 258))

        if Rainbow == True:
            screen.blit(fish_book_Rainbow_image, (488, 258))

        if Bass == True:
            screen.blit(fish_book_Bass_image, (788, 258))

        if Bigmouse_Bass == True:
            screen.blit(fish_book_Bigmouse_Bass_image, (188, 458))

        if Piranha == True:
            screen.blit(fish_book_Piranha_image, (788, 458))

        if Silverfish == True:
            screen.blit(fish_book_Silverfish_image, (488, 458))

        # 각 물고기 설명을 보여주는 버튼
        if Snooze == True:
            Button(fish_book_button_Snooze_image,240,214,'Snooze')

        if Cod == True:
            Button(fish_book_button_Cod_image,541,214,'Cod')

        if mackerel == True:
            Button(fish_book_button_mackerel_image,842,214,'mackerel')

        if Bluegill == True:
            Button(fish_book_button_Bluegill_image,240,415,'Bluegill')

        if Rainbow == True:
            Button(fish_book_button_Rainbow_image,541,415,'Rainbow')

        if Bass == True:
            Button(fish_book_button_Bass_image,842,415,'Bass')

        if Bigmouse_Bass == True:
            Button(fish_book_button_Bigmouse_Bass_image,240,608,'Bigmouse_Bass')

        if Piranha == True:
            Button(fish_book_button_Piranha_image,842,608,'Piranha')

        if Silverfish == True:
            Button(fish_book_button_Silverfish_image,541,608,'Silverfish')

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
        
        screen.blit(game_background_image, (self.x, self.y))

        if count_s == 0:
            self.stage_music.play(-1) #음악 반복 재생
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

            ## 다른 물고기를 잡지 않았으면 무지개 물고기가 생성돼도 바로 삭제
            if fishs[i].type == "Rainbow":
                if mackerel == False or Snooze == False:
                    del fishs[i]
                    i -= 1

                elif Cod == False or Bass == False:
                    del fishs[i]
                    i -= 1
                
                elif Bigmouse_Bass == False or Bluegill == False:
                    del fishs[i]
                    i -= 1
                
                elif Piranha == False or Silverfish == False:
                    del fishs[i]
                    i -= 1

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
                    self.Cod_count += 1
                    Cod = True
                    

                if fishs[i].type == "Silverfish":
                    self.Silverfish_count += 1
                    Silverfish = True
                    

                if fishs[i].type == "Bluegill":
                    self.Bluegill_count += 1
                    Bluegill = True
                    

                if fishs[i].type == "Bass":
                    self.Bass_count += 1
                    Bass = True
                    

                if fishs[i].type == "Bigmouse_Bass":
                    self.Bigmouse_Bass_count += 1
                    Bigmouse_Bass = True
                    

                if fishs[i].type == "Piranha":
                    self.Piranha_count += 1
                    Piranha = True
                    

                if fishs[i].type == "Rainbow":
                    self.Rainbow_count += 1
                    Rainbow = True
                
                limit = True

            if fishs[i].isCatched == 1:
                fishs[i].x = boy.hook_x - 50
                fishs[i].y = boy.hook_y
                fishs[i].isCatched = 1
                
            if(fishs[i].y == 250):
                ### 물고기 처음 잡았을 때 도감 띄워주는거 ###

                if fishs[i].type == "mackerel" and self.mackerel_count == 1:
                    mackerel_fanfare_sound = pygame.mixer.Sound('sounds/고등어_잡았다.wav')
                    mackerel_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_mackerel_window_image, (307, 35))
                        pygame.display.update()

                if fishs[i].type == "Snooze" and self.Snooze_count == 1:
                    Snooze_fanfare_sound = pygame.mixer.Sound('sounds/도루묵_잡았다.wav')
                    Snooze_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Snooze_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Cod" and self.Cod_count == 1:
                    Cod_fanfare_sound = pygame.mixer.Sound('sounds/대구_잡았다.wav')
                    Cod_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Cod_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Silverfish" and self.Silverfish_count == 1:
                    Silverfish_fanfare_sound = pygame.mixer.Sound('sounds/갈치_잡았다.wav')
                    Silverfish_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Silverfish_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Bluegill" and self.Bluegill_count == 1:
                    Bluegill_fanfare_sound = pygame.mixer.Sound('sounds/블루길_잡았다.wav')
                    Bluegill_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Bluegill_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Bass" and self.Bass_count == 1:
                    Bass_fanfare_sound = pygame.mixer.Sound('sounds/배스_잡았다.wav')
                    Bass_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Bass_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Bigmouse_Bass" and self.Bigmouse_Bass_count == 1:
                    Bigmouse_Bass_fanfare_sound = pygame.mixer.Sound('sounds/큰입배스_잡았다.wav')
                    Bigmouse_Bass_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Bigmouse_Bass_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Piranha" and self.Piranha_count == 1:
                    Piranha_fanfare_sound = pygame.mixer.Sound('sounds/피라냐_잡았다.wav')
                    Piranha_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 5):
                        screen.blit(first_catch_Piranha_window_image, (307, 35))
                        pygame.display.update()
                    

                if fishs[i].type == "Rainbow" and self.Rainbow_count == 1:
                    rainbow_fanfare_sound = pygame.mixer.Sound('sounds/무지개_잡았다.wav')
                    rainbow_fanfare_sound.play(0) #음악 반복 재생

                    window_start_time = time.time()
                    while (time.time() - window_start_time <= 9):
                        screen.blit(first_catch_Rainbow_window_image, (307, 35))
                        pygame.display.update()
                
                ### 창 띄워주고, 낚싯대가 다 올라갔으면 그 해당 물고기 삭제 ###
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

    def Isending(self):
        if self.Rainbow_count >= 1: # 무지개 물고기가 잡히면 엔딩 버튼 활성화
            Button(game_ending_button_image,0,0,'ending')
            pygame.display.update()
            return True
        else:
            return False