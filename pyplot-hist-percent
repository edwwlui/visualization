import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

name="yelp.iter1.from0.dev.0"
data=[]
with open(name+".txt") as f:
    for line in f:
        data.append(int(line))  #int for numerical order
fig = plt.figure(figsize=(2,1.5))  #first set size
plt.hist(data, weights=np.ones(len(data)) / len(data))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title(name,fontsize=15)
plt.xlabel('Sentence Length')
plt.ylabel('Percentage')
fig.savefig(name+'.jpg', dpi = 600)
plt.show()
