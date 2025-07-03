import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.write("ff")

x = [1,2,3,4,5]
y = [600,700,800,900,1000]
data = np.random.randn(1234)

items = ["t", "y", "u"]
counts = [100, 200, 300]

fig, axs = plt.subplots(2, 2)

fig.patch.set_color("red")
axs[0, 0].plot(x, y)
axs[0, 0].set_title("line")
axs[0, 0].set_xlabel("time")
axs[0, 0].set_ylabel("money")


axs[0, 1].barh(items, counts)
axs[0, 1].set_title("bar")

# axs[2].subplot(5,2,2)
axs[1, 0].scatter(x, y, color = 'red')
axs[1, 0].set_xlabel("time")
axs[1, 0].set_ylabel("money")


axs[1, 1].hist(data, bins = data.size, color = 'skyblue', edgecolor='yellow')
axs[1, 1].set_xlabel("time")
axs[1, 1].set_ylabel("money")

plt.tight_layout()

st.pyplot(fig)

# plt.figure()
# plt.plot(x, y)
# plt.title("Trying")
# plt.xlabel("x axis...")
# plt.ylabel("y axis...")

# plt.figure()
# plt.barh(items, counts)
# plt.show()
