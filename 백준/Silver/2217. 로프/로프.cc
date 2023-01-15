#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int n, k;
    cin>>n;
    vector <int> v(n);
    
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    sort(v.begin(), v.end());
    
    int w=0;
    for (int i = 0; i<n; i++){
        if(w < v[i]*(n-i)){
            w = v[i]*(n-i);
        }
    }
    cout<<w;
    
    return 0;
}
