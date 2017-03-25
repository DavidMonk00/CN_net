from model import *
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import sys

class Phase1:
    def plotDifferentm(self, N, repeats=10):
        mlim = 6
        colors = iter(cm.rainbow(np.linspace(0, 1, mlim)))
        for i in range(1,mlim):
            data = []
            B = np.zeros(0)
            print "Testing m = ", pow(3,i)
            for j in range(repeats):
                print j
                g = PRAGraph(N,pow(3,i))
                g.generateGraph()
                bins, dat = g.logBinDegrees()
                if len(bins) > len(B):
                    B = bins
                d = np.zeros(100)
                d[:len(dat)] = dat
                data.append(d)
            dat = np.mean(data, axis=0)[:len(bins)]
            plt.scatter(bins, dat, color=next(colors), label="m = %d"%(pow(3,i)))
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-9,1)
        plt.xlim(1)
        plt.xlabel(r"$k$", fontsize=18)
        plt.ylabel(r"$p\left( k \right)$", fontsize=18)
        plt.legend(loc=0)
        plt.savefig('./images/Phase2/plot_m_1e4_%d'%repeats)
        print "m test complete."
    def plotDifferentN(self, m, repeats=10):
        Nlim = 7
        colors = iter(cm.rainbow(np.linspace(0, 1, Nlim)))
        for i in range(1,Nlim):
            print "Testing N = ", pow(10,i)
            data = np.zeros(100)
            B = np.zeros(0)
            for j in range(repeats):
                print j
                g = PRAGraph(pow(10,i),m)
                g.generateGraph()
                bins, dat = g.logBinDegrees()
                if len(bins) > len(B):
                    B = bins
                d = np.zeros(100)
                d[:len(dat)] = dat
                data += d
            dat = data[:len(B)]/repeats
            plt.scatter(B, dat, color=next(colors), label="N = %d"%(pow(10,i)))
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-11,1)
        plt.xlim(1,1e4)
        plt.xlabel(r"$k$", fontsize=18)
        plt.ylabel(r"$p\left( k \right)$", fontsize=18)
        plt.legend(loc=0)
        plt.savefig('./images/Phase2/plot_N_3_%d'%repeats)
        print "N test complete."
    def plotGreatestDegree(self, m, repeats=10):
        Nlim = 17
        kn = []
        ksd = []
        for i in range(Nlim):
            k = []
            print "Testing greatest degree for N = ", pow(2,i)
            for j in range(repeats):
                N = pow(2,i+1)
                g = PRAGraph(N,m)
                g.generateGraph()
                k.append(max(g.G.degree().values()))
            kn.append(np.mean(k))
            ksd.append(np.std(k))
        x = [pow(2,i+1) for i in range(Nlim)]
        plt.errorbar(x,kn,yerr=ksd)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel(r"$N$", fontsize=18)
        plt.ylabel(r"$k_1$", fontsize=18)
        plt.savefig('./images/Phase2/plot_k_3_%d'%repeats)
        print "k test complete."
    def collapseData(self, m, repeats=10):
        Nlim = 7
        gamma = 3
        colors = iter(cm.rainbow(np.linspace(0, 1, Nlim)))
        for i in range(1,Nlim):
            print "Collapsing N = ", pow(10,i)
            data = []
            B = np.zeros(0)
            for j in range(repeats):
                g = PRAGraph(pow(10,i),m)
                g.generateGraph()
                bins, dat = g.logBinDegrees()
                if len(bins) > len(B):
                    B = bins
                d = np.zeros(100)
                d[:len(dat)] = dat
                data.append(d)
            dat = np.mean(data, axis=0)[:len(bins)]
            for j in range(len(dat)):
                dat[j] = pow(bins[j],gamma)*dat[j]
            plt.scatter(np.array(bins)/np.sqrt(pow(10,i)), dat, color=next(colors), label="N = %d"%(pow(10,i)))
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim(1e-5,1e4)
        #plt.xlim(1,1e4)
        plt.xlabel(r"$k$", fontsize=18)
        plt.ylabel(r"$p\left( k \right)$", fontsize=18)
        plt.legend(loc=3)
        plt.savefig('./images/Phase2/collapse_3_%d'%repeats)
        print "Data collapse complete."

def main():
    p = Phase1()
    if (sys.argv[1] == 'm'):
        p.plotDifferentm(pow(10,4), repeats = int(sys.argv[2]))
    elif (sys.argv[1] == 'N'):
        p.plotDifferentN(3, repeats = int(sys.argv[2]))
    elif (sys.argv[1] == 'k'):
        p.plotGreatestDegree(3, repeats = int(sys.argv[2]))
    elif (sys.argv[1] == 'c'):
        p.collapseData(3, repeats = int(sys.argv[2]))

if (__name__ == '__main__'):
    main()
