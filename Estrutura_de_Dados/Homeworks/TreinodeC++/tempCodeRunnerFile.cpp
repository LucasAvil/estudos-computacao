#include <iostream>
#include <string>
using namespace std;
//o size_t significa um dado sem sinal, aceita numeros positivos, serve pra
// guardar tamanhos de vetores, textos e posições de memoria, como a funcao
// .size ou .lenght retorna um valor tipo size_t, é necessario comparar com um size_t

int main(){
    string N;
    cin >> N;
    bool ma_sorte = false;
    for (size_t i =0; i < N.lenght()-1; i++){
        if (N[i] == '1' && N[i + 1] == '3'){
            ma_sorte = true;
            break;
        }
    }
    if (ma_sorte){
        cout << N << " es de Mala Suerte" << endl;
    } else{
        cout << N << " NO es de Mala Suerte" << endl;
    }

    return 0;
}