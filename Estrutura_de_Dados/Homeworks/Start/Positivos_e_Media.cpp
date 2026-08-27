#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int positivos = 0;
    double x, total;
    float media = 0;
    for (int i = 0; i < 6; i++){

        cin >> x;
            if (x >=0){
                positivos++;
                total += x;
            }
            
        }

    cout << positivos << " valores positivos" << endl << fixed << setprecision(1) << total / positivos << endl;
    
    
    return 0;
}