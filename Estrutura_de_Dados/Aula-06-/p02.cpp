#include <iostream>

using namespace std;

//arrays com struct

struct aluno{
int matricula;
string nome;
float nota;
};

const int NA = 5;

int main(){
aluno turma[NA] = {
    {199734, "lukas", 10.0},
    {199999, "piter", 9.9},
    {6767, "balsebos", 6.2},
    {98881, "arsmodels", 7.7},
    {919832, "enzo", 6.0}
};

for(int i=0; i<NA; i++){
    cout << "matricula: " << turma[i].matricula << endl;
    cout << "nome: " << turma[i].nome << endl;
    cout << "nota: " << turma[i].nota << endl;
}

    return 0;
}