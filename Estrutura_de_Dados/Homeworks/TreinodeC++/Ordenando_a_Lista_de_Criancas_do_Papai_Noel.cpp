#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool ordena(const string &a, const string&b){

    return a < b;
}

int main(){
    int N, comport = 0, ncomport = 0;
    string nome;
    char sinal;
    cin >> N;
    string vetor[N];
    for (int i = 0; i<N; i++){
        cin >> sinal >> nome;
        if (sinal == '+'){
            comport++;
        } else{
            ncomport++;
        }

        vetor[i] = nome;
    }
    sort(vetor, vetor+N, ordena);
    for (int i = 0; i<N; i++){
        cout << vetor[i] << endl;
    }
    cout << "Se comportaram: " << comport << " | Nao se comportaram: " << ncomport << endl;


    return 0;
}