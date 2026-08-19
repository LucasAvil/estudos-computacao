#include <iostream>

using namespace std;

int fatorial(int num){
    int aux = 1;
    for(int i=2; i <= num; i++){
        aux = aux * i;
    }


    return aux;
}