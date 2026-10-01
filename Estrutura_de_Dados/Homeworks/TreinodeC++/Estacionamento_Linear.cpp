#include <iostream>
#include <stack>

using namespace std;

int main() {
    int N, K, Ci, Co;

    while (cin >> N >> K && (N != 0 || K != 0)) {
        bool invalida = false;
        stack<int> pilhaout;

        for (int i = 0; i < N; i++) {
            cin >> Ci >> Co;
            if (invalida) continue;
            while (!pilhaout.empty() && Ci >= pilhaout.top()) {
                pilhaout.pop();
            }
            if (pilhaout.empty()) {
                pilhaout.push(Co);
            } 
            else if (pilhaout.size() < K && Co <= pilhaout.top()) {
                pilhaout.push(Co);
            } 
            else {
                invalida = true;
            }
        }

        if (invalida) {
            cout << "Nao" << endl;
        } else {
            cout << "Sim" << endl;
        }
    }

    return 0;
}