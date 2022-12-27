'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-09-10 11:14:27
LastEditTime : 2022-12-27 19:13:48
FilePath     : /Quantum_Mechanics/algorithm_implementation/1.GD/code/gd.py
Description  : 
'''
import numpy as np


class GradientDescent(object):
    '''
    Note
    ----
        1. 计算时需要转换为 np.matrix 形式
        2. 其他时候需要转换为 np.array 形式
        3. x_array: M * N
        4. y_array = y_array.reshpe(-1, 1)
        5. theta_array = theta_array.reshape(-1, 1)
        6. partial_J_array = partial_J_array.reshape(-1, 1)
    '''
    def __init__(self,
                x_array:np.array,
                theta_array:np.array,
                y_array:np.array,
                learning_rate:float,
                num_epochs: int,
                ):
        self.x_array = x_array
        self.theta_array = theta_array.reshape(-1, 1)
        self.y_array = y_array.reshape(-1, 1)
        self.learning_rate = learning_rate
        self.num_examples = self.x_array.shape[0]
        self.num_epochs = num_epochs

    
    def h(self):
        '''
        Description
        -----------
            1. Hypothesis function
        
        Return
        ------
            1. result_array: np.array
                yp_array
        '''
        x_mtx = np.matrix(self.x_array)
        theta_mtx = np.matrix(self.theta_array)    # 转换成列向量形式
        result_array = np.array( np.matmul(x_mtx, theta_mtx) ).reshape(-1, 1)
        return result_array


    def cost_function(self,
            yp_array:np.array,
            y_array:np.array,
            ):
        '''
        Description
        -----------
            1. Cost function
        '''
        return np.sum( np.power(yp_array - y_array, 2) ) / (2 * self.num_examples)


    def run(self):
        '''
        Description
        -----------
            1. The main part of Gradient Descent
        '''
        for _ in range(self.num_epochs):
            yp_array = self.h()
            partial_J_array = (np.sum((yp_array - self.y_array) * self.x_array, axis=0) / self.num_examples).reshape(-1, 1)
            self.theta_array = self.theta_array - self.learning_rate * partial_J_array
        return self.theta_array



if __name__ == "__main__":
    x_array = np.array([[1,2,3], [1,2,3]])
    theta_array = np.array([1,2,3])
    y = np.array([14, 15])
    learning_rate = 0.01
    num_epochs = 1000

    gd = GradientDescent(
                x_array=x_array,
                theta_array=theta_array,
                y_array=y,
                learning_rate=learning_rate,
                num_epochs=num_epochs
                )

    print(gd.cost_function(yp_array=gd.h(), y_array=y))
    print(gd.run())
    print(gd.cost_function(yp_array=gd.h(), y_array=y))
