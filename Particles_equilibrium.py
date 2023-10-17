"""
Yuyang Wang
CS152 sectionB
Lab 10 final project
12/6/2022

Call this file like this:
python3 ideal_gas1.py

This file can simulate the process of particles reaching equilibrium

User can input the start times of temperature and the end times of temperature and the how many steps to go from start to end.

This file use the concept of ideal gas law.

The conjecture is that when the temperature goes up, the average velocity of particles would go up too
With the average velocity of the particles goes up, the time to reach equilibrium would decrease.

This is a ideal model that will not consider frictions, mass, and gravity.

The main function will run for a couple of times and the file would automate the process of ploting a graph.


"""

import graphicsPlus as gr
import physics_objects as pho
import collision as cl
import random
import time
import math
import statistics2 as stat
import matplotlib.pyplot as plt
import numpy as np


def buildObstacles(win):
    """ Create all of the walls in the scene and put them in a list. The return value would be a list of objects"""
    # Each obstacle should be a Thing (e.g. Ball, Block, other)
    # make a empty list to contain blocks
    blocks1 = []

    # make two long blocks
    for i in range(2):
        longblock = pho.Block(win, width=1.5, height=35)
        # set the position
        longblock.setPosition(5+80*i, 27)
        # set the elasticity
        longblock.setElasticity(1)
        # set the color
        longblock.setColor((43, 75, 99))
        # append them into the list
        blocks1.append(longblock)

    # making to blocks to simulate the middle hole
    midblock = pho.Block(win, width=1.5, height=16)
    # set the position
    midblock.setPosition(45, 38)
    # set the color
    midblock.setColor((43, 75, 99))
    # append the this to the list
    blocks1.append(midblock)

    midblock2 = pho.Block(win, width=1.5, height=16)
    # set the position
    midblock2.setPosition(45, 16)
    # set the color
    midblock2.setColor((43, 75, 99))
    # append the this to the list
    blocks1.append(midblock2)

    # creat a topblock
    topblock = pho.Block(win, width=90, height=1.5)
    # set the position
    topblock.setPosition(45, 42)
    # set the color of the block
    topblock.setColor((193, 83, 100))
    # append this object to the list
    blocks1.append(topblock)

    # creat a bottom block
    bottomblock = pho.Block(win, width=90, height=1.5)
    # set the position
    bottomblock.setPosition(45, 12)
    # set the color of the block
    bottomblock.setColor((193, 83, 100))
    # append this object to the list
    blocks1.append(bottomblock)

    # Return the list of Things
    return blocks1


def main(scale):
    """This is a function that can simulate the process of reaching equilibrium, this function should take scale as its argument, and the function will return the time elapsed of the reaching equilibrium """
    # open the extract file and clear it
    fp = open("extract.csv", "w")
    # close file
    fp.close()
    # open file and add data
    fp = open("extract.csv", "a")
    # write the head line
    fp.write('left number 1' + ',' + 'right number 1' +
             ',' + 'velocity' + ',' + 'time' + '\n')
    # create a GraphWin
    win = gr.GraphWin('gas equilibrium', 1000, 500, False)
    # call buildObstacles, storing the return list in a variable (e.g. shapes)
    shapes = buildObstacles(win)
    # loop over the shapes list and have each Thing call its draw method
    for i in shapes:
        i.draw()
    # assign to dt the value 0.02
    dt = 0.02
    # assign to frame the value 0
    frame = 0
    # create an empty list
    o_list = []
    # a for loop that can creat 20 particles
    for i in range(20):
        # creat a particle using physics object file
        oxygen = pho.Ball(win)
        # set its position at the right side of the box and randomize the position
        oxygen.setPosition(random.randint(10, 40), random.randint(15, 35))
        # set the velocity of the particle and randomize the velocity, the velocity should
        oxygen.setVelocity(random.randint(-20, 20) * scale,
                           random.randint(-20, 20) * scale)
        # set the aceeleration to 0 cause we would not consider the gravity
        oxygen.setAcceleration(0, 0)
        # append the particles into list
        o_list.append(oxygen)
        # draw all the particles
        oxygen.draw()

    # record the start time of the while function
    start_time = time.time()
    # creat a timelist
    timelist = []
    # global the list
    global leftlist1
    # create an empty list
    leftlist1 = []
    # global the list
    global rightlist1
    # create an empty list
    rightlist1 = []
    # start an infinite while loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            # call win.update()
            win.update()
        # using checKey, if the user typed a 'q' then break
        key = win.checkKey()
        # if user tyoe q the loop breaks
        if key == 'q':
            break
        # set the collided to False
        collided = False
        # Create a nested for loop and let the particles collide with eachother in the same list and collide with the walls
        for i in range(0, len(o_list)):
            for j in range(0, len(o_list)):
                # the particle will not collide with itself
                if o_list[i] != o_list[j]:
                    # if collision happens
                    if cl.collision(o_list[i], o_list[j], dt) == True:
                        # set the collided to True
                        collided = True
                for k in shapes:
                    # if the collision hapens
                    if cl.collision(o_list[i], k, dt) == True:
                        # set collided to True
                        collided = True

            # if collided is equal to False
            if collided == False:
                # call the update method of the ball with dt as the time step
                o_list[i].update(dt)

        # set the initial number of particles at the left side and right side
        left1 = 0
        right1 = 0
        # create an empty list
        avg_velocity1 = []
        # for i in the o_list
        for i in o_list:
            # if the position of the particle is at the right side of the box
            if i.getPosition()[0] > 45:
                # right side number plus one
                right1 += 1
            # if the position of the particles is at the left side of the box
            if i.getPosition()[0] < 45:
                # left side number plus one
                left1 += 1
            # get the velocity of the particles in the x direction and the y direction
            velocityx = i.getVelocity()[0]
            velocityy = i.getVelocity()[1]
            # speed is the square root of the Vx square plus Vy square
            speed = math.sqrt(velocityx * velocityx + velocityy * velocityy)
            # append the speed to the list
            avg_velocity1.append(speed)
            # global the avg_v1
            global avg_v1
            # use the stat module to calculate the average velocity
            avg_v1 = stat.mean(avg_velocity1)

        # append the number of left side and right side particles
        leftlist1.append(left1)
        rightlist1.append(right1)
        # open file and write the data
        fp = open("extract.csv", "a")
        # record the changing process of left side and right side particles
        fp.write(str(left1) + ',' + str(right1) + ',' + str(avg_v1) + '\n')
        # if the particles reaches equilibrium, break the while loop
        if left1 <= 10:
            break
        # increment frame
        frame += 1
    # close the window
    win.close()
    # record the end time
    end_time = time.time()
    # calculate the time elapsed
    time_elapsed = end_time - start_time
    # return the time passed
    return time_elapsed

def instructions():
    """this function can show instructions for users"""
    # create a GraphWin
    win = gr.GraphWin('instructions', 500, 500, True)
    #create texts
    message = gr.Text(gr.Point(240,100), "Hello! please enter the start times of temperature ")
    message2 = gr.Text(gr.Point(200,150),' and then enter end times of temperature')
    message3 = gr.Text(gr.Point(250,200),'finally the steps you want to take into the command line')
    #set the font bigger
    message.setSize(18)
    message2.setSize(18)
    message3.setSize(18)
    #draw them
    message.draw(win)
    message2.draw(win)
    message3.draw(win)
    #set color of texts
    message.setTextColor("red")
    message2.setTextColor("red")
    message3.setTextColor("red")


if __name__ == "__main__":
    instructions()
    # create to lists
    speedlist = []
    timelist = []
    # set the user inputs
    base_case = float(input('the start times of temperature: '))
    end_case = float(input('the end times of temperature: '))
    step = float(input('the step you want to take: '))
    # create a for loop to simuate the process many times
    for i in np.arange(base_case, end_case, step):
        # append the time passed to the list
        timelist.append(main(i))
        # append the average speed to the list
        speedlist.append(avg_v1)

    # use matplotlib to automate the process of ploting data
    plt.plot(speedlist, timelist)
    plt.title("The time to reach euilibrium")
    plt.xlabel("speed")
    plt.ylabel("time")
    plt.show()
