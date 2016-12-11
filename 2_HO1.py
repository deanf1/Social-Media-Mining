import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv", skipinitialspace=True)

print data.head(), "\n"

print data.mean(), "\n"

print data.std(), "\n"
print data.std().index
print data.std().values

x = len(data.std().values.tolist())
plt.bar(range(x), data.std().values.tolist(), width = 1)
plt.xticks(range(x), data.std().index.tolist())
plt.show()