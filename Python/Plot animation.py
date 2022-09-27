import matplotlib.pyplot as plt
import matplotlib.animation as animate

a = [0, 0, 0, 0, 0]
fig, ax = plt.subplots()


def anim(num):
    ax.clear()
    ste = str(num)
    for i in range(5):
        a[i] += ste.count(str(i))
    ax.pie(a)


ani = animate.FuncAnimation(fig, anim, frames=range(1000))
plt.show()
