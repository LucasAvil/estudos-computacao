#include <iostream>
using namespace std;

int main(){
    int N, par[5], impar[5], pos_par = 0, pos_impar = 0;
    for (int i = 0; i < 15; i++){
        cin >> N;
        if (N%2 != 0){
            impar[pos_impar] = N;
            pos_impar++;
            if(pos_impar == 5){
                for (int k = 0; k < 5; k++){
                    cout << "impar[" << k << "] = " << impar[k] << endl;
                }
                pos_impar = 0;
            }
        } else{
            par[pos_par] = N;
            pos_par++;
            if(pos_par == 5){
                for (int j = 0; j < 5; j++){
                    cout << "par[" << j << "] = " << par[j] << endl;
                }
                pos_par = 0;
        }   
    }

    }
    for (int h = 0; h < pos_impar; h++){
        cout << "impar[" << h << "] = " << impar[h] << endl;
    }
    for (int l = 0; l < pos_par; l++){
        cout << "par[" << l << "] = " << par[l] << endl;
    }
    
    return 0;
}