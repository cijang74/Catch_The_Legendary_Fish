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
        if pygame.mouse.get_pressed()[0] and start_button_rect.collidepoint(pygame.mouse.get_pos()):
            start_time = time.time()
            stage += 1
        elif pygame.mouse.get_pressed()[0] and game_description_button_rect.collidepoint(pygame.mouse.get_pos()):
            stage -= 1

    if stage == -1: # 설명탭 스테이지 값: -1
        Map.descriptionscreen()
        if pygame.mouse.get_pressed()[0] and start_button_rect.collidepoint(pygame.mouse.get_pos()):
            start_time = time.time()
            stage = 1

    if stage == 1: # 게임이 진행되는 스테이지 값: 1
        Map.backgroundscreen(fishs,start_time,pressed_keys)
        if pygame.mouse.get_pressed()[0] and fish_book_button_rect.collidepoint(pygame.mouse.get_pos()):
            stage = 999

        if pygame.mouse.get_pressed()[0] and game_end_button_rect.collidepoint(pygame.mouse.get_pos()):
            running = False # 이것도 논의. 종료 누르면 타이틀로 가게 할 건지? 아니면 바로 게임을 종료시킬 것인지.
            
    if stage == 999: # 도감 화면 스테이지 값: 2
        Map.fishbookscreen()
        if pygame.mouse.get_pressed()[0] and return_button_rect.collidepoint(pygame.mouse.get_pos()):
            stage = 1   

    pygame.display.update() # 루프 내에서 발생한 모든 이미지 변화를 업데이트

# pygame 종료
pygame.time.delay(100)
pygame.quit()