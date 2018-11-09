import pygame
from plane_sprites import *


# 游戏的初始化
pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (200, 500))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(170, 300, 102, 126)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


# 游戏循环 -> 意味着游戏正式开始！
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 判断用户监听是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # qiut 卸载所有模块
            pygame.quit()
            # exit（）直接终止当前正在执行的程序
            exit()

    # # 捕获事件
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3. 调用 blit 方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)


    # 让精灵组调用两个方法
    # update
    enemy_group.update()

    # draw
    enemy_group.draw(screen)

    # 4. 调用update方法显示图像
    pygame.display.update()


pygame.quit()
