from Player import Player
from Enemy import Enemy

def setup():
    global player, enemy1, enemy2
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    enemy1 = Enemy(50, 50, enemyTeam)
    enemy2 = Enemy(150, 150, enemyTeam)
                           
def draw():
    global player, enemy
    background(255)    
    player.animate()
    enemy1.animate()
    enemy2.animate()
    
def keyPressed():
    global player
    player.keyDown()
        
def keyReleased():
    global player
    player.keyUp()
