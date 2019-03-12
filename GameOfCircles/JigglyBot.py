from Sprite import Sprite
class JigglyBot(Sprite):
    
    speed = 6
    diameter = 60
    c = color(255,0,255)

    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
