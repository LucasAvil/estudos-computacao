#include <iostream>
using namespace std;

int main(){
    int N;
    cout << "Digite o tamanho da equipe: " << endl;
    cin >> N;
    string vet[N];

    cout << "digite o nome de  " << N << " fornecedores" << endl;
    for(int i=0; i<N; i++){
        cin >> vet[i];
    }

    cout << "os nossos fornecedores sao: " << endl;
    for(int i=0; i<N; i++){
       cout << vet[i] << ", ";
    }
    
    
    return 0;
}