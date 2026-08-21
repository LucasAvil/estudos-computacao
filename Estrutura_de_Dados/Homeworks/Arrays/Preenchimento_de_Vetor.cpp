#include <iostream>
using namespace std;

int main () {
    int valor;
    cin >> valor;
    int N[10]{valor};

    for (int i = 0; i < 10; i++){
        N[i] = valor;
        cout << "N[" << i << "] = " << N[i] << endl;
        valor *= 2;
    }
    return 0;
}