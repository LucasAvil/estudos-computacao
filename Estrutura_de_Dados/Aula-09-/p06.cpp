#include <iostream>
using namespace std;

void foo(){
    int n=0; //alocacao automatica
    n++;
    cout << &n << " " << n << endl;

}
int main(){
    foo();
    foo();
    foo();


    return 0;
}