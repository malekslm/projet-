import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("country_wise_latest.csv")
df.head(500)
df.plot(kind = 'scatter',
        x = 'Confirmed',
        y = 'Deaths',
        color = 'red')
plt.title('abdelmalek')
plt.show()
# array = df[["Active","Deaths","Confirmed"]].to_numpy()

z= df["Active"]
x= df["Confirmed"]
y= df["Deaths"]
fig = plt.figure(figsize = (10, 7)) 
ax = plt.axes(projection ="3d") 
ax.scatter3D(x, y, z, color = "red") 
plt.title("3D Scatter Plot") 
 
# show plot 
plt.show()