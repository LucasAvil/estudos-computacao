#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double x, total = 0, peso = 0;


    for  (int i = 0; i < 3; i++){
        cin >> x;
        if (i == 0){
            peso = 0.2 * x;
        } else if (i == 1){
            peso = 0.3 * x;
        } else {
            peso = 0.5 * x;
        }
        total += peso;
    }
    cout << "MEDIA = " << fixed << setprecision(1) << total << endl;
    return 0;
}