/*
 * @Author: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @Date: 2022-06-24 18:00:57
 * @LastEditors: Uper 41718895+Hyliu-BUAA@users.noreply.github.com
 * @LastEditTime: 2022-06-25 15:55:09
 * @FilePath: /Quantum_Mechanics/MD/1.basics/md2d/core.h
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#ifndef CORE_H
#define CORE_H


typedef double real;
typedef struct {
    real x, y;
} VecR;
typedef struct {
    int x, y;
} VecI;


class Molecule {
/*
Description
-----------
    1. 单个分子的类
*/
private:
    VecR r, rv, ra;

public:
    // Constructor 1
    Molecule() = default;
    
    // Constructor 2
    Molecule(Vec &r_value, Vec &rv_value, Vec &ra_value) : 
                    r(r_value), 
                    rv(rv_value),
                    ra(ra_value)
    {   }
};



class Molecules {
/*
Description
-----------
    1. 体系内所有分子的类，描述体系内所有的 molecules

Attributes
----------
    1. moleculeLst: pointer to `Molecule`
    2. region: VecR
    3. initUcell: VecI
    4. rCut: real
    5. num_molecules: int
    6. T: real
*/
private:
    Molecule *moleculesLst;
    int dimension;
    VecR region;
    VecI initUcell;
    real rCut;
    int num_molecules;
    real T;


public:
    // Constructor
    Molecules(Molecule*, int, VecR, VecI, real, int, real);

    // Copy constructor
    Molecules(const Molecules&);

    // Copy assignment operator
    Molecules& operator=(const Molecules&);

    // Destructor
    ~Molecules();

    // member function -- CalculateVelMag()
    real CalculateVelMag();

    // member function -- InitCoords()
    void InitCoords();

    // member function -- InitVels()
    void InitVels();

    // member function -- InitAccels()
    void InitAccels();
};



class Property {
private:
    int numMolecules;   // 体系内`分子/原子`的数目
    real value;     // 值
    real sum;       // 和
    real sum2;      // 平方和
    real average;   // 平均值
    real std;   // 标准差standard deviaion

public:
    // Constructor 
    Property(int);

    // Set sum and sum2 to 0
    void SetZero();

    void GetSum();

    void GetAverage();
};



class Properties {
private:
    real totEnergy;
    real kinEnergy;
    real pressure;

public:
    void PropZero()
};



#endif
