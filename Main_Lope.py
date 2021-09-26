# 라이브러리, 메소드 불러오기
import pygame
from Game_Sources import*
from Game_Stages import*

# 파이게임 초기화
pygame.init()

# 이벤트 루프
running = True # running이 참일때 게임은 실행중

while running:
    for event in pygame.event.get():
        screen.blit(home_screen_image, (0, 0))
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        pygame.display.update()

# pygame 종료
pygame.quit()