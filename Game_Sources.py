import pygame

# 게임 타이틀 설정
pygame.display.set_caption("Catch_The_Legendary_Fish")

# FPS
clock = pygame.time.Clock()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 각종 이미지 불러오기
home_screen_image = pygame.image.load("images/Home_Screen.png").convert() # 게임 메인 화면 이미지
game_description_image = pygame.image.load("images/Game_Description.png").convert() # 게임 설명 화면 이미지
fish_book_image = pygame.image.load("images/Fish_Book_Screen.png").convert() # 물고기 도감 화면 이미지
game_background_image = pygame.image.load("images/Game_Background.png").convert() # 물고기 도감 화면 이미지

start_button_image = pygame.image.load("images/Start_Button.png").convert() # 게임 시작 버튼 이미지
start_button_rect = start_button_image.get_rect() # 게임 시작 버튼의 좌표값

game_description_button_image = pygame.image.load("images/Game_Description_Button.png").convert() # 게임 설명 버튼 이미지
game_description_button_rect = game_description_button_image.get_rect() # 게임 설명 버튼의 좌표값

fish_book_button_image = pygame.image.load("images/Fish_Book_Button.png").convert() # 물고기 도감 버튼 이미지
fish_book_button_rect = fish_book_button_image.get_rect() # 물고기 도감 버튼의 좌표값

return_button_image = pygame.image.load("images/Return_Button.png").convert() # 돌아가기 버튼 이미지
return_button_rect = return_button_image.get_rect() # 돌아가기 버튼의 좌표값

# 게임 내 사용될 변수들
stage = 0