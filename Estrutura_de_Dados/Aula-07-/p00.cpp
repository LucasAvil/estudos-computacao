#include <iostream>
#include <stack> // implementa a pilha

using namespace std;

// push(p,valor) insere valor na pilha
// pop(P) retira o valor do topo
// size() retorna a quant de elementos na pilha
// isEmpty() verifica se ta vazia
// isFull() verifica se a pilha está cheia

int main(){
    stack<string> pilha;
    stack<string> pilhabackup;
    pilha.push("A");
    pilha.push("B");
    pilha.push("C");

    do{
        cout << "Tamanho: " << pilha.size() << endl;
        cout << "Topo: " << pilha.top() << endl;
        pilhabackup.push(pilha.top());
        cout << "Topo backup: " << pilhabackup.top() << endl;
        // a pilha backup vai ser a invertida da normal
        pilha.pop();

    }while(!pilha.empty());
    
    
    return 0;
}