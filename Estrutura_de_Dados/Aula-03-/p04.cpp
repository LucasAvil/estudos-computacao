//primeiro exemplo usando TDD
//test driven development
//assert - verifica se a condição satisfaz o resultado esperado
#include <iostream>
#include <cassert>
#include "funcoes.cpp"

using namespace std;

int main(){
    assert(imc(150, 1.90) == 41.55);

    cout << "Passou" << endl;

    return 0;
}