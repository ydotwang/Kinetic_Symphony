"""Yuyang Wang
CS152 sectionB
project 10 final project
12/6/2022
serve as "module" which can be imported into other files 
Call this file like this:
python3 test_ball_block_classes.py
This file would test the ball and block classes
"""

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time

# create two balls heading towards one another
def main():
    """This function can test the ball class and block class"""
    # create a window
    win = gr.GraphWin( 'balls colliding', 500, 500, False )
    # create two balls
    ball1 = pho.Ball( win )
    ball2 = pho.bonds( win )
    # set two balls position
    ball1.setPosition( 0, 0 )
    ball2.setPosition( 30, 20 )
    # draw two balls
    ball1.draw()
    ball2.draw()
    # create a block
    Block = pho.Block( win )
    # set position and velocity of the block
    Block.setPosition( 30, 20 )
    Block.setColor((234,93,34))
    # Draw the block
    Block.draw()


    # set up velocity and acceleration so they collide
    ball1.setVelocity( 20, 45 )
    ball2.setVelocity( -20, 20 )
    ball1.setAcceleration( 0, -20 )
    ball2.setAcceleration( 0, -20 )


    # loop for some time and check for collisions
    dt = 0.01
    for frame in range(120):
        # if no collision update
        if not coll.collision_ball_ball( ball1, ball2, dt ):
            ball1.update(dt)
        # if no collision update
        if not coll.collision_ball_ball( ball2, ball1, dt ):
            ball2.update(dt)
        # update win
        if frame % 10 == 0:
            win.update()

        time.sleep(0.5*dt)
        # if checkMouse = None then break
        if win.checkMouse() != None:
            break
    # get mouse
    win.getMouse()
    # close the window
    win.close()

if __name__ == "__main__":
    main()
