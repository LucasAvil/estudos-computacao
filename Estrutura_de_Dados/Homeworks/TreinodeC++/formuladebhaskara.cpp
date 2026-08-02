#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double a, b, c;
    cin >> a >> b >> c;
    double delta = pow(b, 2) - (4 * a * c);
    if (delta > 0 && a != 0){

        double x1 = ((b*-1) + sqrt(delta)) / (2 * a);
        double x2 = ((b*-1) - sqrt(delta)) / (2 * a);
        cout << "R1 = " << fixed << setprecision(5) << x1 << endl;
        cout << "R2 = " << fixed << setprecision(5) << x2 << endl;
    } else{
        cout << "Impossivel calcular" << endl;
    }

    return 0;
}