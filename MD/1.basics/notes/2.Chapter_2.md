# 1. `C 语言`: 随机数的产生 (Random number generation)
## 1.1. 生成在 `0~1` 范围内均匀分布的随机数
```c++
#include <iostream>

#define IADD 453806245
#define IMUL 314159269
#define MASK 2147483647
#define SCALE 0.4656612873e-9

typedef double real;

real RandR(int randSeed) {  // 产生分布在 `0~1` 范围内、均匀分布的随机数
    randSeed = ( randSeed * IMUL + IADD ) & MASK;
    return (randSeed * SCALE);
}

int main(int argc, char **argv) {
    real a = RandR();
    std::cout << a << std::endl;
    return 0;
}
```
Output:
```shell
$ g++ -std=c++20 -Og main.cpp -o ./main
$ ./main 123
0.205213
$ ./main 1321412341
0.833315
```

## 1.2. 产生均匀分布的、随机分布的单位向量 (二维)
```c++
#include <iostream>
#include <cstdlib>
#include <cmath>

#define IADD 453806245
#define IMUL 314159269
#define MASK 2147483647
#define SCALE 0.4656612873e-9


typedef double real;
typedef struct {
    real x, y;
} VecR;


real RandR(int randSeed) {
    randSeed = ( randSeed * IMUL + IADD ) & MASK;
    return (randSeed * SCALE);
}


void VRand(int randSeed, VecR *p) { // 产生均匀分布的、随机分布的单位向量 (二维)
    /*
    Return
    ------
        1. [sin_value, cos_value]
    */
    real s = 2. * M_PI * RandR(randSeed);
    p->x = sin(s);
    p->y = cos(s);
}



int main(int argc, char **argv) {
    int randSeed = std::atoi(argv[1]);

    VecR *ptr = new VecR;
    VRand(randSeed, ptr);
    std::cout << '[' << ptr->x << ','
            << ptr->y << ']' << std::endl;
    delete ptr;

    return 0;
}
```
Output:
```shell
$ g++ -Og -std=c++20 main.cpp -o main
$ ./main 12
[-0.206959,0.97835]
```

## 1.3. 产生均匀分布的、随机方向的单位向量 (三维)
```c++
#include <iostream>
#include <cstdlib>
#include <cmath>

#define IADD 453806245
#define IMUL 314159269
#define MASK 2147483647
#define SCALE 0.4656612873e-9
#define Sqr(x)  \
    pow(x, 2)

typedef double real;
typedef struct {
    real x, y, z;
} VecR;


real RandR(int randSeed) {
    randSeed = ( randSeed * IMUL + IADD ) & MASK;
    return (randSeed * SCALE);
}


void VRand(int randSeed_1, int randSeed_2, VecR *p) {
    /*
        返回三个在 `-1 ~ 1` 之间的数组成的数组
    */
    real s, x, y;
    
    s= 2.;
    while (s > 1.) {
        x = 2. * RandR(randSeed_1) - 1.;
        y = 2. * RandR(randSeed_2) - 1.;
        s = Sqr(x) + Sqr(y);
    }
    p->z = 1 - 2. * s;
    s = 2. * sqrt(1. - s);
    p->x = s * x;
    p->y = s * y;
}



int main(int argc, char **argv) {
    int randSeed_1 = std::atoi(argv[1]);
    int randSeed_2 = std::atoi(argv[2]);

    VecR *ptr = new VecR;
    VRand(randSeed_1, randSeed_2, ptr);
    std::cout << '[' << ptr->x << ','
            << ptr->y << ','
            << ptr->z << ']' << std::endl;
    delete ptr;

    return 0;
}
```
Output:
```shell
$ g++ -Og -std=c++20 main.cpp -o main
$ ./main 12 23
[0.605608,0.0986358,-0.789627]
```


# 2. `C++` 随机数
## 2.1. `std::rand()`
1. The `std::rand()` function is used in C/C++ to generate random numbers in range of `[0, RAND_MAX)`

<font color="red" size=""3>

Note
----
1. If random numbers are `generated with rand() without first calling srand()`, your program will `create the same sequence of numbers` each time it runs.

</font>

### 2.1.1. Syntax
```c++
int rand(void)

/*
Return
------
    1. Returns a pseudo-random number in the range of [0, RAND_MAX). 

Note
----
    1. `RAND_MAX`: is a constant whose default value may vary  between implementations but it is granted to be at least `32767`.
*/
```

### 2.1.2. Demo 1: generate random number without calling `srand()` first
1. Say if we are generating 5 random numbers in C with the help of rand() in a loop, then every time we compile and run the program our output must be the same sequence of numbers.

```c++
// C++ program to demonstrate the use of rand()

#include <iostream>
#include <cstdlib>


int main() {
    // This program will create same sequence of 
    // random number on every program run

    for (int i = 0; i < 5; i++) {
        std::cout << std::rand() << std::endl;
    }
    
    return 0;
}
```
Output:
```shell
$ g++ -std=c++20 test.cpp -o test
$ ./test    # run at the first time
16807
282475249
1622650073
984943658
1144108930
$ ./test    # run at the second time
16807
282475249
1622650073
984943658
1144108930
```


### 2.1.3. Demo 2: Generate random number `between 0 and 1`
```c++
#include <iostream>
#include <cstdlib>


int main() {
    // This program will create same sequence of 
    // random number on every program run
    for (int i = 0; i < 5; i++) {
        std::cout << (float)std::rand() / RAND_MAX << std::endl;
    }

    return 0;
}
```
Output:
```shell
$ g++ -std=c++20 test.cpp -o test
$ ./test
7.82637e-06
0.131538
0.755605
0.45865
0.532767
```

### 2.1.4. Demo 3: Generate random number `between -9 and 9`

1. `-9 ~ 9` 之间有 `19` 种可能性

```c++
int randomNum = rand() % 18 + (-9);    // wrong
int randomNum = rand() % 19 + (-9);    // right
```



## 2.2. `srand()`
1. The `srand()` function sets the starting point for producing a series of pseudo-random integers. If `srand()` is not called, the `rand()` seed is set as if `srand(1)` were called at program start. Any other value for seed sets the generator to a different starting point. 

### 2.2.1. Syntax
```c++
void srand(unsigned seed);

/*
    1. Seeds the pseudo-random number generator used by rand() with the value seed.
*/
```

<font color="red" size="3">

Note
----
1. The pseudo-random number generator should only be seeded once, before any calls to rand(), and the start of the program. It should not be repeatedly seeded, or reseeded every time you wish to generate a new batch of pseudo-random numbers. 
2. `Standard practice` is to use the result of a call to `srand(time(0))` as the seed. However, time() returns a time_t value which vary everytime and hence the pseudo-random number vary for every program call. 

</font>


### 2.2.2. Demo 1: Calling `srand()` before `rand()`
```c++
#include <iostream>
#include <cstdlib>
#include <time.h>


int main()
{
    // This program will create different sequence of
    // random numbers on every program run
 
    // Use current time as seed for random generator
    srand(time(0));
 
    for(int i = 0; i < 4; i++)
        cout << rand() << " ";
 
    return 0;
}
```
Output:
```shell
$ g++ -std=c++20 test.cpp -o test
$ ./test
1214843087
1740731180
1299219179
363018757
```
















# 完整代码
```c++
#include <iostream>
#include <cmath>
#include <stdlib.h>
#define NDIM 2

// The following definitions can be used for vector addition and subtraction (in two dimensions)
// `extra parentheses` are a safety measure to cover the possible ways these definitions might be employed in practice
#define VAdd(v1, v2, v3)        \
    (v1).x = (v2).x + (v3).x,   \
    (v1).y = (v2).y + (v3).y
#define VSub(v1, v2, v3)        \
    (v1).x = (v2).x - (v3).x    \
    (v1).y = (v2).y - (v3).y

// Other vector operations
#define VDot(v1, v2)        \
    ( (v1).x * (v2).x + (v1).y + (v2).y )
#define VSAdd(v1, v2, s3, v3)           \
    (v1).x = (v2).x + (s3) * (v3).x,    \
    (v1).y = (v2).y + (s3) * (v3).y
#define VSet(v, sx, sy)     \
    (v).x = sx,             \
    (v).y = sy
#define VSetAll(v, s)   \
    VSet(v, s, s)
#define VZero(v)    \
    VSetAll(v, 0)
#define VVSAdd(v1, s2, v2)  \
    VSAdd(v1, v1, s2, v2)
#define VLenSq(v)   \
    VDot(v, v)
#define VMul(v1, v2, v3)        \
    (v1).x = (v2).x * (v3).x    \
    (v1).y = (v2).y * (v3).y
#define VDiv(v1, v2, v3)        \
    (v1).x = (v2).x / (v3).x    \
    (v1).y = (v2).y / (v3).y

// Handling the periodic wraparound can be defined as
#define VWrap(v, t)     \
    if ( v.t >= 0.5 * region.t )    \
        v.t -= -0.5 * region.t      \
    else if ( v.t <= -0.5 * region.t )  \
        v.t += 0.5 * region.t
#define VWrapAll(v)     \
    {VWrap(v, x);       \
     VWrap(v, y);}
#define VScale(v, s)        \
    (v).x *= s,             \
    (v).y *= s
#define VVAdd(v1, v2)       \
    VAdd(v1, v1, v2)

// 
#define Sqr(x)  ( pow(x, 2) )
#define Cube(x) ( pow(x, 3) )
#define DO_MOL  for (n = 0; n < nMol; n++)
#define Max(x1, x2)         \
    ( ( (x1) > (x2) ) ? (x1) : (x2) )

// Macros for measurements
#define PropZero(v)         \
    v.sum = 0.,             \
    v.sum2 = 0.

#define PropAccum(v)        \
    v.sum += v.val,         \
    v.sum2 += Sqr(v.val)    \

#define PropAvg(v)          \
    v.sum /= n,             \
    // 虽然此处评估的平方根函数的参数永远不应为负，但包含 Max 测试以防止在结果接近于零的情况下出现计算机舍入误差。
    v.sum2 /= sqrt( Max(v.sum2/n - Sqr(v.sum), 0.) )    \
#define PropEst(v)      \
    v.sum, v.sum2



typedef double real;

typedef struct {    // Atom coordinates, Velocities, Accelerations
    real x, y;
} VecR;

typedef struct {    // 引入另一种数据结构 `Mol` 来简化与 atom && molecule 相关的变量
    VecR r, rv, ra;
} Mol;

typedef struct { 
    /*
        1. x: x方向上的 primitive_cell（本例子中是一个 atom） 数目
        2. y: y方向上的 primitive_cell（本例子中是一个 atom） 数目
    */
    int x, y;
} VecI;

typedef struct {    // C structure is introduced for representing `property measurements`
    /*
    1. val:
        实际测量值
    2. sum:
        为评估平均值，而在几次测量中累积的总和
    3. sum2:
        用于评估标准差的平方和
    */
    real val, sum, sum2;
} Prop;

// Global Variables：使用全局变量可以避免一大堆参数传来传去
Mol *mol;   // mol 是一个 Mol 指针，指向一个一维向量，长度是 `nMol` 
VecR region, vSum;  // region contains the edge length of the simulation region
VecI initUcell;
Prop kinEnergy, pressure, totEnergy;
real deltaT, density, rCut, temperature, timeNow, uSum, velMag, virSum, vvSum;
int moreCycles, nMol, stepAvg, stepCount, stepEquil, stepLimit;

#define AllocMem(a, n, t)       \
    a = (t*)malloc( (n) * sizeof(t) )

#define VSCopy(v2, s1, v1)      \
    (v2).x = (s1) * (v1).x      \
    (v2).y = (s1) * (v2).y

#define VProd(v)            \
    ( (v).x * (v).y )


void AllocArrays() {
    AllocMem(mol, nMol, Mol);
}


void SetParams() {
    rCut = pow(2., 1./6.);  // 截断半径
    VSCopy(region, 1. / sqrt(density), initUcell);
    nMol = VProd(initUcell);
    // 速度的幅度 (velMag) 取决于温度的高低
    velMag = sqrt( NDIM * (1. - 1. / nMol) * temperature );
}



/* 
Description
-----------
    1. Each loop cycle advances the system by a single timestep.
    2. Do things as below:
        s1. deal with the force evaluation
        s2. integration of the equation of motion
        s3. adjustments required by periodic boundary
        s4. property measurements
*/
void SingleStep() {
    ++stepCount;
    timeNow = stepCount * deltaT;
    LeapfrogStep(1);
    ApplyBoundaryCond();
    ComputeForces();
    LeapfrogStep(2);
    EvalProps();
    AccumProps(1);
    if (stepCount % stepAvg == 0) {
        AccumProps(2);
        PrintSummary(stdout);
        AccumProps(0);
    }
}


/*
Decription
----------
    1. All the work needed for initializing the computation 
        is concentrated in the following function.
*/
void SetupJob() {
    AllocArrays();
    stepCount = 0;
    InitCoords();
    InitVels();
    InitAccels();
    AccumProps();
}



// Part II. Computational Functions
void ComputeForces() {
    /*
    Varibales
    ---------
        1. dr: VecR
            atom_i, atom_j 之间的距离
        2. fcVal:
        3. rr:
            dr.x^2 + dr.y^2 -- atom_i, atom_j 之间距离的平方
        4. rrCut:
            截断半径的平方
        5. rri: 
            1 / (rr^2)
        6. rri3:
            1 / (rr^6)
        7. j1:
            原子序号，用于循环
        8. j2:
            原子序号，用于循环
        9. n:
            原子序号，用于循环
    */
    VecR dr;
    real fcVal, rr, rrCut, rri, rri3;
    int j1, j2, n;

    rrCut = Sqr(rCut);
    DO_MOL VZero(mol[n].ra);
    uSum = 0.;
    virSum = 0.;

    for (j1 = 0; j1 < nMol - 1; j1++) {
        for (j2 = j1 + 1; j2 < nMol; j2++) {
            VSub(dr, mol[j1].r, mol[j2].r);
            // Boundary conditions: perform wraparound operation
            VWrapAll(dr);
            rr = VLenSq(dr);

            if ( rr < rrCut ) {
                rri = 1. / rr;
                rri3 = Cube(rri);
                fcVal = 48. * rri3 * (rri3 - 0.5) * rri;
                VVSAdd(mol[j1].ra, fcVal, dr);
                VVSAdd(mol[j2].ra, -fcVal, dr);
                uSum += 4. * rri3 * (rri3 - 1.) + 1.;   // 没看懂啥意思
                virSum += fcVal * rr;
            }
            
        }
    }
}


void LeapfrogStep(int part) {
    // 蛙跳算法：计算`位移`和`速度`
    int n;
    if (part == 1) {
        DO_MOL {
            VVSAdd(mol[n].rv, 0.5 * deltaT, mol[n].ra); // v(t+h/2) = v(t) + h/2 * a(t)
            VVSAdd(mol[n].r, deltaT, mol[n].rv);        // r(t+h) = r(t) + h * v(t+h/2)
        }
    }
    else {
        /*
        1. Now use the new coordinates to compute the latest acceleration values
        update the velocities over the second half timestep,
        */
        DO_MOL VVSAdd(mol[n].rv, 0.5 * deltaT, mol[n].ra);  // v(t+h) = v(t+h/2) + h/2 * a(t+h/2)
    }
}


void ApplyBoundaryCond() {
    /*
    The function ApplyBoundaryCond, called after `the first call to LeapfrogStep`, is
    responsible for taking care of any periodic wraparound in the updated coordinates.
    */
    int n;
    DO_MOL VWrapAll(mol[n].r);
}



// Part III. Initial state
/*
Description
-----------
    1. Preparation of the initial state uses the following three functions:
        - one for `atomic coordinates`
        - one for `velocities`
        - one for `accelerations`
    2. 
*/
void InitCoords() {
    /*
    Description
    -----------
        初始化坐标。
        这里使用了一个简单的正方形晶格（可以选择不等长的边）,
        因此，每个元胞只包含一个原子，系统以原点为中心，


    Variables
    ---------
        1. c: 
            一个temp值，被用作存储 `任一atom` 的坐标
        2. gap:
            atom 所做 primitive_cell 的大小
        3. n:
            给 atom 计数
        4. nx:
        5. ny:
            - 
        6. region:
            - region.x: 长方形晶格在 x 方向的长度
            - region.y: 长方形晶格在 y 方向的长度
        7. initUcell:
            - initUcell: x 方向上有多少 primitive_cell（本例子中，primitive_cell中只有一个atom）
            - initUcell: y 方向上有多少 primitive_cell
    */
    VecR c, gap;
    int n, nx, ny;

    VDiv(gap, region, initUcell);
    n = 0;
    for (ny = 0; ny < initUcell.y; ny++) {
        for (nx = 0; nx < initUcell.x; nx++) {
            VSet(c, nx + 0.5, ny + 0.5);
            VMul(c, c, gap);
            VVSAdd(c, -0.5, region);    // 系统的区域范围是 (-L/2 ~ L/2)
            mol[n].r = c;
            ++n;
        }
    }
}


void InitVels() {
    /*
    初始化速度
    初始速度被设置为固定幅度 (velMag)
    速度的幅度取决于温度。在分配了随机速度方向后
    调整速度的方向，以确保质心是静止的，因为系统再不受净外力的作用下，其质心速度应该保持不变
    函数 `vRand()` 作为均匀分布的径向单位向量的来源
    */
    int n;
    VZero(vSum);
    DO_MOL {
        VRand(&mol[n].rv);
        VScale(mol[n].rv, velMag);
        VVAdd(vSum, mol[n].rv);
    }
    DO_MOL VVSAdd(mol[n].rv, - 1. / nMol, vSum);
}


void InitAccels() {
    /*
    加速度初始化为 [0, 0]
    */
    int n;
    DO_MOL
        VZero(mol[n].ra);
}



// Part IV. Meassurements
void EvalProps() {
    /*
    Variables
    ---------
        1. vSum:
            accumulate the total volecity (or momentum, since all atoms have unit mass)
            of the system

    Description
    -----------
    计算体系的热力学性质：
        - the velocity
        - velocity-squared sums
        - the instantaneous energy
        - pressure values.
    */
    real vv;
    int n;

    VZero(vSum);
    vvSum = 0.;
    DO_MOL {
        VVAdd(vSum, mol[n].rv);
        vv = VLenSq(mol[n].rv);
        vvSum += vv;
    }
    kinEnergy.val = 0.5 * vvSum / nMol;     // 单个原子的动能
    totEnergy.val = kinEnergy.val + uSum / nMol;    // 单个原子的总能 = 单个原子的动能 + 单个原子的势能
    pressure.val = density * (vvSum + virSum) / (nMol * NDIM);  // 体系压强
}


void AccumProps(int icode) {
    /*
        收集测定量的结果，并根据要求计算平均值和标准偏差。
    */
    if (icode == 0) {   // 0: 初始化
        PropZero(totEnergy);
        PropZero(kinEnergy);
        PropZero(pressure);
    } else if (icode == 1) {    // 1: 求和
        PropAccum(totEnergy);
        PropAccum(kinEnergy);
        PropAccum(pressure);
    } else if (icode == 2) {    // 2: 求平均值和标准差
        PropAvg(totEnergy, stepAvg);
        PropAvg(kinEnergy, stepAvg);
        PropAvg(pressure, stepAvg);
    }
}


// Part V. Input and output
// 略





// Driver code
int main(int argc, char **argv) {
    // Initialization
    GetNameList(argc, argv);
    PrintNameList(stdout);
    SetParams();
    SetupJob();

    moreCycles = 1;
    // Do Loop: the process of MD
    while (moreCycles) {
        SingleStep();
        if (stepCount >= stepLimit)
            moreCycles = 0;
    }
}
```