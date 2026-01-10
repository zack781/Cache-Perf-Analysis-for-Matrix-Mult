
#ifndef __MATMUL_BLOCK_IK_MULTIPLY_H__
#define __MATMUL_BLOCK_IK_MULTIPLY_H__


#include <iostream>

void multiply(double** A, double** B, double** C, int matrix_size, int block_size)
{
    std::cout << "Blocked IK Multiplication" << std::endl;
    std::cout << "Matrix size is " << matrix_size << std::endl;
    std::cout << "Block size is " << block_size << std::endl;
    int i, j, k, kk, jj;
    double sum;
    int en = block_size * (matrix_size / block_size);

    for (i = 0; i < matrix_size; i++) {
        for (j = 0; j < matrix_size; j++) {
            C[i][j] = 0.0;
        }
    }

    for (kk = 0; kk < en; kk += block_size) {
        for (jj = 0; jj < en; jj += block_size) {
            for (i = 0; i < matrix_size; i++) {
                for (k = kk; k < kk + block_size; k++) {
                    // sum = C[i][k];
                    double r = A[i][k];
                    for (j = jj; j < jj + block_size; j++) {
                        C[i][j] += r * B[k][j];
                    }
                    // C[i][j] = sum;
                }
            }
        }
    }

    // std::cout << "result for blocked ik mult: " << std::endl;
    // for (i = 0; i < matrix_size; i++) {
    //     for (j = 0; j < matrix_size; j++) {
    //         std::cout << C[i][j] << " ";
    //     }
    //     std::cout << std::endl;
    // }
    // std::cout << std::endl;
    // std::cout << std::endl;

}

#endif // __MATMUL_BLOCK_IK_MULTIPLY_H__
