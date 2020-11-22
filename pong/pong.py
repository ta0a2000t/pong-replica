#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:28:01 2020

@author: tahaalnufaili

my first game...
"""

import pygame, random
pygame.init()
screen_width = 700
screen_height = 500
dis = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong-First Game')

hit_sound = pygame.mixer.Sound('hit.wav')
hit2_sound = pygame.mixer.Sound('hit2.wav')
goal_sound = pygame.mixer.Sound('goal.wav')
crowd_goal_sound = pygame.mixer.Sound('crowd_goal.wav')


class player:   
    def __init__(self):
        self.width = 12
        self.height = 35
        self.color = (200, 255, 200)
        self.speed = 5
        self.speedup = self.speed
        self.speeddown = self.speed * -1
        self.location_y = screen_height/2 - self.height/2

    def reset_location(self):
        self.location_y = screen_height/2 - self.height/2


class right_player(player):
    def __init__(self):
        super().__init__()
        self.location_x = screen_width - 25 - self.width
        self.points = 0

    def control(self):
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.speedup = self.speed * -1
                if event.key == pygame.K_DOWN:
                    self.speeddown = self.speed
        if event.type == pygame.KEYUP:
            self.speedup = 0
            self.speeddown = 0


class left_player(player):
    def __init__(self):
        super().__init__()
        self.location_x = 25
        self.points = 0    
        
    def bot(self):
        if (self.location_y + self.height/2) - (sqr.location_y + sqr.side/2) > self.speed * 1.5:
            self.speeddown = 0
            self.speedup = self.speed * -1
        else:
            self.speedup = 0
            self.speeddown = self.speed

        if abs(self.location_y + self.height - screen_height) < self.speed * 1.5:
            self.speeddown = 0
        if self.location_y < self.speed * 1.5:
            self.speedup = 0
        self.location_y += self.speeddown + self.speedup


class square: #sqr
    def __init__(self):
        self.side = 12
        self.color = (50, 150, 255)
        self.location_x = screen_width/2 - self.side/2
        self.location_y = screen_height/2 - self.side/2
        self.speed = 5
        self.speedx = 6
        self.speed_x = self.speedx
        self.speed_y = self.speed
        self.goal = False
        enemy.speed = self.speed

    def move(self): #if start == 1:
        if abs(self.location_y + self.side/2 - screen_height) < self.speed * 1.3 or abs(self.location_y + self.side/2) < self.speed * 1.3:                 
            self.speed_y = self.speed_y * -1
            hit_sound.play()
        self.location_y += self.speed_y      
          
        if abs(self.location_x + self.side - hero.location_x) < self.speedx * 1.5 and abs((self.location_y + self.side/2) - (hero.location_y + hero.height/2)) < (self.side/2 + hero.height/2):
            self.speed_x = self.speedx * -1
            hit2_sound.play()
        if abs(self.location_x - (enemy.location_x + enemy.width)) < self.speedx * 1.5 and abs((self.location_y + self.side/2) - (enemy.location_y + enemy.height/2)) < (self.side/2 + enemy.height/2):
            self.speed_x = self.speedx
            hit2_sound.play()
        self.location_x += self.speed_x
        
        if self.location_x > hero.location_x + (screen_width - hero.location_x)/2:
            enemy.points += 1
            goal_sound.play()
            self.speed_x = self.speedx * -1
            self.goal = True
        if self.location_x < self.side/2:
            hero.points += 1
            goal_sound.play()
            self.goal = True            
            self.speed_x = self.speedx
            
    def reset_location(self): # start = 0
        self.location_x = screen_width/2 - self.side/2
        self.location_y = screen_height/2 - self.side/2
        self.goal = False


class lines:
    grid_side = 50
    def __init__(self):
        self.width = 1
        self.height = screen_height
        self.color = (255, 255, 255)
        self.location_x = 0
        self.location_y = 0


class squares_in_middle:
    def __init__(self):
        self.side = 5
        self.color = (255, 255, 255)
        self.location_x = screen_width/2 - self.side/2
        self.location_y = 0


def board(text, x, y, color, font_size = 40):
    font_style = pygame.font.SysFont(None, font_size)
    b = font_style.render(text, True, color)
    dis.blit(b, [x, y])


grid = lines()
hero = right_player()
enemy = left_player()
sqr = square()
squares_middle = squares_in_middle()
game_over = False
start = 0

hero_image = pygame.Surface((hero.width, hero.height)).convert()
hero_image.fill(hero.color)

enemy_image = pygame.Surface((enemy.width, enemy.height)).convert()
enemy_image.fill(enemy.color)

grid_image = pygame.Surface((grid.width, grid.height)).convert()
grid_image.fill(grid.color)


sqr_image = pygame.Surface((sqr.side, sqr.side)).convert()
sqr_image.fill(sqr.color)

squares_middle_image = pygame.Surface((squares_middle.side, squares_middle.side)).convert()
squares_middle_image.fill(squares_middle.color)


while not game_over:

    for i in range(int(screen_width / lines.grid_side)):
        dis.blit(grid_image, (lines.grid_side * i, grid.location_y))
    
    for i in range(int(screen_height / (squares_middle.side * 2))):
        dis.blit(squares_middle_image, (squares_middle.location_x, squares_middle.side * i * 2))
        
    dis.blit(hero_image, (hero.location_x, hero.location_y))
    dis.blit(enemy_image, (enemy.location_x, enemy.location_y))
    dis.blit(sqr_image, (sqr.location_x, sqr.location_y))
        
    board(str(enemy.points) + '  ' + str(hero.points), screen_width/2-22, 10, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                start = 1
        hero.control()
        
    if hero.location_y < hero.speed * 1.5:
        hero.speedup = 0
    if screen_height - (hero.location_y + hero.height) < hero.speed * 1.5:
        hero.speeddown = 0
    hero.location_y += hero.speeddown + hero.speedup
    if start == 1:   
        sqr.move()
        enemy.bot()
    else:
        board('Press T to play', screen_width/2 - screen_width/7, screen_height/2 - screen_height/8, (255, 10, 20))

    if sqr.goal:
        sqr.reset_location()
        enemy.reset_location()
        hero.reset_location()
        start = 0
    pygame.display.flip()
    
    dis.fill((0, 0, 0))


pygame.display.quit()
pygame.quit()
exit()