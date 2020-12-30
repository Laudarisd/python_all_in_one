import copy
import random

class Hat:

  def __init__(self,**colors):
    self.contents = []
    for i in colors.keys():
      for j in range(0,colors.get(i)):
        self.contents = self.contents + [i]

  def draw(self,to_draw):
    if to_draw <= len(self.contents):
      balls = []
      for i in range(0,to_draw):
        #taken = int(random.uniform(0,len(self.contents)))
        taken = random.randint(0,len(self.contents)-1)
        balls = balls + [self.contents[taken]]
        del self.contents[taken]        
    else:
      balls = self.contents
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  occurrences = 0
  failed_experiments = 0
  initial_contents = copy.copy(hat.contents)

  for k in range(0,num_experiments):
    drawn_balls = hat.draw(num_balls_drawn)
    print("Drawn balls : " + str(drawn_balls))
    for i in expected_balls.keys():
      occurrences = 0
      for j in range(0,len(drawn_balls)):
        if drawn_balls[j] == i:
          occurrences = occurrences + 1
      if occurrences < expected_balls.get(i):
        failed_experiments = failed_experiments + 1
        break
    hat.contents = copy.copy(initial_contents)
    print("Count of failed experiments : " + str(failed_experiments))
  
  probability = 1 - failed_experiments/num_experiments
  return probability
