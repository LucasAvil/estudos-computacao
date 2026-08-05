#include <iostream>
using namespace std;

//exemplo de array unidimensional
int main(){
    int vet[6];
    cout << "informe 6 valores : " << endl;
    for (int i=0; i < 6; i++){
        cin >> vet[i];

    }
    cout << "valores invertidos:" << endl;
        for (int i=5; i >=0; i--){
        cout << vet[i] <<  ", ";

    }
    cout << "Exibindo os valores e o indice" << endl;
        for (int i=0; i < 6; i++){
        cout << "vet[" << i << "] = " << vet[i] << endl;
    }

    return 0;
}