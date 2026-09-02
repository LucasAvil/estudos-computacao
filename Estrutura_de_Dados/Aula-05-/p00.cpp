#include <iostream>
#include <algorithm> //serve pra usar o sort

using namespace std;

int main(){
    int numeros[10]={42,15,17,95,06,10,21,16,10,98};

    cout << "vetor original:";
    for(int i=0; i<10; i++){
        cout << numeros [i] << "  ";

    }
    cout << endl << endl;

    //ordenar com a funcao sort
    sort(numeros,numeros+10);
    cout << "vetor ordenado";
    for(int i=0; i<10; i++){
        cout << numeros[i] << "  ";
    }
    return 0;
}