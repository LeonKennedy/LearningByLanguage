#!/usr/bin

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt


class HillClimb:

    def __init__(self, num):
        self.places = np.random.rand(num, 2)
        self.place_size = num
        self.max_iter = 5000
        print(self.places)
        
    def adjust(self, data):
        result = data.copy()
        m, n = random.choice(self.place_size,2,replace=False)
        result[(m, n),:] = result[(n, m),:]
        return result
    
    def sumDistance(self, a):
        distance = np.linalg.norm(a[0] - a[self.place_size-1])
        for i in np.arange(self.place_size - 1):
           distance += np.linalg.norm(a[i] - a[i+1])   
        return distance
        
        
    def hillclimb(self):
        times = 0
        while(times < self.max_iter):
            adjustData = self.adjust(self.places) 
            adjustDis = self.sumDistance(adjustData)
            currentDis = self.sumDistance(self.places)
            if(adjustDis < currentDis):
                self.places = adjustData
                print('swtich, distance is: %d', adjustDis)
            else:
                times += 1
        return currentDis

    def show(self):
        #plt.scatter(self.places[:,0], self.places[:,1])
        plt.plot(self.places[:,0], self.places[:,1], 'go-')
        plt.show()

if __name__ == "__main__":
    #a = np.random.rand(place,2)
    #random.shuffle(a)
    #print("traveling %d places have %d seconds" % (place, 10))
    hc = HillClimb(20)
    hc.hillclimb()
    hc.show()
    
