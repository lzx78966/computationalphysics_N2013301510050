# -*- coding: utf-8 -*-

import matplotlib.pyplot as pl

sigma=10
b=8.0/3

class lorenz_model():
    def __init__(self,_x0=0,_y0=0,_z0=0,_r=0,_dt=0,_time=0):
        self.x0=_x0
        self.y0=_y0
        self.z0=_z0
        self.dt=_dt
        self.time=_time
        self.r=_r
    def calculate(self):
        sigma=10
        b=8.0/3
        self.x=[]
        self.y=[]
        self.z=[]
        self.t=[]
        self.x.append(self.x0)
        self.y.append(self.y0)
        self.z.append(self.z0)
        self.t.append(0)
        nsteps=int(self.time/self.dt)
        for i in range(1,nsteps):
            self.x.append(self.x[-1]+sigma*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]-(self.x[-1]*self.z[-1]-self.r*self.x[-1]+self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-1]*self.y[-1]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
        return 0    
    def plot_phase1(self):
        pl.plot(self.x,self.z,label="r=%r"%(self.r))
        pl.title("Phase space plot:z versus x")
        pl.xlabel("x")
        pl.ylabel("z")    

A= lorenz_model(1,0,0,5,0.0001,50)
A.calculate()
A.plot_phase1()
pl.legend()
pl.show()
A= lorenz_model(1,0,0,10,0.0001,50)
A.calculate()
A.plot_phase1()
pl.legend()
pl.show()
A= lorenz_model(1,0,0,25,0.0001,50)
A.calculate()
A.plot_phase1()
pl.legend()
pl.show()

