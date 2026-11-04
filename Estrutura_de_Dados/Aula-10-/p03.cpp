#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<string> v;
    v.push_back("A");
    v.push_back("B");
    v.push_back("C");
    v.push_back("D");
    v.push_back("E");
    v.push_back("F");
    v.push_back("G");
    v.push_back("H");
    /*
    percorrer o vetor (oldschool)

    for(int i = 0; i<v.size(); i++){
        cout << v[i] << endl;
    }
    percorrer o vetor de forma inversa 
    
    for(int j = v.size() - 1; j >= 0; j--){
        cout << v[j] << endl;
    }
        
    //iterando usando o 'range for'
    for(auto n:v){
        cout << n << endl;
    }
        
       //percorre utilizando o iterator
    for(auto it = v.begin(); it != v.end(); it++){
        cout << *it << endl;
        //ai toda vez q ele incrementa ele pega o endereço de memoria do vetor, dando cout no *it ele pega o valor q ta referenciando

    } //v.begin é o começo do vetor, v.end é o final (logico), it (ponteiro) é iterator (pique i++)
*/
    //reverse iterator (o ultimo passa a ser o primeiro e o primeiro passa a ser o ultimo) continua sendo it++
    for(auto it = v.rbegin(); it != v.rend(); it++){
        cout << *it << endl;
    }
    return 0;
}