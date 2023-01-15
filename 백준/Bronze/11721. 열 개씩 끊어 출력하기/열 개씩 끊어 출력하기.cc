#include <stdio.h>
#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    string str;
    cin>>str;
    
    for (int i = 0; i<str.size(); i++){
        if (i !=0 && i%10 == 0)
            cout<<endl;
        cout<<str[i];
    }
    
    return 0;
}