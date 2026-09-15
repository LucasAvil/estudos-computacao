#include <iostream>
#include <algorithm>
using namespace std;

struct produto {
    string nome;
    float preco;
    int quant;

};
int opcao;

bool ordena(const produto &a, const produto &b){

    if (opcao == 1){
        return (a.nome < b.nome);
    } else if (opcao == 2){
        return (a.preco < b.preco);
    } else if (opcao == 3){
        return (a.quant > b.quant);
    }

    return false;
};

int main(){
    int N;
    cin >> N;
    produto loja[N];
    for (int i =0; i < N; i++){
        cin >> loja[i].nome >> loja[i].preco >> loja[i].quant;
    }
    cin >> opcao;

    sort(loja, loja+N, ordena);
    for (int i = 0; i < N; i++){
        cout << endl << loja[i].nome << " - Preço: " << loja[i].preco << " - Quantidade: " << loja[i].quant << endl;
    };

    return 0;
}