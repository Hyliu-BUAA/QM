import numpy as np
from sklearn.datasets import make_regression

x, y = make_regression(
            n_samples=100,
            n_features=10,
            n_targets=1,
            noise=0.2,
            random_state=42,
)
y = y.reshape(-1, 1)
data = np.concatenate([x, y], axis=1)

np.save(
    file="/Users/mac/我的文件/Notebook/Quantum_Mechanics/algorithm_implementation/1.GD/code/data.csv",
    arr=data,
    allow_pickle=True)