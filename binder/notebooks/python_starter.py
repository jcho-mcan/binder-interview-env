import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100)
})

sns.scatterplot(data=df, x="x", y="y")
plt.show()
