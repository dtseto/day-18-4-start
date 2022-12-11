import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(99):
  tim.left(random.choice(directions))
  tim.color(random.choice(colours))
  #tim.left(random.randint(0,360))
  tim.forward(random.randint(0,30))
  tim.speed('fastest')