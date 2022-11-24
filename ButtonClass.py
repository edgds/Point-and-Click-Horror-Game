# Button Class
#modified for Horror Game.py

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):

        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('red')
        self.label.setStyle('bold italic')#color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    
    def deactivate(self):
        "Sets this button to 'inactive'."
        ##color the text "darkgray"
        ##set the boolean variable that tracks "active"-ness to False
        self.label.setFill('darkgray') 
        self.active = False          

    
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        
        return (self.active and

                self.xmin < p.getX() < self.xmax and

                self.ymin < p.getY() < self.ymax)

if __name__ == "__main__":
    main()
