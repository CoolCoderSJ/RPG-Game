import time
import random
print("Warning: this is an rpg game. Only type when it is time to make a decision")
time.sleep(1)
print("")
Death_Sentence = {"Bridge death1": "You walk onto the bridge... it collapses beneath you. You have fallen to your death. You have died!", "Bridge death2": "You walk out onto the bridge... it doesn't feel stable. Soon you realize the rope you put on was not strong enough... Tash had tricked you, when you got the question wrong! You have fallen to your death furious at Tash... You have died!", "Monster camp death": "You see a giant castle on top of the cliff, hoping it was civilization and they could get you out of the jungle. When you step in you realize they were monsters! They eat you alive. You have died!", "Key door death": "You open the door, stepping in the door closes on you. You search for a keyhole but there isn't one. One week later, You die from starvation. You have died!", "Tracker death": "You pick up what seems to be a torn up rope. Soon you realize it is a tracker. Monsters show up and eat you. You have died!", "Lab death": "As soon as you walk in... kaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabloooooooooooooooooooooooooooooooooeeeeeeeeeeeeeeeeeyyyyyyyy!!!!!!!!!!!! You DEAD!"}
fake_rope_Monster = False
fake_rope_Dissolvable = False
true_rope = False
sword = False
key = False

print("Welcome to Bewildered: Into the jungle!")
time.sleep(1)
print("")
print("Created by: Mason, Shuchir, and Samuel")
time.sleep(1)
print("")
print("")
print("")



def junforward1():
  print("")
  print("")
  print("The giant boulder has ancient writing on it. Behind it you see what looks like a rope.")
  time.sleep(1)
  print("There is an interesting lab to your left. The lab might help but you don't know...") 
  time.sleep(1)
  print("There is a Hut on the right.")
  print("")
  x = int(input("You now face a decision: 1 to get the rope, 2 to go right, 3 to go left, or 4 to go home. "))
  
  if x == 1:
    global fake_rope_Monster
    fake_rope_Monster = True
    if sword == True:
      print("You had the sword and could use it against monsters that attacked you. You are back in the jungle.")
      junforward1()
    else:
      print(Death_Sentence["Tracker death"])
      
  elif x == 2:
    tash_Hut()
  elif x == 3:
    lab()
  elif x == 4:
    junstart()



def junbackward1():
  print("")
  print("Going to cliff")
  print("")
  print("On the wall you see symbols and letters you don't understand")
  print("")
  print("The only thing you can make out is the letters that spell out " + "Tash")
  print("You think that there are people living in the jungle")
  print("The only way out is to go back where you started")
  ttthpw = int(input("Type 1 to go back "))
  if ttthpw == 1:
    junstart()



def junleft1():
  print("")
  print("")
  print("To cave")
  print("You see a dark and scary-looking cave. There may be secrets hidden inside, or there might be traps. You dare to enter the cave...")
  print("You enter the cave and find a key. To the left, there is also a bridge.")
  a = input("Would you like to take the key?")
  a = a.title()
  if a == "Yes":
    global key
    key = True
    print("You Got the Key!")
  b = int(input("Press 1 to go to the bridge or 2 to go back"))
  if b == 1:
    bridge_code()
  elif b == 2:
    junstart()
 
  
def junright1():
  print("")
  print("")
  print("You have come onto the plane crash site. There is a wall behind you that requires a key that you do not have. To the right you see rugged cliffs, but they look barely climbable.")
  y = int(input("Press 1 to go back, press 2 to try to climb the cliff, or press 3 to attempt to use the key"))
  if y == 1:
    junstart()
  elif y == 2:
    climbable_cliffs()
  elif y == 3:
    if key == True:
      print(Death_Sentence["Key door death"])
    else:
      print("You did not have the key.")
      junright1()

def bridge_code():
  print("")
  print("")
  print("You walk out onto a cliff and see a bridge")
  fff = int(input("Would you like to cross the bridge or go back into the cave 1 = cross bridge, 2 = go back"))
  if fff == 1:
    if true_rope == True:
      print("You fixed the bridge. You have escaped the jungle. After walking several miles you find civilization and head home. Congrats, YOU WON!!!!!!")
    elif fake_rope_Dissolvable == True:
      print(Death_Sentence["Bridge death2"])
    else:
      print(Death_Sentence["Bridge death1"])
  elif fff == 2:
    junleft1()




def climbable_cliffs():
  print("")
  print(Death_Sentence["Monster camp death"])

def lab():
  print("")
  print(Death_Sentence["Lab death"])
  
def tash_Hut():
  x = input("Hi! I am the owner of the hut. If you want a rope enter my name. What is my name?  ")
  x = x.title()
  global true_rope
  if x == "Tash":
    true_rope = True
    print("You got the rope! ")
    swordinp = input("Do you want the sword? ")
    swordinp = swordinp.title()
    if swordinp == "Yes":
      global sword
      sword = True
      print("You have the sword!")
    else:
      print("OK")
  else:
    global fake_rope_Dissolvable
    fake_rope_Dissolvable = True
    print("You got the rope!")
  junforward1()

def junstart():
  print("Behind you, there is a giant cliff... you know you can't climb it...")
  time.sleep(1)
  print("To the left you see a cave... you have no idea what is in it...")
  time.sleep(1)
  print("In front of you... you see only more jungle and what seems to be a giant boulder...")
  time.sleep(1)
  print("To the right you see you a crashed plane")
  choice1 = int(input("Where would you like to go: 1 for behind you, 2 go to plane crash, 3 for go in the cave, 4 for go into the jungle."))
  if choice1 == 1:
    junbackward1()
  if choice1 == 2:
    junright1()
  if choice1 == 3:
    junleft1()
  if choice1 == 4:
    junforward1()

  



def jungle():
  print("JUNGLE mode chosen... you have crashed on an island, and you are the only survivor.")
  time.sleep(1)
  print("You wake up in the middle of a dense jungle...")
  time.sleep(1)
  print("You see no sign of civilization...")
  time.sleep(1)
  print("All you hear is the sound of monkeys...")
  time.sleep(1)
  junstart()
  
      

x = int(input("Choose your character: 1 for Anchey, 2 for David, and 3 for Saif "))

characters = ("Anchey", "David", "Saif")
print("")

if x == 1:
  print("Hello, " + characters[0])
elif x == 2:
  print("Hello, " + characters[1])
elif x == 3:
  print("Hello, " + characters[2])
print("")
jungle()

