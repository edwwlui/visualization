import pandas as pd
import matplotlib.pyplot as plt
name="informal_sent_len"
data=pd.read_csv(name+".txt")
data.plot(kind='hist',range=[0,40],bins=20)
plt.xlabel('Sentence Length')
plt.title(name,fontsize=15)
fig = plt.figure(figsize=(4,3))
fig.savefig(name+'.png', dpi = 300)
plt.show()