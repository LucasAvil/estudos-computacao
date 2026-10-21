#include <iostream>

using namespace std;

int main (){
    int a = 10;

    int *p; //o "*" representa que o p é um ponteiro
            //o ponteiro guarda um endereço de memoria em hexadecimal
            //se é do tipo int ele é um ponteiro para um int, que indica para um valor inteiro
    p = &a; // p recebe o endereço de memoria do a
    cout << p << endl; //endereço de memoria que o ponteiro ta apontando
    cout << *p << endl; // valor que o endereço de memoria armazenado no ponteiro ta guardando, nesse caso, &a armazena 'a'

    a = 20;
    cout << p << endl;
    cout << *p << endl;

    int b = *p/4;
    cout << b << endl;

    return 0;
}