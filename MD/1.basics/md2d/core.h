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

#endif