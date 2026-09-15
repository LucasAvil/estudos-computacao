#include <iostream>
#include <algorithm>

using namespace std;

bool ordena(int a, int b) {
    return a > b;
}

int main() {
    int L;
    while (cin >> L) {
        int vetor[L];
        for (int i = 0; i < L; i++) {
            cin >> vetor[i];
        }

        sort(vetor, vetor + L, ordena);

        if (vetor[0] < 10) {
            cout << 1 << endl;
        } else if (vetor[0] < 20) {
            cout << 2 << endl;
        } else {
            cout << 3 << endl;
        }
    }

    return 0;
}