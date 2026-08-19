//primeiro exemplo usando TDD
//test driven development
//assert - verifica se a condição satisfaz o resultado esperado
#include <iostream>
#include <cassert>
#include "funcoes.cpp"

using namespace std;

int main(){
    assert(fatorial(1) == 1);
    assert(fatorial(5) == 121);

    cout << "Passou" << endl;

    return 0;
}