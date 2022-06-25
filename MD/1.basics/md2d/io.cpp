/*
 * @Author: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @Date: 2022-06-24 17:11:41
 * @LastEditors: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @LastEditTime: 2022-06-24 17:53:10
 * @FilePath: /Quantum_Mechanics/MD/1.basics/code/io.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%A
 */
#include "io.h"
#include <fstream>
#include <iostream>
#include <string>

// overload operator<< for `ParamsSetter`
std::ostream& operator<<(std::ostream& COUT, ParamsSetter &ps) {
    std::cout << "delta = " << ps.deltaT << std::endl;
    std::cout << "density = " << ps.density << std::endl;
    std::cout << "initUcell_x = " << ps.initUcell_x << std::endl;
    std::cout << "initUcell_y = " << ps.initUcell_y << std::endl;
    std::cout << "stepAvg = " << ps.stepAvg << std::endl;
    std::cout << "stepEquil = " << ps.stepEquil << std::endl;
    std::cout << "stepLimit = " << ps.stepLimit << std::endl;
    std::cout << "temperature = " << ps.temperature << std::endl;

    return COUT;
}


/*
// Test Code

int main() {
    ParamsSetter ps;
    std::cout << ps;
    return 0;
}
*/