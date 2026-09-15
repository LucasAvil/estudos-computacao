#include <iostream>

using namespace std;
//quando é vetor o void vai sempre alterar o valor na mesma memoria que o valor inserido, logo, existe apenas um vetor, ao inves do original e copia
void dobrar(int v[], int tamanho){
    for (int i =0; i < tamanho; i++)
    v[i] = v[i] * 2;


}

int main(){
    int vet[3]{1,2,3};
    dobrar(vet,3);
    for (int i = 0; i < 3; i++){
        cout << vet[i] << " ";
    }

    return 0;
}