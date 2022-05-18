import pygame
import pygame.mixer
import pygame.font
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import os
from PIL import Image,ImageTk
import yaml
from copy import deepcopy
from Game_set import game_set
import utils


def Image_load(file:str,size:tuple)->ImageTk.PhotoImage:
    img = Image.open(file).resize(size)
    return ImageTk.PhotoImage(img)


    
def run_help():
    def show_operation_txt():
        nonlocal notebook
        notebook.delete('0.0',tk.END)
        notebook.insert('0.0',help_operation_txt)
    def show_note_txt():
        nonlocal notebook
        notebook.delete('0.0',tk.END)
        notebook.insert('0.0',help_note_txt)
    with open('config.yml','r')as f:
        CONFIG = yaml.load(f,yaml.SafeLoader)['help']
    root = tk.Toplevel()
    win_width,win_height = CONFIG['screen_size']
    button_size = CONFIG['button_size']
    bg_color = CONFIG['button_bg_color']
    small_button_size = CONFIG['small_button_size']
    with open(CONFIG['help_operation_txt'],'r',encoding='utf-8')as f:
        help_operation_txt = ''.join(f.readlines())
    with open(CONFIG['help_note_txt'],'r',encoding='utf-8')as f:
        help_note_txt = ''.join(f.readlines())
    root.geometry("{}x{}".format(win_width,win_height))
    root.title('帮助')
    canvas = tk.Canvas(root,height=win_height, width=win_width,
        bd=0, highlightthickness=0)
    canvas.pack()
    notebook = scrolledtext.ScrolledText(root,width=win_width-10,height=win_height-60,font=('songti',10))
    notebook.insert('0.0',help_operation_txt)
    notebook.pack()
    bg_img = Image_load(CONFIG['background_img'],(win_width,win_height))
    operation_icon = Image_load(CONFIG['help_operation_icon'],small_button_size)
    note_icon = Image_load(CONFIG['help_note_icon'],small_button_size)
    operation_button = tk.Button(root,bg=bg_color,image=operation_icon,text='操作',font=('heiti',12),compound='left',fg='white',command=show_operation_txt)
    note_button = tk.Button(root,bg=bg_color,image=note_icon,text='攻略',font=('heiti',12),compound='left',fg='white',command=show_note_txt)
    operation_button.pack()
    note_button.pack()
    canvas.create_image(0,0,anchor='nw',image=bg_img)
    canvas.create_window(*CONFIG['notebook_pos'],anchor='nw',width=win_width-10,height=win_height-60,window=notebook)
    canvas.create_window(*CONFIG['help_operation_pos'],anchor='nw',width=button_size[0],height=button_size[1],window=operation_button)
    canvas.create_window(*CONFIG['help_note_pos'],anchor='nw',width=button_size[0],height=button_size[1],window=note_button)
    root.mainloop()

def run_lab(gameset:game_set):
    with open('config.yml','r')as f:
        CONFIG = yaml.load(f,yaml.SafeLoader)
    gameset_copy = game_set()
    gameset_copy.__dict__ = deepcopy(gameset.__dict__)
    gold_consume_keys = ['HP_gold','HP_recover_gold','energy_gold','energy_recover_gold','cooling_gold','cooling_recover_gold',\
                        'bullet_ID_gold','shooting_cd_gold','missile_num_gold','missile_damage_gold','missile_actime_gold','missile_flyingtime_gold']
    diamond_consume_keys = ['HP_diamond','HP_recover_diamond','energy_diamond','energy_recover_diamond','cooling_diamond','cooling_recover_diamond',\
                        'bullet_ID_diamond','shooting_cd_diamond','missile_num_diamond','missile_damage_diamond','missile_actime_diamond','missile_flyingtime_diamond']
    level_keys = ['player_HP_level','player_HP_recover','player_energy_level','player_energy_recover_level','player_cooling_level','player_cooling_recover_level',\
            'bullet_ID','bullet_shooting_cd_level','missile_num_level','missile_damage_level','missile_actime_level','missile_flyingtime_level']
    def refresh():
        nonlocal gameset_copy
        gameset_copy.__dict__ = deepcopy(gameset.__dict__)
        threading.Thread(target=utils.thread_play_music,args=(config['refresh_sound_file'],1,1.0)).start()
        flash()
    def flash():
        gold_label.config(text=str(gameset_copy.gold))
        diamond_label.config(text=gameset_copy.diamond)
        for index, (consume_gold_label,consume_diamond_label,level_label) in enumerate(zip(gold_label_list,diamond_label_list,level_label_list)):
            level = gameset_copy.__dict__[level_keys[index]]
            gold_key = gold_consume_keys[index]
            diamond_key = diamond_consume_keys[index]
            if level < len(gameset_copy.__dict__[gold_key]):
                consume_gold = gameset_copy.__dict__[gold_key][level]
                consume_diamond = gameset_copy.__dict__[diamond_key][level]
            else:
                consume_gold = 'Max Lv'
                consume_diamond = 'Max Lv'
            level_label.config(text="{}/{}".format(level+1,len(gameset_copy.__dict__[gold_key])+1))
            consume_gold_label.config(text=str(consume_gold))
            consume_diamond_label.config(text=str(consume_diamond))
    def upgrade(index:int):
        level = gameset_copy.__dict__[level_keys[index]]
        gold_key = gold_consume_keys[index]
        diamond_key = diamond_consume_keys[index]
        if level < len(gameset_copy.__dict__[gold_key]):
            consume_gold = gameset_copy.__dict__[gold_key][level]
            consume_diamond = gameset_copy.__dict__[diamond_key][level]
            if gameset_copy.gold >= consume_gold and\
                gameset_copy.diamond >= consume_diamond:
                level += 1
                gameset_copy.gold -= consume_gold
                gameset_copy.diamond -= consume_diamond
                gameset_copy.__dict__[level_keys[index]] += 1
                threading.Thread(target=utils.play_music,args=(pygame.mixer.Sound(config['upgrade_sound_file']),1)).start()
                flash()
            else:
                upgrade_error()
        else:
            upgrade_error()
    def upgrade_error():
        threading.Thread(target=utils.play_music,args=(pygame.mixer.Sound(config['error_sound_file']),1)).start()
    def save():
        nonlocal gameset
        gameset.__dict__ = deepcopy(gameset_copy.__dict__)
        threading.Thread(target=utils.thread_play_music,args=(config['save_sound_file'],1,1.0)).start()
    def print_coord(event:tk.Event):
        print(f"({event.x},{event.y})")
    
        
    def on_closing():
        nonlocal gameset_copy
        if gameset.__dict__ != gameset_copy.__dict__:
            threading.Thread(target=utils.thread_play_music,args=(config['exit_sound_file'],1,2.0)).start()
            if messagebox.askyesno("提示", "未保存，是否退出?"):
                root.destroy()
        else:
            root.destroy()
    if not pygame.get_init():
        pygame.init()  # 初始化背景设置
        pygame.font.init() # 初始化字体设置
        pygame.mixer.init(11025)  # 音乐初始化
        pygame.mixer.music.set_volume(8)  # 音量初始化
    config = CONFIG['interface']
    icon_config = CONFIG['icon']
    root = tk.Toplevel()
    root.title('实验室')
    # root.bind("<Button-1>",print_coord) # for debug
    win_width, win_height = config['lab_screen_size']
    root.geometry('{:d}x{:d}'.format(win_width,win_height))
    img = Image.open(config['lab_img'])
    img = img.resize((win_width, win_height),Image.BICUBIC)
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root,height=win_height, width=win_width,
        bd=0, highlightthickness=0)
    canvas.create_image(0,0,anchor='nw',image=photo)
    canvas.pack()
    gold_ico = Image.open(os.path.join(icon_config['path'],icon_config['gold'])).resize((25,25),Image.BICUBIC)
    gold_ico = ImageTk.PhotoImage(gold_ico)
    diamond_ico = Image.open(os.path.join(icon_config['path'],icon_config['diamond'])).resize((30,25),Image.BICUBIC)
    diamond_ico = ImageTk.PhotoImage(diamond_ico)
    small_gold_ico = Image.open(os.path.join(icon_config['path'],icon_config['gold'])).resize((15,15),Image.BICUBIC)
    small_gold_ico = ImageTk.PhotoImage(small_gold_ico)
    small_diamond_ico = Image.open(os.path.join(icon_config['path'],icon_config['diamond'])).resize((20,15),Image.BICUBIC)
    small_diamond_ico = ImageTk.PhotoImage(small_diamond_ico)
    refresh_icon = Image.open(os.path.join(icon_config['path'],icon_config['refresh'])).resize((25,25),Image.BICUBIC)
    refresh_icon = ImageTk.PhotoImage(refresh_icon)
    save_icon = Image.open(os.path.join(icon_config['path'],icon_config['save'])).resize((25,25),Image.BICUBIC)
    save_icon = ImageTk.PhotoImage(save_icon)
    upgrade_ico = Image.open(os.path.join(icon_config['path'],icon_config['upgrade'])).resize((25,25),Image.BICUBIC)
    upgrade_ico = ImageTk.PhotoImage(upgrade_ico)
    # 显示升级消耗图标
    canvas.create_image(*config['lab_grid']['gold_icon'],anchor='nw',image=gold_ico)
    canvas.create_image(*config['lab_grid']['diamond_icon'],anchor='nw',image=diamond_ico)
    consume_gold_icon_grid = config['lab_grid']['consume_grid']
    gold_value = str(gameset_copy.gold)
    diamond_value = str(gameset_copy.diamond)
    consume_gold_size = (50,12)
    consume_diamond_size = (40,12)
    level_size = (25,12)
    button_size = (25,25)
    gold_label_list = []
    diamond_label_list = []
    level_label_list = []
    consume_label_dict = dict(fg='yellow',font=('arial',8),background=config['lab_grid']['background_color'])

    # 显示升级消耗数值
    consume_gold_value_grid = [[coor[0]+20,coor[1]] for coor in consume_gold_icon_grid]
    consume_diamond_icon_grid = [[coor[0]+50,coor[1]] for coor in consume_gold_value_grid]
    consume_diamond_value_grid = [[coor[0]+20,coor[1]] for coor in consume_diamond_icon_grid]
    for gold_icon_coord,diamond_icon_coord in zip(consume_gold_icon_grid,consume_diamond_icon_grid):
        canvas.create_image(*gold_icon_coord,anchor='nw',image=small_gold_ico)
        canvas.create_image(*diamond_icon_coord,anchor='nw',image=small_diamond_ico)
    gold_label = tk.Label(root,text=gold_value,fg='yellow',font=('arial',12),background=config['lab_grid']['background_color'],justify='left')
    diamond_label = tk.Label(root,text=diamond_value,fg='yellow',font=('arial',12),background=config['lab_grid']['background_color'],justify='left')
    gold_label.pack()
    diamond_label.pack()
    
    canvas.create_window(*config['lab_grid']['gold_value'],anchor='nw',width=60,height=20,window=gold_label)
    canvas.create_window(*config['lab_grid']['diamond_value'],anchor='nw',width=45,height=20,window=diamond_label)
    for index in range(len(gold_consume_keys)):
        level = gameset_copy.__dict__[level_keys[index]]
        gold_key = gold_consume_keys[index] 
        diamond_key = diamond_consume_keys[index]
        consume_gold = gameset_copy.__dict__[gold_key][level] if level < len(gameset_copy.__dict__[gold_key]) else 'Max Lv'
        consume_diamond = gameset_copy.__dict__[diamond_key][level] if level < len(gameset_copy.__dict__[diamond_key]) else 'Max Lv'
        consume_gold_label = tk.Label(root,cnf=consume_label_dict,text=consume_gold,justify='left')
        consume_diamond_label = tk.Label(root,cnf=consume_label_dict,text=consume_diamond,justify='left')
        level_label = tk.Label(root,cnf=consume_label_dict,text="{}/{}".format(level+1,len(gameset_copy.__dict__[gold_key])+1),justify='left')
        button = tk.Button(root,command=lambda i=index: upgrade(i),image=upgrade_ico,background=config['lab_grid']['button_color'])
        consume_gold_label.pack()
        consume_diamond_label.pack()
        level_label.pack()
        button.pack()
        gold_label_list.append(consume_gold_label)
        diamond_label_list.append(consume_diamond_label)
        level_label_list.append(level_label)
        canvas.create_window(*consume_gold_value_grid[index],anchor='nw',width=consume_gold_size[0],height=consume_gold_size[1],window=consume_gold_label)
        canvas.create_window(*consume_diamond_value_grid[index],anchor='nw',width=consume_diamond_size[0],height=consume_diamond_size[1],window=consume_diamond_label)
        canvas.create_window(*config['lab_grid']['level_grid'][index],anchor='nw',width=level_size[0],height=level_size[1],window=level_label)
        canvas.create_window(*config['lab_grid']['upgrade_grid'][index],anchor='nw',width=button_size[0],height=button_size[1],window=button)
    refresh_button = tk.Button(root,text='重置',font=('kaiti',12),background=config['lab_grid']['button_color'],
                               foreground='yellow',image=refresh_icon,compound='left',
                               command=refresh)
    refresh_button.pack()
    save_button = tk.Button(root,text='保存',font=('kaiti',12),background=config['lab_grid']['button_color'],
                               foreground='yellow',image=save_icon,compound='left',
                               command=save)
    save_button.pack()
    canvas.create_window(*config['lab_grid']['refresh_icon'],width=65,height=25,window=refresh_button)
    canvas.create_window(*config['lab_grid']['save_icon'],width=65,height=25,window=save_button)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.mainloop()
