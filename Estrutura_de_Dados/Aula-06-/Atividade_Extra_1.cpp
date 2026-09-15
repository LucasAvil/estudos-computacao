#include <iostream>
#include <algorithm>

using namespace std;

struct carro{
    string nome;
    float valor;
    int ano;
};


bool ordena(const carro &a, const carro &b){

    return (a.valor > b.valor) || (a.valor == b.valor && a.ano > b.ano) || (a.valor == b.valor && a.ano == b.ano && a.nome < b.nome);
};


int main(){
    int N;
    cin >> N;
    carro garagem[N];
    for (int i =0; i < 5; i++){
        //getline(cin,garagem[i].nome); seria assim se usasse o getline, mas teria que ser um blocao só e cada linha seria um cin
        cin >> garagem[i].nome >> garagem[i].valor >> garagem[i].ano;
    };
    sort(garagem, garagem+N, ordena);
    for (int i = 0; i < N; i++){
        cout << garagem[i].nome << " " << garagem[i].valor << " " << garagem[i].ano << endl;

    };

    return 0;
}