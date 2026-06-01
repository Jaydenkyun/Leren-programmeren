from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code start here
robotArm.moveRight()
robotArm.grab()

ready = False
while not ready:
    if robotArm.scan() == "green":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()
    elif robotArm.scan() == "blue":
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
        robotArm.grab()
    else:
        ready = True
    



# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
robotArm.showSolution()
robotArm.wait()

