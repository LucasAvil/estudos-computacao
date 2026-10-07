#include <iostream>
#include <stack>
#include <string>

using namespace std;
int prioridade(char op){
    if (op == '^'){
        return 3;
    } else if (op == '*' || op == '/'){
        return 2;
    } else if (op == '+' || op == '-'){
        return 1;
    }
    return 0;
}
int main(){
    //se eu ler um operando eu adiciono na saida
    //se eu ler um parenteses abrindo eu adiciono direto na lista
    //se for um parenteses fechando eu adiciono na saida e dou pop na lista ate achar o parenteses fechando
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        string s, saida = "";
        stack<char> pilha;
        cin >> s;
        for(char c : s){
            if (c == '('){
                pilha.push(c);
            }
                
            else if (c == ')') {
                while (!pilha.empty() && pilha.top() != '(') {
                saida += pilha.top();
                pilha.pop();
                }
                if (!pilha.empty() && pilha.top() == '(') {
                    pilha.pop();
                }   
            }
            else if (c == '+' || c == '-' || c == '/' || c == '*' || c == '^'){
                while(!pilha.empty() && prioridade(pilha.top()) >= prioridade(c)){
                    saida += pilha.top();
                    pilha.pop();
                }
                pilha.push(c);
            }
            else{
                saida += c;
            }
    }
    while(!pilha.empty()){
        saida += pilha.top();
        pilha.pop();
    }
    cout << saida << endl;
    }
    return 0;
}

