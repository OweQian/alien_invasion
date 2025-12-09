import sys
import pygame

from settings import Settings

class AlienInvasion:
  
  def __init__(self):
    """初始化游戏并创建游戏资源"""
    pygame.init()
    self.settings = Settings()
    # 创建时钟对象
    self.clock = pygame.time.Clock()
    # 创建窗口，固定大小 1200x800
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    # 设置窗口标题
    pygame.display.set_caption(self.settings.caption)
    
  def run_game(self):
    """开始游戏的主循环"""
    while True:
      # 监听键盘和鼠标事件
      for event in pygame.event.get():
        # 响应窗口关闭事件
        if event.type == pygame.QUIT:
          sys.exit()
      # 填充背景颜色
      self.screen.fill(self.bg_color)    
      # 刷新屏幕内容    
      pygame.display.flip()
      # 设置帧率
      self.clock.tick(60)

"""启动游戏"""
if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()