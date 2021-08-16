import pygame
from pygame.sprite import Sprite
class Star(Sprite):
    def __init__(self,stb):
        super().__init__()
        self.screen=stb.screen
        self.screen_rec=self.screen.get_rect()
        self.settings=stb.settings
        # 加载图像
        self.image=pygame.transform.scale(
            pygame.image.load("images/star.bmp"),(80,80))
        self.rect=self.image.get_rect()
        # 设置星星于屏幕左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        # 更精确的表示xy坐标
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    
