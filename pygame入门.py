import pygame

# pygame.init()
#
# # 编写游戏代码
# print("游戏的代码...")
#
# pygame.quit()

hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)