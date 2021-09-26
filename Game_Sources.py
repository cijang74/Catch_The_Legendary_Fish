import pygame

# 게임 타이틀 설정
pygame.display.set_caption("Fishing_Life")

# FPS
clock = pygame.time.Clock()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 각종 이미지 불러오기
home_screen_image = pygame.image.load("images/Home_Screen.png").convert() # 게임 메인 화면
game_description = pygame.image.load("images/Game_Description.png").convert() # 게임 설명 화면
game_description_button = pygame.image.load("images/Game_Description_Button.png").convert() # 게임 설명 버튼
start_button = pygame.image.load("images/Start_Button.png").convert() # 게임 시작 버튼