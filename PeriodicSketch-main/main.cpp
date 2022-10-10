#include <iostream>
#include "benchmark.h"

int main(int argc, char *argv[]) {
    for(uint32_t i = 2;i < argc;++i){
        std::cout << argv[i] << std::endl;
        BenchMark dataset(argv[i]);
        dataset.TopKError(0.0001,argv[1]);
    }
    return 0;
}
