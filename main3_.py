import pgzrun
from random import randint
import time

WIDTH = 600
HEIGHT = 600

playerXDefault = 275
playerYDefault = 475
playerSpeed = 4.4

pressed = {}

fond = Actor('fond')
player = Actor('player')

def initGame():
    global zombies, score
    score = 0
    player.x = playerXDefault
    player.y = playerYDefault
    zombies = []

initGame()

def update():
    global score
    screen.fill((0, 0, 0))
    fond.draw()
    player.draw()

    if player.x <= 0 or player.x >= WIDTH or player.y <= 0 or player.y >= HEIGHT:
        gameOver()

    if pressed.get(keys.LEFT):
        player.x -= playerSpeed
    if pressed.get(keys.RIGHT):
        player.x += playerSpeed
    if pressed.get(keys.UP):
        player.y -= playerSpeed
    if pressed.get(keys.DOWN):
        player.y += playerSpeed

    if randint(1, 12) == 1:
        zombies.append(
            Actor('mechant', (randint(1, WIDTH), 0))
        )
    for z in zombies:
        z.draw()
        if player.colliderect(z):
            gameOver()
        if z.y >= HEIGHT:
            zombies.remove(z)
        z.y += 4.4
    screen.draw.text('Score: ' + str(score), (0, 0))
    score += 1

def gameOver():
    initGame()

def on_key_down(key):
    pressed[key] = True

def on_key_up(key):
    pressed[key] = False

pgzrun.go()