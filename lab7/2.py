import pygame

pygame.init()
size = width, hight = (400, 200)
screen = pygame.display.set_mode(size)
music_list = [
    '5sta Family - Я буду твоей малышкой.mp3',
    'Блестящие - Восточные сказки (feat. Arash).mp3',
    'Дима Билан - Невозможное Возможно.mp3'
]

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

c = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print('The song ended.')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            c += 1
            if c > len(music_list) - 1:
                c = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_list[c])
            pygame.mixer.music.play(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            c -= 1
            if c < 0:
                c = len(music_list) - 1
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_list[c])
            pygame.mixer.music.play(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            pygame.mixer.music.unpause()

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
