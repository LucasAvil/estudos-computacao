#include <iostream>

using namespace std;

int main(){

    int a=5, b=10, c=20;
    int *p;

    p = &a;
    cout << p << " " << *p << endl; //endereço de memoria e o valor que ta no endereço

    p = &b;
    cout << p << " " << *p << endl;

    p = &c;
    cout << p << " " << *p << endl;


    return 0;
}