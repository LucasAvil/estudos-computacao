#include <iostream>
using namespace std;


//funcao void nao possui retorno para quem chamou
void imprimir(string texto){
    cout << "o texto recebido foi: " << texto << endl;


}

int adiciona(int x, int y){
    return x + y;
}

int main (){
    imprimir("FUNÇÃÃÃO");
    int x = 10;
    int y = 2;
    cout << adiciona(x, y) << endl;
    imprimir(adiciona(x,y));
    return 0;
}