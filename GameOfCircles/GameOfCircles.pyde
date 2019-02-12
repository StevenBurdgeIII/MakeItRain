import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from RainDrop import RainDrop
from JigglyBot import JigglyBot
from ScreenSaverBot import ScreenSaverBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    sprites.append(player)
    sprites.append(RainDrop(50, 50, enemyTeam))
    sprites.append(RainDrop(10, 1100, enemyTeam))
    sprites.append(RainDrop(80, 70, enemyTeam))
    sprites.append(RainDrop(120, 50, enemyTeam))
    sprites.append(RainDrop(50, 150, enemyTeam))
    sprites.append(RainDrop(150, 15, enemyTeam))
    sprites.append(ScreenSaverBot(100, 100, enemyTeam))
    sprites.append(JigglyBot(50, 50, enemyTeam))
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
