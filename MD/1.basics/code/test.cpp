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
        std::cout << rand() << std::endl;
 
    return 0;
}