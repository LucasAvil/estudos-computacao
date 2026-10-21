#include <iostream>

using namespace std;

int main(){
    int v[3]={10,20,30};

    cout << v << endl; //o nome do vetor sozinho chama o endereço do primeiro valor

    int *p;
    p = v;
    cout << p << " " << *p << endl; // o p chama o endereço do preimrio indice do vetor e o *p chama o valor que o endereço ta guardando (10)
    p++;
    cout << p << " " << *p << endl; 
    p++;
    cout << p << " " << *p << endl; 
    //incrementou, pegou um indice apos o outro, seu endereço e o valor guardado
    //logo, na memoria, os vetores guardam os seus indices de forma seguida
    
    return 0;
}