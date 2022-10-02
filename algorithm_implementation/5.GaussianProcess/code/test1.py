import numpy as np 
from scipy.optimize import minimize
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(412342)
#np.random.seed(4123)

'''
Part I. Gaussian Process Regressor Class
'''
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
        self.X_train = X
        self.y_train = y

        ### hyper parameters optimization
        ### 注意下段代码的写法
        def negative_log_likehood_loss(params):
            '''
            Note
            -----
                1. y: np.array (一维形式)

            Return
            ------
                1. loss.ravel() : np.array (一维形式)
            '''
            self.params['l'], self.params['sigma_f'] = params[0], params[1]
            Kyy = self.gaussian_kernel(self.X_train, self.X_train) + 1e-8 * np.eye(len(self.X_train))

            loss = (0.5 * self.y_train.T.dot(np.linalg.inv(Kyy)).dot(self.y_train)) + \
                0.5 * np.linalg.slogdet(Kyy)[1] + \
                0.5 * len(self.X_train) * np.log(2 * np.pi)

            #print(np.linalg.inv(Kyy))
            #print( 0.5 * self.y_train.T.dot(np.linalg.inv(Kyy)).dot(self.y_train) ) 
            #print( 0.5 * np.linalg.slogdet(Kyy)[1] )
            #print( 0.5 * len(self.X_train) * np.log(2 * np.pi) )
            
            return loss.ravel()

        if self.optimize:
            res = minimize(negative_log_likehood_loss,
                        [self.params["l"], self.params["sigma_f"]],
                        bounds=((1e-4, 1e4), (1e-4, 1e4)),
                        method="L-BFGS-B")
            self.params["l"], self.params["sigma_f"] = res.x[0], res.x[1]

        self.is_fit = True

    
    def gaussian_kernel(self, x1:np.array, x2:np.array):
        '''
        Parameters
        ----------
            1. x1: np.array (二维, 列向量形式)
            2. x2: np.array (二维, 列向量形式)
        '''
        ### 注意下面这一句的写法
        dist_matrix = np.sum(np.power(x1, 2), 1).reshape(-1, 1) + \
                    np.sum(np.power(x2, 2), 1).reshape(1, -1) - \
                    (2 * x1.dot(x2.T))
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
    

'''
Part II. Get y from X
'''
def get_y_2d(x, noise_sigma=0.0):
    '''
    Parameters
    ----------
        1. x: np.array (二维, 列向量形式)

    Return 
    ------
        1. y.ravel(): np.array (一维)
    '''
    x = np.asarray(x)
    y = np.sin(0.5 * np.linalg.norm(x, axis=1))     # 行向量的模长
    y += np.random.normal(0, noise_sigma, size=y.shape)
    return y.ravel()



'''
Part IV. Driver code
'''
if __name__ == "__main__":
    output_png_path = "/Users/mac/我的文件/Notebook/Quantum_Mechanics/algorithm_implementation/5.GaussianProcess/notes/pics/pic_5.png"

    X_train = np.random.uniform(-4, 4, (100, 2)) #.tolist()
    y_train = get_y_2d(X_train, noise_sigma=1e-4)

    test_d1 = np.arange(-5, 5, 0.2)
    test_d2 = np.arange(-5, 5, 0.2)
    test_d1, test_d2 = np.meshgrid(test_d1, test_d2)
    X_test = np.asarray( [[d1, d2] for d1, d2 in zip(test_d1.ravel(), test_d2.ravel())] )


    gpr = GPR(optimize=False)
    gpr.fit(X_train, y_train)
    mu, cov = gpr.predict(X_test)
    z = mu.reshape(test_d1.shape)

    fig = plt.figure(figsize=(7, 5))
    ax = Axes3D(fig)
    ax.plot_surface(test_d1, test_d2, z, cmap=cm.coolwarm, linewidth=0, alpha=0.2, antialiased=False)
    ax.scatter(np.asarray(X_train)[:,0], np.asarray(X_train)[:,1], y_train, c=y_train, cmap=cm.coolwarm)
    ax.contourf(test_d1, test_d2, z, zdir='z', offset=0, cmap=cm.coolwarm, alpha=0.6)
    ax.set_title("l=%.2f sigma_f=%.2f" % (gpr.params["l"], gpr.params["sigma_f"]))
    
    plt.savefig("/Users/mac/我的文件/Notebook/Quantum_Mechanics/algorithm_implementation/5.GaussianProcess/notes/pics/3d_unopt.jpg",
                dpi=300)