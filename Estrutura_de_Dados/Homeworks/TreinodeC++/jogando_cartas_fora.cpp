#include <iostream>
#include <stack>
using namespace std;
//FIZ TUDO ERRADO ERA UM PROBLEMA DE FILA NAO DE PILHA
//COMO ESTOU ESTUDANDO PILHA, VOU DEIXAR PARA COMPLETAR
//QUANDO EU COMEÇAR A ESTUDAR FILAS
//FIZ UMA GAMBIARRA TA CHEIO DE ERRO DE ACESSO VAZIO

int main(){
    int N;
    while(cin >> N && N != 0){
        string s = "";
        stack<int> pilha1;
        stack<int> pilha2;
        for (int i = 0; i < N; i++){
            pilha.push(i);
        }
        while(pilha1.size() + pilha2.size() != 1){
            while (!pilha1.empty()){
                s += pilha1.top();
                s += ", ";
                pilha1.pop();
                pilha2.push(pilha1.top())
                pilha1.pop();
            }
            while (!pilha2.empty()){
                s += pilha2.top();
                s += ", ";
                pilha2.pop();
                pilha1.push(pilha2.top())
                pilha2.pop()
            }
        }

    }
    return 0;
}