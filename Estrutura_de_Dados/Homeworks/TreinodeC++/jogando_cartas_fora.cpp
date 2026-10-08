#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(){
    int N;
    while(cin >> N && N != 0){
        string s = "";
        queue<int> fila;
        for (int i = 1; i <= N; i++){
            fila.push(i);

        } 
        while (fila.size() > 1){
            s += to_string(fila.front());
            fila.pop();
            if (fila.size() > 1){
                s += ", ";
                fila.push(fila.front());
                fila.pop();
            }else{
                break;
            }
        }
        cout << "Discarded cards: " << s << endl;
        cout << "Remaining card: " << fila.front() << endl;
    }
    return 0;
}