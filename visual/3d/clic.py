from visual import *
scene.range = 4
box() # display a box for context
#sphere(pos=(x,0,0), radius=0.2, color=color.cyan)

y = 0

def showSphere():
	
	sphere(pos=(0,0,0), radius=1.2, color=color.cyan)
	 




    
  
    	


scene.bind('click', showSphere())