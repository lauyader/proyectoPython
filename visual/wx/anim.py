#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################################################
#
#    File Name:    anim.py
#    Description:  generate animation window
#
#######################################################################

#######################################################################
#
#    Author:       esnmlt@gmail.com	
#    Blog:         http://blog.zesn.info (in English)
#                  http://zesn.blogspot.com (in Chinese)
#    Upadate:
#      2009/03/19  File founded
#
#
#######################################################################

from __future__ import division

import visual as v


class Animation(object):
    # Creating parameters
    side = 10.0 
    thk = 0.9 
    pos = [0,0.75*side,-2*side]
    interval = 50
    roadsize = [[0,1.5*side], [-2*side,side]]

    def __init__(self, configfile=None, datafile=None):

        self.cars = {}
        self.colors = [v.color.green, (1,1,0)]
        self.roads = {}
        self.roadcolor = (0, 0, 1)
        self.labels = {}

        v.scene.title = "Demo of Vpython & wxPython"
        v.scene.x = 0
        v.scene.y = 0
        v.scene.width = 600
        v.scene.height = 400
        v.scene.forward = (-0.4,-0.3,-1)
        v.scene.background=v.color.white
        v.scene.center = (0,0,0)
        #v.scene.autoscale = 0

        self.reset()
    

    def reset(self):

        colorIdx = 0
        i = 0
        pos = self.pos
        # pos = time,x, y
        # x -> z, y -> x, self.thk -> y
        self.addcar(pos = (pos[2],self.thk,pos[1]), color=self.colors[colorIdx], name="v%s"%i)
        #colorIdx = (colorIdx+1)%len(self.colors)

        roadsize = self.roadsize
        # x -> z, y -> x, self.thk -> y
        pos = ((roadsize[1][0]+roadsize[1][1])/2.0, 0, (roadsize[0][0]+roadsize[0][1])/2.0)
        size = (abs(roadsize[1][0]-roadsize[1][1]), self.thk, abs(roadsize[0][0]-roadsize[0][1]))
        self.addroad(pos=pos, size=size, color = self.roadcolor)


    def addcar(self, pos, color=v.color.green, name="v"):
        # Creating car 
        car = v.frame()
        car.start = pos
        car.pos = car.start
        car.vector = v.vector(0.05, 0, 0) 
        car.color = color
        car.colorori = car.color

        body = v.box(frame = car, pos = (0,0,0), size = (2.4*self.thk, 0.6*self.thk, 1.4*self.thk), color = car.colorori) 
        wheel1 = v.cylinder(frame=car, pos=(0.8*self.thk,-0.2*self.thk,0.8*self.thk), axis=(0,0,-1.6*self.thk), radius=0.25*self.thk, color=(0.6,0.6,0.6)) 
        wheel2 = v.cylinder(frame=car, pos=(-0.8*self.thk,-0.2*self.thk,0.8*self.thk), axis=(0,0,-1.6*self.thk), radius=0.25*self.thk, color=(0.6,0.6,0.6)) 
        head = v.convex(frame=car, color=car.colorori)
        head.append(pos=v.vector(0.6, 0.3, -0.7)*self.thk)
        head.append(pos=v.vector(0.6, 0.3, 0.7)*self.thk)
        head.append(pos=v.vector(-1.2, 0.3, -0.7)*self.thk)
        head.append(pos=v.vector(-1.2, 0.3, 0.7)*self.thk)
        head.append(pos=v.vector(0.4, 0.7, -0.6)*self.thk)
        head.append(pos=v.vector(0.4, 0.7, 0.6)*self.thk)
        head.append(pos=v.vector(-0.8, 0.7, -0.6)*self.thk)
        head.append(pos=v.vector(-0.8, 0.7, 0.6)*self.thk)

        # Creating Label
        car.vlabel = v.label(justify='center', pos=car.pos, xoffset=3*self.thk, yoffset=39*self.thk, space=3*self.thk, text=name,height=15, line=0,border=3)

        self.cars[name] = car
        self.labels[name] = car.vlabel


    def addroad(self, pos, size, color):
        road = v.box(pos=pos, size=size, lit=False, color = color)
        self.roads["r%d"%(len(self.roads))] = road


    def caract(self, car, direct=1):
        x = self.cars[car].x + (self.roadsize[1][1] - self.roadsize[1][0])/self.interval*direct
        if x > self.roadsize[1][1]:
            x = self.roadsize[1][0]
        if x < self.roadsize[1][0]:
            x = self.roadsize[1][1]

        self.cars[car].x = x
        #self.cars[car].visible = 1
        self.cars[car].vlabel.pos = self.cars[car].pos



    def update(self, direct=1):
        for name,value in self.cars.iteritems():
            self.caract(name, direct)



if __name__ == '__main__':
    anim = Animation()
    anim.reset()
    while True:
        v.rate(10)
        anim.update()
