# 라이브러리, 클래스 불러오기
import pygame,time

# 게임 타이틀 설정
pygame.display.set_caption("Catch!_The_Legendary_Fish")

# FPS
clock = pygame.time.Clock()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#각종 이미지, 렉트값 설정하기
### 스테이지, 버튼 이미지 ###
home_screen_image = pygame.image.load("images/Home_Screen.png").convert() # 게임 메인 화면 이미지
game_description_image = pygame.image.load("images/Game_Description.png").convert() # 게임 설명 화면 이미지
game_background_image = pygame.image.load("images/Game_Background.png").convert() # 게임 진행중일 때 뒷 배경 이미지

game_intro_1_image = pygame.image.load("images/Intro_1.png").convert() # 인트로 1 이미지
game_intro_2_image = pygame.image.load("images/Intro_2.png").convert() # 인트로 2 이미지
game_intro_3_image = pygame.image.load("images/Intro_3.png").convert() # 인트로 2 이미지
pause_screen_image = pygame.image.load("images/Pause_Screen.png").convert() # 일시정지 했을 때 뜨는 작은 화면
pause_screen_image.set_colorkey((85, 56, 30))

start_button_image = pygame.image.load("images/Start_Button.png").convert() # 게임 시작 버튼 이미지
start_button_rect = start_button_image.get_rect() # 게임 시작 버튼의 렉트값

game_description_button_image = pygame.image.load("images/Game_Description_Button.png").convert() # 게임 설명 버튼 이미지
game_description_button_rect = game_description_button_image.get_rect() # 게임 설명 버튼의 렉트값

fish_book_button_image = pygame.image.load("images/Fish_Book_Button.png").convert() # 물고기 도감 버튼 이미지
fish_book_button_rect = fish_book_button_image.get_rect() # 물고기 도감 버튼의 렉트값

return_button_image = pygame.image.load("images/Return_Button.png").convert() # 돌아가기 버튼 이미지
return_button_rect = return_button_image.get_rect() # 돌아가기 버튼의 렉트값

pause_button_image = pygame.image.load("images/Pause_Button.png").convert() # 일시정지 버튼 이미지
pause_button_rect = pause_button_image.get_rect() # 일시정지 버튼의 렉트값

countinue_button_image = pygame.image.load("images/Countinue_Button.png").convert() # 계속하기 버튼 이미지
countinue_button_rect = countinue_button_image.get_rect() # 계속하기 버튼의 렉트값

game_end_button_image = pygame.image.load("images/Game_End_Button.png").convert() # 게임 종료 버튼 이미지
game_end_button_rect = game_end_button_image.get_rect() # 게임 종료 버튼의 렉트값

close_button_imgae = pygame.image.load("images/Close_Button.png").convert() # 게임 종료 버튼 이미지
close_button_rect = close_button_imgae.get_rect() # 도감 창 끄는 버튼의 렉트값

### 도감에서 쓰여질 이미지 ###

# 물고기 도감 화면 이미지
fish_book_image = pygame.image.load("images/Fish_Book_Screen.png").convert()

# 잠으면 도감 화면에 띄울 물고기들 이미지
fish_book_mackerel_image = pygame.image.load("images/고등어_창_1.png").convert()
fish_book_Snooze_image = pygame.image.load("images/도루묵_창_1.png").convert()
fish_book_Cod_image = pygame.image.load("images/대구_창_1.png").convert()
fish_book_Silverfish_image = pygame.image.load("images/갈치_창_1.png").convert()
fish_book_Bluegill_image = pygame.image.load("images/블루길_창_1.png").convert()
fish_book_Bass_image = pygame.image.load("images/배스_창_1.png").convert()
fish_book_Bigmouse_Bass_image = pygame.image.load("images/큰입배스_창_1.png").convert()
fish_book_Piranha_image = pygame.image.load("images/피라냐_창_1.png").convert()
fish_book_Rainbow_image = pygame.image.load("images/무지개_창_1.png").convert()

### 처음 잡았을 때 띄워지는 창 이미지 ###
first_catch_mackerel_window_image = pygame.image.load("images/고등어_잡았다.png").convert()
first_catch_Snooze_window_image = pygame.image.load("images/도루묵_잡았다.png").convert()
first_catch_Cod_window_image = pygame.image.load("images/대구_잡았다.png").convert()
first_catch_Silverfish_window_image = pygame.image.load("images/갈치_잡았다.png").convert()
first_catch_Bluegill_window_image = pygame.image.load("images/블루길_잡았다.png").convert()
first_catch_Bass_window_image = pygame.image.load("images/배스_잡았다.png").convert()
first_catch_Bigmouse_Bass_window_image = pygame.image.load("images/큰입배스_잡았다.png").convert()
first_catch_Piranha_window_image = pygame.image.load("images/피라냐_잡았다.png").convert()
first_catch_Rainbow_window_image = pygame.image.load("images/무지개_잡았다.png").convert()

# 도감 물고기 버튼 이미지
fish_book_button_mackerel_image = pygame.image.load("images/고등어_버튼.png").convert()
fish_book_button_mackerel_rect = fish_book_button_mackerel_image.get_rect()

fish_book_button_Snooze_image = pygame.image.load("images/도루묵_버튼.png").convert()
fish_book_button_Snooze_rect = fish_book_button_Snooze_image.get_rect()

fish_book_button_Cod_image = pygame.image.load("images/대구_버튼.png").convert()
fish_book_button_Cod_rect = fish_book_button_Cod_image.get_rect()

fish_book_button_Silverfish_image = pygame.image.load("images/갈치_버튼.png").convert()
fish_book_button_Silverfish_rect = fish_book_button_Silverfish_image.get_rect()

fish_book_button_Bluegill_image = pygame.image.load("images/블루길_버튼.png").convert()
fish_book_button_Bluegill_rect = fish_book_button_Bluegill_image.get_rect()

fish_book_button_Bass_image = pygame.image.load("images/배스_버튼.png").convert()
fish_book_button_Bass_rect = fish_book_button_Bass_image.get_rect()

fish_book_button_Bigmouse_Bass_image = pygame.image.load("images/큰입배스_버튼.png").convert()
fish_book_button_Bigmouse_Bass_rect = fish_book_button_Bigmouse_Bass_image.get_rect()

fish_book_button_Piranha_image = pygame.image.load("images/피라냐_버튼.png").convert()
fish_book_button_Piranha_rect = fish_book_button_Piranha_image.get_rect()

fish_book_button_Rainbow_image = pygame.image.load("images/무지개_버튼.png").convert()
fish_book_button_Rainbow_rect = fish_book_button_Rainbow_image.get_rect()

# 도감 물고기 설명 창 이미지
fish_book_button_mackerel_discribe_image = pygame.image.load("images/고등어_설명.png").convert()
fish_book_button_Snooze_discribe_image = pygame.image.load("images/도루묵_설명.png").convert()
fish_book_button_Cod_discribe_image = pygame.image.load("images/대구_설명.png").convert()
fish_book_button_Silverfish_discribe_image = pygame.image.load("images/갈치_설명.png").convert()
fish_book_button_Bluegill_discribe_image = pygame.image.load("images/블루길_설명.png").convert()
fish_book_button_Bass_discribe_image = pygame.image.load("images/배스_설명.png").convert()
fish_book_button_Bigmouse_Bass_discribe_image = pygame.image.load("images/큰입배스_설명.png").convert()
fish_book_button_Piranha_discribe_image = pygame.image.load("images/피라냐_설명.png").convert()
fish_book_button_Rainbow_discribe_image = pygame.image.load("images/무지개_설명.png").convert()

### 플레이어(소년) 관련 이미지 ###
boyR_stay_image = pygame.image.load("images/characterR_stay.png")
boyL_stay_image = pygame.image.load("images/characterL_stay.png")
boyR_fishing_image = pygame.image.load("images/characterR_fishing.png")
boyL_fishing_image = pygame.image.load("images/characterL_fishing.png")
boyR_stay_image = pygame.transform.scale(boyR_stay_image, (140, 140)) # 이미지 스케일 변환
boyL_stay_image = pygame.transform.scale(boyL_stay_image, (140, 140))
boyR_fishing_image = pygame.transform.scale(boyR_fishing_image, (140, 140))
boyL_fishing_image = pygame.transform.scale(boyL_fishing_image, (140, 140))

### 낚시바늘 ###
hookR_image = pygame.image.load("images/hookR.png")
hookL_image = pygame.image.load("images/hookL.png")
hookR_image = pygame.transform.scale(hookR_image, (15, 30))
hookL_image = pygame.transform.scale(hookL_image, (15, 30))

### 물고기들 이미지 ###
fish_mackerel_image = pygame.image.load("images/Fish_Mackerel.png").convert() # 고등어 이미지
fish_mackerel_image.set_colorkey((255, 255, 255))
fish_mackerel_image = pygame.transform.scale(fish_mackerel_image, (128, 72))
fish_mackerel_rect = fish_mackerel_image.get_rect() # 고등어의 렉트값

fish_silverfish_image = pygame.image.load("images/Fish_Silverfish.png").convert() # 은갈치 이미지
fish_silverfish_image.set_colorkey((255, 255, 255))
fish_silverfish_image = pygame.transform.scale(fish_silverfish_image, (128, 72))
fish_silverfish_rect = fish_silverfish_image.get_rect() # 은갈치의 렉트값

fish_snooze_image = pygame.image.load("images/Fish_Snooze.png").convert() # 도루묵 이미지
fish_snooze_image.set_colorkey((255, 255, 255))
fish_snooze_image = pygame.transform.scale(fish_snooze_image, (128, 72))
fish_snooze_rect = fish_silverfish_image.get_rect() # 도루묵의 렉트값

fish_cod_image = pygame.image.load("images/Fish_Cod.png").convert() # 대구 이미지
fish_cod_image.set_colorkey((255, 255, 255))
fish_cod_image = pygame.transform.scale(fish_cod_image, (128, 72))
fish_cod_rect = fish_cod_image.get_rect() # 대구의 렉트값

fish_bass_image = pygame.image.load("images/Fish_Bass.png").convert() # 배스 이미지
fish_bass_image.set_colorkey((255, 255, 255))
fish_bass_image = pygame.transform.scale(fish_bass_image, (128, 72))
fish_bass_rect = fish_bass_image.get_rect() # 배스의 렉트값

fish_bluegill_image = pygame.image.load("images/Fish_Bluegill.png").convert() # 블루길 이미지
fish_bluegill_image.set_colorkey((255, 255, 255))
fish_bluegill_image = pygame.transform.scale(fish_bluegill_image, (128, 72))
fish_bluegill_rect = fish_bluegill_image.get_rect() # 블루길의 렉트값

fish_bigmouse_bass_image = pygame.image.load("images/Fish_Bigmouse_Bass.png").convert() # 큰입배스 이미지
fish_bigmouse_bass_image.set_colorkey((255, 255, 255))
fish_bigmouse_bass_image = pygame.transform.scale(fish_bigmouse_bass_image, (128, 72))
fish_bigmouse_bass_rect = fish_bigmouse_bass_image.get_rect() # 큰입배스의 렉트값

fish_piranha_image = pygame.image.load("images/Fish_Piranha.png").convert() # 피라냐 이미지
fish_piranha_image.set_colorkey((255, 255, 255))
fish_piranha_image = pygame.transform.scale(fish_piranha_image, (128, 72))
fish_piranha_rect = fish_piranha_image.get_rect() # 피라냐의 렉트값

fish_rainbow_image = pygame.image.load("images/Fish_Rainbow.png").convert() # 무지개 물고기 이미지
fish_rainbow_image.set_colorkey((255, 255, 255))
fish_rainbow_image = pygame.transform.scale(fish_rainbow_image, (128, 72))
fish_rainbow_rect = fish_rainbow_image.get_rect() # 무지개 물고기의 렉트값

### 쓰레기들 이미지 ###
trash_can_image = pygame.image.load("images/Trash_Can.png").convert() # 쓰레기-캔 이미지
trash_can_image.set_colorkey((255, 255, 255))
trash_can_image = pygame.transform.scale(trash_can_image, (128, 72))
trash_can_rect = trash_can_image.get_rect() # 쓰래기-캔의 렉트값

trash_strow_image = pygame.image.load("images/Trash_Strow.png").convert() # 쓰레기-빨대 이미지
trash_strow_image.set_colorkey((255, 255, 255))
trash_strow_image = pygame.transform.scale(trash_strow_image, (128, 72))
trash_strow_rect = trash_strow_image.get_rect() # 쓰래기-빨대의 렉트값

### 전역변수 ###

# 게임 내 사용될 변수들
stage = 0
last_fish_spawn_time = 0
fishs = []
pause = False
limit = False
stop = 0

# 음악 관련 변수들
count_o = 0
count_s = 0
count_t = 0

# 물고기 도감 관련해서 쓸 변수들
mackerel = False
Snooze = False
Cod = False
Silverfish = False
Bluegill = False
Bass = False
Bigmouse_Bass = False
Piranha = False
Rainbow = False

mackerel_Book = False
Snooze_Book = False
Cod_Book = False
Silverfish_Book = False
Bluegill_Book = False
Bass_Book = False
Bigmouse_Bass_Book = False
Piranha_Book = False
Rainbow_Book = False