#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s); //pega todos os valores da linha e insere na variavel s, tudo, até os espaços
    stack<char> pilha;
    bool bemFormada = true;
    for (char c : s) {
        //para cada caractere da variavel s ele faz:
        if (c == '{') {
            //se for chave abrindo, ele verifica se a pilha nao está vazia e se a chave está dentro de um colchete ou parenteses
            //se estiver, nao é bem formada, da break e ja retorna que ta mal formada
            //tem q ter o !pilha,empty() pq se ele tentar pegar o top de uma pilha vazia ele da erro
            if (!pilha.empty() && (pilha.top() == '[' || pilha.top() == '(')) {
                bemFormada = false;
                break;
            }
            //caso ainda seja bemformada, vai adicionar o caractere na pilha
            pilha.push(c);
        } 
        else if (c == '[') {
            if (!pilha.empty() && pilha.top() == '(') {
                bemFormada = false;
                break;
            }
            pilha.push(c);
        } 
        else if (c == '(') {
            //como o parenteses pode estar dentro de qualquer outro, ele diretamente vai pro push
            pilha.push(c);
        } 
        else if (c == '}' || c == ']' || c == ')') {
            if (pilha.empty()) {
                //se tu for fechar um e a plha tiver vazia, significa que nao tem nada pra fechar, logo, invalida
                bemFormada = false;
                break;
            }
            char topo = pilha.top();
            //se tu for fechar e o topo for o seu equivalente, siginifica que fechou certo e da pop no que ta abrindo
            if ((c == '}' && topo == '{') ||
                (c == ']' && topo == '[') ||
                (c == ')' && topo == '(')) {
                pilha.pop();
            } else {
                bemFormada = false;
                break;
            }
        }
    }
    if (bemFormada && pilha.empty()) {
        cout << "Bem formada" << endl;
    } else {
        cout << "Mal formada" << endl;
    }

    return 0;
}