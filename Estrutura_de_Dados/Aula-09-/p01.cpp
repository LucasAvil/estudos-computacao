#include <iostream>

using namespace std;

int main (){

    float n = 1.5;
    float *p = &n;

    cout << n << " " << *p << endl; // acessando o mesmo valor, um pela variavel e outro pelo ponteiro

    *p = 9.1; // pegou o valor q tava armazenado no endereço que o ponteiro ta apontando e alterou pra ser 9.1, logo ao inves de n ser 1.5, vai ser 9.1

    cout << n << " " << *p << endl; 
    return 0;
}