# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:58:22 2015

@author: Xiang Li
"""
'''
Assignment 3
This week assignment we explore weighted undirected graphs (http://en.wikipedia.org/wiki/Graph_ %28mathematics%29). You can implement them anyway you think is most appropriate –this design is part of the assignment–. You are allowed to use only the python standard library (http://docs.python.org/3/library/).
At a minimum, your implementation must allow to:
1. create a graph given an adjacency list (implemented as an iterable of iterables). The first two
elements of each sub-iterable will represent a vertex id. An optional third element will be the
edge weight. (Property weight in an edge). Assume weight 1 if a weight is not given.
2. get an iterable to the edges and another to get an iterable to the vertexes. (This mechanism will
naturally allow to assign arbitrary properties to edges and vertexes).
'''

'''
At a minimum, your implementation must allow to:
1. create a graph given an adjacency list (implemented as an iterable of iterables). The first two
elements of each sub-iterable will represent a vertex id. An optional third element will be the
edge weight. (Property weight in an edge). Assume weight 1 if a weight is not given.
2. get an iterable to the edges and another to get an iterable to the vertexes. (This mechanism will
naturally allow to assign arbitrary properties to edges and vertexes).

'''
import random
import math
import time
import matplotlib.pyplot as plt
#%%Exercise 1:
'''
1. Provide a function for creating a random graph with v (an integer) vertices and e (an integer) edges.
2. Provide a mechanism for assigning a random location to each vertex of a graph. Do this by assigning a location property to each vertex that consists of a 2-tuple of floats between 0 and 1. Hint: Use mechanism 2 above as your interface.
3. Provide a mechanism for assigning the weight to each vertex of a graph equal to the euclidean distance between its two vertexes. Note that this assumes that the vertexes have a location property. Hint: Use mechanism 2 above as your interface.
'''

'''
@ create 3 classes: graph, vertex and edge
'''
class Vertex:
    def __init__(self, id):      
        self.id = id
        self.location = (None,None)
        
    def setLocation(self,x,y):
        self.location = (x,y)
    
    #vertices_id = []
    #location = (x1,y1)
    #xvertices = dict()
 
class Edge:
    def __init__(self, id):
        self.id = id
        self.edge_pair = (None, None)
        self.edge_weight = 1
    
    def setNodePair(self,v1,v2):
        self.edge_pair = (v1,v2)
    
    def setWeight(self, weight):
        self.edge_weight = weight
    
   
class Graph:
     def __init__(self, id):      
         self.id = id
         self.edgeList = dict()
         self.vertexList = dict()
         self.adjacencyList = dict()
         self.adList = dict()
         self.edgePair = dict ()
         #self.group = dict()
     
#findAdlist() to get adList. adList is a dictionary which has key: vertex; value: all other vertex(es) connected to key     
     def findAdlist(self): 
        k = self.adjacencyList
        k = list(k.keys())
        for x,y in k:
            if x not in self.adList:
                self.adList[x] = set([y])
            else:
                self.adList[x].add(y)    
            if y not in self.adList:
                self.adList[y] = set([x])
            else:
                self.adList[y].add(x)

def distance(p1,p2): # compute distance of two vertex
     dist_sqr = 0
     for x,y in zip(p1,p2): 
     #Zip: took any number of sequences and returned a list of tuples.
         xy = (x - y)**2
         dist_sqr = dist_sqr + xy
     distance = math.sqrt(dist_sqr)
     return distance
     

def randomGraph(v,e,gid=None,connected=False):
     max_e = e*(e-1)/2
     if e > max_e:
         raise RuntimeError("Exceed max number of edges"+str(max_e))
     
     if connected and e < v-1:
         raise RuntimeError("less than min number of edges"+str(v-2))
        
     graph = Graph(gid)
     graph.connected = connected
     
     for i in range(v):
        vobj = Vertex(i)
        x = random.random()
        y = random.random()
        vobj.setLocation (x,y)      
        graph.vertexList[vobj.id]= vobj

     allV = set(range(v))
     a = random.choice(list(allV))     
     checkV = set({a})
     numRemainV = v
     edge_number = 0
     while edge_number < e: 
         if numRemainV == 0 or not connected:
             v1 = random.choice(list(allV))
             v2 = random.choice(list(allV)) 
         else:
             v1 = random.choice(list(checkV))
             v2 = random.choice(list(allV.difference(checkV))) 
         
         pair = tuple(sorted((v1,v2)))
         
         if (v1 != v2) and (pair not in graph.adjacencyList):
             eobj = Edge(edge_number)
             v1_obj = graph.vertexList[v1]
             v2_obj = graph.vertexList[v2]
             eobj.setNodePair(v1_obj,v2_obj)
             graph.edgeList[eobj.id] = eobj
             v1_location = v1_obj.location
             v2_location = v2_obj.location
             weight = distance(v1_location,v2_location)
             eobj.setWeight(weight)
             graph.adjacencyList[pair] = eobj.edge_weight
             graph.edgePair[tuple(sorted(pair))]= eobj
             if connected:
                 checkV.add(v2)
                 numRemainV = len(allV.difference(checkV))

             edge_number += 1
     
     return graph
     
#%% Exercise 2:
'''
Implement a connected component algorithm that adds an integer property connected_component to each vertex so that vertexes in the same connected component have the same value and vertexes in different connected components have different values. (http://en.wikipedia.org/wiki/Connected_component_%28graph_theory%29).
What is the complexity of your algorithm? Produce code to create scalability timing plots like those you produced in assignment 1. You are encouraged to reuse your code from that assignment, but please include all necessary modules in your submission. (Hint: For your plot produce random graphs with n nodes and 3n vertexes).
'''
def dfs(adlist, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(adlist[vertex] - visited)
    return visited

def findGroup(graph):
    graph.findAdlist()    
    groupList = []
    checkList = set()
    for i in range(len(graph.vertexList)):
        checkList.add(i)
    
    keyList = list(graph.adList.keys())
    for i in range(len(graph.vertexList)):
        if i in keyList and i in checkList:
            x = dfs(graph.adList,i)
            groupList.append(x)
            checkList = checkList.difference(x)
            '''
            if x in groupList:
                    pass
            else:
                    groupList.append(x)
            '''
        elif i not in keyList and i in checkList:
            x = {i}
            groupList.append(x) 
            checkList = checkList.difference(x)
            
    return groupList
    
def assignGroup(graph):
    groupList = findGroup(graph)
    for i in range(len(groupList)):
        #graph.group.append(i)
        for a in groupList[i]:
            graph.vertexList[a].connected_comp = i  
            #graph.group[a] = i
        i += 1
    return groupList

#%%Exercise 2 time plot

testRange = range(5000,40000,5000)

list_len = []
time_used = []
for n in testRange:
    list_len.append(n)
    time_one_len = 0
    print(n)
    for i in range(1,5,1):
        g = randomGraph(n, 3*n)
        timeStamp = time.process_time()
        findGroup(g)# run p function
        timeLapse = time.process_time() - timeStamp
        time_one_len = time_one_len + timeLapse
    time_ave = time_one_len / 5
    time_used.append(time_ave)

plt.plot(list_len,time_used, '-bo')
plt.xlabel("number of vertex")
plt.ylabel("time")
plt.show()

#%% Exercise 3
'''
Implement a low level mechanism to display a graph in matplotlib. Assume that each vertex has a location property. Allow for flexible configuration of the appearance of the edges and vertexes based on their properties, so you can reuse it for this exercise, exercise 5, an other future similar exercises.
Use your low level display implementation to provide a high level mechanism for displaying a graph so that each connected component is visually distinct.
'''
def createColor(graph):
    groupList = findGroup(graph)
    colorDict = dict()
    for i in range(len(groupList)):
        colorDict[i] = (random.random(),random.random(),random.random())
    return colorDict
        
def plotGraph(graph):
    plt.ylim([0,1.1])
    plt.xlim([0,1.1])      
    c = createColor(graph)
    for i in range(len(graph.edgeList)):
        cc = c[graph.edgeList[i].edge_pair[0].connected_comp]
        pair = [graph.edgeList[i].edge_pair[0].location,graph.edgeList[i].edge_pair[1].location]
        x, y = zip(*pair) 
        plt.plot(x,y,linestyle = "-",marker = "o", color = cc)

    for v in g.vertexList:
        if (v not in g.adList):
            cc = c[g.vertexList[v].connected_comp]
            plt.plot(g.vertexList[v].location[0], 
                 g.vertexList[v].location[1], marker = "o", color = cc)
    plt.show()

#%% Exercise 4
'''
Implement a minimum spanning tree (MST) algorithm that given one (weighted) graph, adds a boolean property mst to each Edge that is True if the edge is part of the mst and False if it is not. (http://en.wikipedia.org/wiki/Minimum_spanning_tree).
What is the complexity of your algorithm? Produce code to create scalability timing plots like those you produced in assignment 1 with n going to at least 10000. (Hint: For your plot produce random graphs with n nodes and 3n vertices).
'''
def findMST(graph):
    if graph.connected == False:
        raise RuntimeError("Graph not connected, cannot find MST")
    
    allV = set(range(len(graph.vertexList)))
    a = random.choice(list(allV))
    S = set({a})
    edges = set()

    while bool(allV.difference(S)):  
        minWeight = float("inf")
        minV = None
        minE = None
        
        #print("S:" + str(S)) 
        #print("edges:" + str(edges)) 
        
        for b in S:
            #print("b:" + str(b)) 
            for i in graph.adList[b]:
                #print("i:" + str(i)) 
                if i not in S:
                    e = tuple(sorted((b,i)))
                    #print("e:" + str(e))
                    weight = graph.adjacencyList[e]
                    #print("weight:" + str(weight))
                
                    if weight < minWeight:
                        minWeight = weight
                        minV = i
                        minE = e
                        
                        #print("minweight:" + str(minWeight))
                        #print("minV:" + str(minV))
                        #print("minE:" + str(minE))
                        
                      
        edges.add(minE)
        S.add(minV)  
       
        #print("*****")        
    
    #print("mst: " + str(edges))
    return edges

def addBool(graph):
    MST = findMST(graph)
    
    for i in graph.edgePair:
        if i in MST:
            graph.edgePair[i].MST = True
        else:
            graph.edgePair[i].MST = False
            
for k,E in g.edgePair.items():
    print(str(k) + ": " + str(E.MST))
#%%Exercise 4 time plot

testRange = range(10,1000,10)

list_len = []
time_used = []
for n in testRange:
    list_len.append(n)
    time_one_len = 0
    print(n)
    for i in range(1,5,1):
        g = randomGraph(n, 3*n,connected=True)
        assignGroup(g)
        print(str(assignGroup(g)))
        timeStamp = time.process_time()
        findMST(g)# run p function
        timeLapse = time.process_time() - timeStamp
        time_one_len = time_one_len + timeLapse
    time_ave = time_one_len / 5
    time_used.append(time_ave)

plt.plot(list_len,time_used, '-bo')
plt.xlabel("number of vertex")
plt.ylabel("time")
plt.show()

#%% Exercise 5
'''
Produce code that displays a graph and its MST side to side.
'''

def plotGraphMST(graph):
    plt.ylim([0,1.1])
    plt.xlim([0,1.1])      
    
    for i in graph.edgePair.keys():
        if graph.edgePair[i].MST == True:
            pair = [graph.edgePair[i].edge_pair[0].location,graph.edgePair[i].edge_pair[1].location]
        x, y = zip(*pair) 
        plt.plot(x,y,linestyle = "-",marker = "o", color = "b")

    plt.show()