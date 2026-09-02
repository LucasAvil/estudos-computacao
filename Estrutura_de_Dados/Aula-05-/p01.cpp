#include <iostream>
#include <algorithm>
using namespace std;

bool ordena(float a, float b){
    
    
    return a > b;
}

int main (){
    const int N = 5;
    float vet[N] {
        9.5, 9.7, 1.6, 3.0, 6.7
    };
    sort(vet,vet+N,ordena);
        for(int i=0; i<N; i++){
        cout << vet[i] << "  ";
    }

    return 0;
}