import numpy as np
import matplotlib.pyplot as plt

def perturb(x,e):
    return np.random.uniform(low=x-e,high=x+e)

def f(x, y):
    term1 = np.exp(-((x**2) + (y**2)))
    term2 = 2 * np.exp(-((x - 1.7)**2 + (y - 1.7)**2))
    return term1 + term2


x_axis = np.linspace(-2, 4, 1000)
y_axis = np.linspace(-2, 5, 1000)

X,Y = np.meshgrid(x_axis,y_axis)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,f(X,Y), cmap='viridis',)

x_opt = [-2, 4]
f_opt = f(*x_opt)

e = .1
max_it = 10000000000
max_viz = 20
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