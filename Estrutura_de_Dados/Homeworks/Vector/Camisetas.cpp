#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct aluno {
    string nome;
    string cor;
    string tamanho;

};

bool ordena(const aluno &a, const aluno &b){
    return (a.cor < b.cor) || (a.cor == b.cor && a.tamanho > b.tamanho) ||
    (a.cor == b.cor && a.tamanho == b.tamanho && a.nome < b.nome);
};

int main(){
    int N;
    bool primeirocaso = true;
    while(cin >> N && N > 0){
        vector<aluno> v;
        if (!primeirocaso){
            cout << "\n";
        }
        for (int i = 0; i < N; i++){
            aluno a;
            getline(cin >> ws, a.nome);
            cin >> a.cor >> a.tamanho;
            v.push_back(a);


        }
        sort(v.begin(), v.end(), ordena);
        for (int i = 0; i < N; i++){
            cout << v[i].cor << " " << v[i].tamanho << " " << v[i].nome << endl;;
        }
        primeirocaso = false;
    }


    return 0;
}