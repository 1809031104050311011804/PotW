import numpy as np
from numpy import random
import matplotlib.pyplot as plt

try:
    flips = int(input("How many times would you like to flip the coin? "))
except ValueError:
    print("Please enter a valid integer!")
    exit()

result1 = "Heads"
result2 = "Tails"

heads = 0
tails = 0

results = []

#coin flipping
for coin in range(flips):
    
    coin = random.randint(2)
    results.append(coin)
    
    #heads case
    if coin == 0:
        heads += 1
    
    #tails case
    elif coin == 1:
        tails += 1

print("The coin landed on {} {} times!".format(result1.lower(), heads))
print("The coin landed on {} {} times!".format(result2.lower(), tails))

for x in range(len(results)):
    
    #replacing 0 with heads
    if results[x] == 0:
        results[x] = "Heads"
    
    #replacing 1 with tails
    elif results[x] == 1:
        results[x] = "Tails"

#data analysis
percent_heads = round(((heads/flips) * 100), 2)
percent_tails = round(((tails/flips) * 100), 2)

fig, ax = plt.subplots()

x_options = [result1, result2]
y_freq = [heads, tails]

axis_labels = x_options

ax.bar(x_options, y_freq, label=axis_labels, color=("c", "m"))

ax.set_ylabel("Frequency", fontweight="bold")
ax.set_title("Coin Flip Simulation (Flips={})".format(flips), fontweight="bold")

bars = ax.patches

bars_labels = [0, 0]
bars_labels[0] = "{}%".format(percent_heads)
bars_labels[1] = "{}%".format(percent_tails)

for bars, bars_labels in zip(bars, bars_labels):
    bar_heights = bars.get_height()
    ax.text(bars.get_x() + bars.get_width()/2, bar_heights/2, bars_labels, ha="center", va="bottom", backgroundcolor="w")

plt.show()
