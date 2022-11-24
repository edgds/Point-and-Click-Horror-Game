# Transparent Button Class
# Create images that can be "clicked on" if the user clicks within the certain dimensions
#Modified version of Button Class
#For Horror Game.py
from graphics import *

class Transparent:

    """A button is transparent rectangle
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it. becasue it is invisible, an image is drawn instead of the button"""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button behind an image, eg:
        qb = Button(myWin, centerPoint, width, height, 'image.gif') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.image = Image(Point(300,300), label)#all items have transparent backgrounds and dimensions, so the point is the same
        self.image.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.active = True          #set the boolean variable that tracks "active"-ness to True


    def deactivate(self):
        "Sets this button to 'inactive'."
        ##set the boolean variable that tracks "active"-ness to False
        self.active = False

    
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        
        return (self.active and

                self.xmin < p.getX() < self.xmax and

                self.ymin < p.getY() < self.ymax)
    
    def undraw(self):
        "Undraws the image"
        self.image.undraw()

if __name__ == "__main__":
    main()


