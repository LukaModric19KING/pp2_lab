import pygame

pygame.init()
size = width, height = (400, 200)
screen = pygame.display.set_mode(size)
music_list = [
    '5sta Family - Я буду твоей малышкой.mp3',
    'Блестящие - Восточные сказки (feat. Arash).mp3',
    'Дима Билан - Невозможное Возможно.mp3'
]

c = 0
paused = False

# pict upload
play_icon = pygame.image.load('play.png')
pause_icon = pygame.image.load('pause.png')
next_icon = pygame.image.load('next.png')
prev_icon = pygame.image.load('prev.png')

# - the size of icons
icon_size = (40, 40)
play_icon = pygame.transform.scale(play_icon, icon_size)
pause_icon = pygame.transform.scale(pause_icon, icon_size)
next_icon = pygame.transform.scale(next_icon, icon_size)
prev_icon = pygame.transform.scale(prev_icon, icon_size)

# size of the buttons <-> position
play_rect = play_icon.get_rect(topleft=(180, 80))
pause_rect = pause_icon.get_rect(topleft=(180, 80))
next_rect = next_icon.get_rect(topleft=(240, 80))
prev_rect = prev_icon.get_rect(topleft=(120, 80))

pygame.mixer.music.load(music_list[c])
pygame.mixer.music.play()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                c += 1
                if c >= len(music_list):
                    c = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_list[c])
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_LEFT:
                c -= 1
                if c < 0:
                    c = len(music_list) - 1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_list[c])
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_SPACE:
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(pos):
                    if not paused:
                        pygame.mixer.music.pause()
                        paused = True
                    else:
                        pygame.mixer.music.unpause()
                        paused = False
                elif next_rect.collidepoint(pos):
                    c += 1
                    if c >= len(music_list):
                        c = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_list[c])
                    pygame.mixer.music.play(-1)
                elif prev_rect.collidepoint(pos):
                    c -= 1
                    if c < 0:
                        c = len(music_list) - 1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_list[c])
                    pygame.mixer.music.play(-1)

    screen.fill((255, 255, 255))
    if paused:
        screen.blit(play_icon, play_rect)
    else:
        screen.blit(pause_icon, pause_rect)
    screen.blit(next_icon, next_rect)
    screen.blit(prev_icon, prev_rect)
    pygame.display.flip()

pygame.quit()
