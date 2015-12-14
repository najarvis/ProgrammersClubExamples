class powerup(object):

    def __init__(self, pos, image, vel=(0,0)):
        self.x, self.y = pos
        self.vel_x, self.vel_y = vel
        self.image = image
        
    def tick(self, tick):
        self.x+=self.vel_x*tick
        self.y+=self.vel_y*tick
        
    def check(self):
        if self.image.get_rect():
            pass