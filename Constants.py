import ctypes

FPS = 60
dvy = 1.6
resistance_k = 0.02  # Сопротивление при полёте
bounce_k = 0.8  # "Сопротивление" при отскоке
num_targets = 2

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
colors = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

user32 = ctypes.windll.user32
WIDTH = user32.GetSystemMetrics(0)
HEIGHT = user32.GetSystemMetrics(1) - 55