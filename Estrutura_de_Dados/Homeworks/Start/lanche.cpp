#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int cod;
    double quant, total;

    cin >> cod >> quant;
    if (cod == 1){
        total += 4 * quant;
    } else if (cod == 2){
        total += 4.50 * quant;
    } else if (cod == 3){
        total += 5 * quant;
    } else if (cod == 4){
        total += 2 * quant;
    } else if (cod == 5){
        total += 1.5 * quant;
    }
    cout << "Total: R$ " << fixed << setprecision (2) << total << endl;
    return 0;
}