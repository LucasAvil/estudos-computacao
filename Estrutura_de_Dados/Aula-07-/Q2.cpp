#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;
//a declaracao de const vector<string>& é um vetor do tipo string, constante passado por referencia p economizar memoria
//o tokens é o nome desse vetor, entao quando eu chamo tokens.size() eu pego o tamanho do vetor que eu declarei la
//o token é apenas o caractere individual do vetor tokens, chamado pelo indice i
int avaliarRPN(const vector<string>& tokens) {
    stack<int> pilha;

    for (int i = 0; i < tokens.size(); i++) {
        string token = tokens[i];

        if (token == "+" || token == "-" || token == "*" || token == "/") {
            //se for um operando ele pega os dois numeros que tao na pilha, iguala a A e B
            //faz a operação com o operando identificado
            //se nao tiver mais nenhum caractere dentro do vetor tokens ele vai pro return la e retorna o valor da equação
            int b = pilha.top();
            pilha.pop();
            int a = pilha.top();
            pilha.pop();
            if (token == "+") {
                pilha.push(a + b);
            } else if (token == "-") {
                pilha.push(a - b);
            } else if (token == "*") {
                pilha.push(a * b);
            } else if (token == "/") {
                pilha.push(a / b);
            }
        } 
        else {
            //se o token nao for um operando, ele é um numero, logo, deve ser adicionado a pilha de valores
            //o stoi serve pra transformar o caractere em int, ao inves de string
            pilha.push(stoi(token));
        }
    }
    return pilha.top();
}

int main() {
    vector<string> expressao = {"2", "1", "+", "3", "*"};

    int resultado = avaliarRPN(expressao);

    cout << "Resultado: " << resultado << endl;

    return 0;
}