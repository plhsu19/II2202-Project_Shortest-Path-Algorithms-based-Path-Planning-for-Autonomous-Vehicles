#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# {student full name}
# {student id}
# {student email}
# Notice: This is a private project extended from the 
# lab assignment of "DD2410 Introduction to Robotics" offered by KTH, Sweden.
# The simualtion environments and plot modules are provided by and downloaded from 
# course's Github: https://github.com/cisprague/dubins.git

from dubins import *
import math

dt = 0.01

class Node(object):
    def __init__(self, car, x, y, theta, costG, parent = None):
        self.car = car
        self.x = x
        self.y = y
        self.theta = theta
        self.costG = costG
        self.parent = parent

        #other instance variables initialized by the instance method:
        self.costH = 0.0 #initialized by set_cost
        self.cost = 0.0  #initialized by set_cost

        self.time = 0
        self.phi = 0 # turning anle from parent node

    
    def set_cost(self):
        self.costH = math.sqrt(((self.x - self.car.xt)**2 + (self.y - self.car.yt)**2))
        self.cost = self.costG + 3 * self.costH
    
    def verify_goal(self):
        d = math.sqrt(((self.x - self.car.xt)**2 + (self.y - self.car.yt)**2))
        if d <= 1.2:
            return True
        else: 
            return False
def update_next_nodes(car, c_node, timesteps = 30):
    # the list containing available next nodes
    next_nodes = []
    # three steering directions
    steering = [-math.pi/4.0, 0.0, math.pi/4.0]
    # generate primitive three next nodes
    for dir in steering:
        k = -1
        xn = c_node.x
        yn = c_node.y
        thetan = c_node.theta
        for i in range(timesteps):
            k = i
            xn, yn, thetan = step(car, xn, yn, thetan, dir)
            #check if next step nodes are within boundaries and not near obstacles
            if not verify_node(car, xn, yn):
                break
        if k == (timesteps - 1):
            n_costG = c_node.costG + 0.01 * timesteps
            n_node = Node(car, xn, yn, thetan, n_costG, c_node) 
            n_node.set_cost() #initialize cost_H and cost
            n_node.time = c_node.time + timesteps
            n_node.phi = dir
            next_nodes.append(n_node)
    return next_nodes
    

def verify_node(car, x, y):
    if x > car.xub:
        return False
    if x < car.xlb:
        return False
    if y > car.yub:
        return False
    if y < car.ylb:
        return False
    for ob in car.obs:
        if math.sqrt((x - ob[0])**2 + (y - ob[1])**2) < (ob[2] + 0.5):
            return False
    return True

def solution(car):

    ''' <<< write your code below >>> '''
    print(__file__ + " start!!")
    #list of turning angle
    controls=[] 
    #list of turning time times[0]-->times[1] wrt controls[0]
    times=[]
    #initialize start node, initialize cost function
    theta0 = 0.0
    nstar = Node(car, car.x0, car.y0, theta0, 0.0) 
    nstar.set_cost()
    print("start position: (", nstar.x, ", ", nstar.y, ")")
    print("goal position: (", car.xt, ", ", car.yt, ")")
    #initial open set, closed set:
    open_set = [] #changed to grid based map, dictionary
    closed_set = []
    #add start node into openset
    open_set.append(nstar)
    c = 1
    #while loop to explore the path when openset is not empty
    while len(open_set) != 0:
       print("Visited node number: ", c)
       print("\n")
       print("\n")
       #choose the node with smallest cost value from open set
       c_node = min(open_set, key=lambda o: o.cost)
       print("current node position: (", c_node.x, ", ", c_node.y, ")")
       print("current costG = ", c_node.costG)
       print("current theta = ", c_node.theta)
       print("current phi = ", c_node.phi)
       print("current costH = ", c_node.costH)
       print("current cost = ", c_node.cost)
       print("current time = ", c_node.time)
       if c_node.parent == None:
           print("current parent = None")
       else:
           print("current parent != None")
       print("\n")
       print("\n")
       #remove current node from open set
       open_set.remove(c_node)
       #add current node into close set
       closed_set.append(c_node)
       #check if current node reach the goal
       if c_node.verify_goal() or c >= 2000:
           print("Find goal")
           # start to contruct the path by building times list and controls list
           times.insert(0, c_node.time * dt)
           controls.insert(0, c_node.phi)
           #trace back until there is no parent node, ie, current node is the start node
           while True:
               if c_node.parent == None:
                   controls.pop(0)
                   break
               else:
                   c_node = c_node.parent
                   times.insert(0, c_node.time * dt)
                   controls.insert(0, c_node.phi) # need to be poped out if c_node is start node
           break
       else:
           #update list of neighbor nodes
               next_nodes = update_next_nodes(car, c_node)
               for n_node in next_nodes:
                   if n_node in closed_set: #ne effect here
                       continue
                   else:
                       open_set.append(n_node)
       c += 1

    ''' <<< write your code below >>> '''
    
    print(controls)
    print(times)
    return controls, times
