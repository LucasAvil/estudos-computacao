#include <iostream>
using namespace std;

void foo(){
    static int n=0; //alocacao estatica, o n vai ta sempre guardado no mesmo endereço
    n++;
    cout << &n << " " << n << endl;

}
int main(){
    foo();
    foo();
    foo();


    return 0;
}