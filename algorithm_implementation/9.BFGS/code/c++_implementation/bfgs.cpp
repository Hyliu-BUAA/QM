#include <iostream>
#include <Eigen/Dense>

// #define NDIMS 2
const int NDIMS = 2;

class BFGS {
private:
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> x_vector(NDIMS, 1);

public:
    // 1. Constructor function
    BFGS(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> x_vector);

    // 2. Member functions
    double rosenbrock_func(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> x_vectror);    
};


// 1. Constructor function
BFGS::BFGS(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &x_vector) {
    this->x_vector = x_vector;
}


// 2. Member function -- rosenbrock function
double BFGS::rosenbrock_func(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> x_vectror) {
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> dia(NDIMS, NDIMS);
    dia = this->x_vector.asDiagonal();
    return dia;
}



// Driver code
int main {
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> x_vector(NDIMS, 1);
    x_vector << -1.2, 1;

    bfgs = BFGS(x_vector);


    return 0;
}