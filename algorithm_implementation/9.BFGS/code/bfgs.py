'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-10-19 14:25:15
LastEditTime : 2022-10-19 15:40:52
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
                ):
        self.num_dims = x0_array.shape[0]
        self.c1 = c1
        self.c2 = c2
        self.max_step_length = max_step_length

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
            1. Return `search step length`
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
        pass



if __name__ == "__main__":
    x0_array = np.array( [-1.2, 1] )
    bfgs = BFGS(x0_array=x0_array)
    print( bfgs.rosenbrock_func(x_array=x0_array) )
    print( bfgs.get_nabla(x0_array) )