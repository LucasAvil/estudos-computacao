#include <iostream>

using namespace std;

int main(){
    int a = 10;
    int *p = &a;
    int **pp; // ponteiro que aponta pra outro ponteiro, armazena o endereço de outro ponteiro
    
    pp = &p; // endereço de memoria do p atribuido ao ponteiro de ponteiros (pp)
    cout << pp << " " << *pp << " " << **pp << endl; // pp = endereço de memoria de p (ponteiro referenciado)
    // *pp = valor armazenado no p (&a)
    // **pp = busca o valor que o ponteiro referenciado guarda, nesse caso, referencia a memoria de a, a memoria de a guarda a, que é 10
    cout << p <<  " " << *p << endl;
    return 0;
}