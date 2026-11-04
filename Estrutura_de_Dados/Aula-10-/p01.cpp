#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<double> v;
    cout << "digit 0 p sair" << endl;
    double x;

    
    cout << "tamanho: " << v.size() << "capacidade: " << v.capacity() << endl;

    while(cin >> x && x!=0){
        v.push_back(x);
        cout << "tamanho: " << v.size() << "capacidade: " << v.capacity() << endl;


    }
    //tamanho e capacidade sao coisas diferentes (tamanho é quantidade de elementos),
    //a capacidade dobra toda vez que falta memoria pra alocar mais um valor no vetor
    return 0;
}