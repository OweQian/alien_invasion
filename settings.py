class Settings:
  """存储游戏《外星人入侵》中所有设置的类"""
  
  def __init__(self, screen_width=1200, screen_height=800, caption='Alien Invasion', bg_color=(230, 230, 230)):
    """初始化游戏的静态设置"""
    # 屏幕设置
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.caption = caption
    self.bg_color = bg_color
    # 飞船速度
    self.ship_speed = 1.5