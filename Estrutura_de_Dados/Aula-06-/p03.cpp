#include <iostream>
#include <algorithm>
//ordenacao de structs
using namespace std;

struct aluno{
int matricula;
string nome;
float nota;
};

bool ordena(const aluno &a, const aluno &b){

    return a.nome < b.nome; //ordem alfabetica de nome (prioriza os menores)
};

const int NA = 5;
int main(){
aluno turma[NA] = {
    {199734, "lukas", 10.0},
    {199999, "piter", 9.9},
    {6767, "balsebos", 6.2},
    {98881, "arsmodels", 7.7},
    {919832, "enzo", 6.2}
};

sort(turma,turma+NA,ordena);
for(int i=0; i<NA; i++){
    cout << "matricula: " << turma[i].matricula << endl;
    cout << "nome: " << turma[i].nome << endl;
    cout << "nota: " << turma[i].nota << endl;
}


    return 0;
}