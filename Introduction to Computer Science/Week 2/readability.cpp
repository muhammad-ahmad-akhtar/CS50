#include <iostream>
#include <strings>
using namespace std;

int main(){
    string user_input;
    int sentences = 0, words = 0, letters = 0;
    cout << "Input: ";
    cin.getline(user_input);
    for(int i = 0; i < 10; i++){
        if (user_input[i] == ' '){
            words++;
        }
        else if (user_input == "?" || user_input == "." || user_input == "!"){
            sentences++;
        }
        letters++;
        cout << user_input[i] << endl;
    }
    words++;
    cout << "Debugging Details: \n";
    cout << sentences << endl << words << endl << letters << endl;
    return 0;
}