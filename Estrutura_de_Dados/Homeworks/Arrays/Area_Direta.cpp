#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double M[12][12];
    double soma = 0;
    char O;
    int elementos = 0;

    cin >> O;

    for (int i = 0; i < 12; i++){
        for (int j = 0; j < 12; j++){
            cin >> M[i][j];
        }
    }
    for (int i = 0; i < 12; i++){
        for (int j = 0; j < 12; j++){
            if (j > i && j > 11 - i){
                soma += M[i][j];
                elementos++;
            }
        }
    }

    if (O == 'S'){
        cout << fixed << setprecision(1) << soma << endl;

    } else if (O == 'M'){
        cout << fixed << setprecision(1) << soma / elementos << endl;
    }


    return 0;
}