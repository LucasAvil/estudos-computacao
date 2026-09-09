#include <iostream>

using namespace std;
//exemplo de structure 2

struct aluno{
int matricula;
string nome;
float nota;
};

int main(){
    aluno one, two;
    
    //one.matricula = 199734;
    //one.nome = "lukas";
    //one.nota = 10.0;
    one = {199734, "lukas", 10.0};

    cout << "matricula: " << one.matricula << endl;
    cout << "nome: " << one.nome << endl;
    cout << "nota: " << one.nota << endl;
    return 0;
}