#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct aluno {
    string nome;
    string regiao;
    int custo;

};

bool ordena(const aluno &a, const aluno &b){

        return (a.custo < b.custo) || (a.custo == b.custo && a.regiao < b.regiao) ||
        (a.custo == b.custo && a.regiao == b.regiao && a.nome < b.nome);

    return false;
};

int main(){
    int N;
    while(cin >> N){;
        vector<aluno> v;
        for (int i = 0; i< N; i++){
            aluno a;
            cin >> a.nome >> a.regiao >> a.custo;
            v.push_back(a);
        }
        sort(v.begin(), v.end(), ordena);
        for (int i = 0; i < N; i++){
            cout << v[i].nome << endl;
        }
}
    return 0;
}