#include <iostream>

#include <vector>

using namespace std;

//exemplo de vector

int main(){

    vector<int> v; 
    cout << "size: " << v.size() << endl;
    v.push_back(10); // adiciona um elemento no primeiro indice livre
    v.push_back(20);
    v.push_back(30);

    //acessar os valores
    for (int i = 0; i < v.size(); i++){
        cout << i << ": " << v[i] << endl;
    }

    v.pop_back() //remove o ultimo elemento

    return 0;
}