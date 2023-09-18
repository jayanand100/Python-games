import pygame
pygame.init()

height, width = 500, 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping pong")

fps = 60
white = (255,255,255)
black = (0,0,0)

paddle_wdt, paddle_ht = 20, 100
ball_radius = 7

score_font = pygame.font.SysFont("comicsans", 50)
win_score = 10

class paddle:
    colour = white
    velocity = 4


    def __init__(self, x, y, width, height):
        self.x = self.og_x = x
        self.y = self.og_y = y
        self.width = width
        self.height = height

    def draw_paddle(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

    def move(self, up = True):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def reset(self):
        self.x = self.og_x
        self.y = self.og_y

class Ball:
    max_vel = 6
    colour = white

    def __init__(self, x, y, radius):
        self.x = self.og_x = x
        self.y = self.og_y = y
        self.radius = radius
        self.x_vel = self.max_vel
        self.y_vel = 0
    def draw(self, window):
        pygame.draw.circle(window, self.colour,(self.x, self.y), self.radius)
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.og_x
        self.y = self.og_y
        self.y_vel = 0
        self.x_vel *= -1

def draw(win, paddles, ball, left_score, right_score):
    win.fill(black)

    left_score_txt = score_font.render(f"{left_score}", 1, white)
    right_score_txt = score_font.render(f"{right_score}", 1, white)
    win.blit(left_score_txt, (width//4 - left_score_txt.get_width()//2, 20))
    win.blit(right_score_txt, (width *(3/4) - right_score_txt.get_width() // 2, 20))


    for paddle in paddles:
        paddle.draw_paddle(window)

    for i in range(10,height, height//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, white, (width//2 - 5, i, 10, height//20))

    ball.draw(win)
    pygame.display.update()

def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= height:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / Ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / Ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel



def handle_paddle_movmnt(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.velocity + left_paddle.height <= height:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]and right_paddle.y + right_paddle.velocity + right_paddle.height <= height:
        right_paddle.move(up=False)

def main():
    run = True
    clock_speed = pygame.time.Clock()

    left_paddle = paddle(10, height // 2 - paddle_ht // 2, paddle_wdt, paddle_ht)
    right_paddle = paddle(width - 10 - paddle_wdt, height // 2 - paddle_ht // 2, paddle_wdt, paddle_ht)

    the_ball = Ball(width//2,height//2, ball_radius)

    left_score = 0
    right_score = 0

    while run:
        clock_speed.tick(fps)
        draw(window, [left_paddle, right_paddle],the_ball, left_score, right_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movmnt(keys, left_paddle, right_paddle)

        the_ball.move()
        handle_collision(the_ball, left_paddle, right_paddle)

        if the_ball.x < 0:
            right_score += 1
            the_ball.reset()
        elif the_ball.x > width:
            left_score += 1
            the_ball.reset()

        won = False

        if left_score >= win_score:
            won =True
            win_txt = "Left won"
        elif right_score >= win_score:
            won = True
            win_txt = "Right won"
        if won:
            text = score_font.render(win_txt, 1, white)
            window.blit(text,(width//2 - text.get_width()//2, height//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            the_ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()

main()
