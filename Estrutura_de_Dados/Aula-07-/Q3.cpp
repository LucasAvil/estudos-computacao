#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s);
    stack<char> pilha;
    bool bemFormada = true;
    for (char c : s) {
        if (c == '{') {
            if (!pilha.empty() && (pilha.top() == '[' || pilha.top() == '(')) {
                bemFormada = false;
                break;
            }
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
            pilha.push(c);
        } 
        else if (c == '}' || c == ']' || c == ')') {
            if (pilha.empty()) {
                bemFormada = false;
                break;
            }
            char topo = pilha.top();
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