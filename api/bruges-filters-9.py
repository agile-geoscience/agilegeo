import matplotlib.pyplot as plt
import bruges
w, t = bruges.filters.sinc(0.256, 0.002, 40)
plt.plot(t, w)