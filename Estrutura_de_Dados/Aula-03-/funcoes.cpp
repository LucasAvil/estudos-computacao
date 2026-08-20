#include <iostream>

using namespace std;

bool primo(int a) {
    if (a <= 1) return false;

    for (int i = 2; i * i <= a; i++) {
        if (a % i == 0) {
            return false;
        }
    }
    
    return true;
}

int fatorial(int num){
    int aux = 1;
    for(int i=2; i <= num; i++){
        aux = aux * i;
    }


    return aux;
}