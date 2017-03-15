import networkx as nx
from random import choice
from random import random
import numpy as np
import matplotlib.pyplot as plt
from log_bin_CN_2016 import log_bin

class Graph:
    nodes = []
    t = 1
    N = 9
    def __init__(self, N_max, m):
        self.N_max = N_max
        self.m = m
        self.G = nx.cycle_graph(10)
        self.nodes = self.G.nodes()
    def addVertex(self):
        self.N += 1
        self.G.add_node(self.N)
    def addEdge(self, node1,node2):
        self.G.add_edge(node1,node2)
    def getNodes(self):
        return self.G.nodes()
    def getEdges(self):
        return self.G.edges()
    def generateGraph(self):
        for i in xrange(self.N_max):
            #print i
            self.addVertex()
            self.generateEdges()
    def binDegrees(self):
        deg = self.G.degree().values()
        #print self.G.degree()
        bins = np.arange(min(deg),max(deg)+1,1)
        dat = np.histogram(deg,bins)
        dat = dat[0]/float(len(deg))
        print len(bins)
        print len(dat)
        plt.scatter(bins[1:],dat)
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-7,1)
        plt.show()
    def logBinDegrees(self):
        deg = self.G.degree().values()
        bins, dat = log_bin(deg,a=2)
        plt.plot(bins,dat)
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-10,1)
        #plt.show()

class BAGraph(Graph):
    def generateEdges(self):
        node1 = self.N
        n = []
        for i in xrange(self.m):
            while (True):
                node = self.nodes[int(len(self.nodes)*random())]
                if node not in n:
                    break
            n.append(node)
            self.addEdge(node1,node)
            self.nodes.append(node)
        for i in xrange(self.m):
            self.nodes.append(node1)

class PRAGraph(Graph):
    def generateEdges(self):
        node1 = self.N
        n = []
        for i in xrange(self.m):
            while (True):
                node = self.nodes[int(len(self.nodes)*random())]
                if node not in n:
                    break
            n.append(node)
            self.addEdge(node1,node)
        self.nodes.append(node1)

class RWGraph(Graph):
    def generateGraph(self, L):
        for i in xrange(self.N_max):
            self.addVertex()
            self.generateEdges(L)
    def generateEdges(self,L):
        node1 = self.N
        n = []
        for i in xrange(self.m):
            while (True):
                node = self.nodes[int(len(self.nodes)*random())]
                for j in xrange(L):
                    k = self.G[node].keys()
                    node = k[int(len(k)*random())]
                if node not in n:
                    break
            n.append(node)
            self.addEdge(node1,node)
        self.nodes.append(node1)

def main():
    N = int(1e6)
    m = 2
    L = 10
    for i in range(5):
        print i
        N = pow(10,i+2)
        g = BAGraph(N,m)
        g.generateGraph()
        g.logBinDegrees()
    plt.show()

if (__name__ == '__main__'):
    main()
