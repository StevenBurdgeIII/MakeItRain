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
    
    size(650,650)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JigglyBot(200, 50, 2))
    SpriteManager.spawn(ScreenSaver(200,100, 4))
    SpriteManager.spawn(JigglyBot(200, 50, 2))



    SpriteManager.spawn(Enemy(0, 0, enemyTeam))
    SpriteManager.spawn(Enemy(100,100, enemyTeam))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(Raindrop(200,100, 4))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(Raindrop(200,100, 4))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(Raindrop(200,100, 4))
    SpriteManager.spawn(Raindrop(200, 50, 2))
    SpriteManager.spawn(JigglyBot(width/2, height/2, enemyTeam))
    SpriteManager.spawn(ScreenSaver(0, 0, enemyTeam))


                           
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    global player
    SpriteManager.getPlayer().keyDown()
    
def keyReleased():
    global player
    SpriteManager.getPlayer().keyUp()
