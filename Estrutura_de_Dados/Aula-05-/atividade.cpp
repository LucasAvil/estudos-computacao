#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
bool ordena(float a, float b){
    return a > b;
}
int main(){
    int N, excelente = 0, bom = 0, ruim = 0;
    float tempo = 0, media = 0;
    cin >> N;
    float vet[N];
    for(int i = 0; i < N; i++){
        cin >> tempo;
        media += tempo;
        vet[i] = tempo;
        if(tempo < 11){
            excelente++;

        } else if(tempo >= 11 and tempo < 12){
            bom++;
        } else{
            ruim++;
        }
    }
        sort(vet,vet+N,ordena);
        cout << "Excelente: " << excelente << endl;
        cout << "Bom: " << bom << endl;
        cout << "Precisa melhorar: " << ruim << endl << endl;
        cout << "Melhor tempo: " << vet[N - 1] << endl;
        cout << "Pior tempo: " << vet[0] << endl;
        cout << "Tempo médio: " << fixed << setprecision(2) << media/N << endl;
        cout << "Tempo em ordem decrescente: ";
        for(int i=0; i<N; i++){
        cout << vet[i] << "  ";
    }
    return 0;
}