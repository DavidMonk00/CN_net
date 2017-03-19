import networkx as nx
from random import choice
from random import random
import numpy as np
import matplotlib.pyplot as plt
from log_bin_CN_2016 import log_bin

class Graph:
    nodes = []
    t = 1
    def __init__(self, N_max, m):
        self.N_max = N_max
        self.m = m
        self.G = nx.cycle_graph(m+1)
        self.N = m+1
        self.nodes = self.G.nodes()
        #nx.draw(self.G)
        #plt.show()
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
        bins, dat = log_bin(deg,a=1.15)
        '''plt.scatter(bins,dat)
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-10,1)'''
        return bins,dat
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
    L = 20
    kn = []
    ksd = []
    for i in range(17):
        k = []
        print i
        for j in range(20):
            N = pow(2,i+1)
            g = BAGraph(N,m)
            g.generateGraph()
            k.append(max(g.G.degree().values()))
        kn.append(np.mean(k))
        ksd.append(np.std(k))
    x = [pow(2,i+1) for i in range(17)]
    plt.errorbar(x,kn,yerr=ksd)
        #g.logBinDegrees()
        #nx.draw(g.G)
        #plt.show()




if (__name__ == '__main__'):
    main()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
