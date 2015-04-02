# maze program by Nicole Roth
setMediaPath ("/Users/PC5/Documents/GitHub/maze")
class Maze (object):
  """ solves a maze """
  def __init__(self):
    """ initialization """
    self.image = makePicture ("maze.jpg")
    self.w = makeWorld(getWidth (self.image), getHeight (self.image))
    self.w.setPicture(self.image)
    self.t = makeTurtle (self.w)
    
# Tests follow here
doTests =1
if doTests:
  #Test 1, Make maze
  m=Maze()
  
  #Test 2, Make image
  if m.image.__class__ == Picture:
    printNow ("Test 2 passed, image exists.")
  else:
    printNow ("Test 2 failed, image does not exist.")
  
  #Test 3, Make world
  try:
    if m.w.__class__== World:
      printNow ("Test 3 passed, world exists.")
  except:
    printNow ("Test 3 failed, world does not exist.")
    
  #Test 4, Make image in world
  
  try:
    if m.w.getPicture().fileName[-8:] == "maze.jpg":
      printNow ("Test 4 passed, world picture is maze.jpg")
    else:
      printNow ("Test 4 failed, world picture is " + m.w.getPicture())
  except:
    printNow ("Test 4 failed, unable to get filename.")
  
  #Test 5, Check for turtle
  
  try:
    if m.t.__class__== Turtle:
      printNow ("Test 5 passed, turtle exists.")
  except:
    printNow ("Test 5 failed, turtle does not exist.")
  
  #Test 6
  #Test 7
  #Test 8
  #Test 9
  