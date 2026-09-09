#include <iostream>

using namespace std;
//exemplo de structure 

struct aluno{
int matricula;
string nome;
float nota;


};

int main(){
    aluno one, two;
    one.matricula = 199734;
    one.nome = "lukas";
    one.nota = 10.0;

    cout << "matricula: " << one.matricula << endl;
    return 0;
}