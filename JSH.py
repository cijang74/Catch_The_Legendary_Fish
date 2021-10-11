import pygame

pygame.init()

# FPS 객체 생성
clock = pygame.time.Clock()

# 화면 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch! The Legendary Fish")

# 배경 이미지
background = pygame.image.load("images/배경.png")

# 캐릭터 정보
boy = pygame.image.load("images/Character.png")
boy = pygame.transform.scale(boy, (140, 140)) # 이미지 스케일 변환

boy_width = 140
boy_height = 140

boy_x_pos = screen_width / 2 - boy_width / 2
boy_y_pos = screen_height / 4 - boy_height
boy_x_change = 0
boy_speed = 0.5

# 낚시바늘
isHookDown = 0
isHookUp = 1

hook = pygame.image.load("images/hook.png")
hook = pygame.transform.scale(hook, (15, 30))

hook_width = 15
hook_height = 30

hook_x_pos = boy_x_pos + boy_width - hook_width
hook_y_pos = boy_y_pos + boy_height
hook_y_change = 0
hook_speed = 0.2

# 물고기
isCatched = 0

fish = pygame.image.load("images/Fish.png")
fish = pygame.transform.scale(fish, (70, 30))

fish_width = 70
fish_height = 30

fish_x_pos = screen_width / 2 - fish_width / 2
fish_y_pos = screen_height * (3/4) - fish_height / 2
#fish_y_pos = screen_height / 2 - fish_height / 2

isRunning = True
while isRunning :
    dt = clock.tick(60)

# 이벤트 처리
    for event in pygame.event.get() :       # 사용자 입력 감지
        if event.type == pygame.QUIT :      # 창닫기 버튼
            isRunning = False

        if event.type == pygame.KEYDOWN :   # 키보드 감지
            if event.key == pygame.K_LEFT and not(isHookDown) and isHookUp : # 주인공 이동
                boy_x_change -= boy_speed
            elif event.key == pygame.K_RIGHT and not(isHookDown) and isHookUp :
                boy_x_change += boy_speed
            elif event.key == pygame.K_DOWN and isHookUp :# 낚시바늘 내리기
                if not(isHookDown) :
                    hook_y_change += hook_speed
                isHookDown = 1
                isHookUp = 0

        if event.type == pygame.KEYUP :     # 키보드 손 땠나
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                boy_x_change = 0

# 주인공 위치 정의
    boy_x_pos += boy_x_change * dt  # dt: 프레임 변화에 따른 이동 속도 변화 보정
    hook_x_pos = boy_x_pos + boy_width - hook_width
    hook_y_pos += hook_y_change * dt
    # 가로 경계값 처리 - 주인공
    if boy_x_pos < 0 :
        boy_x_pos = 0
        hook_x_pos = boy_x_pos + boy_width - hook_width
    elif boy_x_pos > screen_width - boy_width :
        boy_x_pos = screen_width - boy_width
        hook_x_pos = boy_x_pos + boy_width - hook_width
    # 세로 경계값 처리 - 낚시바늘
    # 다 올렸을 때
    if hook_y_pos < boy_y_pos + boy_height :
        if isCatched :
            isCatched = 0
            pygame.time.delay(500)
        hook_y_pos = boy_y_pos + boy_height
        hook_y_change = 0
        isHookUp = 1
        fish_x_pos = screen_width / 2 - fish_width / 2
        fish_y_pos = screen_height * (3/4) - fish_height / 2
        #fish_y_pos = screen_height / 2 - fish_height / 2
    # 낚시바늘 올리기
    elif hook_y_pos > screen_height - hook_height - 50 or isCatched :
        isHookDown = 0
        if hook_y_change >= 0 :
            hook_y_change -= hook_speed

# 충돌 처리
    # 낚시바늘 rect 정보
    hook_rect = hook.get_rect()
    hook_rect.left = hook_x_pos
    hook_rect.top = hook_y_pos
    # 물고기 rect 정보
    fish_rect = fish.get_rect()
    fish_rect.left = fish_x_pos
    fish_rect.top = fish_y_pos

    # 낚시바늘-물고기 충돌 체크
    if hook_rect.colliderect(fish_rect) :
        fish_x_pos = hook_x_pos + hook_width / 2 - fish_width / 2
        fish_y_pos = hook_y_pos + hook_height / 2 - fish_height / 2
        isCatched = 1

#화면에 그리기  
    # 배경
    screen.blit(background, (0, 0))
    
    # 내려가는 낚시줄
    pygame.draw.line(screen, (0, 0, 0), [boy_x_pos + boy_width - 1, boy_y_pos + boy_height], [hook_x_pos + hook_width - 1, hook_y_pos], 1)


    # 객체
    screen.blit(boy, (boy_x_pos, boy_y_pos))
    screen.blit(hook, (hook_x_pos, hook_y_pos))
    screen.blit(fish, (fish_x_pos, fish_y_pos))

# 업데이트
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
