#include <iostream>
#include <stack>

using namespace std;

int main(){
    stack<string> urlpassd;
    stack<string> urlprox;
    string comando;

    while(cin >> comando){
        if (comando == "VISIT"){
            string url;
            cin >> url;
            urlpassd.push(url);
            while (!urlprox.empty()) {
                urlprox.pop();
    }

        }
        else if (comando == "BACK"){
            if (urlpassd.size() <= 1){
                cout << "SEM HISTORICO" << endl;
            } else{
                urlprox.push(urlpassd.top());
                urlpassd.pop();
            }
        }
        else if (comando == "FORWARD"){
            if (urlprox.empty()){
                cout << "SEM HISTORICO" << endl;
            } else{
                urlpassd.push(urlprox.top());
                urlprox.pop();
            }
        }
        else if (comando == "SHOW"){
            cout << urlpassd.top() << endl;
        }
    }

    return 0;
}