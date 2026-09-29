#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int avaliarRPN(const vector<string>& tokens) {
    stack<int> pilha;

    for (int i = 0; i < tokens.size(); i++) {
        string token = tokens[i];

        if (token == "+" || token == "-" || token == "*" || token == "/") {
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