import numpy as np
import matplotlib.pyplot as plt

def perturb(x,e):
    x_perturb = np.random.uniform(low=x-e,high=x+e)
    if(x_perturb[0] < xl[0] or x_perturb[0] > xu[0] or
       x_perturb[1] < xl[1] or x_perturb[1] > xu[1]):
        return x
    return x_perturb

def f(x, y):
    term1 = x * np.sin(4 * np.pi * x)
    term2 = y * np.sin(4 * np.pi * y + np.pi)
    return term1 - term2 + 1


x_axis = np.linspace(-1, 3, 1000)
y_axis = np.linspace(-1, 3, 1000)

xl = [-1, -1]
xu = [3, 3]

X,Y = np.meshgrid(x_axis,y_axis)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,f(X,Y), cmap='viridis',)

x_opt = [-1, 3]
f_opt = f(*x_opt)

e = 2.75
max_it = 1000000
max_viz = 500
melhoria = True
i = 0
while i<max_it and melhoria:
    melhoria = False
    for j in range(max_viz):
        x_cand = perturb(np.array(x_opt),e)
        f_cand = f(*x_cand)
        if f_cand > f_opt:
            x_opt = x_cand
            f_opt = f_cand
            melhoria = True
            ax.scatter(x_opt[0], x_opt[1], f_opt, color='r', marker='x')
            plt.pause(.001)
            break
    i+=1

ax.scatter(x_opt[0], x_opt[1], f_opt, color='g', marker='x', s=100, linewidth=3)
plt.show()
bp=1