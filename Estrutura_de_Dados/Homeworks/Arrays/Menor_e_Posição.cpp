#include <iostream>

using namespace std;

int main(){

    int N, verificador, vetor;
    cin >> N;
    int X[N];
    for (int i = 0; i < N; i++){
        cin >> X[i];
        if (i == 0){
            verificador = X[i];
            vetor = i;
        } 

        if (X[i] < verificador){
            verificador = X[i];
            vetor = i;
        }

    }
    cout << "Menor valor: " << verificador << endl;
    cout << "Posicao: " << vetor << endl;


    return 0;
}