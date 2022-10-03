import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process.kernels import ConstantKernel, RBF
from sklearn.gaussian_process import GaussianProcessRegressor


'''
Part II. Get y from X
'''
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


'''
Part III. Plot function
'''
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

    plt.show()



if __name__ == "__main__":
    X_train = np.array([3, 1, 4, 5, 9]).reshape(-1, 1)
    y_train = get_y(X_train, noise_sigma=0.0)
    X_test = np.arange(0, 10, 0.1).reshape(-1, 1)

    kernel = ConstantKernel(constant_value=0.2,
                            constant_value_bounds=(1e-4, 1e4) ) * \
            RBF(length_scale=0.5,
                length_scale_bounds=(1e-4, 1e4))

    gpr = GaussianProcessRegressor(kernel=kernel,
                                n_restarts_optimizer=2)

    gpr.fit(X_train, y_train)
    mu, cov = gpr.predict(X_test, return_cov=True)
    uncertainty = 1.96 * np.sqrt( np.diag(cov) )

    y_train = y_train.ravel()
    y_test = mu.ravel()

    plot_gaussian_process(X_train=X_train,
                        y_train=y_train,
                        X_test=X_test,
                        y_test=y_test,
                        uncertainty=uncertainty)
    
    print(gpr.kernel_.k2.length_scale,
            gpr.kernel_.k1.constant_value)