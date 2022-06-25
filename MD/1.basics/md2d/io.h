/*
 * @Author: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @Date: 2022-06-24 17:10:13
 * @LastEditors: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @LastEditTime: 2022-06-24 17:52:08
 * @FilePath: /Quantum_Mechanics/MD/1.basics/code/io.h
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#ifndef IO_H
#define IO_H

#include <iostream>
typedef double real;


class ParamsSetter {
private: 
    // member variables
    real deltaT;        // 时间步长
    real density;       // 流体密度
    int initUcell_x;    // 方格在 x 轴方向上的大小
    int initUcell_y;    // 方格在 y 轴方向上的大小
    int stepAvg;        // 用来抽样统计的步数
    int stepEquil;       // 平衡步数
    int stepLimit;      // 模拟循环步数
    real temperature;   // 温度设置

public:
    // Constructor
    ParamsSetter() : 
        deltaT(0.05),
        density(0.8),
        initUcell_x(20),
        initUcell_y(20),
        stepAvg(100),
        stepEquil(0),
        stepLimit(500),
        temperature(1.)
    {   }

    // friend function -- operator <<
    friend std::ostream& operator<<(std::ostream&, ParamsSetter&);

};


#endif