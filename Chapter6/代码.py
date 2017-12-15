import numpy 
import matplotlib
from matplotlib import pyplot 
matplotlib.rcParams['animation.convert_path'] = 'C:\Program Files\ImageMagick-7.0.7-Q16\convert.exe'
from matplotlib import animation
import math

c1, c2 = 100, 150
det_x = 0.003
det_t= det_x/110
x0, x1 = 0.3, 0.7
k = 1000
X = numpy.arange(0, 1, det_x)
Y1 = [0.5*math.sin(4*math.pi*x) for x in X]
Y1[0], Y1[-1] = 0., 0.
pre_Y1, next_Y1 = [y for y in Y1], [y for y in Y1]
r1, r2 = c1 * det_t / det_x, c2 * det_t / det_x

fig = pyplot.figure(figsize=(15,10))
xmin, xmax =  0, 1
ymin, ymax = -0.5, 0.5
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1
ax = pyplot.axes(xlim=(xmin-dx, xmax+dx), ylim=(ymin-dy, ymax+dy))
line, = ax.plot([], [])

# name the axis
pyplot.xlabel(r'$x(m)$', fontsize=16)
pyplot.ylabel(r'$y(m)$', fontsize=16)

# draw animation
def initAnimation():   
    line.set_data([], [])
    return line,

def animate(i):
    global X, Y1, pre_Y1, next_Y1, Y2, pre_Y2, next_Y2
    for j in range(1, len(X)-1):
        next_Y1[j] = 2*(1-r1**2)*Y1[j] - pre_Y1[j] + r1**2*(Y1[j+1]+Y1[j-1])
    pre_Y1 = [y for y in Y1]
    Y1 = [y for y in next_Y1]
    tmp = [Y1[k] for k in range(len(X))]
    line.set_data(X, tmp)   
    return line,

anim = animation.FuncAnimation(fig, animate, frames=200, init_func=initAnimation, interval=2, blit=True)
anim.save('zhubo.gif', writer='imagemagick', fps=30, dpi=60)
pyplot.show()
