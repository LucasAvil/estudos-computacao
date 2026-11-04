#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cout << "degit o tamanho do vetor: " << endl;
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cout << "degit o valor do indice " << i << ": " << endl;
        cin >> v[i];
    }
    
    
    return 0;
}