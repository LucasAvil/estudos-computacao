#include <iostream>

using namespace std;

struct aluno{
    int matricula;
    string nome;
};

int main(){
    aluno a = {199734, "Lugas Avila"};
    aluno *p = &a;

    cout << a.matricula << endl; //acesso direto normal
    cout << p->matricula << endl; //a setinha substitui o asterisco antes do p, o compilador ja entende que a gente ta referenciando o valor da matricula da struct
    p->nome = "professor baguga";
    cout << p->nome << endl;

    return 0;
}