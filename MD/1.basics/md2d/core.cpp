/*
 * @Author: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @Date: 2022-06-24 18:28:24
 * @LastEditors: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @LastEditTime: 2022-06-25 14:28:56
 * @FilePath: /Quantum_Mechanics/MD/1.basics/code/core.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include "core.h"
#include <cmath>



/*
    Part II. class `Molecules`
*/
// Constructor
Molecules::Molecules(
        Molecule *moleculesLst_value, 
        int dimension_value,
        VecR region_value,  // region.x = x轴方向长度，region.y = y轴方向长度
        VecI initUcell_value,
        real rCut_value,
        real T_value) {
    num_molecules = initUcell_value.x * initUcell_value.y;
    moleculesLst = new Molecule[num_molecules];

    dimension = dimension_value;
    region = region_value;
    initUcell = initUcell_value;
    rCut = rCut_value;
    T = T_value;
}


// Copy constructor
Molecules::Molecules(const Molecules& origin_Molecules) {
    num_molecules = origin_Molecules.num_molecules;
    moleculesLst = new Molecule[num_molecules];

    dimension = origin_Molecules.dimension;
    region = origin_Molecules.region;
    initUcell = origin_Molecules.initUcell;
    rCut = origin_Molecules.rCut;
    T = origin_Molecules.T;
}


// operator=
Molecules& Molecules::operator=(const Molecules& origin_Molecules) {
    num_molecules = origin_Molecules.num_molecules;
    moleculesLst = new Molecules[num_molecules];

    dimension = origin_Molecules.dimension;
    region = origin_Molecules.region;
    initUcell = origin_Molecules.initUcell;
    rCut = origin_Molecules.rCut;
    T = origin_Molecules.T;

    return *this;
}


// Destructor
Molecules::~Molecules() {
    delete [] moleculesLst;
}


// member function -- CalculateVelMag(): 根据温度计算速度的振幅
real Molecules::CalculateVelMag() {
    real velMag = sqrt( dimension * (1-num_molecules) * T );
    return velMag;
}


// member function -- InitCoords()
void Molecules::InitCoords() {
    VecR tmp_coord, gap;
    
    gap.x = region.x / initUcell.x;
    gap.y = region.y / initUcell.y;

    int n = 0;
    for (int nx = 0; nx < initUcell.x; nx++)    {
        for (int ny = 0; ny < initUcell.y; ny++) {
            tmp_coord.x = nx + 0.5;
            tmp_coord.y = ny + 0.5;
            // 缩放
            tmp_coord.x = tmp_coord.x * gap.x;
            tmp_coord.y = tmp_coord.y * gap.y;
            // 移动该区域，使区域的中心在原点
            tmp_coord.x = tmp_coord.x - 0.5 * region.x;
            tmp_coord.y = tmp_coord.y - 0.5 * region.y;
            // 初始化第 n 个 molecule 的坐标
            moleculesLst[n].r = tmp_coord;
            ++n;
        }
    }
}


// member function -- InitVels()
void Molecules::InitAccels() {
    real velMag = CalculateVelMag();
    
}



// member function -- InitAccels()
void Molecules::InitAccels() {
    // 加速度均初始化为 [0, 0]
    for (int i = 0; i < num_molecules; i++) {
        moleculesLst[i].ra.x = 0;
        moleculesLst[i].ra.y = 0;
    }
}