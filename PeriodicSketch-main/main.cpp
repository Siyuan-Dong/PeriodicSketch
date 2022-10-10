#include <iostream>
#include "benchmark.h"

int main(int argc, char *argv[]) {
    srand(1205);
    for(uint32_t i = 3;i < argc;++i){
        std::cout << argv[i] << std::endl;
        BenchMark dataset(argv[i]);
        double alpha = atof(argv[1]);
        dataset.TopKError(alpha,argv[2]);
        // dataset.TopKError(0.000005,argv[1]);
    }
    return 0;
}
