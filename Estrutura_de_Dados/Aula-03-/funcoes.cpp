#include <iostream>
#include <cmath>
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

int cf(int C){
    
    double res = (C + 32) * 1.8;
    return res;
}

int fc(int F){
    double res = (F - 32) / 1.8;
    return res;
}

double imc(double peso, double altura){
    double res = peso / (pow(altura, 2));
    return res;

}