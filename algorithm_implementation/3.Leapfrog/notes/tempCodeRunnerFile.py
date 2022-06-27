import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("./output.csv",
                header=None)
df.columns = ["Time", "Location"]
plt.plot(df.loc[:, "Time"], df.loc[:, "Location"])

plt.xlabel("Time")
plt.ylabel("Location")

plt.show()