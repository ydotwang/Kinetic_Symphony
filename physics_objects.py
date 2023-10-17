"""
Yuyang Wang
CS152 sectionB
Lab 10
12/6/2022

Call this file like this:
python3 physica_objects.py

new classses such as Ball, Block, and bonds are made in this file

This file can be imported to other files

This file is based on the concept of parent class and child class(inheritance)

Different methods were define for the classes

"""


import graphicsPlus as gr
import random
import time



class Thing (object):
    """the parent class"""
    def __init__(self, win, the_type):
        # A string, indicating the type of the object.               (e.g., self.type = the_type)
        self.type = the_type
        self.mass = 1  # give it an initial value of 1.
        # this will be a two-element list, representing the x and y location values. Give the x and y positions initial values of 0.
        self.position = [0, 0]
        # a two-element list, with initial values of 0.
        self.velocity = [0, 0]
        # a two-element list, with initial values of 0.
        self.acceleration = [0, 0]
        # The amount of energy retained after a collision.
        self.elasticity = 1
        # The scale factor between the simulation space and pixels. Default to 10.
        self.scale = 10
        # An empty list that will hold Zelle graphics.
        self.vis = []
        # An (r, g, b) tuple. A good default value is black (0, 0, 0)
        self.color = (0, 0, 0)
        # A boolean indicating if the shape has been drawn, initially False.
        self.drawn = False
        # A reference to the GraphWin object representing the window.
        self.win = win

    def getPosition(self):
        """this function can get the position of the object, return the position"""
        # returns a 2-element tuple with the x, y position.
        return self.position[:]

    def getVelocity(self):
        """this function can get the velocitiy of the object, return the velocity"""
        return self.velocity[:]

    def getAcceleration(self):
        """this function can get the acceleration of the object, return the acceleration"""
        # returns a 2-element tuple with the x and y acceleration values.
        return self.acceleration[:]

    def getMass(self):
        """this function can get the mass of the object, return the mass value"""
        # Returns the mass of the object as a scalar value
        result = self.mass
        return result

    def getElasticity(self):
        """this function can get the elasticity of the object, return the elasticity value"""
        result = self.elasticity
        return result

    def getColor(self):
        """this function can get the color of the object, return the color tuple"""
        result = self.color
        return result

    def getType(self):
        """this function can get the type of the object, return the type string"""
        result = self.type
        return result

    def draw(self):
        """this function can draw all the objects"""
        # loop over the self.vis list of graphics objects and draw them into the window specified by self.win
        for i in self.vis:
            i.draw(self.win)
        # draw method should finish by setting self.drawn to True.
        self.drawn = True

    def undraw(self):
        """this function can undraw the onjects"""
        # undraw method should also loop over the self.vis list of graphics objects and undraw each one
        for i in self.vis:
            i.undraw()
        # The undraw method should finish by setting self.drawn to False
        self.drawn = False

    def setPosition(self, px, py):
        """this function can set the position of the object, two parameters, new x value and new y value"""
        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # assign to the x coordinate in self.pos the new x coordinate
        self.position[0] = px
        # assign to the y coordinate in self.pos the new y coordinate
        self.position[1] = py
        # assign to dx the change in the x position times self.scale
        dx = (self.position[0]-x_old) * self.scale
        # assign to dy the change in the y position times -self.scale
        dy = (self.position[1]-y_old) * (-self.scale)
        # for each item in the vis field of self
        for i in self.vis:
            # call the move method of the item, passing in dx and dy
            i.move(dx, dy)

    def setVelocity(self, vx, vy):
        """this funtion can set the velocity of the call, two parameters, Vx value and Vy value"""
        # vx and vy are the new x and y velocities
        self.velocity[0] = vx
        self.velocity[1] = vy
        return self.velocity[:]

    def setAcceleration(self, ax, ay):
        """this function can set the acceleration of the ball, two parameters, Ax and Ay ,in x direction and y direction"""
        # ax and ay are new x and y accelerations.
        self.acceleration[0] = ax
        self.acceleration[1] = ay
        return self.acceleration[:]

    def setMass(self, m):
        """this function can set the mass, one parameter, the mass of the ball"""
        # m is the new mass of the object
        self.mass = m
        return self.mass

    def setElasticity(self, e):
        """this function can set the elasticity of the ball"""
        self.elasticity = e
        result = self.elasticity
        return result

    def setColor(self, c):  # takes in an (r, g, b) tuple
        """set the color of the object"""
        self.color = c
        for i in self.vis:
            i.setFill(gr.color_rgb(c[0], c[1], c[2]))

    def update(self, dt):
        """this function can update the pbject, one parameter, the tims passed"""
        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]
        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = x_old + self.velocity[0] * \
            dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt
        self.position[1] = y_old + self.velocity[1] * \
            dt + 0.5*self.acceleration[1] * dt*dt
        # assign to dx the change in the x position times the scale factor (self.scale)
        dx = (self.position[0]-x_old) * self.scale
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        dy = (self.position[1]-y_old) * (-self.scale)
        # for each item in self.vis
        for i in self.vis:

            # call the move method of the graphics object with dx and dy as arguments..
            i.move(dx, dy)
        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] += dt * self.acceleration[0]
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] += dt * self.acceleration[1]


class Ball(Thing):
    """the child class"""
    def __init__(self, win, x0=0, y0=0, color=(255, 255, 51), radius=0.5):

        Thing.__init__(self, win, "ball")
        # self x position
        self.x0 = x0
        # self y position
        self.y0 = y0
        # self color tuple
        self.color = color
        self.win = win
        # self radius
        self.radius = radius
        # position list
        self.position = [x0, y0]
        self.refresh()
        self.setColor(self.color)
        self.type = 'ball'

    def refresh(self):
        """This function can undraw and draw the object again"""
        drawn = self.drawn
        # if the object is drawn
        if drawn:
            # undraw
            self.undraw()
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight() -
                              self.position[1]*self.scale), self.radius * self.scale)]
        # if drawn, draw the object
        if drawn:
            self.draw()

    def getRadius(self):
        """this function can get the radius of the ball"""
        # Returns the radius of the Ball as a scalar value
        result = self.radius
        return result

    def setColor(self, c):  # takes in an (r, g, b) tuple
        """set the color of the object"""
        self.color = c
        for i in self.vis:
            i.setFill(gr.color_rgb(c[0], c[1], c[2]))

    def collision(self, ball):
        """this function can detect the collision"""
        if abs(ball.getPosition()[0] - self.position[0]) <= 2 * ball.getRadius() and abs(ball.getPosition()[1] - self.position[1]) <= 2 * ball.getRadius():
            return True
        else:
            return False

    


class Ball2(Thing):
    """the child class"""
    def __init__(self, win, x0=0, y0=0, color=(220, 20, 60), radius=0.5):

        Thing.__init__(self, win, "ball")
        # self x position
        self.x0 = x0
        # self y position
        self.y0 = y0
        # self color tuple
        self.color = color
        self.win = win
        # self radius
        self.radius = radius
        # position list
        self.position = [x0, y0]
        self.refresh()
        self.setColor(self.color)
        self.type = 'ball'

    def refresh(self):
        """This function can undraw and draw the object again"""
        drawn = self.drawn
        # if the object is drawn
        if drawn:
            # undraw
            self.undraw()
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight() -
                              self.position[1]*self.scale), self.radius * self.scale)]
        # if drawn, draw the object
        if drawn:
            self.draw()

    def getRadius(self):
        """this function can get the radius of the ball"""
        # Returns the radius of the Ball as a scalar value
        result = self.radius
        return result

    def collision(self, ball):
        """this function can detect the collision"""
        if abs(ball.getPosition()[1] - self.position[1]) <= 2 * ball.getRadius():
            return True
        else:
            return False


class Block(Thing):
    """a child class"""
    def __init__(self, win, width = 2,height = 1,x0=0, y0=0, color=None):
        Thing.__init__(self, win, 'block')
        self.win = win
        #the width of the block
        self.width = width
        # the height of the block
        self.height = height
        # the position x 
        self.x0 = x0
        # the position y
        self.y0 = y0
        # the position list
        self.position = [x0, y0]
        self.reshape()
        # the color of the object
        self.color = color
        self.type = 'block'

    def reshape(self):
        """this function can undraw and draw the object again"""
        drawn = self.drawn
        if drawn:
            self.undraw()
        self.vis = [gr.Rectangle(gr.Point(self.x0 - self.width / 2 * self.scale, self.win.getHeight() - self.y0 * self.scale - self.height / 2 * self.scale),
                                 gr.Point(self.x0 + self.width / 2 * self.scale, self.win.getHeight() - self.y0 * self.scale + self.height / 2 * self.scale))]

        if drawn:
            self.draw()

    def getWidth(self):
        """this function can get the width of the blcok, return a integer"""
        result = self.width
        return result

    def getHeight(self):
        """this function can get the height of the block, return a integer"""
        result = self.height
        return result

    def setWidth(self, dx):
        """this function can set the width of the block"""
        self.width = dx
        # cal the reshape method
        self.reshape

    def setHeight(self, dy):
        """this function can set the height of the block"""
        self.height = dy
        # cal the reshape method    
        self.reshape

    def collision(self, ball):
        """this function can detect the collision"""
        if abs(ball.getPosition()[1] - self.position[1]) <= 2 * ball.getRadius():
            return True
        else:
            return False



class bonds(Thing):
    """this is a child class"""
    def __init__(self, win, x0=0, y0=0, color=(0, 0, 0), radius=0.5):
        Thing.__init__(self, win, "ball")
        # the x position
        self.x0 = x0
        # the y position 
        self.y0 = y0
        # the self color
        self.color = color
        # self window
        self.win = win  
        # the self radius
        self.radius = radius
        # the self position
        self.position = [x0, y0]
        # the self width
        self.width = 1.2
        # the self height
        self.height = 1.2
        # the vis list
        self.vis = []
        # append the shape of the bird, the eyes and the mouth
        self.vis.append(gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight() -
                              self.position[1]*self.scale), self.radius * self.scale))

        self.vis.append(gr.Circle(gr.Point(self.position[0]*self.scale + 10, self.win.getHeight() -
                              self.position[1]*self.scale + 2), self.radius * self.scale))
        self.refresh()
        # set the colors
        self.vis[0].setFill(gr.color_rgb(220, 20, 60))
        self.vis[1].setFill(gr.color_rgb(255, 255, 51))


        self.type = 'ball'

    def refresh(self):
        """this function can undraw and draw the object again"""
        drawn = self.drawn
        if drawn:
            self.undraw()

        if drawn:
            self.draw()

    def getRadius(self):
        """this function can get the radius of the bird"""
        result = self.radius
        return result
        

