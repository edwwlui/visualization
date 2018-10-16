import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import os

dir_location=".\length_distribution"
for root, dirs, files in os.walk(dir_location):  
    for name in files:
        data=[]
        with open(dir_location+"\\"+name) as f:
            for line in f:
                data.append(int(line))  #int for numerical order
        fig = plt.figure(figsize=(3.5,2))  #first set size
        plt.hist(data, weights=np.ones(len(data)) / len(data))
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
        plt.title(name[:-4],fontsize=15)
        plt.xlabel('Sentence Length')
        plt.ylabel('Percentage')
        plt.tight_layout()  #fit everything into the figsize
        fig.savefig(name[:-4]+'.jpg', dpi = 600)
        plt.show()
