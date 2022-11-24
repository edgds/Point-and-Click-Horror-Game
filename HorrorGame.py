#Murder Game :-) .py
#Compsci 110
#Due Dec 22
#Lien Har

#import classes:
from graphics import *
from ButtonClass import * 
from Transparent_ButtonClass import *
from audioplayer import *


def JumpScare(win): #jumpscare room, win as parameter

    #Draw room:
    Jumpscare = Image(Point(300,300),'Rooms/jumpscare.gif') #background
    Jumpscare.draw(win)
    
    #wait for user to click, then draw jumpscare:
    win.getMouse()
    #startSound('scream.wav', asyncPlay=True, loop=False)
    face= Image(Point(300,300),'face.gif')
    face.draw(win)

   
def drawHall(win, GardenButton, BedroomButton, QuitButton, pt, ItemList): 
#(Function that draws the Hall, 3 buttons, pt, and ItemList passed as parameters)

        
    Hall = Image(Point(300,300),'Rooms/b.gif')
    Hall.draw(win)
    
#Draw transparent buttons and draw item images:
    matB= Transparent(win, Point(230,510), 60, 50,'Items/mat.gif')
    lampB= Transparent(win, Point(560,100), 30, 50,'Items/lamp.gif')

#While the user keeps on clicking within the Hall room, this loop runs:    
    while not GardenButton.clicked(pt) and not BedroomButton.clicked(pt):
    
        if matB.clicked(pt): #If map button clicked, undraw it, draw a check mark, and change ItemList's False to True
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            matB.undraw()
            check4 = Image(Point(270,630),'check.gif')
            check4.draw(win)
            ItemList[3]=True #change False with index 3 to True in ItemList
            
        if lampB.clicked(pt):#same as map button
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            lampB.undraw()
            check5 = Image(Point(320,630),'check.gif')
            check5.draw(win)
            ItemList[4]=True #change False with index 4 to True        

        if QuitButton.clicked(pt):#close if QuitButton is clicked twice
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            return False

        pt=win.getMouse()



def drawGarden(win, HallButton, BedroomButton, QuitButton, pt, ItemList, TrueList):
#(Function that draws the Garden, 3 buttons, pt, and ItemList, and TrueList passed as parameters)

#LakeButton for hidden ending in game(jumpscare room), deactivated until all items collected (TrueList is all True)
    LakeButton=Transparent(win, Point(400, 350), 70, 70,'')
    LakeButton.deactivate()
    
    Garden = Image(Point(300,300),'Rooms/c.gif') #background
    Garden.draw(win)
        
#Draw transparent buttons and draw item images:    
    koiB=Transparent(win, Point(260, 570), 40,30, 'Items/koi.gif')
    emptybottleB=Transparent(win, Point(540, 260), 20,30, 'Items/emptybottle.gif')

#If all items clicked on, TrueList will have 7 'True' appended to it from ItemList then LakeButton is activated, message is drawn
    if len(TrueList)==7:                
        message=Text(Point(400,350),"help....\nbottom...center of.. \nthe lake...")
        message.setTextColor('red')
        message.draw(win)
        LakeButton.activate()
        
                
#Loop runs until quit button is clicked:    
    while not HallButton.clicked(pt) and not BedroomButton.clicked(pt):
        
        #If (activated) LakeButton is clicked, send user to jumpscare room
        if LakeButton.clicked(pt):
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            JumpScare(win)
        
        if koiB.clicked(pt):
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            koiB.undraw()
            check7 = Image(Point(370,630),'check.gif')
            check7.draw(win)
            ItemList[5]=True
            
        if emptybottleB.clicked(pt):
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            emptybottleB.undraw()
            check6 = Image(Point(420,630),'check.gif')
            check6.draw(win)
            ItemList[6]=True
            
        

        if QuitButton.clicked(pt):
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            return False
        
        pt=win.getMouse()

def drawBedroom(win, HallButton, GardenButton, QuitButton, pt, ItemList):
#(Function that draws the Bedroom, 3 buttons, pt, and ItemList passed as parameters)
    
    Bedroom = Image(Point(300,300),'Rooms/a.gif')
    Bedroom.draw(win)

    dollB= Transparent(win, Point(380,510), 70, 50,'Items/doll.gif')
    blindsB= Transparent(win, Point(510,360), 70, 50,'Items/blinds.gif')
    frameB= Transparent(win, Point(50,160), 40, 70,'Items/frame.gif')
   

    while not HallButton.clicked(pt) and not GardenButton.clicked(pt):

        if dollB.clicked(pt):
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            dollB.undraw()
            check = Image(Point(120,630),'check.gif')
            check.draw(win)
            ItemList[0]=True
            
        if blindsB.clicked(pt):
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            blindsB.undraw()
            ItemList[1]=True
            check2 = Image(Point(170,630),'check.gif')
            check2.draw(win)

        if frameB.clicked(pt):
            #startSound('ItemClick.wav', asyncPlay=True, loop=False)
            frameB.undraw()
            ItemList[2]=True
            check3 = Image(Point(220,630),'check.gif')
            check3.draw(win)
            
        

        if QuitButton.clicked(pt):
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            return False
        
        pt=win.getMouse()

def game():

    win = GraphWin('game',700,650)
#BGM music at start of game:
    #startSound('BGM.wav', asyncPlay=True, loop=True)
    #draw the side bars:
    Bar2 = Image(Point(300,300),'bar2.gif')
    Bar2.draw(win)
    Bar = Image(Point(300,750),'bar.gif')
    Bar.draw(win)
    

#draw the StartMenu:
    StartMenu = Image(Point(300,300),'Rooms/start.gif')
    StartMenu.draw(win)
    
            
#for loop to draw the checkboxes and its message:
    x=100
    x2=150
    for i in range(7):
        
        i=Rectangle(Point(x,600), Point(x2,700))
        i.setFill("white")
        i.draw(win)
        x+=50
        x2+=50

    note=Text(Point(40, 620), "Items\ncollected:")
    note.setTextColor('white')
    note.draw(win)


    
    #draw text on top of starting menu:
    opening=Text(Point(450,590),"Double click on the sidebar buttons")
    opening.setTextColor('white')
    opening.setStyle('bold')
    opening.draw(win)
   
    #Visible buttons on the side bar:
    QuitButton=Button(win, Point(620, 630), 50, 30, 'Quit')
    HallButton= Button(win, Point(660, 50), 70, 70, 'Hall')
    GardenButton= Button(win, Point(660, 200), 70, 70, 'Garden')
    BedroomButton= Button(win, Point(660, 350), 70, 70, 'Bedroom')
    
    #Create list with a False for each item. each index is for an item:
    ItemList=[]
    for i in range(7):
        ItemList.append(False)
        

    pt=win.getMouse()

    #while loop runs indefinitly until quit button is clicked on:
    while not QuitButton.clicked(pt):

        GardenButton.activate()
        HallButton.activate()
        BedroomButton.activate()


#If user has collected all the items, then hidden room will be unlocked:
        TrueList=[] 
        for i in range(7): 
            if ItemList[i]==True: #check each index in ItemList to see if it is 'True'
                TrueList.append(i) #append 'True' to TrueList


#If user clicks on the three buttons, then that function is called and that room is drawn        
        if BedroomButton.clicked(pt):
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            BedroomButton.deactivate()
            drawBedroom(win, HallButton, GardenButton, QuitButton, pt, ItemList)
            
        if HallButton.clicked(pt):
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            HallButton.deactivate()
            drawHall(win, GardenButton, BedroomButton, QuitButton, pt, ItemList)
            
        if GardenButton.clicked(pt):
            #startSound('MenuClick.wav', asyncPlay=True, loop=False)
            GardenButton.deactivate()
            drawGarden(win, HallButton, BedroomButton, QuitButton, pt, ItemList, TrueList)

            
            
        pt=win.getMouse()
            
                      
#stop sound before close program:    
    #stopSound()    
    win.close()
   
game()
