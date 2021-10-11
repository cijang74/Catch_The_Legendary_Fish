import pygame
from Game_Sources import*

class Boy:
    def __init__(self):
        ## 소년 관련 변수 ##
        self.boy_x = 100
        self.boy_y = 100
        self.boy_dx = 0 # 원래 변수명: boy_x_change
        self.boy_speed = 0.5

        ## 갈고리 관련 변수 ##
        self.isHookDown = 0
        self.isHookUp = 1
        
        self.hook_width = 15
        self.hook_height = 30

        self.hook_x = self.boy_x + self.boy_width - self.hook_width
        self.hook_y = self.boy_y + self.boy_height
        self.hook_dy = 0
        self.hook_speed = 0.2

        hook_rect.left = self.hook_x
        hook_rect.top = self.hook_y

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :   # 키보드 감지
                if event.key == pygame.K_LEFT and not(self.isHookDown) and self.isHookUp : # 주인공 이동
                    self.boy_dx -= self.boy_speed
                elif event.key == pygame.K_RIGHT and not(self.isHookDown) and self.isHookUp :
                    self.boy_dx += self.boy_speed
                elif event.key == pygame.K_DOWN and self.isHookUp :# 낚시바늘 내리기
                    if not(self.isHookDown) :
                        self.hook_dy += self.hook_speed
                    self.isHookDown = 1
                    self.isHookUp = 0

            if event.type == pygame.KEYUP :     # 키보드 손 땠나
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    self.boy_dx = 0

        # 주인공 위치 정의
        self.boy_x += self.boy_dx  # dt: 프레임 변화에 따른 이동 속도 변화 보정
        self.hook_x = self.boy_x + self.boy_width - self.hook_width
        self.hook_y += self.hook_dy
        # 가로 경계값 처리 - 주인공
        if self.boy_x < 0 :
            self.boy_x = 0
            self.hook_x = self.boy_x + self.boy_width - self.hook_width
        elif self.boy_x > screen_width - self.boy_width :
            self.boy_x = screen_width - self.boy_width
            self.hook_x = self.boy_x + self.boy_width - self.hook_width

    def draw(self):
        screen.blit(boy_image, (self.boy_x, self.boy_y))
        screen.blit(hook_image, (self.hook_x, self.hook_y))

        pygame.draw.line(screen, (0, 0, 0), [self.boy_x + self.boy_width - 1, self.boy_y + self.boy_height], [self.hook_x + self.hook_width - 1, self.hook_y], 1)

boy = Boy() # boy 객체 생성