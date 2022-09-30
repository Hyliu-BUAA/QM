import numpy as np


class GPR(object):
    def __init__(self, optimize:bool=True):
        self.is_fit = False
        self.train_X, self.train_y = None, None
        self.params = {"l": 0.5, "sigma_f": 0.2}    # 500 10
        self.optimize = optimize
    

    def fit(self, X, y):
        # store
        self.train_X = np.asarray(X)
        self.train_y = np.asarray(y)
        self.is_fit = True

    
    def kernel(self, x1, x2):
        dist_matrix = np.sum( np.power(x1, 2), 1 ).reshape(-1, 1) + \
                        np.sum( np.power(x2, 2), 1 ).reshape(1, -1) - \
                        2 * x1 * x2.T
        return self.params["sigma_f"] ** 2 * np.exp(-0.5 / self.params["l"] ** 2 * dist_matrix)


if __name__ == "__main__":
    x = np.array([700, 800, 1029]).reshape(-1, 1)
    gpr = GPR()
    gpr.params["l"] = 500
    gpr.params["sigma_F"] = 10
    print( gpr.kernel(x, x) )