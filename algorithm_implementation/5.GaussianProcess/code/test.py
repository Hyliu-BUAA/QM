import numpy as np 
import matplotlib.pyplot as plt


class GPR(object):
    def __init__(self, optimize:bool=True):
        self.is_fit = False
        self.X_train, self.y_train = None, None
        self.params = {'l': 0.5, 'sigma_f': 0.2}
        self.optimize = optimize
    
    
    def fit(self, X:np.array, y:np.array):
        '''
        Parameters
        ----------
            1. X: np.array (二维, 列向量形式)
            2. y: np.array (一维)
        '''
        self.is_fit = True
        self.X_train = X
        self.y_train = y

    
    def gaussian_kernel(self, x1:np.array, x2:np.array):
        '''
        Parameters
        ----------
            1. x1: np.array (二维, 列向量形式)
            2. x2: np.array (二维, 列向量形式)
        '''
        print((np.sum(np.power(x1, 2), 1).reshape(-1, 1) + np.sum(np.power(x2, 2), 1).reshape(1, -1)).shape)
        print((2 * x1.T * x2).shape)
        ### 注意下面这一句的写法
        dist_matrix = np.sum(np.power(x1, 2), 1).reshape(-1, 1) + \
                    np.sum(np.power(x2, 2), 1).reshape(1, -1) - \
                    2 * x1 * x2.T
        return np.power(self.params["sigma_f"], 2) * np.exp(-0.5 * dist_matrix / np.power(self.params["l"], 2))
    

    def predict(self, X:np.array):
        '''
        Parameters
        ----------
            1. X: np.array (二维, 列向量形式)
        '''
        if not self.is_fit:
            print("GPR Model not fit yet.")
            return None
        
        X = np.asarray(X)
        Kff = self.gaussian_kernel(self.X_train, self.X_train)  # (N, N)
        Kyy = self.gaussian_kernel(X, X)                        # (k, k)
        Kfy = self.gaussian_kernel(self.X_train, X)             # (N, k)
        Kff_inv = np.linalg.inv(Kff)

        mu = Kfy.T.dot(Kff_inv).dot(self.y_train)   # 矩阵的乘法
        cov = Kyy - Kfy.T.dot(Kff_inv).dot(Kfy)     # 矩阵的乘法
        
        return mu, cov
    

def get_y(x, noise_sigma=0.0):
    '''
    Parameters
    ----------
        1. x: np.array (二维, 列向量形式)

    Return 
    ------
        1. y.ravel(): np.array (一维)
    '''
    x = np.asarray(x)
    y = np.cos(x) + np.random.normal(0, noise_sigma, size=x.shape)
    return y.ravel()


def plot_gaussian_process(X_train:np.array,
                        y_train:np.array,
                        X_test:np.array,
                        y_test:np.array,
                        uncertainty:np.array):
    '''
    Parameters
    ----------
        1. X_train: np.array (二维，列向量形式)
        2. y_train: np.array (二维，列向量形式)
        3. X_test:  np.array (一维)
        4. y_test:  np.array (一维)
    '''
    X_train = X_train.ravel()
    y_train = y_train.ravel()
    X_test = X_test.ravel()
    y_test = y_test.ravel()
    uncertainty = uncertainty.ravel()

    plt.figure(figsize=(8, 6))
    plt.fill_between(X_test,
                    y_test+uncertainty,
                    y_test-uncertainty,
                    alpha=0.1)
    plt.plot(X_test,
            y_test,
            label="predict")
    plt.scatter(X_train,
                y_train,
                marker='^',
                color="red",
                s=80,
                zorder=2,
                label="train")
    plt.legend()

    plt.savefig(output_png_path, dpi=300)


if __name__ == "__main__":
    output_png_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/algorithm_implementation/5.GaussianProcess/notes/pics/pic_2.png"

    X_train = np.array([3, 1, 4, 5, 9]).reshape(-1, 1)
    y_train = get_y(X_train, noise_sigma=0.0)
    X_test = np.arange(0, 10, 0.1).reshape(-1, 1)

    gpr = GPR()
    gpr.fit(X_train, y_train)
    mu, cov = gpr.predict(X_test)
    uncertainty = 1.96 * np.sqrt( np.diag(cov) )
    
    y_train = y_train.ravel()
    y_test = mu.ravel()

    # 绘图
    plot_gaussian_process(X_train=X_train,
                        y_train=y_train,
                        X_test=X_test,
                        y_test=y_test,
                        uncertainty=uncertainty)