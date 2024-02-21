import pygame
import random
import math

pygame.init()

# Title and icons
pygame.display.set_caption('Galaxy space invaders with pygame')
icon = pygame.image.load('./resources/icono.png')
pygame.display.set_icon(icon)

display = pygame.display.set_mode((800, 600))

execution = True

subject_x = 368
subject_y = 530
speed_subject = 0.6

# Enemies
icon_enemy = []
enemy_x = []
enemy_y = []
speed_enemy = []
number_enemies = 6

speed = 1

icon_bullet = pygame.image.load('./resources/municion.png')
bullet_x = 0
bullet_y = 530
speed_bullet = 2
bullet_visible = False

puntuacion = 0
puntaje_texto = pygame.font.Font('./resources/poppins.ttf', 35)
puntaje_x = 500
puntaje_y = 15

game_over_texto = pygame.font.Font('./resources/poppins.ttf', 75)
game_over_x = 175
game_over_y = 250

fuente_tiempo = pygame.font.Font('./resources/poppins.ttf', 36)
tiempo_inicio = pygame.time.get_ticks()


for e in range(number_enemies):
    icon_enemy.append(pygame.image.load('./resources/enemigo.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(0, 200))
    speed_enemy.append(1)


def enemy(x, y, num):
    display.blit(icon_enemy[num], (x, y))


def subject(icon, x, y):
    display.blit(icon, (x, y))


def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    display.blit(icon_bullet, (x + 16, y + 10))
    

def compute_distance(x_1, y_1, x_2, y_2):
    distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    if distance <= 50:
        return True
    else:
        return False


def game_over():
    texto_final = game_over_texto.render(f"GAME OVER", True, (255, 0, 0))
    display.blit[texto_final, (game_over_x, game_over_y)]


while execution:
    icon_subject = pygame.image.load('./resources/personaje.png')
    display.fill((0, 0, 0))
    
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcrurrido = (tiempo_actual - tiempo_inicio) // 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execution = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = subject_x
                shoot_bullet(bullet_x, bullet_y)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            subject_x -= speed_subject
            icon_subject = pygame.image.load('./resources/personaje_rot_i.png')

        elif event.key == pygame.K_RIGHT:
            subject_x += speed_subject
            icon_subject = pygame.image.load('./resources/personaje_rot_d.png')

    if subject_x <= 0:
        subject_x = 0
    elif subject_x >= 736:
        subject_x = 736

    for e in range(number_enemies):
        
        if enemy_y[e] > 450 or tiempo_transcrurrido >= 60:
            for n in range(number_enemies):
                enemy_y[n] = 1000
            game_over()
            break
        
        
        enemy_x[e] += speed_enemy[e]

        if enemy_x[e] <= 0:
            speed_enemy[e] = 1 * speed
            enemy_y[e] += 50
        elif enemy_x[e] >= 736:
            speed_enemy[e] = -1 * speed
            enemy_y[e] += 50

        enemy(enemy_x[e], enemy_y[e], e)
        
        collision = compute_distance(enemy_x[e], enemy_y[e], bullet_y, bullet_x)
        
        if collision:
            bullet_y = 500
            bullet_visible = False
            puntuacion += 1
            
            speed += 0.05
            
            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(0, 200)
            
        subject(icon_subject, subject_x, subject_y)

    subject(icon_subject, subject_x, subject_y)
    
    if bullet_y <= -16:
        bullet_y = 530
        bullet_visible = False
        
    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= speed_bullet
        
    texto_puntuation = puntaje_texto.render(f"Puntuation: {puntuacion}", True, (0,255,0))
    display.blit(texto_puntuation, (puntaje_x, puntaje_y))
    
    texto_tiempo = fuente_tiempo.render(f"Tiempo: {tiempo_transcrurrido}", True, (255, 255, 255))
    display.blit(texto_tiempo, (10, 10))

    pygame.display.update()
