# 라이브러리, 클래스 불러오기
import pygame
from Game_Sources import*
from Game_Stages import*
from Game_Fishs import*

# 파이게임 초기화
pygame.init()
Map = Stages()

# 이벤트 루프
running = True # running이 참일때 게임은 실행중

while running:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        
    if stage == 0: # 메인탭 스테이지 값: 0
        Map.homescreen()
        if count_t == 0:
            title_music = pygame.mixer.Sound('sounds/타이틀.wav')
            title_music.play(-1) #음악 반복 재생
        count_t += 1

        if pygame.mouse.get_pressed()[0] and start_button_rect.collidepoint(pygame.mouse.get_pos()):
            start_button_sound = pygame.mixer.Sound('sounds/버튼_게임 스타트.wav')
            start_button_sound.play(0) #음악 반복 재생
            start_time = time.time()
            stage += 1
            title_music.stop()

        elif pygame.mouse.get_pressed()[0] and game_description_button_rect.collidepoint(pygame.mouse.get_pos()):
            discribe_button_sound = pygame.mixer.Sound('sounds/버튼_게임 설명.wav')
            discribe_button_sound.play(0) #음악 반복 재생
            stage -= 1

    if stage == -1: # 설명탭 스테이지 값: -1
        Map.descriptionscreen()
        if pygame.mouse.get_pressed()[0] and start_button_rect.collidepoint(pygame.mouse.get_pos()):
            start_button_sound = pygame.mixer.Sound('sounds/버튼_게임 스타트.wav')
            start_button_sound.play(0) #음악 반복 재생
            start_time = time.time()
            stage = 1
            title_music.stop()

    if stage == 1: # 게임이 진행되는 스테이지 값: 1
        Map.backgroundscreen(fishs,start_time,pressed_keys)
        if pygame.mouse.get_pressed()[0] and fish_book_button_rect.collidepoint(pygame.mouse.get_pos()):
            normal_button_sound = pygame.mixer.Sound('sounds/버튼_대부분의 버튼.wav')
            normal_button_sound.play(0) #음악 반복 재생
            print(Bluegill)
            stage = 999

        if pygame.mouse.get_pressed()[0] and game_end_button_rect.collidepoint(pygame.mouse.get_pos()):
            running = False # 이것도 논의. 종료 누르면 타이틀로 가게 할 건지? 아니면 바로 게임을 종료시킬 것인지.
            
    if stage == 999: # 도감 화면 스테이지 값: 2
        Map.fishbookscreen()

        ### 버튼 이벤트 리스너 ###

        # 뒤로가기 버튼을 눌렀을 때
        if pygame.mouse.get_pressed()[0] and return_button_rect.collidepoint(pygame.mouse.get_pos()):
            weak_button_sound = pygame.mixer.Sound('sounds/버튼_힘없음.wav')
            weak_button_sound.play(0) #음악 반복 재생
            stage = 1
            Snooze_Book = False

        # 각 물고기 설명 버튼을 눌렀을 때

        if pygame.mouse.get_pressed()[0] and fish_book_button_Snooze_rect.collidepoint(pygame.mouse.get_pos()):
            Snooze_Book = True

        if Snooze_Book == True:
            screen.blit(fish_book_button_Snooze_discribe_image, (188, 58))

            Button(close_button_imgae,1058,58,'close')

        if pygame.mouse.get_pressed()[0] and close_button_rect.collidepoint(pygame.mouse.get_pos()):
            Snooze_Book = False

    pygame.display.update() # 루프 내에서 발생한 모든 이미지 변화를 업데이트

# pygame 종료
pygame.time.delay(100)
pygame.quit()