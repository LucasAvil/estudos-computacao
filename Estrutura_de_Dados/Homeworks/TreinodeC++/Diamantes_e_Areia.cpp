#include <iostream>
#include <stack>

using namespace std;

int main() {
    int N;
    string s;
    cin >> N;

    for (int i = 0; i < N; i++) {
        stack<char> pilhadiamantes;
        int diamantes = 0;
        cin >> s;

        for (char c : s) {
            if (c == '<') {
                pilhadiamantes.push(c);
            } else if (c == '>') {
                if (!pilhadiamantes.empty() && pilhadiamantes.top() == '<') {
                    pilhadiamantes.pop();
                    diamantes++;
                }
            }
        }

        cout << diamantes << endl; 
    }

    return 0;
}