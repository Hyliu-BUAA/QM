/*
 * @Author: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @Date: 2022-06-27 15:25:32
 * @LastEditors: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @LastEditTime: 2022-06-28 00:10:01
 * @FilePath: /Quantum_Mechanics/algorithm_implementation/3.Leapfrog/code/test.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <fstream>
#include <vector>
#include <string>
#include <cmath>


class LeapFrog {
private:
    std::vector<double> LocationsLst;       // 存储 full-step 的位置
    std::vector<double> AccelerationsLst;   // 存储 full-step 的加速度
    std::vector<double> VelocitiesLst;      // 存储 half-step 的速度
    double DeltaT;                          // 时间步长
    double TotalT;                          // 总模拟时间
    int NumSteps;                           // 总模拟步数 = 总模拟时间 / 时间步长
    std::ofstream FileCout;     


public:
    LeapFrog(double location_origin,
            double velocity_origin,
            double deltaT,
            double totalT,
            std::string output_path) {
        /*
        Description
        -----------
            1. Constructor function
        */
        LocationsLst.push_back(location_origin);       // 初始化 full-step 处的 `位置`
        double acceleration_origin = CalculateAcceleration(location_origin);
        AccelerationsLst.push_back(acceleration_origin);   // 初始化 full-step 处的 `加速度`
        VelocitiesLst.push_back(velocity_origin);      // 初始化 half-step 处的 `速度`

        DeltaT = deltaT;    // 初始化时间步长
        TotalT = totalT;    // 初始化总模拟时长
        NumSteps = TotalT / DeltaT; // 初始化总模拟步数

        FileCout.open(output_path);
    }


    double CalculateAcceleration(double location) {
        /*
        Description
        -----------
            1. 已知 `加速度` 与 `位移` 的关系为： x'' + x = 0
        */
        return (-location);
    }


    double CalculateTime(int idx_step) {
        /*
        Description
        -----------
            1. 根据 idx_step 计算当前时间
        */
        return idx_step * DeltaT;
    }


    void WalkFullStep(int idx_step) {
        /*
        Description
        -----------
            1. 计算下一个 full-step 的 `位置` 和 `加速度`
        */
        double new_location = LocationsLst[idx_step-1] + DeltaT * VelocitiesLst[idx_step-1];
        LocationsLst.push_back(new_location);
        double new_acceleration = CalculateAcceleration(new_location);
        AccelerationsLst.push_back(new_acceleration);
    }


    void WalkHalfStep(int idx_step) {
        /*
        Description
        -----------
            1. 计算下一个 half-step 的 `速度`
        */
       double new_velocity = VelocitiesLst[idx_step-1] + DeltaT * AccelerationsLst[idx_step];
       VelocitiesLst.push_back(new_velocity);
    }


    void run() {
        // 输出格式：时间、加速度、速度、位置
        FileCout << 0 << ',' 
                << LocationsLst[0] << std::endl;

        for (int i=1; i < NumSteps + 1; i++) {
            WalkFullStep(i);
            WalkHalfStep(i);

            // 输出
            double timeNow = CalculateTime(i);
            FileCout << timeNow << ',' 
                    << LocationsLst[i] << std::endl;
        }
    }
};


int main() {
    double location_origin = 0;
    double velocity_origin = 1;

    double num_cycles = 5;   // 模拟周期的个数
    double totalT = num_cycles * 2 * M_PI;   // 模拟总时长 = 模拟周期的个数 * 周期长度

    double num_points_per_cycle = 16;   // 每个周期内取点个数
    double deltaT = 2 * M_PI / num_points_per_cycle;    // 时间步长 = 周期长度 / 周期内取点个数

    std::string output_path = "./output.csv";


    LeapFrog leap_frog(location_origin, velocity_origin, deltaT, totalT, output_path);
    leap_frog.run();

    return 0;
}