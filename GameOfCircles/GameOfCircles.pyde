import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop
from JigglyBot import JigglyBot
from ScreenSaverBot import ScreenSaverBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    size(650,650)
    player = Player(width/2, height/2, 1)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JigglyBot(200, 50, 2))
    SpriteManager.spawn(ScreenSaverBot(200,100, 2))
    SpriteManager.spawn(JigglyBot(200, 50, 2))
    SpriteManager.spawn(Enemy(100,100, 2))
    SpriteManager.spawn(RainDrop(200, 50, 2))
    SpriteManager.spawn(RainDrop(200,100, 2))
    SpriteManager.spawn(JigglyBot(width/2, height/2, 2))
    SpriteManager.spawn(ScreenSaverBot(0, 0, 2))
                           
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.getPlayer().keyDown()
    
def keyReleased():
    SpriteManager.getPlayer().keyUp()
