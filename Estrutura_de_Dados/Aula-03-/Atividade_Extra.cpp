#include <iostream>
#include <cassert>
#include "funcoes.cpp"
using namespace std;

int main() {
    int numero = 89;

    if (primo(numero)) {
        cout << numero << " é primo" << endl;
    } else {
        cout << numero << " não é primo" << endl;
    }

    return 0;
}