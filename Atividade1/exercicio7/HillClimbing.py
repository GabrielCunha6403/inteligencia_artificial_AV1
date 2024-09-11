import numpy as np
import matplotlib.pyplot as plt

def perturb(x,e):
    x_perturb = np.random.uniform(low=x-e,high=x+e)
    if(x_perturb[0] < xl[0] or x_perturb[0] > xu[0] or
       x_perturb[1] < xl[1] or x_perturb[1] > xu[1]):
        return x
    return x_perturb

def f(x, y):
    term1 = -np.sin(x) * (np.sin(x**2 / np.pi))**20
    term2 = -np.sin(y) * (np.sin(2 * y**2 / np.pi))**20
    return term1 + term2


x_axis = np.linspace(0, np.pi, 1000)
y_axis = np.linspace(0, np.pi, 1000)

xl = [0, 0]
xu = [np.pi, np.pi]

X,Y = np.meshgrid(x_axis,y_axis)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,f(X,Y), cmap='viridis',)

x_opt = [0, np.pi]
f_opt = f(*x_opt)

e = 1
max_it = 1000000
max_viz = 400
melhoria = True
i = 0
while i<max_it and melhoria:
    melhoria = False
    for j in range(max_viz):
        x_cand = perturb(np.array(x_opt),e)
        f_cand = f(*x_cand)
        if f_cand < f_opt:
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