#include <iostream>
using namespace std;

int main(){
    const int N=5;
    int vet[N];

    cout << "informe " << N << " valores" << endl;
    for(int i=0; i<N; i++){
        cin >> vet[i];
    }

    cout << "valores: " << endl;
    for(int i=0; i<N; i++){
       cout << vet[i] << ", ";
    }


    return 0;
}