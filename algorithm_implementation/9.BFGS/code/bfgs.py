'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-10-19 14:25:15
LastEditTime : 2022-10-19 16:51:23
FilePath     : /Quantum_Mechanics/algorithm_implementation/9.BFGS/code/bfgs.py
Description  : 
'''
import numpy as np


class BFGS(object):
    def __init__(self,
                x0_array:np.array,
                c1:float,
                c2:float,
                max_step_length:float,
                max_num_iters:int,
                ):
        self.x0_array = x0_array
        self.num_dims = x0_array.shape[0]
        self.c1 = c1
        self.c2 = c2
        self.max_step_length = max_step_length
        self.max_num_iters = max_num_iters

        self.h = np.cbrt( np.finfo(float).eps )


    def rosenbrock_func(self,
                        x_array:np.array,
                        ):
        dia = np.diag(x_array, 0)
        off_dia = np.ones(self.num_dims - 1)
        off_dia = np.diag(off_dia, 1)
        first_term = 100 * np.power((-dia + off_dia)@x_array, 2)
        second_term = np.power(x_array - 1, 2)
        result = np.sum((first_term+second_term)[:-1], axis=0)
        
        return result

    
    def get_nabla(self,
                x_array:np.array,
                ):
        nabla_array = np.zeros(self.num_dims)

        for idx in range(self.num_dims):
            x_before = np.copy(x_array)
            x_next = np.copy(x_array)

            x_before[idx] -= self.h
            x_next[idx] += self.h
            
            nabla_array[idx] = \
                (self.rosenbrock_func(x_next) - self.rosenbrock_func(x_before)) / (2*self.h)

        return nabla_array                


    def line_search(self,
                    x_array:np.array,
                    direction:np.array,
                    ):
        '''
        Description
        -----------
            1. 已知`search direction`, 返回`search step length`
        '''
        alpha = self.max_step_length
        nabla_array = self.get_nabla(x_array=x_array)
        x_array_new = x_array + alpha * direction
        nabla_array_new = self.get_nabla(x_array=x_array)

        while (
                self.rosenbrock_func(x_array=x_array_new) >= 
                (self.rosenbrock_func(x_array=x_array) + self.c1*alpha*nabla_array.T@direction)
                ).any() \
            and \
              (
                nabla_array_new.T@direction <= self.c2*nabla_array.T@direction
              ).any():
            alpha *= 0.5
            x_array_new = x_array + alpha * direction
            nabla_array_new = self.get_nabla(x_array=x_array)
        
        return alpha

    
    def optimize(self):
        num_iters = 0                                       # dimension of problem 
        x_array = self.x0_array
        nabla_array = self.get_nabla(x_array=x_array)       # initial gradient 
        H = np.eye(self.num_dims)                           # initial Hessian


        ### Loop to optimize
        while np.linalg.norm(nabla_array) > 1e-5:   # While gradient is positive
            if num_iters > self.max_num_iters:
                print("Maximum iterations reached!")
                break
                
            
            num_iters += 1
            #print(nabla_array)
            direction = -H@nabla_array                      # search direction (Newton Method), np.array
            alpha = self.line_search(x_array=x_array,       # seach step length, float
                                    direction=direction)

            s = alpha * direction                           # 1. calcualte `s` in BFGS equation 
            x_array_new = x_array + alpha * direction
            nabla_array_new = self.get_nabla(x_array=x_array_new)
            y = nabla_array_new - nabla_array               # 2. calculate `y` in BFGS equation

            ### Importance!!!
            # s.reshape(-1, 1), y.reshape(-1, 1): make s, y to be column vector
            s = np.array([s]).reshape(-1, 1)
            y = np.array([y]).reshape(-1, 1)


            H_left = np.eye(self.num_dims) - s@y.T / (y.T@s)[0, 0]
            H_right = np.eye(self.num_dims) - y@s.T / (y.T@s)[0, 0]
            addition_term = s@s.T / (y.T@s)[0, 0]

            ### Update the Hessian_matrix, x_array, nabla_array
            H = H_left@H@H_right + addition_term    # 3. update Hessian matrix
            nabla_array = nabla_array_new
            x_array = x_array_new
        
        return x_array




if __name__ == "__main__":
    x0_array = np.array( [-1.2, 1] )
    c1 = 1e-4
    c2 = 0.9
    max_step_length = 1
    max_num_iters = 100

    bfgs = BFGS(
                x0_array=x0_array,
                c1=c1,
                c2=c2,
                max_step_length=max_step_length,
                max_num_iters=max_num_iters
                )

    print( bfgs.optimize() )