#include <iostream>
#include <algorithm>

using namespace std;

struct quadro {
    string nome;
    int ouro;
    int prata;
    int bronze;
};

bool ordena(const quadro &a, const quadro &b){
    return (a.ouro > b.ouro) || (a.ouro == b.ouro && a.prata > b.prata) || (a.ouro == b.ouro && a.prata == b.prata && a.bronze > b.bronze) || 
    (a.ouro == b.ouro && a.prata == b.prata && a.bronze == b.bronze && a.nome < b.nome);
}

int main(){
    int N;
    cin >> N;
    quadro medalhas[N];
    for (int i = 0; i < N; i++){
        cin >> medalhas[i].nome >> medalhas[i].ouro >> medalhas[i].prata >> medalhas[i].bronze;

    }
    sort(medalhas, medalhas+N, ordena);
    for (int i = 0; i < N; i++){
        cout << medalhas[i].nome << " " << medalhas[i].ouro << " " << medalhas[i].prata << " " << medalhas[i].bronze << endl;
    }

    return 0;
}