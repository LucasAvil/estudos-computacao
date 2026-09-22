#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int X, Y, Z;
    cin >> X >> Y >> Z;
    int vet[3] = {X, Y, Z};
    sort(vet, vet + 3);
    for (int i = 0; i < 3; i++) {
        cout << vet[i] << endl;
    }

    cout << endl;

    cout << X << endl << Y << endl << Z << endl;

    return 0;
}