#include <iostream>
using namespace std;

int main(){

    // declaramos um ponteiro e apontamos para um espaco de memoria que armazenara um int
    //nesse caso, a unica forma de acessar esse endereco é via ponteiro, pois nao temos um nome de variavel
    //a aquele endereco de memoria
    int *p = new int;
    *p = 0;

    cout << p << " " << *p << endl;
    delete p; //desaloca o espaço de memoria qndo n for mais usado (boa pratica)

    int a = 5;
    int*p1 = &a;

    int *p2 = new int;
    *p2 = 35;
    p2 = p1;


    return 0;
}