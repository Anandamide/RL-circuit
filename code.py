import numpy as np
import scipy as sp
import math
import matplotlib.pyplot as plt

#computes the euler approximation of a differential equation in the form dy/dx=f(x,y) with the
#initial condition y(x_0)=y_0, running from x_0 to x= end(inclusive) with a step size of h, printing the 
#intermediate values
def euler(fn, x_0, y_0, h, end):
    y = y_0
    r = int(-1*math.log10(h))
    txt = "x: {} y:{}"
    for x in np.arange(x_0,end + h, h):
        print(txt.format(round(x,r),y))
        y = y + h*fn(x,y)
#same as euler(), but instead of printing the intermediate values returns the final y value
def ffeuler(fn, x_0, y_0, h, end):
    y = y_0
    r = int(-1*math.log10(h))
    txt = "x: {} y:{}"
    for x in np.arange(x_0,end, h):
        y = y + h*fn(x,y)    
    return y

#when given a plot object 'ax', graphs the euler approximation for the given values with legend label lbl
def plot_euler(fn, x_0, y_0, h, end, ax, lbl):
    y = y_0
    r = int(-1*math.log10(h))
    txt = "x: {} y:{}"
    lst = []
    for x in np.arange(x_0,end + h, h):
        lst.append((x,y))
        y = y + h*fn(x,y)
    ax.plot([i for i,j in lst],[j for i,j in lst],label=lbl)

#plots the slope field of a function 'fn(x,y)' over the range of values on the plot 'ax' with h and d being scaling constants
def slope_field(fn, x1, x2, y1, y2, h, d, ax):
    def seg_from_point_slope(p,m,h):
        x, y = p[0], p[1]
        a = (h/2)*math.cos(math.atan(m))
        b = (h/2)*math.sin(math.atan(m))
        return[(x-a,y-b),(x+a,y+b)]
        
    def plot_segments(segments, g):
        for seg in segments:
            g.plot([seg[0][0],seg[1][0]],[seg[0][1],seg[1][1]],'black')
            
    xp = np.arange(x1,x2+d,d)
    yp = np.linspace(y1,y2,len(xp))
    points = [[i,j] for i in xp
                    for j in yp]
    segments = [seg_from_point_slope(p,fn(p[0],p[1]),h) for p in points]
    plot_segments(segments,ax)
  fig, ax = plt.subplots()
ax.set(xlabel='t(seconds)',ylabel='amps',title=r'$\frac{1}{4}\frac{di}{dt}+8i=18$')
ax.grid()

fn = lambda t, i : 72-32*i

plot_euler(fn, 0, 0, .02, 0.25, ax, "h = .02")
plot_euler(fn, 0, 0, .01, 0.25, ax, "h = .01")
plot_euler(fn, 0, 0, .0001, 0.25, ax, "h = .0001")
slope_field(fn, 0, 0.25, 0, 3, .05, .025, ax)
ax.legend()
fig.savefig("plot.png")
    
