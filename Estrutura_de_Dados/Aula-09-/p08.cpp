#include <iostream>
using namespace std;
//STACK OVERFLOW
void foo(int n){
    //loop infinito que rompe o tamanho limite da pilha
    double d;
    cout << n << " " << &d << endl;
    foo(n+1);
}
int main(){
    foo(1);
    return 0;
}