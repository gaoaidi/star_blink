from star import Star
from random import randint
import pygame
import sys
from settings import Settings

class StarBlink:
    """创建一个星星闪烁的类"""
    def __init__(self):
        # 初始化各项数据
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Star Blink")

        self.stars=pygame.sprite.Group()
        self._stars_group()

    def _stars_group(self):
        star=Star(self)
        star_width,star_height=star.rect.size
        available_space_X=self.settings.screen_width-2*star_width
        number_star_x=available_space_X//(2*star_width)
        available_space_y=self.settings.screen_height-2*star_height
        row_number=available_space_y//(2*star_height)
        print(self.settings.screen_width)
        print(star_width)
        for row in range(row_number):
            for number in range(number_star_x+1):
                self._create_star(row,number)
        
    def _create_star(self,row,number):
        star=Star(self)
        star_width,star_height=star.rect.size
        star.rect.x=star_width+2*star_width*number
        star.rect.y=star_height+2*star_height*row
        self.stars.add(star)

    def run(self):
        while True:
            self._check_events()
            # self._star_update()
            self._screen_update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    sys.exit()
    
    def _screen_update(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self._draw_stars()
        pygame.display.update()

    def _draw_stars(self):
        random_stars=pygame.sprite.Group()
        for star in self.stars:
            if randint(0,1)==1:
                random_stars.add(star)
        print(len(random_stars))
        random_stars.draw(self.screen)

if __name__=="__main__":
    stb=StarBlink()
    stb.run()