import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
  
  def __init__(self):
    """初始化游戏并创建游戏资源"""
    pygame.init()
    self.settings = Settings()
    # 创建时钟对象
    self.clock = pygame.time.Clock()
    # 创建全屏窗口
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    
    # 设置窗口标题
    pygame.display.set_caption(self.settings.caption)
    # 创建飞船实例
    self.ship = Ship(self)
    
  def _check_keydown_events(self, event):
    """响应按键按下事件"""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    # 响应退出游戏事件
    elif event.key == pygame.K_q:
      sys.exit()
  
  def _check_keyup_events(self, event):
    """响应按键松开事件"""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False
  
  def _check_events(self):
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
      # 响应窗口关闭事件
      if event.type == pygame.QUIT:
        sys.exit()
      # 响应键盘按下事件
      elif event.type == pygame.KEYDOWN:
        # 响应向右移动事件
        self._check_keydown_events(event)
      # 响应键盘松开事件
      elif event.type == pygame.KEYUP:
        # 响应向右移动松开事件
        self._check_keyup_events(event)
          
  def _update_screen(self):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 填充背景颜色
    self.screen.fill(self.settings.bg_color)
    # 绘制飞船
    self.ship.blitme()    
    # 刷新屏幕内容    
    pygame.display.flip()
    
  def run_game(self):
    """开始游戏的主循环"""
    while True:
      self._check_events()
      self.ship.update()
      self._update_screen()
      # 设置帧率
      self.clock.tick(60)

"""启动游戏"""
if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()