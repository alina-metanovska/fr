from pygame import *
import random

WIDTH, HEIGHT = 800, 600

init()

screen = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption("Пінг-Понг Single Player")

font_main = font.Font(None, 36)
font_win = font.Font(None, 72)

player_y = HEIGHT // 2 - 50
ai_y = HEIGHT // 2 - 50

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5 * random.choice([-1, 1])
ball_dy = 4 * random.choice([-1, 1])
ball_r = 10

score_player = 0
score_ai = 0

running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    keys = key.get_pressed()
    if keys[K_w]:
        player_y -= 6
    if keys[K_s]:
        player_y += 6

    player_y = max(0, min(HEIGHT - 100, player_y))

    if ai_y + 50 < ball_y:
        ai_y += 4
    elif ai_y + 50 > ball_y:
        ai_y -= 4

    ai_y = max(0, min(HEIGHT - 100, ai_y))

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy *= -1

    if 20 < ball_x < 40 and player_y < ball_y < player_y + 100:
        ball_dx *= -1

    if WIDTH - 40 < ball_x < WIDTH - 20 and ai_y < ball_y < ai_y + 100:
        ball_dx *= -1

    if ball_x < 0:
        score_ai += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2

    if ball_x > WIDTH:
        score_player += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2

    screen.fill((30, 30, 30))

    draw.rect(screen, (0, 255, 0), (20, player_y, 20, 100))
    draw.rect(screen, (255, 0, 255), (WIDTH - 40, ai_y, 20, 100))

    draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_r)

    score = font_main.render(f"{score_player} : {score_ai}", True, (255, 255, 255))
    screen.blit(score, (WIDTH // 2 - 30, 20))

    display.update()
    clock.tick(60)

quit()