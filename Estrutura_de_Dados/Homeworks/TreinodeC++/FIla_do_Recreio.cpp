#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct aluno {
    int nota;
    int pos_orig;
};

bool ordena(const aluno &a, const aluno &b) {
    return a.nota > b.nota;
}

int main() {
    int N;
    if (!(cin >> N)) return 0;

    for (int i = 0; i < N; i++) {
        int M;
        cin >> M;
        vector<aluno> vet(M);
        for (int j = 0; j < M; j++) {
            cin >> vet[j].nota;
            vet[j].pos_orig = j;
        }

        sort(vet.begin(), vet.end(), ordena);

        int R = 0;
        for (int k = 0; k < M; k++) {
            if (vet[k].pos_orig == k) {
                R++;
            }
        }

        cout << R << "\n";
    }

    return 0;
}