#include <iostream>

using namespace std;

int main(){
    int a = 10;
    int *p = &a;
    int **pp; // ponteiro que aponta pra outro ponteiro, armazena o endereço de outro ponteiro
    
    pp = &p; // endereço de memoria do p atribuido ao ponteiro de ponteiros (pp)
    cout << pp << " " << *pp << " " << **pp << endl;
    cout << p <<  " " << *p << endl;

    return 0;
}