import sys
import time
import pygame
from pygame.locals import *

def play_ball():
    
    pygame.init()
    
    #窗口大小
    window_size = (width, height) =(800, 600)
    
    #小球运行偏移量[水平，垂直]，值越大，移动越快
    a=1
    b=i=1
    
    speed = [a, b]
    
    
    #窗口背景色RGB值
    color_black = (0, 255, 0)
    
    #设置窗口模式
    screen = pygame.display.set_mode(window_size)
    
    #设置窗口标题
    pygame.display.set_caption('运动的小球')
    
    #加载小球图片
    
    ball_image = pygame.image.load('ball.jpg')
    ball_image1 = pygame.image.load('fly0.png')
    
    #获取小球图片的区域开状
    ball_rect = ball_image.get_rect()
    ball_rect = ball_image1.get_rect()
    screen.blit(ball_image1, ball_rect)

    
    
    while True:
        
        #退出事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #使小球移动，速度由speed变量控制
        ball_rect = ball_rect.move(speed)
        
        #当小球运动出窗口时，重新设置偏移量
        if (ball_rect.left < 0) or (ball_rect.right > width or ball_rect.top < 0) or (ball_rect.bottom > height):
            speed[0] =0
            speed[1] =0
        
            
        
        #填充窗口背景
        screen.fill(color_black)
        
        #在背景Surface上绘制 小球
        screen.blit(ball_image, ball_rect)
        
        
        #更新窗口内容
        pygame.display.update()
        
if __name__ == '__main__':
    
    play_ball()
   
    

