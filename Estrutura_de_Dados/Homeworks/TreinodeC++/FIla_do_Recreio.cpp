#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Aluno {
    int nota;
    int pos_orig;
};

bool ordena(const Aluno &a, const Aluno &b) {
    if (a.nota != b.nota) {
        return a.nota > b.nota;
    }
    return a.pos_orig < b.pos_orig;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    while (N--) {
        int M;
        cin >> M;

        vector<Aluno> vet(M);
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