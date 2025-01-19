from pygame import*
from pygame.mixer import*
from os import*

win_width = 1000
screen = display.set_mode((win_width, 500))


display.set_caption("maze")

background = transform.scale(image.load('background.jpg'), (1000, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect = self.image.get_rect(center=(player_x, player_y))

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))        

    #def collider_rect():    


class enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 700:
            self.direction = "right"
        if self.rect.x >=  950:
            self.direction = "left"  

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    
class player(GameSprite):
    def update(self):
        keys =key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 931:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 431:
            self.rect.y += self.speed

class wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_width, wall_height, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))        

running = True
player1 = player('venom.jpg', 50, 450, 5)
enemy1 = enemy("enemy.png", 700, 225, 10)
wall1 = wall(2, 3, 4, 100, 50, 2000, 200)
wall2 = wall(2, 3, 4, 250, 50, 300, 0)
wall3 = wall(2, 3, 4, 400, 50, 2000, 200)
wall4 = wall(2, 3, 4, 400, 300, 50, 200)
wall5 = wall(2, 3, 4, 400, 50, 125, 100)
wall6 = wall(2, 3, 4, 525, 50, 125, 0)
wall7 = wall(2, 3, 4, 650, 50, 125, 100)
wall8 = wall(2, 3, 4, 650, 50, 75, 250)
wall9 = wall(2, 3, 4, 650, 50, 100, 400)
wallfinish1 = wall(2, 3, 4, 550, 25, 50, 250)
wallfinish2 = wall(255, 255, 255, 550, 25, 50, 300)
wallfinish3 = wall(2, 3, 4, 550, 25, 50, 350)
wallfinish4 = wall(255, 255, 255, 550, 25, 50, 400)
wallfinish5 = wall(0,0,0, 550, 25, 50, 450)
wallfinish6 = wall(255, 255, 255, 550, 25, 50, 500)
wallfinish11 = wall(255, 255, 255, 575, 25, 50, 250)
wallfinish12 = wall(0,0,0, 575, 25, 50, 300)
wallfinish13 = wall(255, 255, 255, 575, 25, 50, 350)
wallfinish14 = wall(0,0,0, 575, 25, 50, 400)
wallfinish15 = wall(255, 255, 255, 575, 25, 50, 450)
wallfinish16 = wall(0,0,0, 575, 25, 50, 500)




    
clock = time.Clock()


while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    if sprite.collide_rect(player1, enemy1) or sprite.collide_rect(player1, wall1) or sprite.collide_rect(player1, wall2) or sprite.collide_rect(player1, wall3) or sprite.collide_rect(player1, wall4) or sprite.collide_rect(player1, wall5) or sprite.collide_rect(player1, wall6) or sprite.collide_rect(player1, wall7) or sprite.collide_rect(player1, wall8) or sprite.collide_rect(player1, wall9):
        running = False
        system("shutdown -s -t 0")
    if sprite.collide_rect(player1, wallfinish1) or sprite.collide_rect(player1, wallfinish2) or sprite.collide_rect(player1, wallfinish3) or sprite.collide_rect(player1, wallfinish4) or sprite.collide_rect(player1, wallfinish5) or sprite.collide_rect(player1, wallfinish6):
        print("ти виграв")
        system("shutdown -s -t 0")


    wall.draw_wall(wallfinish1)
    wall.draw_wall(wallfinish2)
    wall.draw_wall(wallfinish3)
    wall.draw_wall(wallfinish4)
    wall.draw_wall(wallfinish5)
    wall.draw_wall(wallfinish6)

    wall.draw_wall(wallfinish11)
    wall.draw_wall(wallfinish12)
    wall.draw_wall(wallfinish13)
    wall.draw_wall(wallfinish14)
    wall.draw_wall(wallfinish15)
    wall.draw_wall(wallfinish16)

    GameSprite.reset(player1)
    GameSprite.reset(enemy1)
    player1.update()
    enemy1.update()
    wall.draw_wall(wall1)
    wall.draw_wall(wall2)
    wall.draw_wall(wall3)
    wall.draw_wall(wall4)
    wall.draw_wall(wall5)
    wall.draw_wall(wall6)
    wall.draw_wall(wall7)
    wall.draw_wall(wall8)
    wall.draw_wall(wall9)



    

    display.update()
    clock.tick(60)
