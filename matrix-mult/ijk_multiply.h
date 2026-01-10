
#ifndef __MATMUL_IJK_MULTIPLY_H__
#define __MATMUL_IJK_MULTIPLY_H__
#include <iostream>

void multiply(double** A, double** B, double** C, int size)
{
    std::cout << "IJK Multiplication" << std::endl;
    std::cout << "Size = " << size << std::endl;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            for (int k = 0; k < size; k++) {
                // std::cout << "C = " << C[i][j] << std::endl;
                // std::cout << "A = " << A[i][j] << std::endl;
                // std::cout << "B = " << B[k][j] << std::endl;
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

#endif // __MATMUL_IJK_MULTIPLY_H__
