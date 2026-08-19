#include <iostream>
using namespace std;

void adiciona(float a, float b){
    a = a + b;
    cout << "na funcao adiciona temos: " <<  a << endl;
}

int main (){
    float x = 10, y=0.5;
    adiciona(x,y);

    cout << "na main temos: " << x << endl;
    return 0;
}