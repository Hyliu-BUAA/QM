'''
Author: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
Date: 2022-06-27 22:28:17
LastEditors: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
LastEditTime: 2022-06-28 00:10:06
FilePath: /Quantum_Mechanics/algorithm_implementation/3.Leapfrog/code/plot.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))

df = pd.read_csv("./output.csv",
                header=None)
df.columns = ["Time", "Location"]
plt.plot(df.loc[:, "Time"],
        df.loc[:, "Location"],
        color="lightseagreen",
        linewidth=3)


# 1. Retouch the xlabel, ylabel
plt.xlabel("Time", 
            fontsize=28, 
            fontweight="bold"
)
plt.ylabel("Location", 
            fontsize=28, 
            fontweight="bold"
)

# 2. Retouch the ticks of x-axis/y-axis
plt.xticks(fontsize=20, 
        fontweight="bold"
        )
plt.yticks(fontsize=20, 
        fontweight="bold"
        )

# 3. title
plt.title("num_points_per_cycle = 16",
        fontsize=24,
        fontweight="bold")



# Save the figure
plt.savefig("./Locations_16.png", dpi=300, bbox_inches="tight")