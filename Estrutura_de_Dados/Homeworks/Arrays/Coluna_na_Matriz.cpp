#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int C;
    char T;
    float M[12][12];
    double soma = 0;
    cin >> C >> T;

    for (int i = 0; i < 12; i++){
        for (int j = 0; j < 12; j++){
            cin >> M[i][j];
        }
    }
    for (int i = 0; i < 12; i++){
        soma += M[i][C];
    }
    if (T == 'S'){
        cout << soma << endl;

    } else if (T == 'M'){
        cout << soma / 12 << endl;
    }


    return 0;
}