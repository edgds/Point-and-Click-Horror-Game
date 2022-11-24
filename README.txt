READ ME:

This is a point and click horror game. 

Guide:
The goal is for the user to collect all 7 items.
After doing so, the Garden room will have a message upon re-entry
Clicking on the lake, will reveal a hidden room, and a hidden jumpscare
(the text says "this is a jumpscare" but it may be unreadable on a smaller screen)
the end  

Major components:
-if an item is clicked on, ItemList[i]==True. If all 7 'False' is now 'True', then append 'True' to TrueList and len(TrueList)==7
-Transparent Class: modified ButtonClass. instead of drawing the button visibly, the image is drawn instead. def clicked method returns true if the click is on the 
invisible button. The image is always on point (300,300) becuase they are partially transparent. The parameter for button label is instead used for the .gif
It has an undraw method also for the image
-Room functions: Function that draws the room, 3 buttons, pt, and ItemList passed as parameters)
def drawGarden takes TrueList as a parameter in addition

Testing and modifications:
-I made sure that the user can only interect with the items belonging to a specific room. 
-the starting screen was added so the code can jump from main to the room functions smoothly, without a user acciently clicking on
an item in main if a room was drawn there instead.
-find a way to make it one click instead of two when clicking on sidebar buttons
make the rooms a class to not repetively draw the items and buttons inside

Sources:
music:
https://www.sfxbuzz.com/summary/8-scarry-horror-sounds/124-scary-horror-scream
https://freemusicarchive.org/music/Soularflair/CUES_for_film_TV_games_etc_DARK/Cue_6_-_Ghostly-Somewhat_Sad-Scary-HipHop_Infinity_Ad_Nauseum_1097
https://www.fesliyanstudios.com/royalty-free-sound-effects-download/video-game-menu-153
images:
https://drawception.com/player/111858/artistformerlyknownasjef/