"""
Yuyang Wang
CS152 sectionB
Lab 10 Final project
12/6/2022

Call this file like this:
python3 Extensional_Bonding.py

This file can simulate the particles separate process.

User can input the start times of temperature and the end times of temperature and the how many steps to go from start to end.

User can quit the simulation by typing 'q' on the keyboard

With the increase of temperature, the velocity of the particles goes up. 

The velocity of the particles goes up causes the separating process.

Each simulation would last 5 seconds

The percent separated can be calculated.

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
    
    """ Create all of the obstacles in the scene and put them in a list. The return value would be a list of objects"""
    # Each obstacle should be a Thing (e.g. Ball, Block, other)
    # make a empty list to contain blocks
    blocks1 = []

    # make two long blocks
    for i in range(2):
        longblock = pho.Block(win, width=1.5, height=35)
        # set the position
        longblock.setPosition(5+80*i , 27)
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

        # creat a topblock
    topblock = pho.Block(win, width=90, height=1.5)
    # set the position
    topblock.setPosition(45, 12)
    # set the color of the block
    topblock.setColor((193, 83, 100))
    # append this object to the list
    blocks1.append(topblock)



    # Return the list of Things
    return blocks1


def main(scale):

    # create a GraphWin
    win = gr.GraphWin('balls colliding', 1000, 500, False)
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
    bonds = []
    # create 50 bonds using a for loop
    for i in range(50):
        # create bonds using physics objects module
        bond = pho.bonds(win)
        # set the random position of bonds to the left side
        bond.setPosition(random.randint(50,80),random.randint(15,35))
        # set the random velocity of the bonds and times the scale
        bond.setVelocity(random.randint(-20,20) * scale,random.randint(-20,20) * scale)
        # set the acceleration to 0
        bond.setAcceleration(0,0)
        # append the bond to the list
        bonds.append(bond)
        # draw the bond
        bond.draw()
    #create two empty lists
    balls = []
    balls2 = []
    #record the start time
    timestart = time.time()
    
    # start an infinite loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            # call win.update()
            win.update()
        # using checKey, if the user typed a 'q' then break
        key = win.checkKey()
        if key == 'q':
            break
        # set the collided to False
        collided = False
        # Create a nested for loop and let the bonds collide with eachother in the same list and collide with the walls
        for i in range(0,len(bonds)):
            for j in range(0,len(bonds)):
                # the bond will not collide with itself
                if bonds[i] != bonds[j]:
                    # if collision happens
                    if cl.collision(bonds[i], bonds[j], dt) == True:
                        # set the collided to True
                        collided = True
                for k in shapes:
                    # if collision hapens
                    if cl.collision(bonds[i], k, dt) == True:
                        # set collided to True
                        collided = True


            

            # if collided is equal to False
            if collided == False:
            # call the update method of the ball with dt as the time step
                    bonds[i].update(dt)

        #record the time now
        timenow = time.time()
        # create an empty list
        avg_velocity1 = []
        # if time past two seconds
        if  timenow - timestart > 2:
            # loop over bonds list
            for i in bonds: 
                        # get the bond velocity in x and y direction
                        velocityx = i.getVelocity()[0]
                        velocityy = i.getVelocity()[1]
                        # calculate the speed
                        speed = math.sqrt(velocityx * velocityx + velocityy * velocityy)
                        # append the speed
                        avg_velocity1.append(speed)
                        #globla the avg
                        global avg_v1
                        #calculate the mean value
                        avg_v1 = stat.mean(avg_velocity1)
                        #if speed exceeds 100 bonds break
                        if speed > 100:
                            # loop over bonds
                            for i in bonds:
                                        #get bond velocity and position
                                        v1 = i.getVelocity()
                                        p1 = i.getPosition()
                                        # set two particles with its velocity and position
                                        ball1 = pho.Ball(win)
                                        ball1.setPosition(p1[0], p1[1])
                                        ball1.setVelocity(v1[0],v1[1])
                                        ball1.setAcceleration(0,0)
                                        #draw them 
                                        ball1.draw()
                                        #append to list
                                        balls.append(ball1)
                                        # set two particles with its velocity and position
                                        ball2 = pho.Ball2(win)
                                        ball2.setPosition(p1[0], p1[1])
                                        ball2.setVelocity(v1[0],v1[1])
                                        ball2.setAcceleration(0,0)
                                        #draw them
                                        ball2.draw()
                                        # append to list
                                        balls.append(ball2)
                                        # undraw the bond
                                        i.undraw()
                                        # remove the bond from its original list
                                        bonds.remove(i)
                        
                    
        # Create a nested for loop and let the particles collide with eachother in the same list and collide with the walls
        for i in range(0,len(balls)):
                for j in range(0,len(balls)):
                    # the particle will not collide with itself
                    if balls[i] != balls[j]:
                        # if collision happens
                        if cl.collision(balls[i], balls[j], dt) == True:
                            # set the collided to True
                            collided = True
                    for k in shapes:
                        # if collision happens
                        if cl.collision(balls[i], k, dt) == True:
                    # set collided to True
                            collided = True
            # if collided is equal to False
                if collided == False:
                # call the update method of the ball with dt as the time step
                        balls[i].update(dt)
        # Create a nested for loop and let the particles collide with eachother in the same list and collide with the walls
        for i in range(0,len(balls2)):
                for j in range(0,len(balls2)):
                    # the particle will not collide with itself
                    if balls2[i] != balls2[j]:
                        # if collision happens
                        if cl.collision(balls2[i], balls2[j], dt) == True:
                            # set the collided to True
                            collided = True
                    for k in shapes:
                        # if collision happens
                        if cl.collision(balls[i], k, dt) == True:
                            # set collided to True
                            collided = True
                 # if collided is equal to False
                if collided == False:
                        # call the update method of the ball with dt as the time step
                        balls2[i].update(dt)
        # initialize number of bonds 1
        number_of_bond = 0
        # create a for loop to calculate how many bonds separated
        for i in range(len(bonds)):
            number_of_bond += 1
        separated = 50 - number_of_bond
        percent_seperated = separated/50

        #record time end 
        timeend = time.time()
        # if time past 5 seconds, break
        if timeend - timestart> 5:
            break
        
        # increment frame
        frame += 1


    
    # close the window
    win.close()
    # return percent_separated
    return percent_seperated

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
    # plt.plot(speedlist, percentlist)
    plt.plot(speedlist, percentlist,'x')
    plt.title("separate rate (%)")
    plt.xlabel("speed of particles")
    plt.ylabel("percent separated")
    plt.show()