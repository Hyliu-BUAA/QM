'''
Author       : Liu Hanyu
Email        : hyliu2016@buaa.edu.cn
Date         : 2022-10-04 15:26:51
LastEditTime : 2022-10-04 16:23:30
FilePath     : /Quantum_Mechanics/algorithm_implementation/5.GaussianProcess+贝叶斯优化/notes/BayesianOptimization_package/test.py
Description  : 
'''
import scipy

assert (scipy.__version__ == "1.7.0")

from bayes_opt import BayesianOptimization


def black_box_function(x, y):
    return -x ** 2 - (y-1) ** 2 + 1



if __name__ == "__main__":
    pbounds = {'x': (2, 4),
                'y':(-3, 3)}

    ### 1. Initialize
    bo = BayesianOptimization(
                f=black_box_function,
                pbounds=pbounds,
                verbose=2,
                random_state=1,
                )

    
    ### 2. Run
    bo.maximize(
            init_points=2,
            n_iter=3,
            )

    ### 3. change pbounds
    bo.set_bounds(
            new_bounds={"x": (-2, 3)},
            )
    bo.maximize(
            init_points=0, 
            n_iter=5,
            )
    

    ### 4. probe 
    # way1: dict
    bo.probe(
            params={"x": 0.5, "y":0.7},
            lazy=True,
            )
    
    # way 2: list
    print(bo.space.keys)
    bo.probe(
            params=[-0.3, 0.1],
            lazy=True
            )
    
    bo.maximize(
            init_points=0,
            n_iter=0
            )