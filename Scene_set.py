scenes = [dict(type='scene1',
               point_list=[[0.12, -0.06], [0.12, 0.01], [0.12, 0.09], [0.12, 0.17], [0.12, 0.23],\
                              [0.12, 0.28], [0.13, 0.32], [0.13, 0.37], [0.13, 0.4], [0.13, 0.45],\
                              [0.13, 0.49], [0.13, 0.53], [0.13, 0.57], [0.13, 0.56], [0.13, 0.52],\
                              [0.13, 0.48], [0.13, 0.46], [0.13, 0.5], [0.13, 0.54], [0.12, 0.58],\
                              [0.12, 0.62], [0.12, 0.67], [0.12, 0.73], [0.12, 0.78], [0.1, 0.84],\
                              [0.09, 0.91], [0.09, 0.95], [0.09, 1.0], [0.08, 1.03], [0.08, 1.09]],
               enemy_num=8,
               enemy_id='e13',
               enemy_fire_id=10,
               bullet_time=1.5,
               bullet_speed=3,
               bullet_target=[1,1],
               enemy_speed=3,
               dt=1.0,
               scene_time=1.0),
          dict(type='scene1',
               point_list=[[0.87, -0.07], [0.87, -0.02], [0.87, 0.04], [0.86, 0.1], [0.86, 0.15],
                           [0.86, 0.19], [0.86, 0.25], [0.86, 0.3], [0.86, 0.35], [0.86, 0.39],
                           [0.85, 0.43], [0.85, 0.48], [0.85, 0.52], [0.84, 0.56], [0.83, 0.52],
                           [0.84, 0.49], [0.85, 0.45], [0.86, 0.47], [0.86, 0.52], [0.86, 0.56],
                           [0.86, 0.61], [0.86, 0.66], [0.86, 0.72], [0.86, 0.78], [0.86, 0.83], [0.86, 0.88], [0.86, 0.95], [0.86, 1.0], [0.86, 1.04], [0.86, 1.07]],
               enemy_num=8,
               enemy_id='e0',
               enemy_fire_id=8,
               bullet_time=1.0,
               bullet_speed=3,
               bullet_target=[0.3,1.0],
               enemy_speed=3,
               dt=1.0,
               scene_time=3.0),
          dict(type='scene2',
               point_list=[[0.5, 0.1], [0.45, 0.11], [0.41, 0.12], [0.38, 0.13], [0.35, 0.15], [0.34, 0.17], [0.36, 0.2], [0.39, 0.21], [0.43, 0.22], [0.48, 0.22], [0.52, 0.21], [0.56, 0.19], [0.6, 0.17], [0.6, 0.15], [0.56, 0.14], [0.52, 0.13], [0.48, 0.13], [0.43, 0.13], [0.39, 0.13], [0.36, 0.15], [0.35, 0.17], [0.37, 0.19], [0.42, 0.19], [0.47, 0.19], [0.5, 0.17], [0.52, 0.15], [0.5, 0.13], [0.45, 0.13], [0.42, 0.14], [0.4, 0.16], [0.41, 0.18], [0.44, 0.18], [0.48, 0.19], [0.53, 0.18], [0.56, 0.17], [0.58, 0.15], [0.59, 0.12], [0.56, 0.11], [0.51, 0.11]],
               enemy_id='eb1',
               enemy_fire_id=12,
               enemy_speed=0.5,
               enemy_init_speed=1.5,
               max_iter=4,
               bullet_speed=2.0,
               bullet_target=[1,1],
               bullet_cd=0.4,
               bullet_break_cnt=5,
               bullet_break=2.0,
               wait_time=0.8,
               scene_time=3.5
               ),
          dict(type='scene2',
               point_list=[[0.53, 0.04], [0.48, 0.04], [0.45, 0.04], [0.43, 0.05], [0.42, 0.07], [0.44, 0.08], [0.46, 0.08], [0.51, 0.08], [0.52, 0.07], [0.5, 0.05], [0.47, 0.05], [0.44, 0.06], [0.42, 0.07], [0.43, 0.09], [0.47, 0.1], [0.51, 0.1], [0.54, 0.09], [0.55, 0.07], [0.55, 0.05], [0.52, 0.05]],
               enemy_id='eb2',
               enemy_fire_id=13,
               enemy_speed=0.5,
               enemy_init_speed=1.5,
               max_iter=4,
               bullet_speed=1.8,
               bullet_target=[0,-1],
               bullet_cd=0.5,
               bullet_break_cnt=3,
               bullet_break=2.0,
               wait_time=0.8,
               scene_time=4.5
               ),
          dict(type='scene1',
               point_list=[[0.09, -0.07], [0.09, 0.0], [0.05, 0.11], [0.02, 0.21], [0.01, 0.29], [0.01, 0.36], [0.04, 0.42], [0.11, 0.47], [0.23, 0.48], [0.35, 0.48], [0.47, 0.48], [0.58, 0.5], [0.72, 0.52], [0.82, 0.55], [0.88, 0.6], [0.95, 0.64], [0.97, 0.7], [1.02, 0.79], [1.05, 0.87], [1.06, 0.93]],
               enemy_num=8,
               enemy_id='e16',
               enemy_fire_id=4,
               bullet_time=2.5,
               bullet_speed=1.5,
               bullet_target=[1,1],
               enemy_speed=3,
               dt=0.8,
               scene_time=8.0),
          dict(type='scene1',
               point_list=[[0.84, -0.06], [0.84, 0.03], [0.85, 0.1], [0.88, 0.17], [0.96, 0.23], [1.0, 0.3], [1.0, 0.37], [0.98, 0.45], [0.89, 0.5], [0.79, 0.53], [0.68, 0.55], [0.57, 0.57], [0.47, 0.58], [0.37, 0.6], [0.26, 0.61], [0.18, 0.65], [0.1, 0.68], [0.02, 0.75], [-0.03, 0.8], [-0.12, 0.84]],
               enemy_num=8,
               enemy_id='e16',
               enemy_fire_id=0,
               bullet_time=1.5,
               bullet_speed=4,
               bullet_target=[0,0],
               enemy_speed=3,
               dt=0.8,
               scene_time=14.0),
          dict(type='scene1',
               point_list=[[0.16, -0.05], [0.15, 0.01], [0.15, 0.08], [0.15, 0.15], [0.15, 0.21], [0.14, 0.27], [0.13, 0.35], [0.12, 0.41], [0.12, 0.46], [0.18, 0.5], [0.27, 0.51], [0.37, 0.5], [0.45, 0.48], [0.52, 0.46], [0.59, 0.42], [0.61, 0.37], 
                         [0.56, 0.32], [0.48, 0.31], [0.37, 0.31], [0.27, 0.34], [0.21, 0.39], [0.17, 0.45], [0.14, 0.51], [0.12, 0.58], 
                         [0.12, 0.66], [0.11, 0.76], [0.11, 0.83], [0.1, 0.91], [0.08, 0.99], [0.07, 1.04]],
               enemy_num=5,
               enemy_id='e5',
               enemy_fire_id=0,
               bullet_time=1.0,
               bullet_speed=1.5,
               bullet_target=[1,1],
               enemy_speed=3,
               dt=0.6,
               scene_time=17.0),
          dict(type='scene1',
               point_list=[[0.82, -0.06], [0.84, 0.05], [0.85, 0.11], [0.85, 0.16], [0.84, 0.22], [0.82, 0.28], [0.79, 0.33], [0.74, 0.38], [0.68, 0.41], [0.6, 0.42], [0.53, 0.43], [0.45, 0.43], [0.42, 0.4], [0.42, 0.36], [0.47, 0.32], [0.53, 0.32], 
                         [0.6, 0.33], [0.66, 0.35], [0.7, 0.4], [0.71, 0.44], [0.72, 0.5], [0.72, 0.55], [0.72, 0.6], [0.71, 0.65], [0.71, 0.74], [0.71, 0.8], [0.7, 0.86], [0.69, 0.94], [0.68, 1.0], [0.68, 1.05]],
               enemy_num=5,
               enemy_id='e5',
               enemy_fire_id=0,
               bullet_time=2.0,
               bullet_speed=1.5,
               bullet_target=[1,1],
               enemy_speed=3,
               dt=0.6,
               scene_time=21.0),
          dict(type='scene2',
               point_list=[[0.5, 0.1], [0.45, 0.11], [0.41, 0.12], [0.38, 0.13], [0.35, 0.15], [0.34, 0.17], [0.36, 0.2], [0.39, 0.21], [0.43, 0.22], [0.48, 0.22], [0.52, 0.21], [0.56, 0.19], [0.6, 0.17], [0.6, 0.15], [0.56, 0.14], [0.52, 0.13], [0.48, 0.13], [0.43, 0.13], [0.39, 0.13], [0.36, 0.15], [0.35, 0.17], [0.37, 0.19], [0.42, 0.19], [0.47, 0.19], [0.5, 0.17], [0.52, 0.15], [0.5, 0.13], [0.45, 0.13], [0.42, 0.14], [0.4, 0.16], [0.41, 0.18], [0.44, 0.18], [0.48, 0.19], [0.53, 0.18], [0.56, 0.17], [0.58, 0.15], [0.59, 0.12], [0.56, 0.11], [0.51, 0.11]],
               enemy_id='eb0',
               enemy_fire_id=10,
               enemy_speed=0.5,
               enemy_init_speed=1.5,
               max_iter=4,
               bullet_speed=2.0,
               bullet_target=[1,1],
               bullet_cd=0.4,
               bullet_break_cnt=5,
               bullet_break=2.0,
               wait_time=0.8,
               scene_time=18.0
               ),
          dict(type='scene2',
               point_list=[[0.53, 0.04], [0.48, 0.04], [0.45, 0.04], [0.43, 0.05], [0.42, 0.07], [0.44, 0.08], [0.46, 0.08], [0.51, 0.08], [0.52, 0.07], [0.5, 0.05], [0.47, 0.05], [0.44, 0.06], [0.42, 0.07], [0.43, 0.09], [0.47, 0.1], [0.51, 0.1], [0.54, 0.09], [0.55, 0.07], [0.55, 0.05], [0.52, 0.05]],
               enemy_id='eb3',
               enemy_fire_id=11,
               enemy_speed=0.5,
               enemy_init_speed=1.5,
               max_iter=4,
               bullet_speed=1.8,
               bullet_target=[1,1],
               bullet_cd=0.5,
               bullet_break_cnt=3,
               bullet_break=2.0,
               wait_time=0.8,
               scene_time=23.0
               ),
          dict(type='scene1',
               point_list=[(0.5,1.2),(0.44,0.89),(0.31,0.84),(0.21,0.74),(0.14,0.60),\
                                (0.11,0.45),(0.11,0.30),(0.16,0.17),(0.22,0.08),\
                                (0.29,0.02),(0.36,0),(0.42,0.01),(0.46,0.03),\
                                (0.48,0.06),(0.49,0.09),(0.5,0.12),(0.51,0.09),\
                                (0.52,0.06),(0.54,0.03),(0.58,0.01),(0.64,0),\
                                (0.71,0.02),(0.78,0.08),(0.84,0.17),(0.89,0.3),\
                                (0.86,0.6),(0.79,0.74),(0.69,0.84),(0.56,0.89),\
                                (0.5,1.2)],
               enemy_num=8,
               enemy_id='ea0',
               enemy_fire_id=0,
               bullet_time=1,
               bullet_speed=3,
               bullet_target=[0.5,1.0],
               enemy_speed=4,
               dt=0.5,
               scene_time=27.0),
          dict(type='scene2',
               point_list=[[0.5, 0.1], [0.45, 0.11], [0.41, 0.12], [0.38, 0.13], [0.35, 0.15], [0.34, 0.17], [0.36, 0.2], [0.39, 0.21], [0.43, 0.22], [0.48, 0.22], [0.52, 0.21], [0.56, 0.19], [0.6, 0.17], [0.6, 0.15], [0.56, 0.14], [0.52, 0.13], [0.48, 0.13], [0.43, 0.13], [0.39, 0.13], [0.36, 0.15], [0.35, 0.17], [0.37, 0.19], [0.42, 0.19], [0.47, 0.19], [0.5, 0.17], [0.52, 0.15], [0.5, 0.13], [0.45, 0.13], [0.42, 0.14], [0.4, 0.16], [0.41, 0.18], [0.44, 0.18], [0.48, 0.19], [0.53, 0.18], [0.56, 0.17], [0.58, 0.15], [0.59, 0.12], [0.56, 0.11], [0.51, 0.11]],
               enemy_id='eb5',
               enemy_fire_id=9,
               enemy_speed=0.5,
               enemy_init_speed=1.5,
               max_iter=4,
               bullet_speed=2.0,
               bullet_target=[0,-1],
               bullet_cd=0.4,
               bullet_break_cnt=5,
               bullet_break=2.0,
               wait_time=0.8,
               scene_time=28.0
               ),
          dict(type='scene1',
               point_list=[(0.5, 1.2), (0.56, 0.89), (0.69, 0.84), (0.79, 0.74), \
                   (0.86, 0.6), (0.89, 0.3), (0.84, 0.17), (0.78, 0.08), (0.71, 0.02),\
                    (0.64, 0), (0.58, 0.01), (0.54, 0.03), (0.52, 0.06), (0.51, 0.09),\
                    (0.5, 0.12), (0.49, 0.09), (0.48, 0.06), (0.46, 0.03), (0.42, 0.01),\
                    (0.36, 0), (0.29, 0.02), (0.22, 0.08), (0.16, 0.17), (0.11, 0.3),\
                    (0.11, 0.45), (0.14, 0.6), (0.21, 0.74), (0.31, 0.84), (0.44, 0.89), (0.5, 1.2)],
               enemy_num=8,
               enemy_id='ea1',
               enemy_fire_id=1,
               bullet_time=1,
               bullet_speed=3,
               bullet_target=[0.5,1],
               enemy_speed=4,
               dt=0.5,
               scene_time=32.0)]