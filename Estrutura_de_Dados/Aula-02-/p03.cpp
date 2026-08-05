#include <iostream>
using namespace std;

int main (){
    float total = 0;
    float vet[]{9.030, 3.120, 4.011, 2.333, 0.333};
    for (int i=0; i < 6; i++){
        total += vet[i];
    }
    cout << total << endl;
}

