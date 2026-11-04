#include <iostream>

#include <vector>

using namespace std;

//exemplo de vector

int main(){

    vector<int> v; 
    cout << "size: " << v.size() << endl;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);

    //acessar os valores
    for (int i = 0; i < v.size(); i++){
        cout << i << ": " << v[i] << endl;
    }

    return 0;
}