#include <iostream>
#include <queue>

using namespace std;



int main(){
    queue<string> filanorm;
    queue<string> filapri;
    string N;
    int tipo, op;
    while (true){
        cout << "Digite a opção desejada: " << endl << "1. Atendimento" << endl << "2. Adicionar Cliente" << endl << "3. Sair" << endl;
        cin >> op;
        if (op == 2){
            cout << "Digite o nome do cliente: ";
            cin >> N;
            cout << "Digite o tipo de atendimento: " << endl << "1. Prioritário" << endl << "2. Normal" << endl;
            cin >> tipo;
            if (tipo == 1){
                filapri.push(N);
            } else if (tipo == 2){
                filanorm.push(N);
            }
        }
        else if (op == 1){
            if (!filapri.empty()){
                cout << "Próximo a ser atendido: " << filapri.front() << endl;
                filapri.pop();
            } else if (!filanorm.empty() && filapri.empty()){
                cout << "Próximo a ser atendido: " << filanorm.front() << endl;
                filanorm.pop();
            } else{
                cout << "Fila vazia" << endl;
            }
    } else if (op == 3){
        cout << "Encerrando..." << endl;
        break;
    }
}
    return 0;
}