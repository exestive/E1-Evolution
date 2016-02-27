import pygame

def text_to_screen(screen, text, x, y, size = 15,
                   color =(255,255,255), font_type = "FreeSans"):
    try:
        text = str(text)
        font = pygame.font.SysFont('/E1 game /project 2/FreeSans.ttf', size)
        text = font.render(text, True, color)
        screen.blit(text,(x,y))

    except Exception:
        print('font error')

                    
