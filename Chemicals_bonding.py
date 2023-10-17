"""
Yuyang Wang
CS152 sectionB
Lab 10 Final project
12/6/2022

Call this file like this:
python3 Extensional_Bonding.py

This file can simulate the particles bonding process. Everytime two particles collide with each other, they will make a bond.

User can input the start times of temperature and the end times of temperature and the how many steps to go from start to end.

User can quit the simulation by typing 'q' on the keyboard

With the increase of temperature, the velocity of the particles goes up. 

The velocity of the particles goes up causes the bonding process to be faster.

Each simulation would last 5 seconds

The percent bonded can be calculated.

The main function will run for a couple of times and automate the process of ploting a graph

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
    """This function can simulate the bonding process. This function takes scale as its argument and return the perent bonded value"""
    # create a GraphWin
    win = gr.GraphWin('bonding', 1000, 500, False)
    
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
    p_list = []
    # create 50 particles using a for loop
    for i in range(50):
        # create particles using physics objects module
        particle = pho.Ball(win)
        # set the random position of particles to the left side
        particle.setPosition(random.randint(10, 40), random.randint(15, 35))
        # set the random velocity of the particles and times the scale
        particle.setVelocity(random.randint(-20, 20) * scale,
                           random.randint(-20, 20) * scale)
        # set the acceleration to 0
        particle.setAcceleration(0, 0)
        # append the particle to the list
        p_list.append(particle)
        # draw the particle
        particle.draw()
    # create an empty list
    p_list2 = []
    # create 50 particles using a for loop
    for i in range(50):
        # create particles using physics objects module
        particle = pho.Ball2(win)
        # set the random position of particles to the right side
        particle.setPosition(random.randint(50, 80), random.randint(15, 35))
        # set the random velocity of the particles and times the scale
        particle.setVelocity(random.randint(-20, 20) * scale,
                           random.randint(-20, 20) * scale)
        # set the acceleration to 0
        particle.setAcceleration(0, 0)
        # append the particle to the list
        p_list2.append(particle)
        # draw the particle
        particle.draw()
    # create an empty list
    balls = []
    # record the starttime
    timestart = time.time()
    # start an infinite loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            # call win.update()
            win.update()
        # using checKey, if the user typed a 'q' then break
        key = win.checkKey()
        # if user type q, break the loop
        if key == 'q':
            break
        # set the collided to False
        collided = False
        # Create a nested for loop and let the particles collide with eachother in the same list and collide with the walls
        for i in range(0, len(p_list)):
            for j in range(0, len(p_list)):
                # the particle will not collide with itself
                if p_list[i] != p_list[j]:
                    # if collision happens
                    if cl.collision(p_list[i], p_list[j], dt) == True:
                        
                        collided = True
                for k in shapes:
                    # if collision hapens
                    if cl.collision(p_list[i], k, dt) == True:
                        # set collided to True
                        collided = True

            # if collided is equal to False
            if collided == False:
                # call the update method of the ball with dt as the time step
                p_list[i].update(dt)
        # Create a nested for loop and let the particles collide with eachother in the same list and collide with the walls
        for i in range(0, len(p_list2)):
            for j in range(0, len(p_list2)):
                # the particle will not collide with itself
                if p_list2[i] != p_list2[j]:
                    # if collision happens
                    if cl.collision(p_list2[i], p_list2[j], dt) == True:
                        # set the collided to True
                        collided = True
                for k in shapes:
                    # if the collision hapens
                    if cl.collision(p_list2[i], k, dt) == True:
                        # set collided to True
                        collided = True

             # if collided is equal to False
            if collided == False:
                # call the update method of the ball with dt as the time step
                p_list2[i].update(dt)

        # create a nested for loop
        for particle1 in p_list2:
            # initialize i = 0
            i = 0
            for particle2 in p_list:
                # if i = 1 break the for loop
                if i == 1:
                    break
                # if colision hapens between to different particles
                if particle2.collision(particle1) == True:
                    # get the velocity and the position of one particle
                    v1 = particle1.getVelocity()
                    p1 = particle1.getPosition()
                    # generate a new bond
                    ball = pho.bonds(win)
                    # set the position
                    ball.setPosition(p1[0], p1[1])
                    # set the velocity
                    ball.setVelocity(v1[0], v1[1])
                    # set the acceleration
                    ball.setAcceleration(0, 0)
                    # draw the bond
                    ball.draw()
                    # append this bond to list
                    balls.append(ball)
                    # undraw and remove two particles from the original list
                    particle2.undraw()
                    p_list.remove(particle2)
                    particle1.undraw()
                    p_list2.remove(particle1)
                    # i plus one
                    i += 1
        # create a nested for loop to simulate bonded chemicals collide with eachother
        for i in range(0, len(balls)):
            for j in range(0, len(balls)):
                # the particle will not collide with itself
                if balls[i] != balls[j]:
                    # if collision hapens
                    if cl.collision(balls[i], balls[j], dt) == True:
                        # set collided to True
                        collided = True
                # create a for loop to simulate the collision with walls
                for k in shapes:
                    # if collision hapens
                    if cl.collision(balls[i], k, dt) == True:
                        # set collided to True
                        collided = True
          # if collided is equal to False
            if collided == False:
                # call the update method of the ball with dt as the time step
                balls[i].update(dt)

        # initialize the particle number
        number_of_particle1 = 0
        # create a for loop to calculate the number of bonded particles
        for i in range(len(p_list2)):
            # set number plus one
            number_of_particle1 += 1
        # calculate the bonded number
        bonded = 50 - number_of_particle1
        # calculate the percent bonded
        percent_bonded = bonded/50

        # record the time
        timenow = time.time()
        # if time elapse 5 seconds
        if timenow - timestart > 5:
            # break the while loop
            break

        # increment frame
        frame += 1
    # create a empty list
    avg_velocity1 = []
    # create a for loop
    for i in p_list:
        # get the velocity of particle in x direction and y direction
        velocityx = i.getVelocity()[0]
        velocityy = i.getVelocity()[1]
        # calculate the speed using square root of Vx squsre plus Vy square
        speed = math.sqrt(velocityx * velocityx + velocityy * velocityy)
        # append the speed
        avg_velocity1.append(speed)
        #global avg_v1
        global avg_v1
        # calculate the average speed
        avg_v1 = stat.mean(avg_velocity1)

    # close the window
    win.close()
    # return the percent bonded
    return percent_bonded

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
    # create two lists
    instructions()
    speedlist = []
    percentlist = []
    # create user input
    base_case = float(input('the start times of temperature: '))
    end_case = float(input('the end times of temperature: '))
    step = float(input('the step you want to take: '))
    #create a for loop 
    for i in np.arange(base_case, end_case, step):
        #append the percent bonded
        percentlist.append(main(i))
        #append the average speed
        speedlist.append(avg_v1)
    #automate the ploting process
    plt.plot(speedlist, percentlist)
    plt.plot(speedlist, percentlist,'x')
    plt.title("Bonded rate (%)")
    plt.xlabel("speed of particles")
    plt.ylabel("percent bonded")
    plt.show()
