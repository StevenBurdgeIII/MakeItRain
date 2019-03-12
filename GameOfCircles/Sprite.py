import SpriteManager

class Sprite(object): 
    team = 3 
    diameter = 60
    c = color(255)
    
    
    def __int__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
                
    def animate(self):
        self.move()
        self.display
        
    def isColliding(self, other):
        r1 = self.diameter / 2.0
        r2 = other.diameter / 2.0
        return r1 + r2 > dist(self.x, self.y, other.x, other.y)
    
    def handleCollisions(self):
        SpriteManager.destroy(self)
