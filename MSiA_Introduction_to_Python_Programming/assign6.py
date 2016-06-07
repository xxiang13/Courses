# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:31:15 2015

@author: Xiang Li
http://effbot.org/imagingbook/introduction.htm#reading-and-writing-images
http://pillow.readthedocs.org/en/latest/reference/PixelAccess.html
"""
#import os
#os.chdir("/Users/apple/Documents/MSiA/Spring 2015/MSiA 490 Python/hw6")

from PIL import Image
import graph
import graphalgorithms as galgo
import math
      
def Distance(p1,p2):
     dist_sqr = 0
     for x,y in zip(p1,p2): 
         xy = (x - y)**2
         dist_sqr = dist_sqr + xy
     distance = math.sqrt(dist_sqr)
     return distance    
     
def forEachNodeCC(node, cc):
        node.cc = cc

#pic_path = input('Enter the path of picture: ')
#resolution = float(input('Enter level of image resolution (lower input number, higher resolution): '))

def imSegment(pic_path,resolution):
    im = Image.open(pic_path)
    (width, height) = im.size
    rgb_im = im.convert("RGB")
    
    g = graph.UndirectedGraph()
    for x in range(width):
        for y in range(height):  
            pixel = g.addVertex((x,y))
            pixel.location = (x,y)
            for a in range(x-1,x+2):
                for b in range(y-1,y+2):
                    if a >=0 and a < width and a !=x and b != y and b >= 0 and b < height:
                        rgb1 = rgb_im.getpixel((x,y))
                        rgb2 = rgb_im.getpixel((a,b))
                        rgbDistance = Distance(rgb1,rgb2)
                        if rgbDistance < resolution:
                            edge = g.addEdge((x,y),(a,b))
    
    cc_list = galgo.connectedComponents(g, forEachNodeCC)
    
    colorDict = dict()
    for cc in cc_list.keys():
        R,G,B = 0,0,0
        c = 0
        for p in cc_list[cc]: 
            x,y,z = rgb_im.getpixel(p.name)
            R,G,B = R+x,G+y,B+z
            c = c+1
        avgR,avgG,avgB = R/c,G/c,B/c
        colorDict[cc] = round(avgR),round(avgG),round(avgB)
    
    for v in g.vertexes():
        p = v.name
        color = colorDict[g._vertexes[p].cc]
        im.putpixel(p,color)
    im.show()