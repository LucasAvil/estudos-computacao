#include <iostream>
#include <queue>

using namespace std;

    struct pessoa{
        string nome, email;
    };

int main(){
    queue<pessoa> fila;
    pessoa aux;
    int N;

    while(true){
        cout << "Digite o nome ou FIM para sair: ";
        getline(cin,aux.nome);
        if (aux.nome == "FIM"){
            cout << "Encerrando..." << endl;
            break;
        }
        cout << "dijit seu email: " << endl;
        getline(cin,aux.email);
        fila.push(aux);
        cout << "Tamanhio: " << fila.size() << endl;

    }
    while(!fila.empty()){
        cout << "primeiro: " << fila.front().nome << " " << fila.front().email << endl;
        fila.pop();
    }

    return 0;

}