#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double n1, n2, n3, n4, exame;
    cin >> n1 >> n2 >> n3 >> n4;
    double media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10.0;
    cout << "Media: " << fixed << setprecision(1) << media << endl;
    if (media < 7 && media >= 5){
        cout << "Aluno em exame." << endl;
        cin >> exame;
        media = (media + exame) / 2;
        cout << "Nota do exame: " << fixed << setprecision(1) << exame << endl;
        if (media >= 5){
            cout << "Aluno aprovado." << endl;
        } else {
            cout << "Aluno reprovado." << endl;
        }
        cout << "Media final: " << fixed << setprecision(1) << media << endl;
    } else if (media < 5){
        cout << "Aluno reprovado." << endl;
    } else if (media >= 7){
        cout << "Aluno aprovado." << endl;
    }

    return 0;
}