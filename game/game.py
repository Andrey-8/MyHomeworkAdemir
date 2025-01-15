from difflib import restore

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'ping-pong'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.1)
        self.change_x = 4
        self.change_y = 4

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -1.5 * self.change_y
            if self.change_y >= 100:
                self.change_y = 5






class Raketka(arcade.Sprite):
    def __init__(self):
        super().__init__('raketka.png', 0.15)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0




class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.raketka = Raketka()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.raketka.center_x = SCREEN_WIDTH / 2
        self.raketka.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2


    def on_draw(self): # отрисовка элементов в окне
        self.clear((255, 255, 255))
        self.raketka.draw()
        self.ball.draw()

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.raketka, self.ball):
            self.ball.change_y = -self.ball.change_y

        self.ball.update()
        self.raketka.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.raketka.change_x = 10
        if key == arcade.key.LEFT:
            self.raketka.change_x = -10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.raketka.change_x = 0





if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()