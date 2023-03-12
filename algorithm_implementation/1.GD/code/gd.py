import numpy as np



class GradientDescent(object):
    def __init__(
                self,
                theta_array:np.ndarray,
                x_array:np.ndarray,
                y_array:np.ndarray,
                learning_rate:float,
                num_epochs:int,
                ):
        self.theta_array = theta_array
        self.x_array = x_array
        self.y_array = y_array
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.num_examples = x_array.shape[0]
    

    def h(
        self,
        theta_array:np.ndarray,
        x_array:np.ndarray,
        ):
        result = np.dot( x_array, theta_array.reshape(-1, 1) )
        return result.flatten()


    def cost_func(
            self,
            theta_array:np.ndarray,
            x_array:np.ndarray,
            y_array:np.ndarray,
            ):
        y_pred = self.h(
                    theta_array=theta_array,
                    x_array=x_array)
        loss = np.sum(np.power(y_pred - y_array, 2), axis=0) / (2*self.num_examples)
        return loss


    def update(
            self,
            theta_array:np.ndarray,
            x_array:np.ndarray,
            y_array:np.ndarray,
            learning_rate:float,
    ):
        y_pred = np.dot(x_array, theta_array.reshape(-1, 1)).flatten()
        diff_array = y_pred - y_array
        differential_array = (np.dot(x_array.T, diff_array.reshape(-1, 1)) / self.num_examples).flatten()
        new_theta_array = theta_array - learning_rate * differential_array.reshape(1, -1)

        return new_theta_array


    def loop_update(            
            self,
            theta_array:np.ndarray,
            x_array:np.ndarray,
            y_array:np.ndarray,
            learning_rate:float,
    ):
        for _ in range(self.num_epochs):
            theta_array = self.update(
                        theta_array=theta_array,
                        x_array=x_array,
                        y_array=y_array,
                        learning_rate=learning_rate,
                        )
            print(self.cost_func(theta_array=theta_array, x_array=self.x_array, y_array=self.y_array))
        return theta_array


if __name__ == "__main__":
    data = np.load(file="/Users/mac/我的文件/Notebook/Quantum_Mechanics/algorithm_implementation/1.GD/code/data.npy")
    x_array = data[:, :-1]      # (100, 10)
    y_array = data[:, -1].flatten() # (100,)
    theta_array = np.random.randn(10)   # (10,)
    learning_rate = 0.01
    num_epochs = 1000


    gd = GradientDescent(
                theta_array=theta_array,
                x_array=x_array,
                y_array=y_array,
                learning_rate=learning_rate,
                num_epochs=num_epochs,
    )

    """
    print(gd.h(gd.theta_array, gd.x_array))
    print(gd.cost_func(
                    theta_array=gd.theta_array,
                    x_array=gd.x_array,
                    y_array=gd.y_array)
    )
    print(gd.update(
                    theta_array=gd.theta_array,
                    x_array=gd.x_array,
                    y_array=gd.y_array,
                    learning_rate=learning_rate
    ))
    """
    print(gd.loop_update(
            theta_array=gd.theta_array,
            x_array=gd.x_array,
            y_array=gd.y_array,
            learning_rate=gd.learning_rate,
            ))