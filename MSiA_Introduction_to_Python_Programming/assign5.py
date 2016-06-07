# -*- coding: utf-8 -*-
"""
@author: Xiang Li
This assignment is advised by Ameer Khan
"""
'''
In this assignment, the goal is to acomplish a Bayes Network library.

Your library should be able to:
1. Allow ways to create the structure of the network (directed graph)

2. Create, observe and change variables, including their names, possible values and marginal and
conditional distributions as appropriate. For this assignment we will confine ourselves to discrete
random variables exclusively.

3. Save and load a Bayesian network from file using a json format of your own design.

4. Set and remove evidence on one or more variables. For this assignment you it is sufficient to limit
yourselves to hard evidence.

5. Do inference on the network after setting evidence. Using einsum is acceptable in this exercise. You
need not implement variable elimination or a Junction Tree algorithm.
'''

import numpy as np;

import graph;

#%%
class BayesNetwork(graph.DirectedGraph):
    def __init__(self, *args, **kwargs):
        super( ).__init__(*args, **kwargs);
        self.evidenceList = [ ];
    
    def addNode(self, variable):
        self.addVertex(variable);
    
    def addChild(self, parent, child):
        self.addEdge(parent, child);
    
    def setParents(self, name):
        u = self.vertexObject(name);
        parents = {v for v in self.vertexes( ) if u in v.neighbors};
        return parents;
    
    def addConditionalProb(self, name, probability, states, dependencyList = None):
        if (dependencyList is None):
            dependencyList = [ ];        
        
        u = self.vertexObject(name);
        u.probability = probability;
        u.states = states;
        u.dependencyList = dependencyList;
    
    def jointProb(self, vertexList = None):
        if (vertexList is None or self.evidenceList):
            vertexList = self.vertexes( );
        
        probList = tuple([v.probability for v in vertexList]);
        indexDict = {v.name: chr(i + 97) for i, v in enumerate(self.vertexes( ))};
        
        rhs = ''.join([indexDict[v.name] for v in vertexList ]);
        lhsList = [ ];
        
        for u in vertexList:
            lhsTerm = [indexDict[u.name]] + [indexDict[v] for v in u.dependencyList];
            lhsList.append(''.join(lhsTerm));
        
        lhs = ','.join(lhsList);
        
        expr = '->'.join([lhs, rhs]);
        jointProb =  np.einsum(expr, *probList);
        jointProb = jointProb/np.sum(jointProb);
        
        dimList = [slice(None)] * len(np.shape(jointProb));
        
        for vName, vState in self.evidenceList:
            vIndex = ord(indexDict[vName]) - 97;
            dimList[vIndex] = self.vertexObject(vName).states.index(vState);
        
        slicedProb = jointProb[tuple(dimList)];
        slicedProb = slicedProb/np.sum(slicedProb);
        return slicedProb;
    
    def marginalProb(self, name, total = True):
        u = self.vertexObject(name);
        
        if (not u.dependencyList and not self.evidenceList):
            return u.probability;
            
        if (self.evidenceList):
            total = True;
        
        if (total):
            vertexList = self.vertexes( );
        else:
            vertexList = [u] + [ self.vertexObject(vName) for vName in u.dependencyList];
        
        jointProb = self.jointProb(vertexList);
        
        indexDict = {v.name: chr(i + 97) for i, v in enumerate( self.vertexes( ))};
        setVertexes = [vName for vName, vState in self.evidenceList];
        
        lhs = ''.join( [indexDict[v.name] for v in vertexList if v.name not in setVertexes]);
        rhs = indexDict[name];
        
        expr = '->'.join([lhs, rhs]);
        return np.einsum(expr, jointProb);
    
    def setEvidence(self, evidenceList):
        for vName, vState in evidenceList:
            try:
                self.vertexObject(vName);
            except KeyError:
                print("Invalid node specified");
                return;
            
            if (vState not in self.vertexObject(vName).states):
                raise ValueError("Invalid value for node specified");
            
        self.evidenceList = evidenceList;
    
    def getInference(self, name):
        for vName, vState in self.evidenceList:
            if (name == vName):
                return vState;
        
        return self.marginalProb(name, total = True);
    
    def __repr__(self):
        return 'BayesNetwork: [{}]'.format( ', '
                .join( [str(k) for k in sorted(self._edges.values( ))]));

#%%Run test using data from slides
g = BayesNetwork( );
g.addNode('Smoking');
g.addChild('Smoking', 'Cancer');

g.addConditionalProb('Smoking', np.array( [ 0.8, 0.15, 0.05 ]),
                       ['None', 'Light', 'Heavy']);
g.addConditionalProb('Cancer', np.array([[0.96, 0.88, 0.60],
                                             [0.03, 0.08, 0.25],
                                             [0.01, 0.04, 0.15]]),
                       ['None', 'Benign', 'Malignant'], ['Smoking']);
prob = g.jointProb( );

g.setEvidence([('Smoking', 'Light')]);

