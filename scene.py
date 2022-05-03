import os
from collections import Iterable
import pygame
import pygame.sprite
import pygame.image
import pygame.transform
import pygame.time
from elements import enemy, fighter
import utils
from utils import path_cal,PointList_tran,transgress_xy
import yaml


with open("config.yml",'r')as f:
    CONIFG = yaml.load(f,yaml.SafeLoader)
    ICON_CONFIG = CONIFG['icon']
    GAME_SCREEN = CONIFG['setting']['gamescreen_size']




# 警告标志
class warn_mark(pygame.sprite.Sprite):
    def __init__(self,myscreen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.screen = myscreen
        self.size = (20,20)
        self.pos = pos
        self.image_ad = os.path.join(ICON_CONFIG['path'],ICON_CONFIG['warn'])
        self.image = pygame.transform.scale(pygame.image.load(self.image_ad),self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos # 摆放位置
        self.time = pygame.time.get_ticks()
        self.i = 0
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def change_size(self):
        if self.size == (20,20):
            self.size = (15,15)
            self.image = pygame.transform.scale(pygame.image.load(self.image_ad),self.size)
            self.rect.topleft = self.pos
        else:
            self.size = (20,20)
            self.image = pygame.transform.scale(pygame.image.load(self.image_ad),self.size)
            self.rect.topleft = self.pos
    def update_time(self):
        self.time = pygame.time.get_ticks()
    def update(self):
        self.blitme()
        if pygame.time.get_ticks()-self.time > 300:
            self.change_size()
            self.i += 1
            self.update_time()
        if self.i > 5:
            self.kill()


# 场景函数
"""场景1:
在指定屏幕上生成N个型号为ID的敌机, 每架敌机只会在t0时刻向player发射一发速度为bullet_speed的
型号为bullet_ID的子弹, 发射方向为bullet_target ([0,0]为向下发射子弹，[1,1]为向玩家方向发射子弹，其他为向目标点发射)。
敌机的运动轨迹依次经过PointList=[(x1,y1),(x2,y2),...,(xn,yn)]个点，
运动速度大小恒为speed, 两架敌机的出现间隔为dt
"""
class scene1():
    def __init__(self,myscreen,t0,enemy_num,enemy_ID,bullet_speed,bullet_ID,speed,PointList,dt,bullet_target,
                 hook_global_info:utils.Info,hook_enemyfire_group:pygame.sprite.Group,
                 hook_player:fighter,hook_enemy_group:pygame.sprite.Group,
                 hook_background_group:pygame.sprite.Group,init_time:int):
        self.screen = myscreen
        self.N = enemy_num # 场景初始敌机数
        self.t0 =t0
        self.PointList = PointList
        self.enemy_group = pygame.sprite.Group() # 敌机群
        self.hook_global_info = hook_global_info
        self.hook_player = hook_player
        self.hook_enemy_group = hook_enemy_group
        self.hook_enemyfire_group = hook_enemyfire_group
        self.hook_background_group = hook_background_group
        self.dt = dt # 两架敌机的出现间隔（秒）
        self.isshooted = [0]*enemy_num # 记录下敌机是否已经开火 
        self.path,self.point,self.speed_dir = path_cal(PointList,speed)
        self.need_to_end = False
        self.started = False
        self.init_time = init_time   
        self.bullet_speed = bullet_speed
        self.bullet_ID = bullet_ID
        self.bullet_target = bullet_target
        self.speed = speed
        self.enemy_ID = enemy_ID
    def scene_init(self): # 初始化场景，加入敌机，与__init__()区别开，节省内存开支
        for i in range(self.N):
            enemy0 = enemy(self.screen,self.enemy_ID,self.PointList[0],self.speed,(0,-1),self.bullet_speed,self.bullet_ID,
                           self.hook_global_info,self.hook_enemy_group,self.hook_enemyfire_group,self.hook_background_group)
            enemy0.data = [0,0,len(self.path),i] 
            '''
            data[0]:敌机目前处在的最小分段点
            data[1]:敌机目前处于的关键点（用于确定速度分量）
            data[2]:敌机总共需要经过的最小分段点
            data[3]:敌机的序号, 防止kill()方法打乱顺序
            '''
            enemy0.rotate(self.speed_dir[enemy0.data[1]])
            self.enemy_group.add(enemy0) # 场景中加入该敌机
            self.hook_enemy_group.add(enemy0) # 总敌机群加入该敌机
            # 第一个点是敌机出现的初始位置
    def update_time(self):
        self.init_time = pygame.time.get_ticks()
    def update(self):
        # 第一次进入时更新该类时间
        if self.started == False:
            self.started = True
            self.scene_init()
            rect0 = pygame.Rect(0,0,20,20)
            rect0.topleft = self.PointList[0]
            warning0 = warn_mark(self.screen,transgress_xy(rect0))
            self.hook_background_group.add(warning0)
            self.update_time()
        # 判断场景中的敌人是否该移动/删除
        for enemy0 in self.enemy_group.sprites():
            assert isinstance(enemy0,enemy), "Class must be enemy!"
            if not enemy0.need_to_remove:
                enemy0.update_time()
                if enemy0.time - self.init_time > (enemy0.data[3]+1)*self.dt*1000:
                    enemy0.need_to_move = True
                if enemy0.data[0] >= enemy0.data[2] - 1:
                    enemy0.need_to_remove = True
        # 对场景中的敌人进行移动
        for enemy0 in self.enemy_group.sprites():
            assert isinstance(enemy0,enemy), "Class must be enemy!"
            if enemy0.need_to_move and not enemy0.need_to_remove:
                enemy0.data[0] += 1
                if enemy0.data[0] > self.point[enemy0.data[1]]:
                    enemy0.data[1] += 1
                    enemy0.rotate(self.speed_dir[enemy0.data[1]])
                enemy0.move_to(self.path[enemy0.data[0]])
                if self.t0: # 当t0=0或None时不发射子弹
                    if enemy0.time-self.init_time>self.t0*1000+(enemy0.data[3]+1)*self.dt*1000 and not enemy0.shooted:
                        if self.bullet_target == [1,1]:  # shoot at player
                            enemy0.orientated_shoot((self.hook_player.rect.centerx,self.hook_player.rect.centery))
                        elif self.bullet_target == [0,0]:  # shoot at speed direction
                            enemy0.default_shoot()
                        else:  # shoot at target position
                            target_position = (GAME_SCREEN[0]*self.bullet_target[0],GAME_SCREEN[1]*self.bullet_target[1])
                            enemy0.orientated_shoot(target_position)
                        enemy0.shooted = True
        # 所有敌人都需删除，场景删除所有敌人并不再更新
        flag = True
        for enemy0 in self.enemy_group.sprites():
            assert isinstance(enemy0,enemy), "Class must be enemy!"
            flag = flag and enemy0.need_to_remove
        self.need_to_end = flag
        if self.need_to_end:
            self.end()
    def end(self):
        for sprite in self.enemy_group.sprites():
            sprite.kill()
    @staticmethod
    def create(cls_info:dict,scene_list:list,scene_time:list,background:pygame.Surface,
               hook_player:fighter,hook_global_info:utils.Info,
               hook_enemy_group:pygame.sprite.Group,
               hook_enemyfire_group:pygame.sprite.Group,
               hook_background_group:pygame.sprite.Group,
               init_time=pygame.time.get_ticks()):
        assert cls_info['type'] == 'scene1', "types of scene_info and scene dont't fit"
        scene = scene1(myscreen=background,
                       t0=cls_info['bullet_time'],
                       enemy_num=cls_info['enemy_num'],
                       enemy_ID=cls_info['enemy_id'],
                       bullet_speed=cls_info['bullet_speed'],
                       bullet_target=cls_info['bullet_target'],
                       bullet_ID=cls_info['enemy_fire_id'],
                       speed=cls_info['enemy_speed'],
                       PointList=PointList_tran(cls_info['point_list']),
                       dt=cls_info['dt'],
                       hook_global_info=hook_global_info,
                       hook_enemy_group=hook_enemy_group,
                       hook_enemyfire_group=hook_enemyfire_group,
                       hook_player=hook_player,
                       hook_background_group=hook_background_group,
                       init_time=init_time)
        scene_list.append(scene)
        scene_time.append(cls_info['scene_time'])